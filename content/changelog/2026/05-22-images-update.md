---
title: "Images update: PHP 8.5.6, Java security patches, Python 3.14.5, Hugo 0.161"
description: All images updated with security patches across every runtime, PHP included. Hugo support narrows to 0.160 and later from June 15th.
date: 2026-05-22
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
  * Apache 2.4.67
  * Chromium 148.0.7778.167
  * Clever Tools 4.10.0
  * cURL 8.20.0
  * Mise 2026.5.3
  * NGINX 1.30.1
  * OAuth2 Proxy 7.15.2
  * Redis 8.6.3
  * SQLite 3.53.1
* **FrankenPHP:**
  * Update to 1.12.3 (For `CC_PHP_VERSION=8.5`)
* **Go:**
  * Go 1.26.3
* **Java:**
  * Update to 1.8.0.492_p09
  * Update to 11.0.31_p11
  * Update to 17.0.19_p10
  * Update to 21.0.11_p10
  * Update to 25.0.3_p9
  * Gradle 8.14.5
  * Gradle 9.5.1
* **Node.js & Bun:**
  * Bun 1.3.14
* **PHP:**
  * Update to 8.2.31
  * Update to 8.3.31
  * Update to 8.4.21
  * Update to 8.5.6
  * Composer 2.2.27
  * Composer 2.9.7
* **Python:**
  * Update to 3.14.5
  * uv 0.11.15
* **Ruby:**
  * Update to 4.0.5
* **Scala:**
  * Play Framework 1.2.7.2
  * Play Framework 1.11.0
* **Static:**
  * Hugo 0.152.2
  * Hugo 0.159.2
  * Hugo 0.160.1
  * Hugo 0.161.1

## Linux Kernel

Kernel is [now updated independently](/changelog/2026/05-12-linux-kernel-7.0.6). Current version is 7.0.9.

## Fixes for Java, Node.js & Bun, PHP

This image includes multiple fixes for bug we encountered for Java applications using Maven, PHP applications using `apcu` or `zip` extensions, Node.js 25/26 applications using `pnpm` or `yarn`.

## Hugo version update

Starting June 15th, we will only support Hugo 0.160 release and later. If you are using an older version, update your application or [use Mise](/doc/reference/reference-environment-variables#install-tools-with-mise-package-manager) to download it during deployment.
