---
title: "Images update: Node.js 26.13, Varnish 9.0, Composer 2.11, Clever Tools 5.3, Python variables renaming"
description: Node.js 26.13 as the default LTS version, Varnish 9.0, Composer 2.11 and 2.2.31 security fixes, Clever Tools 5.3, CC_ prefixed names for Python variables, stricter value checks for environment variables, and a fix for Java tasks
date: 2026-11-03
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

We updated all our images. Deployment is in progress for all our users.

- **Common:**
  - Chromium 156.0.8078.73
  - Clever Tools 5.3.0
  - ExifTool 13.60
  - gifsicle 1.98
  - iproute2 7.3.0
  - Mise 2026.10.25
  - SQLite 3.54.1
  - Tailscale 1.104.4
  - Varnish 9.0.3
  - varnish-modules 0.28.0
- **.NET:**
  - Update to 8.0.133
  - Update to 9.0.123
  - Update to 10.0.114
- **Erlang/Elixir:**
  - Elixir 1.18.6
  - Elixir 1.19.7
  - Elixir 1.20.5
- **Node.js:**
  - Update to 26.13.0 (npm 11.20.0)
- **PHP:**
  - Composer 2.2.31
  - Composer 2.11.1
  - gRPC extension 1.85.0
- **Python:**
  - uv 0.13.6
- **Ruby:**
  - Fixes for Ruby 3.2/3.3

## Varnish 9.0

[Varnish](/doc/develop/request-flow/varnish/) now runs version 9.0, with varnish-modules 0.28. This major release changes how Varnish handles requests to an absolute URI, such as `GET http://example.com HTTP/1.1`: it now requires a host and moves it to the `Host` header, leaving the path in `req.url`. The built-in VCL also requires URLs to start with `/`, accepts `*` for `OPTIONS` requests and doesn't check `CONNECT` requests, which remain denied by default. This fixes the [VSV00018](https://vinyl-cache.org/security/VSV00018.html) vulnerability.

It also removes the `beresp.storage_hint` VCL variable, so a `varnish.vcl` file that still uses it no longer compiles: remove it before your next deployment. `req.ttl` becomes `req.max_age`, the previous name still works but is deprecated. For requests without a body, Varnish now sends a `Content-Length: 0` header to your application, except for `GET`, `HEAD`, `DELETE`, `OPTIONS` and `TRACE` methods.

In the coming weeks, we will start a migration to the open source [Vinyl Cache](https://vinyl-cache.org/) project. We will roll it out progressively, so you have time to adapt your applications.

- [Read the Upgrading to Varnish 9.0 guide](https://www.varnish.org/docs/whats-new/upgrading-9.0/)

## Composer 2.11

[Composer](/doc/deploy/applications/php/composer/) 2.11.1, used by default, and 2.2.31, used with `CC_COMPOSER_VERSION=lts`, are security releases. They fix package names able to write files outside the `vendor` folder during installation, and inline repository HTTP headers, such as API tokens, written into `composer.lock`. Both now reject TLS connections presenting the intermediate certificates of the [eMudhra distrust](/changelog/2026/10-21-images-update/#emudhra-certificate-authorities-distrust).

Composer 2.11 removes the `source-fallback` option introduced in 2.10: when a package archive fails to download, Composer no longer falls back to a source install. It also adds a `cooldown` policy, which withholds newly released package versions for a configurable period to reduce exposure to compromised releases.

- [Read the Composer 2.11 release announcement](https://blog.packagist.com/composer-2-11-release/)

## Node.js 26 LTS by default

Node.js 26 is now the latest long-term support (LTS) branch, so our images include Node.js 26.13.0 instead of a 24.x release. Your application uses it when it doesn't request a version through `CC_NODE_VERSION` or `engines.node` in `package.json`. Applications that request a version keep the same behavior.

If your application isn't compatible with Node.js 26 yet, set `CC_NODE_VERSION` to `24` to stay on the Node.js 24 LTS branch, then redeploy:

```bash
clever env set CC_NODE_VERSION 24
clever restart --without-cache
```

- [Learn more about the Node.js release schedule](https://nodejs.org/en/about/previous-releases)
- [Learn more about Node.js versions on Clever Cloud](/doc/deploy/applications/nodejs/#set-nodejs-version)

## Python environment variables renaming

Python applications now accept `CC_` prefixed names for the uWSGI, Gunicorn and `setup.py` [configuration variables](/doc/deploy/applications/python/servers/):

- `CC_PYTHON_SETUP_PY_GOAL` replaces `PYTHON_SETUP_PY_GOAL`
- `CC_UWSGI_ASYNC` replaces `UWSGI_ASYNC`
- `CC_UWSGI_ASYNC_ENGINE` replaces `UWSGI_ASYNC_ENGINE`
- `CC_UWSGI_HARAKIRI` replaces `HARAKIRI`
- `CC_UWSGI_INTERCEPT_ERRORS` replaces `UWSGI_INTERCEPT_ERRORS`
- `CC_UWSGI_WORKERS` replaces `WSGI_WORKERS`, and also sets the number of Gunicorn workers and threads

The previous names still work, with a deprecation warning in the deployment logs. If you set both the previous and the new name of a variable, the deployment fails: keep only the new one.

## Stricter environment variable values

Following the [stricter environment variable names](/changelog/2026/10-14-images-update/#stricter-environment-variable-names), more variables now have their value checked before the build, mostly in Docker, Elixir, Java, Python and Ruby applications. An invalid value makes the deployment fail with an error naming the variable, where previous releases ignored it or used the default value. For example, `CC_PUMA_WORKERS`, `CC_UWSGI_HARAKIRI` or `CC_UWSGI_WORKERS` must be integers. These newly checked variables also reject empty values: remove the variable to use its default value.

`CC_DISABLE_JVM_AGENT` now disables the JVM metrics agent only when set to a true value: previous releases disabled it for any non-empty value.

`IGNORE_FROM_BUILDCACHE` becomes a deprecated name of `CC_IGNORE_FROM_BUILDCACHE`. Previous releases merged the paths of both variables, setting both now makes the deployment fail.

## Java tasks fix

Since the [21 October release](/changelog/2026/10-21-images-update/), the deployment of a Java [Clever Task](/doc/develop/tasks/) failed without running its `CC_RUN_COMMAND`. Java tasks now run their command again.

## Linux Kernel

Kernel is [now updated independently](/changelog/2026/05-12-linux-kernel-7.0.6). Current version is 7.2.15.
