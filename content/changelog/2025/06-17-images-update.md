---
title: "Images update: FrankenPHP 1.7, Docker buildx"
date: 2025-06-17
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: And more new features for runtimes to come…
excludeSearch: true
---

We updated all our images. Deployment is in progress for all our users.

* **Common:**
  * Linux kernel 6.14.11
  * Mise 2025.6.4
* **Docker:**
  * Update to 28.2.2
  * Buildx 0.24.0
* **FrankenPHP:**
  * Update to 1.7.0 (PHP 8.4.8)
* **Go:**
  * Update to 1.24.4
* **Node.js:**
  * Bun 1.2.16
* **Python:**
  * Update to 3.13.4
  * Update to 3.12.11
  * Update to 3.11.13
  * Update to 3.10.18
  * Update to 3.9.23
  * uv 0.7.13

## Other changes

- Multiple fixes for logs
- [Varnish support](/developers/doc/administrate/cache/) for FrankenPHP, [upcoming Linux, Static and V runtimes](https://github.com/CleverCloud/Community/discussions/66)
- Astro, Docusaurus, MkDocs autobuild support for [upcoming static runtime](https://github.com/CleverCloud/Community/discussions/66)
- `-x -race` flags are added to `go install` if `CC_TROUBLESHOOT` is set to `true` in Go runtime
- `proxy_fcgi` is now default in PHP with Apache if `CC_CGI_IMPLEMENTATION` environment variable is not set
- Try `buildx` support in Docker by setting `CC_DOCKER_BUILDX` to `true` (it will become the default in some weeks)
