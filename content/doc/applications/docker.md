---
type: docs
linkTitle: Docker
title: Docker
description: Deploy Docker containers on Clever Cloud with secure VM isolation, custom stacks, and flexible application deployment options
keywords:
- app hosting
- container deployment
- containerization
- custom stacks
- docker app hosting
- docker cloud
- docker containers
- flexible hosting
- secure deployment
- VM isolation
aliases:
- /applications/docker
- /developers/doc/applications/docker
- /doc/deploy/application/docker
- /doc/deploy/application/docker/docker
- /doc/docker
- /doc/docker/docker
- /doc/getting-started/by-language/docker
- /doc/partials/language-specific-deploy/docker
- /docker
- /docker-hosting
---
{{< hextra/hero-subtitle style="margin:.3rem 0 2rem 0">}}
  Clever Cloud offers support for Docker containers. These are deployed inside virtual machines to guarantee a secure level of isolation.
{{< /hextra/hero-subtitle >}}

## Overview

Docker containers can encapsulate any payload, and will run consistently on and between virtually any server. The same container that a developer builds and tests on a laptop will run at scale, in production, on VMs, bare-metal servers, public instances, or combinations of the above.

Clever Cloud allows you to deploy any application running inside a Docker container. This page explains how to set up your application to run it on our service.

> [!NOTE]
> Clever Cloud supports many languages, but some users have specific application needs. With Docker, they can create custom stacks without relying on Clever Cloud's specific support.

> [!WARNING]
> [FS Buckets](/doc/best-practices/cloud-storage/#what-is-fs-bucket) access, Dockerfile validation, and Docker Compose functionalities are not supported.

### How it works

When you create a Docker application on Clever Cloud, the deployment process involves the following steps:

1. **Login:** The system checks for a Dockerfile and logs into the Docker registry you configured, if any, to find the necessary image.
2. **Build:** The application pulls the specified image and executes the commands specified in your Dockerfile.
3. **Run:** The application starts in a Docker container and exposes the service on port 8080 by default.

{{% content "set-env-vars" %}}

## Configure your Docker application

### Mandatory configuration

Be sure that you:

- Have and commit a file named **Dockerfile**, or use the `CC_DOCKERFILE` [environment variable](/doc/reference/reference-environment-variables#docker) if your Dockerfile has a different name. [Here is what it will look like](https://docs.docker.com/develop/develop-images/dockerfile_best-practices "Dockerfile").
- Run the application with `CMD` or `ENTRYPOINT` in your Dockerfile.
- Listen on HTTP **port 8080** by default (you can set your own port using `CC_DOCKER_EXPOSED_HTTP_PORT`).

- [Learn more about environment variables on Clever Cloud](/doc/reference/reference-environment-variables/)

### Dockerfile contents

You can virtually put everything you want in your Dockerfile. The only mandatory instruction is:

```dockerfile
CMD <command to run>
```

**command to run**: this is the command that starts your application. Your application **must** listen on the port defined by `CC_DOCKER_EXPOSED_HTTP_PORT` (default: `8080`). It can be easier for you to put a script in your Docker image and call it with the CMD instruction.

### Docker Buildx

The default build uses `docker buildx`. To use Docker legacy build instead, set `CC_DOCKER_BUILDX` to `false`.

### Memory management

The Docker container runs with a memory limit equal to the instance's available memory, with swap disabled. If the building step of your application crashes due to memory usage, split the building and running steps and enable [Dedicated build instance](/doc/administrate/apps-management#edit-application-configuration):

```dockerfile
# The base image
FROM outlinewiki/outline:version-0.44.0

# Run the memory intensive build on an instance with 4 GB of memory (M)
RUN yarn install && yarn build

# Start the app on a smaller instance (nano)
CMD yarn start
```

### Login to registry

As Docker Hub limits the number of image pulls without authentication, use your own account to get higher limits. You can also use a private registry where you store your images. This runs `docker login` before the build phase.

- `CC_DOCKER_LOGIN_USERNAME`: the username to use
- `CC_DOCKER_LOGIN_PASSWORD`: the password for your username
- `CC_DOCKER_LOGIN_SERVER` (optional): the server of your private registry, default is Docker Hub

> [!NOTE]
> The name of the Docker registry may vary depending on the provider (e.g. "container registry" in GitHub). If login fails, the build continues without authentication.

### Network mode

When using default ports (`CC_DOCKER_EXPOSED_HTTP_PORT=8080` and `CC_DOCKER_EXPOSED_TCP_PORT=4040`), the container runs with `--net host` for direct network access. When custom ports are specified, Docker's port mapping is used instead (`-p 8080:<your_http_port> -p 4040:<your_tcp_port>`).

### TCP support

Clever Cloud enables you to use TCP over Docker applications using the environment variable `CC_DOCKER_EXPOSED_TCP_PORT` (default: `4040`).

- [Learn more about TCP redirections](/doc/administrate/tcp-redirections)

### Docker socket access

Some containers require access to the Docker socket, to spawn sibling containers for instance.

> [!WARNING]
> Giving access to the Docker socket breaks all isolation provided by Docker. **DO NOT** give socket access to untrusted code.

You can make the Docker socket available from inside the container by adding the `CC_MOUNT_DOCKER_SOCKET=true` environment variable. In that case, Docker is started in the namespaced mode (user namespace remapping), and the container uses port mapping instead of host network mode.

### Enable IPv6 networking

You can activate the support of IPv6 with an IPv6 subnet in the Docker daemon by adding the `CC_DOCKER_FIXED_CIDR_V6=<CIDR>` environment variable (e.g. `fd00::/80`).

### Build-time variables

You can use the [ARG](https://docs.docker.com/engine/reference/builder/#arg) instruction to define build-time environment variables.

Every environment variable defined for your application is passed as a build environment variable using the `--build-arg` parameter during the `docker build` phase.

### Deployment hooks

Docker applications support all [deployment hooks](/doc/develop/build-hooks/). The `CC_PRE_BUILD_HOOK`, `CC_POST_BUILD_HOOK`, and `CC_PRE_RUN_HOOK` run on the host. The `CC_RUN_SUCCEEDED_HOOK` runs inside the container after successful start.

### Docker applications as Clever Tasks

Docker containers can run as on-demand workloads on Clever Cloud. Configure an application as Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/cli/applications/#tasks). The container runs, executes its command, and stops.

- [Learn more about Clever Tasks](/doc/develop/tasks/)

### Sample dockerized applications

- [Elixir App](https://github.com/CleverCloud/demo-docker-elixir/blob/master/Dockerfile)
- [Seaside / Smalltalk App](https://github.com/CleverCloud/demo-seaside)
- [Rust App](https://github.com/CleverCloud/demo-rust)

{{% content "env-injection" %}}

{{% content "deploy-git" %}}

{{% content "link-addon" %}}

{{% content "more-config" %}}

{{% content "url_healthcheck" %}}
