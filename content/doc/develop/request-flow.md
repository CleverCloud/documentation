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

Request Flow is available in the following runtimes:

- [.NET](/doc/applications/dotnet/)
- [Elixir](/doc/applications/elixir/)
- [FrankenPHP](/doc/applications/frankenphp/)
- [Go](/doc/applications/golang/)
- [Haskell](/doc/applications/haskell/)
- [Java](/doc/applications/java/)
- [Linux](/doc/applications/linux/)
- [Meteor](/doc/applications/meteor/)
- [Node.js & Bun](/doc/applications/nodejs/)
- [PHP with Apache](/doc/applications/php/)
- [Python with uv](/doc/applications/python/uv/)
- [Rust](/doc/applications/rust/)
- [Scala](/doc/applications/scala/)
- [Static](/doc/applications/static/)
- [Static with Apache](/doc/applications/static-apache/)
- [V (Vlang)](/doc/applications/v/)

## Supported services

| Service | Activation | Description |
|---------|-----------|-------------|
| `block` | `CC_REQUEST_FLOW="block"` | Blocks public access with a `200 OK` response. Other ports remain accessible through [Network Groups](/doc/develop/network-groups/) |
| `custom` | `CC_REQUEST_FLOW_CUSTOM` | Any custom reverse proxy |
| `oauth2-proxy` | `CC_REQUEST_FLOW="oauth2-proxy"` | Authentication proxy using [OAuth2 Proxy](https://oauth2-proxy.github.io/oauth2-proxy/) |
| `otoroshi-challenge` | `OTOROSHI_CHALLENGE_SECRET` | [Otoroshi](/doc/addons/otoroshi/) challenge verification proxy |
| `redirectionio` | `CC_REDIRECTIONIO_PROJECT_KEY` | HTTP redirects, rewrites, SEO |
| `varnish` | `clevercloud/varnish.vcl` file or `CC_VARNISH_FILE` | HTTP cache accelerator |

## Automatic detection

When no `CC_REQUEST_FLOW` is set, Clever Cloud detects and activates services automatically:

- If `OTOROSHI_CHALLENGE_SECRET` is set, Otoroshi Challenge is activated
- If a `clevercloud/varnish.vcl` file exists (or `CC_VARNISH_FILE` is set), Varnish is activated
- If `CC_REDIRECTIONIO_PROJECT_KEY` is set, Redirection.io is activated

All three can be active simultaneously. Default order: Otoroshi Challenge first, then Varnish, then Redirection.io.

## Port management

Request Flow allocates ports in a chain from port `8080` (public) down to the application:

- With no middleware: your application listens directly on port `8080`
- With one middleware: the middleware listens on `8080`, forwards to your application on port `9000`
- With two middleware: first listens on `8080`, forwards to second on `8081`, which forwards to the application on `9000`

Your application must listen on port `8080` when no middleware is active, or on port `9000` when at least one middleware is configured.

> [!NOTE]
> In runtimes where Clever Cloud manages the port configuration (FrankenPHP, Java, PHP, Static), port allocation is handled transparently with no additional configuration.

## Explicit configuration with CC_REQUEST_FLOW

To control the order or selection of middleware, set `CC_REQUEST_FLOW` to a comma-separated list of services:

```bash
CC_REQUEST_FLOW="redirectionio,varnish"
```

This inverts the default order: Redirection.io listens on `8080`, forwards to Varnish on `8081`, which forwards to the application on `9000`.

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

By default, `block` responds `200 OK` regardless of your application's actual state. If [`CC_HEALTH_CHECK_PATH` or `CC_HEALTH_CHECK_PATH_0` to `CC_HEALTH_CHECK_PATH_5`](/doc/develop/healthcheck/) are configured, the blocking service also checks these paths on your application and responds accordingly:

- `200 OK` if all configured paths return a `2xx` status
- `503 Service Unavailable` if the application is down or any path returns a non-`2xx` status

This way, the platform's health check still reflects the actual state of your application even when public traffic is blocked.

## Custom middleware

To insert a custom reverse proxy in the chain, add `custom` to `CC_REQUEST_FLOW` and define the command with `CC_REQUEST_FLOW_CUSTOM`. The deployment process replaces `@@LISTEN_PORT@@` and `@@FORWARD_PORT@@` placeholders with the actual allocated ports:

```bash
CC_REQUEST_FLOW="redirectionio,custom,varnish"
CC_REQUEST_FLOW_CUSTOM="./my-proxy --listen @@LISTEN_PORT@@ --forward @@FORWARD_PORT@@"
```

In this example:
- Redirection.io listens on `8080`, forwards to custom middleware on `8081`
- Custom middleware listens on `8081`, forwards to Varnish on `8082`
- Varnish listens on `8082`, forwards to the application on `9000`

## Environment variables reference

| Name | Description |
|------|-------------|
| `CC_REQUEST_FLOW` | Comma-separated list of middleware to chain (e.g. `varnish,redirectionio`). Special values: `disable`, `block` |
| `CC_REQUEST_FLOW_CUSTOM` | Command to start a custom middleware. Must contain `@@LISTEN_PORT@@` and `@@FORWARD_PORT@@` placeholders |
| `CC_REDIRECTIONIO_PROJECT_KEY` | Redirection.io project key. Activates Redirection.io in the request flow |
| `CC_VARNISH_FILE` | Path to a custom Varnish VCL file (default: `clevercloud/varnish.vcl`) |
| `OTOROSHI_CHALLENGE_SECRET` | Otoroshi challenge secret. Activates Otoroshi Challenge verification in the request flow |

- [Learn more about Varnish on Clever Cloud](/doc/develop/varnish/)
- [Learn more about Redirection.io](https://redirection.io/)
- [Learn more about OAuth2 Proxy](https://oauth2-proxy.github.io/oauth2-proxy/)
- [Learn more about Otoroshi on Clever Cloud](/doc/addons/otoroshi/)
- [Learn more about Network Groups](/doc/develop/network-groups/)
