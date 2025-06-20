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

Static is a flexible, light and simple runtime dedicated to static sites generators (SSG), designed for minimum configuration effort with Auto-build feature. Pico instances are available, it allows users to put services in front of it, such as [Redirection.io](https://www.clever-cloud.com/developers/doc/reference/reference-environment-variables/#use-redirectionio-as-a-proxy) or [Varnish](http://localhost:1313/developers/doc/administrate/cache/).

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

If a `CC_WEBROOT` is set, it's also used as the build cache directory to reduce its size and archive time. If none, the application root is used. You can bypass this behavior by setting the `CC_OVERRIDE_BUILD_CACHE` environment variable with directories and files, relative to the application root, separated by a `:`. For example `myScript.sh:/myBuildDir`.

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

If you don't set a `CC_BUILD_COMMAND`, Clever Cloud try to detect and configure the Static Site Generator (SSG) through the presence of specific files in the project root. If detected the static website is built in `cc_static_autobuilt` folder, used as `CC_WEBROOT` and build cache content.

Supported Static Site Generators (SSG) are:

### Astro

* Build command: `npm i && npm run astro build -- --outDir cc_static_autobuilt`
* Detected file: `astro.config.mjs`, `astro.config.ts`, `astro.config.js`, `astro.config.cjs`

### Docusaurus

* Build command: `npm i && npm run docusaurus build -- --out-dir cc_static_autobuilt`
* Detected file: `docusaurus.config.js`, `docusaurus.config.ts`

### Hugo

* Build command: `hugo --gc --minify --destination cc_static_autobuilt`
* Detected file: `hugo.json`, `hugo.toml`, `hugo.yaml`

>[!TIP] Set the Hugo version
>Use a specific Hugo version by setting the `CC_HUGO_VERSION` environment variable to `0.145`, `0.146` or `0.147` (default)

### mdBook

* Build command: `mdbook build --dest-dir cc_static_autobuilt`
* Detected file: `book.toml`

### Mkdocs

* Build command: `uvx mkdocs build --site-dir cc_static_autobuilt`
* Detected file: `mkdocs.yml`

{{% content/redirectionio %}}
{{% content/varnish %}}
