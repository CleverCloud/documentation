---
title: "Images update: Clever Tools 5.0, Go 1.27, Rust 1.98, Gradle 9.7"
description: Runtime updates for Elixir, Erlang, Go, PHP, Ruby and Rust, with Clever Tools 5.0, Gradle 9.7, LibreOffice 26.8 and Symfony CLI 5.20
date: 2026-09-23
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
  - Anubis 1.27.0
  - Chromium 153.0.8010.52
  - Clever Tools 5.0.2
  - curl 8.22.0
  - glibc 2.44
  - LibreOffice 26.8.0.3
  - OAuth2 Proxy 7.15.4
  - Otoroshictl 0.0.18
  - Poppler 26.09.0
  - Redis 8.10.2
  - rsync 3.5.1
- **Docker:**
  - Update to 29.8.1
  - Buildx 0.37.0
- **Erlang/Elixir:**
  - Elixir 1.18.5
  - Elixir 1.19.6
  - Erlang 27.3.4.17
  - Erlang 28.5.0.6
- **Go:**
  - Update to 1.27.0
- **Java:**
  - Gradle 9.7.1
- **Node.js:**
  - nvm 0.40.7
- **PHP:**
  - Update to 8.4.25
  - Update to 8.5.10
  - Composer 2.2.30
  - Composer 2.10.3
  - Symfony CLI 5.20.0
- **Python:**
  - uv 0.12.17
- **Ruby:**
  - Update to 3.4.10
  - Update to 4.0.7
- **Rust:**
  - Update to 1.98.1
- **Static:**
  - mdBook 0.5.4
  - Static Web Server 2.44.0
- **V:**
  - Update to 0.5.2

## Health check paths and the Otoroshi challenge

Otoroshictl 0.0.18 excludes health check paths from the [Otoroshi challenge](/doc/develop/request-flow/otoroshi-challenge/). The middleware reads `CC_HEALTH_CHECK_PATH` and its numbered variants, then forwards `GET` and `HEAD` requests on these paths to your application without asking for a challenge. Setting a health check path on a protected application no longer fails the deployment because of a missing challenge, as long as your application answers `2xx` on that path, and `OTOROSHI_CHALLENGE_EXCLUDE_PATHS` excludes any other path.

- [Learn more about the Otoroshi challenge](/doc/develop/request-flow/otoroshi-challenge/)

## Development dependencies with pnpm

Applications built with pnpm and `CC_NODE_DEV_DEPENDENCIES="install"` now run `pnpm install --no-prod` to pull [development dependencies](/doc/deploy/applications/nodejs/#development-dependencies), instead of the `--prod false` form. pnpm 12 reads `false` as a package name instead of a flag value, and leaves development dependencies out. The new form works with pnpm 10, 11 and 12, and your configuration stays the same.

## PHP 8.5 becomes the default in October 2026

PHP 8.4 remains the default version in this release. With the first release after **1st October 2026**, a PHP or FrankenPHP application deployed without `CC_PHP_VERSION`, or with `CC_PHP_VERSION=8`, will run PHP 8.5. To stay on your current version, set it explicitly before then:

```bash
clever env set CC_PHP_VERSION 8.4
```

Applications that already pin a version, such as `CC_PHP_VERSION=8.3`, are not affected. Read [PHP 8.5 becomes the default version in October](/changelog/2026/09-01-php-8.5-default/) for the extension check and the support timeline of each version.

## Linux Kernel

Kernel is [now updated independently](/changelog/2026/05-12-linux-kernel-7.0.6). Current version is 7.2.7.
