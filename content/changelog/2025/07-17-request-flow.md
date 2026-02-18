---
title: 'Introducing Request Flow: use Redirection.io, Varnish, reverse proxy with no effort'
date: 2025-07-17
tags:
  - runtimes
  - configuration
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Ease your reverse proxy configuration more and more
excludeSearch: true
---

Clever Cloud exists to ease developers' life. For many years, you can use [Varnish in front of your application](/doc/develop/varnish/) just by adding a `varnish.vcl` file in your repository. For some months, you can also use [Redirection.io](/doc/reference/reference-environment-variables/#use-redirectionio-as-a-proxy) as a reverse proxy to handle redirects, rewrites, and more. In our latest release, we've gone a step further with Request Flow, available in new runtimes first :

- `frankenphp`
- `linux`
- `python` with `uv`
- `static`
- `v`

## Easier Redirection.io and Varnish activation

First, we've removed some barriers to use Redirection.io and Varnish:
- To setup Varnish add a `clevercloud/varnish.vcl` file or define it with `CC_VARNISH_FILE` environment variable
- To setup Redirection.io, `CC_REDIRECTIONIO_PROJECT_KEY` is now the only required environment variable

## Request Flow: automatic port configuration, easy ordering

In recent runtimes where Clever Cloud manage the port configuration (`frankenphp`, `static`), nothing else is needed. By default, Clever Cloud will configure the reverse proxy to listen on port `8080` and redirect to port `9000`. So in runtimes where the user controls the port configuration, the application must listen on port `9000` once Redirection.io or Varnish is activated.

If both are activated:
- Varnish is exposed first: listens on port `8080`, forward to Redirection.io on port `8081`
- Redirection.io listens on port `8081`, forward to the application on port `9000`

If you prefer to invert the order and expose Redirection.io first, set `CC_REQUEST_FLOW` environment variable to `redirectionio,varnish`.

## Use any reverse proxy with Request Flow

Last but not least, you can use any other middleware in the Request Flow. Just add `custom` value in the `CC_REQUEST_FLOW` chain and ports will be automatically configured accordingly. For example, if you set `CC_REQUEST_FLOW=redirectionio,custom,varnish`:

- Redirection.io listens on port `8080`, forward to custom middleware on port `8081`
- Custom middleware must listen on port `8081`, forward to Varnish on port `8082`
- Varnish listens on port `8082`, forward to the application on port `9000`

You can define the custom middleware command to start with `CC_REQUEST_FLOW_CUSTOM` environment variable, for example:

```bash
CC_REQUEST_FLOW_CUSTOM="./custom_reverse_proxy --listen @@LISTEN_PORT@@ --forward @@FORWARD_PORT@@"
```

As Request Flow is a new feature on Clever Cloud, feel free to [give us feedback](https://github.com/CleverCloud/Community/discussions/categories/paas-runtimes).
