---
title: "Images update: Bun 1.3, Elixir 1.19, Hugo 0.151, uv 0.9 (with Python 3.14)"
description: "Many runtimes updates, prepare for Node.js 24 LTS and next end-of-life versions: Elixir 1.14, Python 3.9"
date: 2025-10-23
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
  * Linux kernel 6.17.4
  * Clever Tools 4.3.0
  * Mise 2025.10.11
  * OpenSSH 10.2_p1
  * Ripgrep 15.0.0
  * Tailscale 1.88.3
* **Docker:**
  * Update to 28.5.1
  * Buildx 0.29.1
* **Elixir:**
  * Update to 1.19.1
  * Erlang 28.1.1
* **Go:**
  * Update to 1.25.3
* **Node.js:**
  * Update to 22.21.0
  * Bun 1.3.1
  * Yarn 4.10.3
* **PHP:**
  * Update to 8.3.27
  * Update to 8.4.14
  * memcached 1.6.39
  * memcached extension 3.4.0
* **Python:**
  * Update to Python 3.9.24
  * Update to Python 3.10.19
  * Update to Python 3.11.14
  * Update to Python 3.12.12
  * Update to Python 3.13.9
  * uv 0.9.4
* **Ruby:**
  * Update to Ruby 3.4.7
* **Static:**
  * Hugo 0.151.2

## Node.js 25 support, 24 LTS as default version

As [Node.js 25 is now available](https://nodejs.org/fr/blog/release/v25.0.0), you can use it in your applications by setting `CC_NODE_VERSION=25` in your environment variables. As previously mentioned, Node.js 24 will soon be the latest LTS. Then we'll use it as the default Node.js version in our images. If your application doesn't support Node.js 24 yet, set `CC_NODE_VERSION=22` to keep using Node.js 22 LTS.

- [Learn more about Node.js on Clever Cloud](/doc/applications/nodejs)

## Elixir 1.14 is end-of-life, 1.19 support

As [Elixir 1.19 is now available](https://elixir-lang.org/blog/2025/10/16/elixir-v1-19-0-released/), we have updated our images to use it as the default Elixir version. Elixir 1.14 is now end-of-life according to the [official Elixir release schedule](https://hexdocs.pm/elixir/compatibility-and-deprecations.html) and will not receive any security update. We recommend you to upgrade to a supported version of Elixir (1.15 or later).

We'll remove Elixir 1.11 and previous releases support in our next image update, as they are not used anymore. We'll progressively align with the official Elixir support policy as customers are migrating to supported versions.

- [Learn more about Elixir on Clever Cloud](/doc/applications/elixir)

## Python 3.9 is end-of life, 3.14 support

[Python 3.14 is now available](https://blog.python.org/2025/10/python-3140-final-is-here.html). It's not natively supported yet on Clever Cloud and will come soon. In the meantime, you can try it by declaring it as default version for your applications using `uv` package manager starting with this image update.

Python 3.9 is now end-of-life according to the [official Python release schedule](https://devguide.python.org/versions/#python-release-cycle) and will not receive any security update. We recommend you to upgrade to a supported version of Python (3.10 or later). We'll remove Python 3.9 from our images starting May 2026.

- [Learn more about Python on Clever Cloud](/doc/applications/python)
