---
title: "Images update: custom port for FrankenPHP, Erlang 28"
date: 2025-06-03
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: More flexible FrankenPHP, and more under the hood…
excludeSearch: true
---

We updated all our images. Deployment is in progress for all our users.

* **Common:**
  * Linux kernel 6.14.9
  * Mise 2025.5.17
  * Redis 8.0.2
  * SQLite 3.50.0
* **Elixir:**
  * Update to 1.18.4
  * Erlang 28.0
* **FrankenPHP:**
  * Update to 1.6.2
* **Go:**
  * Update to 1.24.3
* **Node.js:**
  * Update to 22.16.0 (npm 10.9.2)
  * Bun 1.2.15
* **Python:**
  * uv 0.7.9
* **Ruby:**
  * Update to 3.4.4

## Bun native support
This release introduces [Bun](https://bun.sh) native support on Clever Cloud, with auto-detection of `bun.lock` file.

- [Learn more about Bun support on Clever Cloud](/developers/changelog/2025/06-03-native-bun-support/)

## FrankenPHP custom port
You can also set `CC_FRANKENPHP_PORT` to use a different port than the default `8080`. It allows you to use services in front of your FrankenPHP application such as [Redirection.io](/developers/doc/reference/reference-environment-variables/#use-redirectionio-as-a-proxy) for example.

- [Learn more about FrankenPHP on Clever Cloud](/developers/doc/applications/frankenphp/)
