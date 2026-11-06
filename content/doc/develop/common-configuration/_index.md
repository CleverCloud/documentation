---
type: docs
linkTitle: Configure applications
title: Configure applications
description: Settings common to all Clever Cloud applications, whatever their runtime, from the port your application listens on to its region, zero downtime deployment, and sticky sessions
keywords:
- configuration
- port
- listen
- 8080
- region
- zero downtime
- sticky sessions
- force https
- dedicated build instance
- instances
- ssh-keys
- build-hooks
- deployment
- settings
aliases:
- /doc/clever-cloud-overview/common-application-configuration
- /doc/common-configuration
- /doc/clever-cloud-overview/common-application-configuration/
- /doc/reference/common-configuration
---

Each runtime has its own options, described on its page. The settings of this page apply to all applications, whatever their runtime.

## Listen on the right port

Clever Cloud sends the HTTP traffic of your application to port `8080` of its instances. If your application starts its own HTTP server, make it listen on all interfaces, on the port of the `PORT` environment variable: `0.0.0.0:$PORT`.

Clever Cloud sets `PORT` to `8080` for you: don't add it to your environment variables or your code. For instance, with Node.js:

```javascript {filename="server.js"}
const http = require("node:http");

http.createServer((req, res) => res.end("Hello")).listen(process.env.PORT, "0.0.0.0");
```

A server receiving the public traffic and listening only on `localhost` or `127.0.0.1` isn't reachable: the deployment fails with `Your application is listening on localhost instead of publicly`. An application running as a [Clever Task](/doc/develop/tasks/) doesn't need an HTTP server.

### With Request Flow

When a [Request Flow](/doc/develop/request-flow/) middleware is active, such as Varnish or Redirection.io, it listens on port `8080` and forwards the requests to port `9000`. Clever Cloud doesn't change `PORT` for you: set `PORT=9000` in the environment variables of your application.

