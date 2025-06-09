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

Static runtime only requires a working web application, with an `index.htm` or `index.html` file. If you need to serve files from a specific directory, set the `CC_WEBROOT` environment variable, relative to the root of your project (default: `/`).

* [Learn more about environment variables on Clever Cloud](/developers/doc/reference/reference-environment-variables/)

### Build phase

`CC_BUILD_COMMAND`

- [Learn more about Deployment hooks](/developers/doc/develop/build-hooks/)
- [Learn more about Static Site Generators (SSGs) Auto-build](#static-site-generators-ssg-auto-build)

### Optimized build cache

If a `CC_WEBROOT` is set, it's also used as the build cache directory to reduce its size and archive time. If none, the application root is used. You can bypass this behavior by setting the `CC_OVERRIDE_BUILD_CACHE` environment variable with directories and files, relative to the application root, separated by a `:`. For example `myScript.sh:/myBuildDir`.

## Supported web servers

Pass your own command line flags with `CC_STATIC_FLAGS`.
Use a custom port with `CC_STATIC_PORT`, default is `8080`.

By default, the Rust-based Static Web Server (SWS) is used to serve your website. If a valid Caddyfile is present at the root of your project, it will be automatically used with Caddy. You can bypass this behavior by setting the `CC_STATIC_SERVER` environment variable to `static-web-server` or `caddy`.

### Static Web Server


### Caddy

`CC_STATIC_CADDYFILE`: Default is `./Caddyfile`

### Download and use your own

## Static Site Generators (SSG) Auto-build

If you don't set any `CC_BUILD_COMMAND` and `CC_WEBROOT`, Clever Cloud will try to detect your Static Site Generator (SSG) through the presence of specific files in your project root. If detected, it will run the build command and set the webroot automatically.

>[!NOTE]
>SSG Auto-build doesn't work with dedicated build instance and so `pico` flavor.

Supported Static Site Generators (SSG) are:

### Astro

* Build command: `npm i && npm run build`
* Default web root: `/dist`
* Detected file: `astro.config.mjs`

### Docusaurus

* Build command: `npm i && npm run docusaurus build`
* Default web root: `/build`
* Detected file: `docusaurus.config.js`, `docusaurus.config.ts`

### Hugo

* Build command: `hugo`
* Default web root: `/public`
* Detected file: `hugo.json`, `hugo.toml`, `hugo.yaml`

### mdBook

* Build command: `mdbook build`
* Default web root: `/book`
* Detected file: `book.toml`

### Mkdocs

* Build command: `uvx mkdocs build`
* Default web root: `/site`
* Detected file: `mkdocs.yml`

{{% content/redirectionio %}}
