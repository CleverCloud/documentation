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
- /doc/deploy/application/docker
- /doc/deploy/application/docker/docker
- /doc/getting-started/by-language/docker/
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
[FS Buckets](/doc/best-practices/cloud-storage/#what-is-fs-bucket) access, Dockerfile validation, and Docker Compose functionalities are not supported.
{{< /callout >}}

### How it works

When you create a Docker application on Clever Cloud, the deployment process involves the following steps:

1. **Install/Login:**
   - The system checks for a Dockerfile and an entrypoint.
- It logs into the docker registry that was configured in the Dockerfile, if any, to find the necessary image (**note:** the name of the docker registry may vary depending on the provider. It is called "container registry" in Github, for instance)
2. **Build:**
   - The application pulls the specified image and execute commands you specified in Dockerfile.
   - **Note:** This step focuses on executing commands in your Dockerfile and doesn't require build instructions if you are using a pre-compiled image.
3. **Run:**
   - The application starts in a Docker container and exposes the service on port 8080 by default.
   - If you need to expose your application on a different port, you can specify this using the environment variable `CC_DOCKER_EXPOSED_HTTP_PORT`.

 {{% content/set-env-vars %}}

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

### TCP support

Clever Cloud enables you to use TCP over Docker applications using the environment variable `CC_DOCKER_EXPOSED_TCP_PORT=<port>`. Refer to the documentation page to know how to create [TCP redirections](/doc/administrate/tcp-redirections).

### Docker socket access

Some containers require access to the docker socket, to spawn sibling containers for instance.

{{< callout type="warning" >}}
Giving access to the docker socket breaks all isolation provided by docker. **DO NOT** give socket access to untrusted code.
{{< /callout >}}

You can make the docker socket available from inside the container by adding the `CC_MOUNT_DOCKER_SOCKET=true` environment variable. In that case, docker is started in the namespaced mode, and in bridge network mode.

### Private registry

We support pulling private images through the `docker build` command. To login to a private registry, you need to set a few environment variables:

* `CC_DOCKER_LOGIN_USERNAME`: the username to use to login
* `CC_DOCKER_LOGIN_PASSWORD`: the password of your username
* `CC_DOCKER_LOGIN_SERVER` (optional): the server of your private registry. Defaults to Docker's public registry.

This uses the `docker login` command under the hood.

### Enable IPv6 networking

You can activate the support of IPv6 with a IPv6 subnet in the docker daemon by adding the `CC_DOCKER_FIXED-CIDR-V6=<IP>` environment variable.

### Build-time variables

You can use the [ARG](https://docs.docker.com/engine/reference/builder/#arg) instruction to define build-time environment variables.

Every environment variable defined for your application will be passed as a build environment variable using the `--build-arg=<ENV>` parameter during the `docker build` phase.

### Dockerized Rust application Deployment

To make your dockerized application run on clever Cloud, you need to:

* expose port 8080 in your docker file
* run the application with `CMD` or `ENTRYPOINT`

For instance, here is the `Dockerfile` used for the Rust application:

```Dockerfile{linenos=table}
# rust tooling is provided by `archlinux-rust`
FROM geal/archlinux-rust
MAINTAINER Geoffroy Couprie, contact@geoffroycouprie.com

# needed by rust
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

# relevant files are in `./source`
ADD . /source
WORKDIR /source

# Clever Cloud expects your app to listen on port 8080
EXPOSE 8080
RUN rustc -V

# Build your application
RUN cargo build

# Run the application with `CMD`
CMD cargo run
```

### Dockerized HHVM application Deployment

Deploying a [HHVM](https://hhvm.com/) application is a bit trickier as it needs to have both HHVM and [nginx](https://www.nginx.com/) running as daemons. To be able to have them running both, we need to put them in a start script:

```bash{linenos=table}
#!/bin/sh

hhvm --mode server -vServer.Type=fastcgi -vServer.Port=9000&

service nginx start

composer install

echo "App running on port 8080"

tail -f /var/log/hhvm/error.log
```

Since the two servers are running as daemons, we need to start a long-running process. In this case we use `tail -f`. We then add `start.sh` as the `CMD` in the `Dockerfile`

```Dockerfile{linenos=table}
# We need HHVM
FROM jolicode/hhvm

# We need nginx
RUN sudo apt-get update \
 && sudo apt-get install -y nginx

ADD . /root
RUN sudo chmod +x /root/start.sh

# Nginx configuration
ADD hhvm.hdf /etc/hhvm/server.hdf
ADD nginx.conf /etc/nginx/sites-available/hack.conf
RUN sudo ln -s /etc/nginx/sites-available/hack.conf /etc/nginx/sites-enabled/hack.conf
# Checking nginx config
RUN sudo nginx -t

RUN sudo chown -R www-data:www-data /root
WORKDIR /root

# The app needs to listen on port 8080
EXPOSE 8080

# Launch the start script
CMD ["sudo","/root/start.sh"]
```

### Sample dockerized applications

We provide a few examples of dockerized applications on Clever Cloud.

* [Elixir App](https://GitHub.com/CleverCloud/demo-docker-elixir/blob/master/Dockerfile)
* [Haskell App](https://GitHub.com/CleverCloud/demo-haskell)
* [Hack / HHVM App](https://GitHub.com/CleverCloud/demo-hhvm)
* [Seaside / Smalltalk App](https://GitHub.com/CleverCloud/demo-seaside)
* [Rust App](https://GitHub.com/CleverCloud/demo-rust)

{{% content/env-injection %}}

{{% content/deploy-git %}}

{{% content/link-addon %}}

{{% content/more-config %}}

{{% content/url_healthcheck %}}