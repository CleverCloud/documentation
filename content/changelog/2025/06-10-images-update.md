---
title: "Images update: custom port for FrankenPHP, Erlang 28"
date: 2025-06-10
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: More flexible FrankenPHP, and more under the hood...
excludeSearch: true
---

We updated all our images. Deployment is in progress for all our users.

* **Common:**
  * Linux kernel 6.14.9
  * Mise 2025.5.17
  * Redis 8.0.2
  * SQLite 3.50.0
* **Elixir:**
  * Update to 1.18.4
  * Erlang 28.0
* **FrankenPHP:**
  * Update to 1.7.0
* **Go:**
  * Update to 1.24.3
* **Node.js:**
  * Update to 22.16.1 (npm 10.9.2)
  * Bun 1.2.15
* **Python:**
  * uv 0.7.9
* **Ruby:**
  * Update to 3.4.4

This release also includes:
- Multiple fixes for logs
- Varnish support for [new Linux, Static and V runtimes](https://github.com/CleverCloud/Community/discussions/66)
- Astro, Docusaurus, MkDocs support for [new Static runtime SSGs Auto-build](https://github.com/CleverCloud/Community/discussions/66)
- `-x -race`  flags are added to `go install` if `CC_TROUBLESHOOT` is set to `true` in Go runtime
- `proxy_fcgi` is now default for `CC_CGI_IMPLEMENTATION` in PHP if environment variable is not set
- Try `buildx` support in Docker by setting `CC_DOCKER_BUILDX` to `true` (it will become the default in some weeks)
