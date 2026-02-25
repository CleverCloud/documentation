---
title: "Images update: FrankenPHP 1.11.3 (PHP 8.5), Request Flow in all runtimes"
description: Request Flow expansion is now done. You can use PHP 8.4 or 8.5 in FrankenPHP
date: 2026-02-25
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

* **Common:**
  * Clever Tools 4.6.1
  * md4c 0.5.2
  * Redis 8.6.1
  * Mise 2026.2.19
  * Otoroshictl 0.0.17
* **FrankenPHP:**
  * Update to 1.11.3 (with `CC_PHP_VERSION=8.5`)
* **Python:**
  * uv 0.10.4
* **Static:**
  * Caddy 2.11.1
  * Static Web Server 2.41.0

## PHP Version in FrankenPHP

Customers asked for PHP version choice in our FrankenPHP runtime. PHP 8.4 is still the default, but you can now select PHP 8.5 by setting `CC_PHP_VERSION=8.5` in your environment variables. It will use the latest FrankenPHP binary release (currently `1.11.3`). PHP 8.5 will be the default in the coming months.

We'll only support non end-of-life (EOL) versions of PHP in FrankenPHP, so regularly check [PHP's supported versions](https://www.php.net/supported-versions.php).

## Request Flow extension

Request Flow is now available in all our runtimes, including Python without uv and Ruby.

- [Learn more about Request Flow](/doc/develop/request-flow/)

## Fixes

This release fixes issues with logs in some Java applications.
