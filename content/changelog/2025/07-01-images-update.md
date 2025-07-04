---
title: "Images update: easier Varnish, Redirection.io, uv native support"
date: 2025-07-01
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Last mile before new runtimes public release
excludeSearch: true
---

We updated all our images. Deployment is in progress for all our users.

* **Common:**
  * Linux kernel 6.14.11
  * Mise 2025.6.6
  * SQLite 3.50.1
* **Docker:**
  * Update to 28.3
  * Buildx 0.25.0
* **Node.js:**
  * Update to 22.17.0
  * Bun 1.2.17
* **Python:**
  * Update to 3.13.5
  * uv 0.7.17
* **Rust:**
  * Update to 1.88.0
* **V:**
  * Update to 0.4.11

## Linux, Static and V runtimes

- Better V dependencies management
- Better support of Astro in the `static` auto build feature
- `static` runtime auto-build supports Nuxt.js, Storybook, Vitepress and Zola
- If a Mise `build` or `run` task is defined, it's used in build/run phase in `linux` runtime

These runtimes are in early access, let us know what you think about it, [your suggestions and feedback are welcome](https://github.com/CleverCloud/Community/discussions/66).

## Preliminary native uv support in Python applications

`uv` is now natively supported for deploying Python applications on Clever Cloud. Using `uv` bypass all the legacy Python deployment process. There is no mandatory `nginx` server and your application should listen on the port `8080`. Thus, you can use it with Varnish and easy to configure services such as Redirection.io. We'll progressively enhance the `uv` experience on Clever Cloud.

`uv` native support is still preliminary, let us know what you think about it, [your suggestions and feedback are welcome](https://github.com/CleverCloud/Community/discussions/67).

- [Learn more about uv](https://docs.astral.sh/uv/)
- [Learn more about Python on Clever Cloud](/developers/doc/applications/python)
- [A ready to deploy Python with uv application](https://github.com/CleverCloud/python-fastapi-uv-example)

## Other changes

- `CC_GIT_FULL_CLONE=false` enables shallow cloning (`--depth 1`), it will become the default in some weeks
- `CC_VARNISH_FILE` allows to set a custom location for `varnish.vcl`, relative to your application (for example `/varnish.vcl`)
- Port auto-configuration for `frankenphp` and `static` when a Varnish file is present or set with `CC_VARNISH_FILE`
- Port auto-configuration for `frankenphp` and `static` when [Redirection.io is enabled](/developers/doc/reference/reference-environment-variables/#redirectionio-support)
- You can now disable Mise package manager by setting `CC_DISABLE_MISE` to `true`
