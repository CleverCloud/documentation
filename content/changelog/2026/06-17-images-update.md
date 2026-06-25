---
title: "Images update: Static Web Server 2.43, Yarn 4.16, Rust 1.96, Hugo 0.162"
description: All runtimes updated, PHP included, with fresh Rust, Yarn and Static Web Server releases. Hugo now requires 0.160 or newer.
date: 2026-06-17
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
  * Apache 2.4.68
  * Chromium 149.0.7827.114
  * Mise 2026.6.0
  * NGINX 1.30.2
  * OAuth2 Proxy 7.15.3
  * Redis 8.8.0
* **Docker:**
  * Update to 29.5.2
* **Erlang/Elixir:**
  * Rebar 3.27.0
* **FrankenPHP:**
  * Update to 1.12.4 (For `CC_PHP_VERSION=8.5`)
* **Go:**
  * Go 1.26.4
* **Node.js & Bun:**
  * Yarn 4.16.0
* **PHP:**
  * Update to 8.4.22
  * Update to 8.5.7
  * Composer 1.20.28
  * Composer 2.2.28
  * Composer 2.10.1
* **Python:**
  * Update to 3.13.14
  * Update to 3.14.6
  * pip 26.1.2
  * uv 0.11.21
* **Rust:**
  * Rust 1.96.0
* **Static:**
  * Hugo 0.162.1
  * Static Web Server 2.43.0

## Hugo version update

Starting with next release, we will only support Hugo 0.160 and newer. If you are using an older version, update your application or [use Mise](/doc/reference/reference-environment-variables#install-tools-with-mise-package-manager) to download it during deployment.
