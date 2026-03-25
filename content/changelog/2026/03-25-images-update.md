---
title: "Images update: FrankenPHP 1.12, Gradle 9.4, Rust 1.94, set PHP & Composer versions in all runtimes"
description: All runtimes updated except PHP. CC_PHP_VERSION and CC_COMPOSER_VERSION are now available in all runtimes
date: 2026-03-25
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

We updated all our images, except PHP. Deployment is in progress for all our users.

* **Common:**
  * Linux kernel 6.19.7
  * Anubis 1.25.0
  * Chromium 146.0.7680.153
  * Clever Tools 4.7.1
  * cURL 8.19.0
  * FFmpeg 8.1
  * Ghostscript 10.07
  * OAuth2Proxy 7.14.3
  * Poppler 26.03
  * SQLite 3.52.0
  * Varnish 8.0.1
  * Vim 9.2.0096
* **Elixir:**
  * Erlang 26.2.5.18
  * Erlang 27.3.4.9
  * Erlang 28.4.1
* **FrankenPHP:**
  * Update to 1.12.1 with PHP 8.5.4 (with `CC_PHP_VERSION=8.5`)
* **Go:**
  * Update to 1.26.1
* **Java:**
  * Gradle 9.4.1
  * Maven 3.9.14
* **Node.js & Bun:**
  * Update to 24.14.1 (npm 11.11.0)
  * Bun 1.3.11
  * Yarn 4.13.0
* **Python:**
  * Update to 3.10.20
  * Update to 3.11.15
  * Update to 3.12.13
  * uv 0.10.12
* **Ruby:**
  * Update to 3.4.9
* **Rust:**
  * Update to 1.94.0
  * Rustup 1.29.0
* **Static:**
  * Caddy 2.11.2

## PHP & Composer version

You can now set `CC_PHP_VERSION` and `CC_COMPOSER_VERSION` in any runtime. We also fixed a bug that prevented to use another Composer version than the LTS with FrankenPHP.

## Log drains collection

We removed old log drains stack, except for application still using it.

- [Learn more about log drains old stack deprecation](/changelog/2026/03-19-drains-legacy/)
