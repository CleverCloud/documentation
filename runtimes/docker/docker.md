---
title: Deploy Docker images
shortdesc: Docker is an easy, lightweight virtualized environment for portable applications.
tags:
- docker
---

Clever Cloud allows you to deploy any application running inside a
Docker container. This page will explain how to set up your application
to run it on our service.

<div class="panel panel-warning">
  <div class="panel-heading">
     <h4>Note for Beta Version</h4>
  </div>
  <div class="panel-body">
    Docker support is still in beta. It does not yet support FS Buckets, validation of your Dockerfile, or other advanced features.
  </div>
</div>

## Overview

Docker is an easy, lightweight virtualized environment for portable
applications.

Docker containers can encapsulate any payload, and will run consistently
on and between virtually any server. The same container that a developer
builds and tests on a laptop will run at scale, in production, on VMs,
bare-metal servers, public instances, or combinations of the above.

## Create an application

1. Create a new app by clicking on the **Add an Application** button, in the sidebar.
2. Select a brand new instance (or a repository from GitHub if your account is linked).
3. Then select Docker in the platforms list.
4. Configure your scaling options.
5. Enter your application's name and description and click "Next". You can also select the region you want (North America or Europe).

## Requirements

Clever Cloud does not have a lot of requirements, here is what you *need*
to do to ensure that your application will run:

* Push on the **master branch**.

* Commit a file named **Dockerfile**, [Here is what it will look like](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices "Dockerfile")

* Listen on **port 8080**.

## Dockerfile contents

You can virtually put everything you want in your Dockerfile. The only
mandatory (for us) instruction to put in it is:

```bash
CMD <command to run>
```

**command to run**: this is the command that starts your
   application. Your application **must** listen on port 8080. It can be
   easier for you to put a script in your docker image and call it with
   the CMD instruction.

## Docker socket access

Some containers require access to the docker socket, to spawn sibling containers for instance.

<div class="panel panel-warning">
  <div class="panel-heading">
    <h4 class="panel-title">Giving access to the docker socket breaks isolation</h4>
  </div>
  <div class="panel-body">
    <p>
    Giving access to the docker socket breaks all isolation provided by docker. <b>DO NOT</b> give socket access to untrusted code.
    </p>
  </div>
</div>

You can make the docker socket available from inside the container by adding `CC_MOUNT_DOCKER_SOCKET=true` in your application's environment variables. In that case, docker is started in the namespaced mode, and in bridge network mode.

### Sample apps

We provide a few examples of dockerized applications on Clever Cloud.

[Elixir App](https://github.com/CleverCloud/demo-docker-elixir/blob/master/Dockerfile)
[Haskell App](https://github.com/CleverCloud/demo-haskell)
[Hack / HHVM App](https://github.com/CleverCloud/demo-hhvm)
[Seaside / Smalltalk App](https://github.com/CleverCloud/demo-seaside)
[Rust App](https://github.com/CleverCloud/demo-rust)

#### Deploying a Rust application

To make your dockerized application run on clever Cloud, you need to:

 - expose port 8080 in your docker file
 - run the application with `CMD` or `ENTRYPOINT`

For instance, here is the `Dockerfile` used for the Rust application.

```bash
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

### Deploying a HHVM application

Deploying a HHVM application is a bit trickier as it needs to have both HHVM
and nginx running as daemons. To be able to have them running both, we need to
put them in a start script:

```bash
#!/bin/sh

hhvm --mode server -vServer.Type=fastcgi -vServer.Port=9000&

service nginx start

composer install

echo "App running on port 8080"

tail -f /var/log/hhvm/error.log
```

Since the two servers are running as daemons, we need to start a long-running
process. In this case we use `tail -f`

We then add `start.sh` as the `CMD` in the `Dockerfile`

```bash
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
