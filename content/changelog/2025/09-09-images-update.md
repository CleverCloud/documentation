---
title: "Images update: Bun 1.2.21 with MySQL support, FrankenPHP 1.9, Hugo 0.149"
description: Use Bun with many Clever Cloud add-ons, latest FrankenPHP or Hugo for static sites
date: 2025-09-09
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
  * FFmpeg 8.0
  * Linux kernel 6.15.9
  * Mise 2025.9.6
  * Redis 8.2.1
  * SQLite 3.50.4
  * Varnish 7.7.3
* **Docker:**
  * Update to 28.4.0
  * Buildx 0.28.0
* **FrankenPHP:**
  * Update to 1.9.1
* **Go:**
  * Update to 1.25.1
* **Node.js & Bun:**
  * Update to 22.19.0 (npm 10.9.3)
  * Bun 1.2.21
  * Yarn 4.9.4
* **PHP:**
  * Update to PHP 8.3.25
  * Update to PHP 8.4.12
  * Composer 2.2.25 (LTS)
  * Composer 2.8.11
* **Python:**
  * 3.13.7
  * uv 0.8.15
* **Static:**
  * Hugo 0.145 removal
  * Hugo 0.149.1

## Bun 1.2.21: native Clever Cloud add-ons support

The latest Bun 1.2 release [brings native MySQL support](https://bun.com/blog/bun-v1.2.21) and various improvements. It already support PostgreSQL, Redis, S3-compatible Object Storage. Thus, you can use it in your applications and scripts with many Clever Cloud add-ons.

We provide a GitHub repository with ready-to-use examples:

* [Clever Cloud add-ons native Bun support example scripts](https://github.com/CleverCloud/bun-addons-examples)

## Hugo version update

As Hugo 0.149 is now available, we removed Hugo 0.145 from our images. If you don't set `CC_HUGO_VERSION`, `0.147` is still the default. As `0.150` will be in the next release, We'll move default to `0.149` starting October 2025.
