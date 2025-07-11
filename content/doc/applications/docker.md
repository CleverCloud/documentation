---
type: docs
title: Docker
shortdesc: Docker is an easy, lightweight virtualized environment for portable applications.
keywords:
- docker
tags:
- deploy
str_replace_dict:
  "@application-type@": "Docker"
type: docs
aliases:
- /developers/doc/docker/docker
- /doc/deploy/application/docker
- /doc/deploy/application/docker/docker
- /doc/docker/docker
- /doc/getting-started/by-language/docker
- /doc/partials/language-specific-deploy/docker
---
{{< hextra/hero-subtitle style="margin:.3rem 0 2rem 0">}}
  Clever Cloud offers support for Docker containers. These are deployed inside virtual machines to guarantee a secure level of isolation.
{{< /hextra/hero-subtitle >}}

## Overview

Docker containers can encapsulate any payload, and will run consistently on and between virtually any server. The same container that a developer builds and tests on a laptop will run at scale, in production, on VMs, bare-metal servers, public instances, or combinations of the above.

Clever Cloud allows you to deploy any application running inside a Docker container. This page will explain how to set up your application to run it on our service.

{{< callout type="info" >}}
  Clever Cloud supports many languages, but some users have specific application needs. With Docker, they can create custom stacks without relying on Clever Cloud's specific support.
{{< /callout >}}

{{< callout type="warning" >}}
[FS Buckets](../../best-practices/cloud-storage/#what-is-fs-bucket) access, Dockerfile validation, and Docker Compose functionalities are not supported.
{{< /callout >}}

### How it works

When you create a Docker application on Clever Cloud, the deployment process involves the following steps:

1. **Install/Login:**
   - The system checks for a Dockerfile and an entrypoint.
    - It logs into the docker registry that you configured in the Dockerfile, if any, to find the necessary image (**note:** the name of the Docker registry may vary depending on the provider. It's called "container registry" in GitHub, for instance)
2. **Build:**
   - The application pulls the specified image and execute commands you specified in Dockerfile.
   - **Note:** This step focuses on executing commands in your Dockerfile and doesn't require build instructions if you are using a pre-compiled image.
3. **Run:**
   - The application starts in a Docker container and exposes the service on port 8080 by default.
   - If you need to expose your application on a different port, you can specify this using the environment variable `CC_DOCKER_EXPOSED_HTTP_PORT`.

 {{< content "set-env-vars" >}}

## Configure your Docker application

### Mandatory configuration

Be sure that you:

* push on the **master branch**.
* have and commit a file named **Dockerfile** or use the **CC_DOCKERFILE** [environment variable]({{< ref "doc/reference/reference-environment-variables.md#docker" >}}) if your Dockerfile has a different name, [Here is what it will look like](https://docs.docker.com/develop/develop-images/dockerfile_best-practices "Dockerfile").
* run the application with `CMD` or `ENTRYPOINT` in your Dockerfile.
* listen on HTTP **port 8080** by default (you can set your own port using `CC_DOCKER_EXPOSED_HTTP_PORT=<port>` environment variable).

### Dockerfile contents

You can virtually put everything you want in your Dockerfile. The only mandatory (for us) instruction to put in it is:

```bash
CMD <command to run>
```

**command to run**: this is the command that starts your application. Your application **must** listen on port 8080. It can be easier for you to put a script in your docker image and call it with the CMD instruction.

### Docker Buildx

We still use `docker build` command for legacy reasons, but you can use `docker buildx` instead, setting `CC_DOCKER_BUILDX` to `true`.

### Memory usage during building

If the building step of your app crashes because it uses more memory that it's available, you'll have to split the building and running steps and enable [Dedicated build instance]({{< ref "doc/administrate/apps-management.md#edit-application-configuration" >}})

```bash
# The base image
FROM outlinewiki/outline:version-0.44.0

# Run the memory intensive build on an instance with 4 GB of memory (M)
RUN yarn install && yarn build

# Start the app on a smaller instance (nano)
CMD yarn start
```

### Login to registry

As Docker Hub limits the number of image pulls and actions without authentication, use you own account to get higher limits. You can also use a private registry where you store your images. This feature launch `docker login` command before the build phase.

* `CC_DOCKER_LOGIN_USERNAME`: the username to use to login
* `CC_DOCKER_LOGIN_PASSWORD`: the password of your username
* `CC_DOCKER_LOGIN_SERVER` (optional): the server of your private registry, default is Docker Hub

### TCP support

Clever Cloud enables you to use TCP over Docker applications using the environment variable `CC_DOCKER_EXPOSED_TCP_PORT=<port>`.

* [Learn more about TCP redirections](/developers/doc/administrate/tcp-redirections)

### Docker socket access

Some containers require access to the docker socket, to spawn sibling containers for instance.

{{< callout type="warning" >}}
Giving access to the docker socket breaks all isolation provided by docker. **DO NOT** give socket access to untrusted code.
{{< /callout >}}

You can make the docker socket available from inside the container by adding the `CC_MOUNT_DOCKER_SOCKET=true` environment variable. In that case, docker is started in the namespaced mode, and in bridge network mode.

### Enable IPv6 networking

You can activate the support of IPv6 with a IPv6 subnet in the docker daemon by adding the `CC_DOCKER_FIXED-CIDR-V6=<IP>` environment variable.

### Build-time variables

You can use the [ARG](https://docs.docker.com/engine/reference/builder/#arg) instruction to define build-time environment variables.

Every environment variable defined for your application will be passed as a build environment variable using the `--build-arg=<ENV>` parameter during the `docker build` phase.

### Sample dockerized applications

We provide a few examples of dockerized applications on Clever Cloud.

* [Elixir App](https://GitHub.com/CleverCloud/demo-docker-elixir/blob/master/Dockerfile)
* [Seaside / Smalltalk App](https://GitHub.com/CleverCloud/demo-seaside)
* [Rust App](https://GitHub.com/CleverCloud/demo-rust)

You might need to use the `CC_DOCKERFILE = <name of your Dockerfile>` variable.


{{< content "env-injection" >}}

{{< content "deploy-git" >}}

{{< content "link-addon" >}}

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}