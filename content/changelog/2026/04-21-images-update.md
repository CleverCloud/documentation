---
title: "Images update: Node.js 24.15, Clever Tools 4.8, nginx 1.30, FrankenPHP 1.12.2"
description: All runtimes updated except PHP, with a new Clever Tools release and many tool updates
date: 2026-04-21
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
  * Linux kernel 6.19.13
  * Chromium 147.0.7727.101
  * Clever Tools 4.8.0
  * htop 3.5.0
  * nano 9.0
  * nginx 1.30.0
  * OpenSSH 10.3p1
  * OpenSSL 3.5.6
  * SQLite 3.53.0
* **FrankenPHP:**
  * Update to 1.12.2 (with `CC_PHP_VERSION=8.5`)
  * Symfony CLI 5.17.1
* **Go:**
  * Update to 1.26.2
* **Node.js & Bun:**
  * Update to 24.15.0 (npm 11.12.1)
  * Bun 1.3.12
* **Python:**
  * Update to 3.13.13
  * Update to 3.14.4
  * uv 0.11.7
* **Ruby:**
  * Update to 3.2.11
