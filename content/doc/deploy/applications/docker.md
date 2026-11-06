---
type: docs
linkTitle: Docker
title: Docker
description: Build and run Docker containers on Clever Cloud from a Dockerfile, each instance in its own virtual machine, with private registries, custom ports and the Docker socket
keywords:
- buildx
- container deployment
- docker app hosting
- docker cloud
- docker containers
- dockerfile
- VM isolation
aliases:
- /applications/docker
- /doc/applications/docker
- /doc/deploy/application/docker
- /doc/deploy/application/docker/docker
- /doc/develop/deploy/docker
- /doc/docker
- /doc/docker-hosting
- /doc/docker/docker
- /doc/getting-started/by-language/docker
- /doc/partials/language-specific-deploy/docker
- /docker
- /doc/deploy/docker/
- /doc/develop/build/apps/docker/
- /docker-hosting
---

## Overview

Clever Cloud builds an image from the [Dockerfile](https://docs.docker.com/reference/dockerfile/) of your project and runs it as a container. Each instance is a virtual machine with its own Docker daemon, running one application container, which isolates it from other applications. Use Docker for a language or system libraries no other runtime provides, or to deploy an application you already ship as an image, built in your own CI for instance.

## What's different with the Docker runtime

Other runtimes run your application in an environment Clever Cloud prepares and maintains: an image with the language, its tools and their versions, and services in front of your application. With Docker, Clever Cloud manages the operating system of the virtual machine and the Docker daemon, then builds and runs your image. What happens inside the container is up to you:

- The base image, and thus the operating system of the container, its packages, and their versions
- The tools and package managers of the image, such as [Mise](https://mise.jdx.dev/): Clever Cloud doesn't install or run any in the container
- The ports the container listens on, and the processes that answer on them
- The updates of all of this: change the base image or the versions in your Dockerfile, then deploy again

Thus, features that rely on the application environment of other runtimes don't apply to Docker applications:

- [Workers](/doc/develop/common-configuration/workers/): start your background processes from your image
- [CRON jobs](/doc/develop/cron/) of a `clevercloud/cron.json` file: run a scheduler within your container
- [Request Flow](/doc/develop/request-flow/) middleware, such as Varnish or Redirection.io: run them in your container
- [Deployment hooks](/doc/develop/common-configuration/build-hooks/), except `CC_RUN_SUCCEEDED_HOOK`, which runs inside the container: put the build steps in your Dockerfile

Docker applications don't support [FS Buckets](/doc/deploy/storage/fs-bucket/) and [Docker Compose](https://docs.docker.com/compose/): each instance runs one application container. For several containers working together or persistent volumes, use [Clever Kubernetes Engine](/doc/deploy/kubernetes/), and manage your add-ons with the [Clever Kubernetes Operator](/doc/deploy/kubernetes/operator/).

## Create your Docker application

To create a new Docker application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type docker
```

- [Learn more about Clever Tools](/doc/manage/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

## Configure your Docker application

### Mandatory needs

A Docker application needs:

- A `Dockerfile` at the root of the project
- A web server listening on `0.0.0.0:8080` in the container
- A command that starts your application, set with `CMD` or `ENTRYPOINT` in your Dockerfile or in its base image

To use another file, set its path in `CC_DOCKERFILE`, such as `docker/Dockerfile.prod`. With `APP_FOLDER`, Clever Cloud looks for the `Dockerfile` in this folder. To listen on another port, set it in `CC_DOCKER_EXPOSED_HTTP_PORT`. A [Clever Task](#docker-applications-as-clever-tasks) doesn't need a web server.

In most cases, `CMD` gives the whole command, such as `CMD ["node", "server.js"]`. If the image sets an `ENTRYPOINT`, it's the program to run, and `CMD` only gives its arguments, as in the following example. Learn more in the [Docker documentation](https://docs.docker.com/reference/dockerfile/#understand-how-cmd-and-entrypoint-interact).

For instance, this Dockerfile serves a small language model on CPU with [llama.cpp](https://github.com/ggml-org/llama.cpp), with a chat interface and an OpenAI-compatible API. Its image sets `llama-server` as `ENTRYPOINT`: the `CMD` gives the model and the port:

```dockerfile {filename="Dockerfile"}
FROM ghcr.io/ggml-org/llama.cpp:server-b12124
ADD https://huggingface.co/ggml-org/gemma-3-270m-it-GGUF/resolve/main/gemma-3-270m-it-Q8_0.gguf /models/model.gguf
CMD ["--model", "/models/model.gguf", "--host", "0.0.0.0", "--port", "8080"]
```

### Container environment

Clever Cloud starts the container with:

- The environment variables of your application, such as the credentials of the add-ons you link to it
- A memory limit based on the memory available on the instance, without swap
- A limit of `1024` open files, which processes can raise up to `524288`

The container writes its logs to its standard output and error: Clever Cloud collects them as the [logs of your application](/doc/develop/observability/logs/).

### Build phase

On a new build, Clever Cloud builds the image with [Buildx](https://docs.docker.com/build/). The build context is the root of your project, or the folder set in `APP_FOLDER`. Set `CC_DOCKER_BUILDX=false` to use the legacy builder instead (deprecated, and to be removed).

Clever Cloud passes each [environment variable](/doc/develop/common-configuration/environment-variables/) of your application with `--build-arg`. Declare the ones a build step needs with an [`ARG`](https://docs.docker.com/reference/dockerfile/#arg) instruction. For instance, a [Vite](https://vite.dev/) application embeds its `VITE_*` variables in its files at build time. With a `VITE_API_URL` environment variable, this Dockerfile builds the application, then serves it with Nginx. Declare `ARG` in the stage that uses it:

```dockerfile {filename="Dockerfile"}
FROM node:26-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
ARG VITE_API_URL
RUN npm run build

FROM nginxinc/nginx-unprivileged:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

Each new commit builds the image from scratch: Clever Cloud doesn't keep the Docker layers between builds, base image included. Restarting the application without a code change reuses the image of the build cache when it's available, without building it again. Thus, a new value of a build variable, such as `VITE_API_URL` in the above example, only applies after a rebuild.

To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

If a build fails for lack of memory, enable a [dedicated build instance](/doc/develop/common-configuration/#dedicated-build-instance) larger than your application instances.

### Optimize your image

Clever Cloud saves the image as the build cache of the commit, and loads it again on restart: a smaller image is faster to save and to restore. To keep yours small and safe:

- Exclude what the build doesn't need, such as `.git` or `node_modules`, with a [`.dockerignore`](https://docs.docker.com/build/concepts/context/#dockerignore-files) file
- Use a [multi-stage build](https://docs.docker.com/build/building/multi-stage/), as in the [Vite example](#build-phase): build in a first stage, and copy only the result into the final image
- Start from a small base image, such as an `alpine` or `slim` variant, with a pinned version tag, or from [`scratch`](#deploy-a-static-binary-from-scratch)
- Run your application as a non-root user, with the [`USER`](https://docs.docker.com/reference/dockerfile/#user) instruction or from an unprivileged image such as `nginxinc/nginx-unprivileged`

Learn more in the [Docker build best practices](https://docs.docker.com/build/building/best-practices/).

### Deploy a static binary from scratch

[`scratch`](https://hub.docker.com/_/scratch) is an empty image. For a program compiled as a static binary, such as a Go or Rust program, copy only the binary into it: the image is then barely larger than the binary. For instance, for a Go web server:

```dockerfile {filename="Dockerfile"}
FROM golang:1.27-alpine AS build
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /server

FROM scratch
COPY --from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=build /server /server
CMD ["/server"]
```

Such an image only holds what you copy into it, without the certificate authorities other images include. Most apps read them from the system to check HTTPS servers: without the `COPY` of the certificates, HTTPS requests fail with `x509: certificate signed by unknown authority`. It has no shell either: [SSH access](/doc/develop/ssh-access/#docker-applications) doesn't work, and `CC_RUN_SUCCEEDED_HOOK` can only run the programs you copy into the image.

### Deploy a pre-built image

Clever Cloud always builds the image of your Dockerfile, but this Dockerfile can start from an image you build elsewhere, in your CI for instance, or from a ready-to-use image. Set this image in the `FROM` instruction. If it defines a `CMD` or an `ENTRYPOINT` and listens on port `8080`, you don't need anything else. Otherwise, add the `CMD` that starts your application, or set its port in `CC_DOCKER_EXPOSED_HTTP_PORT`.

For instance, to deploy [Stirling-PDF](https://www.stirlingpdf.com/), a ready-to-use PDF toolbox, a single line is enough. Its image already listens on port `8080`:

```dockerfile {filename="Dockerfile"}
FROM stirlingtools/stirling-pdf:3.3.0
```

To pull the image from a private registry, [log in to it](#log-in-to-a-registry). To deploy a new version, change its tag in the Dockerfile and push the commit. A restart reuses the image of the build cache. If you publish a new image under the same tag, restart without the cache to pull it.

### Log in to a registry

To pull images from a private registry, or to raise the pull limits of Docker Hub, set registry credentials. Clever Cloud uses them with `docker login` before the build:

- `CC_DOCKER_LOGIN_USERNAME`: the username
- `CC_DOCKER_LOGIN_PASSWORD`: the password or an access token
- `CC_DOCKER_LOGIN_SERVER`: the registry, such as `ghcr.io`. Without it, Clever Cloud logs in to Docker Hub

If one of the credentials is missing or the login fails, Clever Cloud builds the image without authentication.

### Ports, Mapping, and Network Groups

The container receives HTTP traffic on port `8080`, and the traffic of [TCP redirections](/doc/develop/common-configuration/tcp-redirections/) on port `4040`. Its network depends on the ports it listens on. With the default ports, the container shares the network of the instance (`--net host`). If it's part of a [Network Group](/doc/network/network-groups/), the other members can reach every port your application listens on, such as an internal API on port `9000`. It works as with any other runtime.

If your container needs to map ports `8080` and `4040` of the instance to other ports, set them in `CC_DOCKER_EXPOSED_HTTP_PORT` and `CC_DOCKER_EXPOSED_TCP_PORT`. Docker then uses `-p 8080:<http_port>` and `-p 4040:<tcp_port>`, and the container doesn't share the network of the instance anymore. In such a configuration, the other ports of the container are unreachable, even from a Network Group.

In both cases, your container reaches other Network Group members by their domain name: `<member_id>.m.<ng_id>.cc-ng.cloud`.

The `PORT` environment variable still holds `8080`, even with an `ENV PORT` instruction in your Dockerfile. If your application reads it, set `PORT` in the environment variables of your application, to the value of `CC_DOCKER_EXPOSED_HTTP_PORT`.

To enable IPv6 in the Docker daemon, set an IPv6 range in CIDR notation in `CC_DOCKER_FIXED_CIDR_V6`, such as `fd00::/80`.

### Docker socket access

Some containers need the Docker socket, to start sibling containers for instance. Set `CC_MOUNT_DOCKER_SOCKET=true` to mount it in `/var/run/docker.sock`. Docker then runs your container, and the ones it starts, with [user namespace remapping](https://docs.docker.com/engine/security/userns-remap/): the `root` user of a container is an unprivileged user on the instance. Your container also receives its traffic through [port mapping](#ports-mapping-and-network-groups), not on the network of the instance.

> [!WARNING] The Docker socket gives control over the instance
> A container with access to the Docker socket controls the Docker daemon of the instance. Don't give it to code you don't trust.

## Docker applications as Clever Tasks

A Docker container can run as a [Clever Task](/doc/develop/tasks/), such as a job or a migration. Clever Cloud builds the image, runs the container, and stops the task when the container exits. Configure an application as Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/manage/cli/applications/#tasks).

A Docker task runs the `CMD` or `ENTRYPOINT` of the image, not `CC_RUN_COMMAND`, nor the command you give to `clever create --task`. Build an image whose command exits once it finishes its work, or the task keeps running.

## Examples

- [Phoenix (Elixir)](https://github.com/CleverCloud/phoenix-docker-example)
- [Rust](https://github.com/CleverCloud/rust-docker-example)
- [Seaside (Smalltalk)](https://github.com/CleverCloud/demo-seaside)

{{% content "url_healthcheck" %}}
