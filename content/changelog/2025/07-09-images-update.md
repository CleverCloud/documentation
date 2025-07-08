---
title: "Images update: FrankenPHP 1.8, Java 24, Storybook auto-build"
date: 2025-07-09
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Welcome Java in the unified image!
excludeSearch: true
---

We updated all our images, except PHP with Apache. Deployment is in progress for all our users.

* **Common:**
  * Linux kernel 6.15.5
  * Hugo 0.148.0
  * Mise 2025.7.1
  * SQLite 3.50.2
  * Redis 8.0.3
* **Docker:**
  * Update to 28.3.1
* **FrankenPHP:**
  * Update to 1.8.0 (PHP 8.4.10, Caddy 2.10.0)
* **Java:**
  * Now part of the unified image
  * Java 24 support
  * GraalVM CE 23.0.2 (Java 17)
  * GraalVM CE 23.1.2 (Java 21)
  * Gradle 8.14.3
  * Maven 3.9.10
* **Node.js:**
  * Bun 1.2.18
* **Python:**
  * uv 0.7.19

## FrankenPHP, Linux, Static and V runtimes

- You can define `build` and `run` commands with `build:` and `run:` targets in a `Makefile` in `linux` runtime
- You can now set `CC_STATIC_AUTOBUILD_OUTDIR` in `static` runtime to specify the output directory for auto-build
- `v install` command is executed in the build phase if a `v.mod` file is present
- Storybook auto-build is now supported in the `static` runtime
- Easier `uv` activation in the `python` runtime
- `APP_FOLDER` support in new runtimes

## Other changes

- Authentication to a npm registry is now also supported through the `CC_NPM_BASIC_AUTH` environment variable
