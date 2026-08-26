---
type: docs
linkTitle: Request Flow
title: Request Flow
description: Automatically chain reverse proxies and middleware (Varnish, Redirection.io, OAuth2 Proxy, custom) in front of your application with Request Flow on Clever Cloud
keywords:
- request flow
- reverse proxy
- varnish
- redirection.io
- oauth2-proxy
- otoroshi
- middleware
- port configuration
aliases:
- /doc/request-flow
---

## Overview

Request Flow is Clever Cloud's automatic middleware chaining mechanism. It configures reverse proxies and services between the public port (`8080`) and your application, managing port allocation automatically. There is no need to manually configure listening ports for each service.

Request Flow is available for all runtimes except Docker, where you define and manage services within the container image.

## Supported services

| Service              | Activation                                          | Description                                                                                                                         |
| -------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `block`              | `CC_REQUEST_FLOW="block"`                           | Blocks public access with a `200 OK` response. Other ports remain accessible through [Network Groups](/doc/develop/network-groups/) |
| `custom`             | `CC_REQUEST_FLOW="custom"`                          | Any custom reverse proxy, started with `CC_REQUEST_FLOW_CUSTOM`                                                                     |
| `oauth2-proxy`       | `CC_REQUEST_FLOW="oauth2-proxy"`                    | Authentication proxy using [OAuth2 Proxy](/doc/develop/oauth2-proxy/)                                                               |
| `otoroshi-challenge` | `OTOROSHI_CHALLENGE_SECRET`                         | [Otoroshi](/doc/addons/otoroshi/) challenge verification proxy                                                                      |
| `redirectionio`      | `CC_REDIRECTIONIO_PROJECT_KEY`                      | HTTP redirects, rewrites, SEO                                                                                                       |
| `varnish`            | `clevercloud/varnish.vcl` file or `CC_VARNISH_FILE` | HTTP cache accelerator                                                                                                              |

## Automatic detection

When no `CC_REQUEST_FLOW` is set, Clever Cloud detects and activates services automatically:

- If `OTOROSHI_CHALLENGE_SECRET` is set, Otoroshi Challenge is activated
- If a `clevercloud/varnish.vcl` file exists (or `CC_VARNISH_FILE` is set), Varnish is activated
- If `CC_REDIRECTIONIO_PROJECT_KEY` is set, Redirection.io is activated

When automatically detected, Otoroshi Challenge, Varnish and Redirection.io can run simultaneously, in this order: Otoroshi Challenge, Varnish, then Redirection.io.

No automatic detection exists for `oauth2-proxy` and `custom`. Only `CC_REQUEST_FLOW` activates them. Setting this variable also replaces automatic detection for the whole chain, so a `CC_REQUEST_FLOW="oauth2-proxy"` on an application holding a `clevercloud/varnish.vcl` file starts OAuth2 Proxy alone. List every middleware you need: `CC_REQUEST_FLOW="oauth2-proxy,varnish"`.

## Port management

Request Flow allocates middleware ports in a chain from port `8080` (public) down to your application. For runtimes where you configure the application HTTP server yourself:

- With no middleware: your application listens directly on port `8080`
- With one middleware: the middleware listens on `8080`, forwards to your application on port `9000`
- With two middleware services: the first listens on `8080`, forwards to the second on `8081`, which forwards to the application on `9000`

> [!NOTE]
> FrankenPHP, Java, PHP, legacy Python, Ruby and Static applications need no additional configuration, as Clever Cloud manages their web server or port transparently. Python applications using native uv support manage their own HTTP server and follow the port rule above.

In every runtime where your application manages its own HTTP server, have it listen on `0.0.0.0:$PORT` and set `PORT` to `9000` when a middleware is active:

```bash
PORT="9000"
```

## Explicit configuration with CC_REQUEST_FLOW

To control the order or selection of middleware, set `CC_REQUEST_FLOW` to a comma-separated list of services:

```bash
CC_REQUEST_FLOW="redirectionio,varnish"
```

For an application that manages its own HTTP server, this inverts the default order: Redirection.io listens on `8080`, forwards to Varnish on `8081`, which forwards to the application on `9000`.

### Disable Request Flow

To disable Request Flow entirely and have your application listen directly on port `8080`:

```bash
CC_REQUEST_FLOW="disable"
```

## Block public access

Setting `CC_REQUEST_FLOW=block` replaces the public endpoint (port `8080`) with a service that responds `200 OK` to every request. Your application still runs normally, but no external HTTP traffic reaches it through the default route. This is useful for applications that should only communicate through [Network Groups](/doc/develop/network-groups/) or internal services, while keeping the public health check endpoint alive.

When `block` is set, all other Request Flow services are ignored.

```bash
CC_REQUEST_FLOW="block"
```

### Health check with block mode

With `block` enabled, the deployment health check only verifies that the blocking service listens on port `8080` and responds `200 OK`. It doesn't send an HTTP request to your application, including when you configure [`CC_HEALTH_CHECK_PATH` or `CC_HEALTH_CHECK_PATH_0` to `CC_HEALTH_CHECK_PATH_5`](/doc/develop/healthcheck/).

## Custom middleware

To insert a custom reverse proxy in the chain, add `custom` to `CC_REQUEST_FLOW` and define the command with `CC_REQUEST_FLOW_CUSTOM`. The deployment process replaces `@@LISTEN_PORT@@` and `@@FORWARD_PORT@@` placeholders with the actual allocated ports:

```bash
CC_REQUEST_FLOW="redirectionio,custom,varnish"
CC_REQUEST_FLOW_CUSTOM="./my-proxy --listen @@LISTEN_PORT@@ --forward @@FORWARD_PORT@@"
```

For an application that manages its own HTTP server, this example produces the following chain:

- Redirection.io listens on `8080`, forwards to custom middleware on `8081`
- Custom middleware listens on `8081`, forwards to Varnish on `8082`
- Varnish listens on `8082`, forwards to the application on `9000`

## Environment variables reference

| Name                           | Description                                                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `CC_REQUEST_FLOW`              | Comma-separated list of middleware to chain (e.g. `varnish,redirectionio`). Special values: `disable`, `block` |
| `CC_REQUEST_FLOW_CUSTOM`       | Command to start a custom middleware. Must contain `@@LISTEN_PORT@@` and `@@FORWARD_PORT@@` placeholders       |
| `CC_REDIRECTIONIO_PROJECT_KEY` | Redirection.io project key. Activates Redirection.io in the request flow                                       |
| `CC_VARNISH_FILE`              | Path to a custom Varnish VCL file (default: `clevercloud/varnish.vcl`)                                         |
| `OTOROSHI_CHALLENGE_SECRET`    | Otoroshi challenge secret. Activates Otoroshi Challenge verification in the request flow                       |

## Troubleshooting

A middleware that fails to start leaves the public port closed, and the deployment ends with `Your application is not listening on 8080`. This message names the public port of the chain, which belongs to the first middleware rather than to your application. Read the preceding deployment logs: the middleware logs its own error before exiting.

The message `Some software are not listening as expected: 9000` means the opposite. Every middleware runs, and your application doesn't listen on the port the chain forwards to. Check the [port management](#port-management) section for the port your runtime expects.

- [Learn more about Varnish on Clever Cloud](/doc/develop/varnish/)
- [Learn more about Redirection.io](https://redirection.io/)
- [Learn more about OAuth2 Proxy on Clever Cloud](/doc/develop/oauth2-proxy/)
- [Learn more about Otoroshi on Clever Cloud](/doc/addons/otoroshi/)
- [Learn more about Network Groups](/doc/develop/network-groups/)
