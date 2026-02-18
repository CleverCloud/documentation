---
title: "Images update: Bun 1.3.8, OAuth2 Proxy 7.14, more PHP 8.5 extensions"
description: "Many tiny updates, and some surprises we'll detail soon"
date: 2026-02-03
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
  * OAuth2 Proxy 7.14.2
  * Otoroshictl 0.0.15
  * Tailscale 1.94.1
* **.NET:**
  * Update to 6.0.136
* **Docker:**
  * Docker Buildx 0.31.1
* **Java:**
  * Update to 11.0.30_p7
  * Update to 17.0.18_p8
  * Update to 21.0.10_p7
  * Update to 25.0.2_p10
  * Gradle 9.3.1
* **Node.js & Bun:**
  * Bun 1.3.8
* **PHP:**
  * Composer 2.9.5
  * mcrypt extension 1.0.9
  * PDFlib extension 11.0.0
  * solr extension 2.9.1
  * xdebug extension 3.5.0
* **Python:**
  * uv 0.9.28

## Docker Buildx

[As previously announced](/changelog/2025/11-04-docker-buildx-default/), Docker Buildx is now the default build system for Docker applications. You can switch back to the legacy build system by setting the `CC_DOCKER_BUILDX` environment variable to `false`.
