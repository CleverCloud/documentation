---
title: "Images update: Bun included, Rust 1.86"
date: 2025-04-16
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Native support for Bun incoming
excludeSearch: true
---

We updated all our images, except Java. Deployment is in progress for all our users.

* **Common:**
  * Linux kernel 6.14.2
  * Mise 2025.4.2
  * OpenSSH 10.0p2
  * OpenSSL 3.5.0
  * Tailscale 1.82.0
* **Node.js:**
  * Bun 1.2.9
* **PHP:**
  * Update to 8.4.6
  * Composer 2.8.8
* **Python:**
  * Update to 3.13.3
  * uv 0.6.14
* **Rust:**
  * Update to 1.86.0

Bun is now part of our included tools, and will be natively supported in an upcoming release of our Node.js runtime.
