---
title: "Images update: Elixir 1.20, Erlang 29, Rust 1.99, Hugo 0.167, OpenSSL 3.6"
description: Runtime updates for Elixir, Erlang, Go, Java, PHP, Python and Rust, with Hugo 0.165 to 0.167, OpenSSL 3.6, Gradle 9.8 and Clever Tools 5.1
date: 2026-10-09
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
  - Apache 2.4.69
  - Chromium 154.0.8037.92
  - Clever Tools 5.1.1
  - Git 2.56.0
  - Mise 2026.9.16
  - NGINX 1.30.5
  - OAuth2 Proxy 7.15.5
  - OpenSSH 10.6_p1
  - OpenSSL 3.6.5
  - Poppler 26.10.0
  - SOPS 3.13.3
  - Tailscale 1.102.5
  - Zellij 0.45.1
- **Erlang/Elixir:**
  - Elixir 1.20.4 is now available
  - Erlang 26.2.5.21
  - Erlang 27.3.4.18
  - Erlang 28.5.0.7
  - Erlang 29.1.1 is now available
  - rebar3 3.27.1
- **FrankenPHP:**
  - Update to 1.12.7 (For `CC_PHP_VERSION=8.5`)
- **Go:**
  - Update to 1.27.1
- **Java:**
  - Update to 1.8.0.504_p01
  - Update to 11.0.32.1_p1
  - Update to 17.0.20.1_p1
  - Update to 21.0.12.1_p1
  - Update to 25.0.4.1_p1
  - Gradle 9.8.0
  - Maven 3.9.16
- **Node.js:**
  - Yarn 4.18.1
- **PHP:**
  - Update to 8.2.34
  - Update to 8.3.35
  - Update to 8.4.26
  - Update to 8.5.11
  - Symfony CLI 5.22.0
  - AMQP extension 2.2.0
  - Blackfire extension 2026.9.2
  - Event extension 3.1.6
  - Excimer extension 1.2.6
  - gRPC extension 1.84.0
  - Mailparse extension 3.2.0
  - Maxmind DB extension 1.14.0
  - New Relic extension 12.11.0.40
  - OAuth extension 2.0.13
  - OpenTelemetry extension 1.4.2
  - Protobuf extension 4.33.6
  - Solr extension 2.9.3
  - SQLSRV and PDO_SQLSRV extensions 5.13.3
  - Tideways extension 5.46.0
- **Python:**
  - Update to 3.10.22
  - Update to 3.11.17
  - Update to 3.12.15
  - Update to 3.13.16
  - Update to 3.14.8
  - uv 0.12.21
- **Rust:**
  - Update to 1.99.0
  - rustup 1.29.1
- **Static:**
  - Caddy 2.11.7
  - Hugo 0.165.0, 0.166.0 and 0.167.0 are now available
  - Zola 0.23.6

## Elixir 1.20 and Erlang/OTP 29

Elixir 1.20 is now available and runs on Erlang/OTP 29. Elixir 1.19 remains the default version, so set `CC_ELIXIR_VERSION` to use the new release:

```bash
clever env set CC_ELIXIR_VERSION 1.20
```

- [Learn more about Elixir on Clever Cloud](/doc/deploy/applications/elixir/)

## Hugo 0.165 to 0.167

Static applications can now use Hugo `0.165`, `0.166` or `0.167` through `CC_HUGO_VERSION`. If you don't set it, `0.163` remains the default.

- [Learn more about Hugo on Clever Cloud](/doc/deploy/applications/static/#static-site-generators-ssg-auto-build)

## Webroot validation in PHP

PHP applications now always serve the directory set in `CC_WEBROOT`. Its value must be an absolute path from the root of your project, such as `/public`, and can't contain `..`, or the deployment fails with an error naming the variable.

Previous releases silently ignored an invalid value or a missing directory, and served the root of your project instead. If the directory doesn't exist after the build, the deployment logs now show a warning.

`CC_OPCACHE_MAX_ACCELERATED_FILES` now applies the value you set, which previous releases ignored. `ALWAYS_POPULATE_RAW_POST_DATA`, which only affected PHP 5.6, is no longer supported, and the documentation no longer lists the `CC_LDAP_CA_CERT` and `LDAPTLS_CACERT` variables, which had no effect.

- [Learn more about PHP on Clever Cloud](/doc/deploy/applications/php/)

## PHP 8.5 by default in the next release

[As announced](/changelog/2026/09-01-php-8.5-default/), PHP 8.5 was to become the default version with this release. As this release already brings significant changes to the PHP runtime, the switch is postponed to the next one.

Until then, PHP and FrankenPHP applications deployed without `CC_PHP_VERSION`, or with `CC_PHP_VERSION=8`, keep running PHP 8.4. If you want to stay on this version once PHP 8.5 becomes the default, set it explicitly:

```bash
clever env set CC_PHP_VERSION 8.4
```

## Clearer configuration errors

When an environment variable or a configuration file holds an invalid value, the deployment now stops with an error that names it and explains the expected format, for example a malformed `clevercloud/cron.json` or a non-numeric `CC_NGINX_PROXY_BUFFER_SIZE`. The content of a `clevercloud/python_version` file now goes through the same validation as `CC_PYTHON_VERSION`, instead of silently falling back to the default version.

## Linux Kernel

Kernel is [now updated independently](/changelog/2026/05-12-linux-kernel-7.0.6). Current version is 7.2.9.
