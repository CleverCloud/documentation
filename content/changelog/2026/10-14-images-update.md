---
title: "Images update: Bun 1.4, Docker 29.9, Tailscale 1.104, tmux 3.8"
description: Bun 1.4 by default, PHP 8.5 with CC_PHP_VERSION=8, Docker 29.9, Go and Gradle updates, Tailscale 1.104, and stricter checks on environment variable names
date: 2026-10-14
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
  - GraphicsMagick 1.3.49
  - LibreOffice 26.8.1.1
  - Tailscale 1.104.1
  - tmux 3.8
- **Docker:**
  - Update to 29.9.0
  - Buildx 0.38.0
- **Go:**
  - Update to 1.27.2
- **Java:**
  - Gradle 8.14.6
  - Gradle 9.8.1
- **Node.js & Bun:**
  - Bun 1.4.3
- **Python:**
  - uv 0.12.24
- **Static:**
  - Static Web Server 2.44.1

## Bun 1.4

This release is the first one to ship Bun 1.4, now Rust-based: applications using Bun as build tool and runtime run Bun 1.4.3. If you want to stay on Bun 1.3, add a `mise.toml` file at the root of your project:

```toml {filename="mise.toml"}
[tools]
bun = "1.3"
```

Mise installs this version before the build phase, and Clever Cloud uses it for both `bun install` and your application.

- [Learn more about Bun on Clever Cloud](/doc/deploy/applications/nodejs/#bun-version)
- [Learn more about Mise on Clever Cloud](/doc/develop/mise/)

## PHP 8.5 with `CC_PHP_VERSION=8`

[As announced](/changelog/2026/09-01-php-8.5-default/), PHP and FrankenPHP applications deployed with `CC_PHP_VERSION=8` now run PHP 8.5 instead of PHP 8.4. If you want to stay on PHP 8.4, set it explicitly:

```bash
clever env set CC_PHP_VERSION 8.4
```

- [Learn more about PHP on Clever Cloud](/doc/deploy/applications/php/)
- [PHP migration guide from 8.4 to 8.5](https://www.php.net/migration85)

## Stricter environment variable names

Variable names with dots (`.`) or dashes (`-`) are Java properties, only allowed in Java applications. Deploying any other application with such a variable now fails, with an error listing the variables to remove. Previous releases silently left variables with dots out of the environment. Names that don't follow the [environment variable rules](/doc/develop/common-configuration/environment-variables/#rules) are also rejected.

In Java applications, variables with dashes are now passed as Java system properties, as variables with dots already were.

In PHP applications, the file set in `CC_OPCACHE_PRELOAD` must be inside your application directory, or the deployment fails with an error naming the variable.

## Linux Kernel

Kernel is [now updated independently](/changelog/2026/05-12-linux-kernel-7.0.6). Current version is 7.2.10.
