---
type: docs
linkTitle: Static
title: Static Site Generators (SSGs) runtime
description: Deploy static websites. Astro, Docusaurus, Hugo, mdBook and Mkdocs autobuild
type: docs
aliases:
- /doc/deploy/application/static
- /doc/deploy/application/static/static
- /doc/partials/language-specific-deploy/static
---

## Overview

Static is a flexible, light and simple runtime dedicated to static sites generators (SSG), designed for minimum configuration effort with Auto-build feature. Pico instances are available, it allows users to put services in front of it, such as [Redirection.io](https://www.clever-cloud.com/developers/doc/reference/reference-environment-variables/#use-redirectionio-as-a-proxy) or [Varnish](/developers/doc/administrate/cache/).

> [!NOTE] Static is a new runtime. Help us to improve it by reporting any issue or suggestion on the [Clever Cloud Community](https://github.com/CleverCloud/Community/discussions/categories/paas-runtimes)

## Create your Static application

To create a new Static application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type static
```
* [Learn more about Clever Tools](/developers/doc/cli/)
* [Learn more about Clever Cloud application deployment](/developers/doc/quickstart/#create-an-application-step-by-step)

## Configure your Static application

### Mandatory needs

Static runtime only requires a working web application, with an `index.htm` or `index.html` file. If you need to serve files from a specific directory, set the `CC_WEBROOT` environment variable, relative to the root of your project (for example `/public`, default is `/`).

* [Learn more about environment variables on Clever Cloud](/developers/doc/reference/reference-environment-variables/)

### Build phase

During the build phase, Clever Cloud will run the `CC_BUILD_COMMAND` if provided. You can use it to install dependencies, build your static website, or any other task you need to perform before running your application. If no `CC_BUILD_COMMAND` is provided, Clever Cloud will try to detect your Static Site Generator (SSG), build and deploy your website automatically.

- [Learn more about Deployment hooks](/developers/doc/develop/build-hooks/)
- [Learn more about Static Site Generators (SSGs) Auto-build](#static-site-generators-ssg-auto-build)

### Optimized build cache

When [auto-build](#static-site-generators-ssg-auto-build) activates, or if you define `CC_WEBROOT`, the build cache contains only the served directory to optimize size and reduce archive time. When neither option applies, the system caches the entire application root directory instead.

To override this behavior, set the `CC_OVERRIDE_BUILD_CACHE` environment variable with a colon-separated list of directories and files, relative to the application root. For example: `CC_OVERRIDE_BUILD_CACHE=myScript.sh:/myBuildDir`.

## Supported web servers

By default, the Rust-based [Static Web Server (SWS)](https://static-web-server.net) serves your website. If a valid Caddyfile is present at the root of your project, it will be used with [Caddy](https://caddyserver.com) and the `caddy run` command, you can also set its location with `CC_STATIC_CADDYFILE` (Default is `./Caddyfile`).

You can force the use of Caddy by setting the `CC_STATIC_SERVER` environment variable to `caddy`. It configures your application to serve the website with the `caddy file-server` command which don't rely on a Caddyfile.

## Custom configuration and port

Caddy and SWS can be configured with a configuration file or through environment variables. You can also pass your own command line flags with `CC_STATIC_FLAGS`. To define a custom listen port, use `CC_STATIC_PORT` (default is `8080`).

- Caddy configuration:
  - [Command Line Arguments](https://caddyserver.com/docs/command-line)
  - [Environment Variables](https://caddyserver.com/docs/caddyfile/concepts#environment-variables)
  - [Caddyfile](https://caddyserver.com/docs/caddyfile)
- Static Web Server (SWS) configuration:
  - [Command Line Arguments](https://static-web-server.net/configuration/command-line-arguments/)
  - [Environment Variables](https://static-web-server.net/configuration/environment-variables/)
  - [TOML Configuration File](https://static-web-server.net/configuration/config-file/)

## Static Site Generators (SSG) Auto-build

If you don't set a `CC_BUILD_COMMAND`, Clever Cloud try to detect and configure the Static Site Generator (SSG) through the presence of specific files in the project root. If detected the static website is built in the `cc_static_autobuilt` folder (or `CC_STATIC_AUTOBUILD_OUTDIR`), used as `CC_WEBROOT` and build cache content. If you defined a `CC_WEBROOT`, it will be used instead of `cc_static_autobuilt`.

Supported Static Site Generators (SSG) are:

### Astro

* Build command: `npm i && npm run astro build -- --outDir <out-dir>`
* Detected file: `astro.config.mjs`, `astro.config.ts`, `astro.config.js`, `astro.config.cjs`

### Docusaurus

* Build command: `npm i && npm run docusaurus build -- --out-dir <out-dir>`
* Detected file: `docusaurus.config.js`, `docusaurus.config.ts`

### Hugo

* Build command: `hugo --gc --minify --destination <out-dir>`
* Detected file: `hugo.json`, `hugo.toml`, `hugo.yaml`

>[!TIP] Set the Hugo version
>Use a specific Hugo version by setting the `CC_HUGO_VERSION` environment variable to `0.145`, `0.146`, `0.147` (default) or `0.148`

### mdBook

* Build command: `mdbook build --dest-dir <out-dir>`
* Detected file: `book.toml`

### Mkdocs

* Build command: `uvx mkdocs build --site-dir <out-dir>`
* Detected file: `mkdocs.yml`

### Nuxt.js

* Build command: `npm i && npm run generate && mv .output/public <out-dir>`
* Detected file: `nuxt.config.ts`

## Vitepress

* Build command: `npm i && npm run docs:build -- --outDir <out-dir>`
* Detected file: `vitepress.config.js`, `vitepress.config.ts`, `vitepress.config.mjs`, `vitepress.config.mts`

## Zola

* Build command: `zola build --minify --output-dir <out-dir>`
* Detected file: `config.toml`

{{< content "redirectionio" >}}
{{< content "varnish" >}}