With [`CC_REQUEST_FLOW=block`](/doc/develop/request-flow/#block-public-access), no request reaches your application: it doesn't need to listen on port `9000`.

```bash
clever env set PORT 9000
```

### Frameworks listening on another port

Some frameworks don't read `PORT`, or listen on another port by default, such as ASP.NET Core on `localhost:5000`. Configure them on `0.0.0.0:8080`, or on `0.0.0.0:9000` with Request Flow, through their own variable, an option of their start command, or their configuration file. Each [runtime page](/doc/deploy/applications/) gives the setting to use.

### Runtimes with a managed web server

On some runtimes, Clever Cloud starts the web server and sets its port, Request Flow included, you have nothing to configure:

- [FrankenPHP](/doc/deploy/applications/frankenphp/), [PHP with Apache](/doc/deploy/applications/php/), and [Static](/doc/deploy/applications/static/)
- [Java](/doc/deploy/applications/java/), which receives the port as the `http.port` system property
- [Python](/doc/deploy/applications/python/) with its supported backends, and [Ruby](/doc/deploy/applications/ruby/)

If you replace the server with `CC_RUN_COMMAND`, your command starts the HTTP server: the rule of this section applies to it. On Static, a custom Caddyfile also sets its own address: listen on `:{$PORT}`. In a Python application without uv, Nginx stays in front of your command: it must listen on port `9000`, so set `PORT=9000` even without Request Flow.

[Docker](/doc/deploy/applications/docker/#ports-mapping-and-network-groups) applications work differently: the container listens on port `8080`, or on `CC_DOCKER_EXPOSED_HTTP_PORT`. Request Flow isn't available.

### Other ports

The public traffic only reaches port `8080`. The other ports of an instance are reachable from:

- A [Network Group](/doc/network/network-groups/), whose members reach every port your application listens on
- A [TCP redirection](/doc/develop/common-configuration/tcp-redirections/), which forwards a public TCP port to port `4040`

## Application settings

Each application has settings you change in the **Information** menu of the [Console](https://console.clever-cloud.com). With [Clever Tools](/doc/manage/cli/applications/configuration/#config), use `clever config` for most of them:

```bash
clever config get zero-downtime
clever config set sticky-sessions true
```

### Region

The region sets where your instances run. Choose it when you create your application, for instance with the `--region rbx` option of `clever create`, and change it from the Console. Your application moves at its next deployment, and its `cleverapps.io` domains follow it. Your own domains need the new DNS records shown in the **Domain names** menu.

PHP applications can't change region, and an [FS Bucket](/doc/deploy/storage/fs-bucket/) only mounts in its own region.

- [Learn how to move an application and its add-ons to another region](/doc/manage/zone-migration/)

### Zero downtime deployment

Enabled by default. During a deployment, the new instances start and must pass the [health check](/doc/develop/common-configuration/healthcheck/) before the old ones stop. When you disable it, the old instances stop first, and your application doesn't answer during the deployment. As old and new instances run at the same time, make sure your application supports it, for instance for database migrations.

### Sticky sessions

Disabled by default. With several instances, the load balancer sends the requests of a visitor to the same instance, through the `X-Clever-Cloud-Sticky-Id` cookie. Enable it if your application keeps sessions in memory. These sessions don't survive an instance that stops, as during a deployment. To keep them, store them in a [Materia KV](/doc/deploy/databases/materia-kv/) or [Redis®](/doc/deploy/databases/redis/) add-on, so that any instance serves them.

### Dedicated build instance

Disabled by default, unless you choose a build instance size when you create your application in the Console. Your application then builds on a separate instance of this size, before running on its own instances. A small application can then build with more memory and CPU. Starting this instance takes a few seconds, while a larger instance can shorten the build. To set its size with Clever Tools:

```bash
clever scale --build-flavor M
```

To disable it:

```bash
clever scale --build-flavor disabled
```

Applications running on `pico` or `nano` instances always build on a dedicated instance: their memory is too low for most builds. It uses the build size of your application, which defaults to `S` for Node.js or `M` for Rust.

### Cancel deployment on push

Enabled by default. A new `git push` cancels the ongoing deployment, and starts a new one with the latest commit.

### Force HTTPS

Enabled by default. The load balancer redirects HTTP requests to HTTPS, with a `301 Moved Permanently` status code.

### Clever Task

Disabled by default. At each deployment, your application runs its command, then its instances stop. It receives no public HTTP or TCP traffic, and doesn't need to listen on a port.

- [Learn more about Clever Tasks](/doc/develop/tasks/)

## Private SSH key

To fetch private dependencies over SSH, provide a private key for your application.
Clever Cloud installs it in `~/.ssh/` before the build. Register its public key
with the service that hosts the dependencies. This key is separate from the
[public keys on your Clever Cloud account](/doc/account-billing/ssh-keys/),
which authenticate your Git deployments and access to instances. Use a key
without a passphrase: the deployment can't unlock it interactively.

Store the key in the `CC_SSH_PRIVATE_KEY` environment variable of your
application, not in your repository. Its value is the whole content of the
private key file, from the `-----BEGIN` line to the `-----END` line, line
breaks included.

With Clever Tools, write `--` before the key, otherwise Clever Tools reads its
`-----BEGIN` line as an option:

```bash
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519_dependencies
clever env set CC_SSH_PRIVATE_KEY -- "$(cat ~/.ssh/id_ed25519_dependencies)"
```

Clever Cloud saves the key as `~/.ssh/id_ed25519` by default. To change its
name, set `CC_SSH_PRIVATE_KEY_FILE` to a file name, such as `dependencies_key`.
This value is a file name within `~/.ssh/`, not a path, and can't contain `/`.

## Other settings

{{< cards >}}
  {{< card link="/developers/doc/develop/common-configuration/build-hooks" title="Deployment hooks" subtitle="Run your own commands before and after the build, and at startup" icon="rocket-launch" >}}
  {{< card link="/developers/doc/develop/common-configuration/domain-names" title="Domain names" subtitle="Serve your application on your own domains, or on a shared path" icon="globe-alt" >}}
  {{< card link="/developers/doc/develop/common-configuration/environment-variables" title="Environment variables" subtitle="Configure your application and get the credentials of its add-ons" icon="pencil-square" >}}
  {{< card link="/developers/doc/develop/common-configuration/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/develop/common-configuration/lifecycle" title="Lifecycle" subtitle="Restart, stop, or delete your application, and redeploy a commit" icon="arrow-path" >}}
  {{< card link="/developers/doc/develop/common-configuration/scaling" title="Scaling" subtitle="Set the size and number of instances, or let them follow the load" icon="server-stack" >}}
  {{< card link="/developers/doc/develop/common-configuration/tcp-redirections" title="TCP redirections" subtitle="Expose a public TCP port of your application for non-HTTP protocols" icon="tcp-ip-service" >}}
  {{< card link="/developers/doc/develop/common-configuration/workers" title="Workers" subtitle="Keep background processes running next to your application" icon="cog-6-tooth" >}}
{{< /cards >}}
