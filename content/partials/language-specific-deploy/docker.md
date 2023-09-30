## Configure your Docker application

### Mandatory configuration

Be sure that you:

* push on the **master branch**.
* have and commit a file named **Dockerfile** or use the **CC_DOCKERFILE** [environment variable]({{< ref "doc/reference/reference-environment-variables.md#docker" >}}) if your Dockerfile has a different name, [Here is what it will look like](https://docs.docker.com/develop/develop-images/dockerfile_best-practices "Dockerfile").
* run the application with `CMD` or `ENTRYPOINT` in your Dockerfile.
* listen on HTTP **port 8080** by default (you can set your own port using `CC_DOCKER_EXPOSED_HTTP_PORT=<port>` [environment variable](#setting-up-environment-variables-on-clever-cloud)).

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

Clever Cloud enables you to use TCP over Docker applications using using the [environment variable](#setting-up-environment-variables-on-clever-cloud) `CC_DOCKER_EXPOSED_TCP_PORT=<port>`. Refer to the documentation page to know how to create [TCP redirections]({{< ref "doc/administrate/tcp-redirections.md" >}}].

### Docker socket access

Some containers require access to the docker socket, to spawn sibling containers for instance.

{{< callout type="warning" >}}
    <p>
    Giving access to the docker socket breaks all isolation provided by docker. **DO NOT** give socket access to untrusted code.
    </p>
{{< /callout >}}


You can make the docker socket available from inside the container by adding the `CC_MOUNT_DOCKER_SOCKET=true` [environment variable](#setting-up-environment-variables-on-clever-cloud). In that case, docker is started in the namespaced mode, and in bridge network mode.

### Private registry

We support pulling private images through the `docker build` command. To login to a private registry, you need to set a few [environment variables](#setting-up-environment-variables-on-clever-cloud):

- `CC_DOCKER_LOGIN_USERNAME`: the username to use to login
- `CC_DOCKER_LOGIN_PASSWORD`: the password of your username
- `CC_DOCKER_LOGIN_SERVER` (optional): the server of your private registry. Defaults to Docker's public registry.

This uses the `docker login` command under the hood.

### Enable IPv6 networking

You can activate the support of IPv6 with a IPv6 subnet in the docker daemon by adding the `CC_DOCKER_FIXED-CIDR-V6=<IP>` [environment variable](#setting-up-environment-variables-on-clever-cloud).

### Build-time variables

You can use the [ARG](https://docs.docker.com/engine/reference/builder/#arg) instruction to define build-time environment variables.

Every environment variable defined for your application will be passed as a build environment variable using the `--build-arg=<ENV>` parameter during the `docker build` phase.


### Dockerized Rust application Deployment
To make your dockerized application run on clever Cloud, you need to:

* expose port 8080 in your docker file
* run the application with `CMD` or `ENTRYPOINT`

For instance, here is the `Dockerfile` used for the Rust application:

```Dockerfile
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

```bash
#!/bin/sh

hhvm --mode server -vServer.Type=fastcgi -vServer.Port=9000&

service nginx start

composer install

echo "App running on port 8080"

tail -f /var/log/hhvm/error.log
```

Since the two servers are running as daemons, we need to start a long-running process. In this case we use `tail -f`. We then add `start.sh` as the `CMD` in the `Dockerfile`

```Dockerfile
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
