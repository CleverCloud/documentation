---
title: "Images update: Gradle 9.6, Hugo 0.163, Docker 29.6"
description: A tools bump release, Hugo 0.163 is now the default for static applications
date: 2026-07-01
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
  * cURL 8.21.0
  * Mise 2026.6.14
  * NGINX 1.30.3
* **Docker:**
  * Update to 29.6.1
* **Java:**
  * Gradle 9.6.1
* **PHP:**
  * `mod_ssl` module is now loaded
* **Python:**
  * uv 0.11.25
* **Static:**
  * Hugo 0.163.3

## Hugo version update

Starting with this release, we only support Hugo 0.160 and newer. If you are using an older version, update your application or [use Mise](/doc/reference/reference-environment-variables#install-tools-with-mise-package-manager) to download it during deployment. If you don't set `CC_HUGO_VERSION`, `0.163` is now the default.
