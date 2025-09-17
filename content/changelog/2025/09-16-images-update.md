---
title: "Images update: Clever Tools 4.0, Hugo 150, Kernel 6.16, Tailscale 1.88"
description: A wide tools bump release, prepare for Hugo 0.149 used by default
date: 2025-09-16
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
  * Linux kernel 6.16.7
  * Clever Tools 4.0.2
  * Mise 2025.9.9
  * Tailscale 1.88.1
* **Elixir:**
  * Erlang 26.2.5.15
  * Erlang 27.3.4.3
  * Erlang 28.0.3
* **Node.js & Bun:**
  * Bun 1.2.22
* **PHP:**
  * Apache 2.4.65
  * Imagick extension 3.8.0
  * Symfony: fix binary name (was `symfony-cli`, now `symfony`)
* **Python:**
  * uv 0.8.17
* **Static:**
  * Caddy 2.10.2
  * Hugo 0.146 removal
  * Hugo 0.150.0
  * Static Web Server 2.38.1

## Hugo version update

As Hugo 0.150 is now available, we removed Hugo 0.146 from our images. If you don't set `CC_HUGO_VERSION`, `0.147` is still the default. We'll move default to `0.149` starting October 2025.
