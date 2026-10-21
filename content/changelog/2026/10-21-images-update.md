---
title: "Images update: eMudhra certificates distrust, PHP and Node.js security releases, Chromium 155, Clever Tools 5.2"
description: PHP and Node.js security releases, eMudhra certificate authorities distrust, PHP 8.5 by default, FrankenPHP 1.13, Ruby 2.5 and 3.0 removal, Clever Tools 5.2, Chromium 155 and uv 0.13
date: 2026-10-21
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
  - Anubis 1.28.1
  - Chromium 155.0.8059.79
  - Clever Tools 5.2.0
  - curl 8.23.0
  - Mise 2026.10.15
  - NGINX 1.30.6
  - Otoroshictl 0.0.19
  - Tailscale 1.104.2
- **.NET:**
  - Update to 8.0.132
  - Update to 9.0.122
  - Update to 10.0.113
- **Erlang/Elixir:**
  - Erlang 27.3.4.19
  - Erlang 28.5.0.8
  - Erlang 29.1.2
  - rebar3 3.27.3
- **FrankenPHP:**
  - Update to 1.13.1
- **Go:**
  - Update to 1.27.3
- **Java:**
  - Gradle 9.8.2
- **PHP:**
  - FrankenPHP 1.13.1 (released today)
  - Update to 8.2.35
  - Update to 8.3.36
  - Update to 8.4.27
  - Update to 8.5.12
  - Symfony CLI 5.22.1
- **Python:**
  - uv 0.13.4
- **Ruby:**
  - Update to 3.4.11
  - Ruby 2.5 and 3.0 are no longer available
- **Rust:**
  - Update to 1.99.1

## PHP security releases

PHP 8.2.35, 8.3.36, 8.4.27 and 8.5.12 fix two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619. FrankenPHP 1.13 is now the only version available, whatever the value of `CC_PHP_VERSION`, as earlier versions won't receive the fixes.

The [dedicated changelog entry](/changelog/2026/10-21-php-security-vulnerabilities/) details the mitigations we applied, the situation of FrankenPHP and of PHP 8.1 and earlier, and the actions you might need to take.

## PHP 8.5 by default

[As announced](/changelog/2026/09-01-php-8.5-default/), PHP and FrankenPHP applications deployed without `CC_PHP_VERSION` now run PHP 8.5, as those with `CC_PHP_VERSION=8` already did since the [previous release](/changelog/2026/10-14-images-update/). If you want to stay on PHP 8.4, set it explicitly:

```bash
clever env set CC_PHP_VERSION 8.4
```

- [Learn more about PHP on Clever Cloud](/doc/deploy/applications/php/)
- [PHP migration guide from 8.4 to 8.5](https://www.php.net/migration85)

## Node.js security releases

The Node.js project published [security releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) fixing 10 vulnerabilities, four of them rated high, for all its supported branches. Our images now ship Node.js 24.22.1, the latest LTS, used when your application doesn't request a specific version.

Node.js 22.23.4 and 26.12.1 are available through nvm alongside this system version. If you set `CC_NODE_VERSION` or `engines.node` in your `package.json` to `22` or `26`, your application gets the patched release at its next deployment. A version pinned to its patch level, such as `22.23.3`, stays on it until you update it.

- [Learn more about Node.js versions on Clever Cloud](/doc/deploy/applications/nodejs/#set-nodejs-version)

## eMudhra certificate authorities distrust

On 17 October 2026, a researcher reported the compromise of eight intermediate certificate authority keys from eMudhra ([CVE-2026-111943](https://www.cve.org/CVERecord?id=CVE-2026-111943)). Anyone holding these keys can issue certificates that TLS clients trusting the emSign roots accept. Browsers quickly distrusted them, but other clients, such as the ones your applications use, rely on a trust store that needs an update.

Our images no longer trust the affected certificate authorities, through several updates:

- The system trust store from `ca-certificates` drops the emSign Root CA - C1, emSign ECC Root CA - C3 and emSign ECC Root CA - G3 roots
- NSS 3.131.1 drops the same roots from its built-in trust store
- certifi 2026.10.19, used by the system Python, no longer includes them
- Go 1.27.3 rejects certificate chains containing the affected intermediates
- Node.js 22.23.4, 24.22.1 and 26.12.1 update their bundled certificate store
- Otoroshictl 0.0.19 moves to rustls 0.23, which distrusts the affected intermediates
- uv 0.13.4 removes the affected root from its own certificate store

If your application ships its own trust store, for example a `certifi` version pinned in your Python dependencies, update it as well.

## Ruby 2.5 and 3.0 removal

Ruby 2.5 and 3.0, end of life since 2021 and 2024, are no longer part of our images, and applications can't deploy with them anymore. If your application still uses one of these versions, move it to a supported branch, such as Ruby 3.4 or 4.0:

```bash
clever env set CC_RUBY_VERSION 4.0.7
```

- [Learn more about Ruby on Clever Cloud](/doc/deploy/applications/ruby/)

## Other changes

[Request Flow](/doc/develop/request-flow/) now starts the custom middleware set in `CC_REQUEST_FLOW_CUSTOM` from your application folder, as hooks already were. Relative commands such as `./my-proxy` now resolve against it.

When [ClamAV](/doc/security/clamav/) stops, for example under memory pressure, it now restarts automatically, instead of leaving your instance without scanning until the next restart of your application.

Following the [clearer configuration errors](/changelog/2026/10-09-images-update/#clearer-configuration-errors) of a previous release, a failing build step now stops the deployment in every runtime with an error naming it, such as dependency installation or the Meteor build. Configuration errors detected at startup now also show up on the build instance, before your application reaches the run instances. A static application whose `CC_WEBROOT` doesn't exist after the build now caches its whole folder instead of failing to build its cache.

## Linux Kernel

Kernel is [now updated independently](/changelog/2026/05-12-linux-kernel-7.0.6). Current version is 7.2.12.
