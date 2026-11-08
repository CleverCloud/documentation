---
type: docs
linkTitle: Static
title: Static Site Generators (SSGs) runtime
description: Deploy static websites on Clever Cloud, built from their sources with Astro, Docusaurus, Hugo, mdBook, MkDocs and more, served by Static Web Server or Caddy
keywords:
- astro
- caddy
- docusaurus
- hugo
- mdbook
- mkdocs
- nuxt.js
- ssg
- static app hosting
- static cloud
- static site generator
- static web server
- storybook
- vitepress
- zola
aliases:
- /doc/applications/static
- /doc/deploy/application/static
- /doc/deploy/application/static/static
- /doc/partials/language-specific-deploy/static
- /doc/static
- /doc/static/static
---

## Overview

A static website is a set of files that a web server sends as they are: HTML pages, style sheets, scripts, and images. Clever Cloud can build them from your sources with a static site generator (SSG), such as Hugo or Astro, then serves them with [Static Web Server](https://static-web-server.net) or [Caddy](https://caddyserver.com).

A Static application needs no application server, and runs on the smallest instance size, `pico`. To use [`.htaccess` files](https://httpd.apache.org/docs/current/howto/htaccess.html) or to run PHP code, use the [Static with Apache](/doc/deploy/applications/static-apache/) runtime or the [PHP](/doc/deploy/applications/php/) runtime instead.

## Create your Static application

To create a new Static application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type static
```

- [Learn more about Clever Tools](/doc/tools/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

## Configure your Static application

### Mandatory needs

A Static application needs an `index.html` file, the home page of your website, at the root of the folder Clever Cloud serves. Its other pages, styles, and images sit next to it. For instance, the smallest website:

```html {filename="index.html"}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Hello</title>
  </head>
  <body>
    <h1>Hello from Clever Cloud</h1>
  </body>
</html>
```

With a static site generator, Clever Cloud can [build your website](#static-site-generators-ssg-auto-build) for you. Otherwise, push the files to serve.

### Served folder

By default, Clever Cloud serves the root of your repository. To serve one of its folders instead, set its path in `CC_WEBROOT`:

```bash
clever env set CC_WEBROOT /public
```

Every file in the served folder is public: keep notes, scripts, configuration files, and secrets out of it.

The build, the generators, and the servers run from the root of your project: the folder set in `APP_FOLDER`, or the root of the repository. They read their configuration files, such as a Caddyfile or the file set in `SERVER_CONFIG_FILE`, from there.

### Build phase

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/), then one of these, in order:

- The command set in `CC_BUILD_COMMAND`
- Otherwise, the build command of a [static site generator](#static-site-generators-ssg-auto-build) it detects
- Otherwise, nothing: it serves your files as they are

The build runs from the root of your project, or from the folder set in `APP_FOLDER`. The image includes the tools of the supported generators, and [`CC_HUGO_VERSION`](#hugo) sets the version of Hugo. To use a tool Clever Cloud doesn't provide, or a version the image doesn't include, declare it in a [`mise.toml` file](/doc/manage/mise/). For instance, [Pagefind](https://pagefind.app), which indexes your website for its search:

```toml {filename="mise.toml"}
[tools]
"github:Pagefind/pagefind" = "1.6.0"
```

Clever Cloud doesn't know where a command set in `CC_BUILD_COMMAND` writes the website: set `CC_WEBROOT` to this folder. For instance, to build a Hugo website, then index its pages for search with Pagefind:

```bash
clever env set CC_BUILD_COMMAND "hugo --minify --destination public && pagefind --site public"
clever env set CC_WEBROOT /public
```

### Start command

Clever Cloud serves the folder with [Static Web Server](https://static-web-server.net) (SWS) `{{< runtime_version sws >}}`, on port `8080`, or `9000` with [Request Flow](/doc/manage/request-flow/). It runs `static-web-server --host 0.0.0.0 --port 8080`, with the served folder in `--root`.

`CC_STATIC_FLAGS` adds options to this command, and `CC_STATIC_PORT` sets another port. With `CC_RUN_COMMAND`, Clever Cloud runs your own command instead, from the root of the repository. It must listen on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port).

### Configure Static Web Server

Static Web Server reads its settings from [its command options](https://static-web-server.net/v2/configuration/command-line-arguments/), from [environment variables](https://static-web-server.net/v2/configuration/environment-variables/), or from a [TOML configuration file](https://static-web-server.net/v2/configuration/config-file/). For instance, this file adds a header to the HTML pages, and sets the page of the 404 errors, from the served folder:

```toml {filename="sws.toml"}
[general]
page404 = "404.html"

[advanced]

[[advanced.headers]]
source = "**/*.html"
[advanced.headers.headers]
Cache-Control = "public, max-age=3600"
```

To load it, set its path in `SERVER_CONFIG_FILE`:

```bash
clever env set SERVER_CONFIG_FILE sws.toml
```

### Use Caddy

If your project has a valid [Caddyfile](https://caddyserver.com/docs/caddyfile), the configuration file of Caddy, at its root, Clever Cloud serves your website with [Caddy](https://caddyserver.com) `{{< runtime_version caddy >}}` and `caddy run`. Set another path in `CC_STATIC_CADDYFILE`. Your Caddyfile sets the port and the served folder itself:

```text {filename="Caddyfile"}
:{$PORT} {
    root * public
    file_server
}
```

With Request Flow, set `PORT=9000`, as [Clever Cloud doesn't change it](/doc/manage/#with-request-flow). `CC_STATIC_PORT` doesn't change the address of a Caddyfile.

Clever Cloud checks the file with `caddy validate`. If it's invalid, the deployment log shows `Provided Caddyfile is invalid`, and Clever Cloud serves your website with Static Web Server instead.

Set `CC_STATIC_SERVER` to choose the server whatever the files of your project:

- `caddy` serves the folder with `caddy file-server`, without a Caddyfile
- `static-web-server` uses Static Web Server, even if a Caddyfile exists

### Protect your website with a password

Static Web Server and Caddy can ask visitors for a login and a password, with HTTP basic authentication. Both read a password hashed with bcrypt, which [`htpasswd`](https://httpd.apache.org/docs/current/programs/htpasswd.html) generates: it comes with macOS, and with the `apache2-utils` package on Debian or Ubuntu.

With Static Web Server, set the user and the hash of its password in `SERVER_BASIC_AUTH`, here for an `admin` user:

```bash
clever env set SERVER_BASIC_AUTH "$(htpasswd -nbBC 10 admin 'your-password')"
```

With Caddy, add a `basic_auth` block to your Caddyfile, which reads the user and the hash from environment variables:

```text {filename="Caddyfile"}
:{$PORT} {
    root * public
    basic_auth {
        {$BASIC_AUTH_USER} {$BASIC_AUTH_HASH}
    }
    file_server
}
```

```bash
clever env set BASIC_AUTH_USER admin
clever env set BASIC_AUTH_HASH "$(htpasswd -nbBC 10 admin 'your-password' | cut -d: -f2)"
```

To sign visitors in with an identity provider, through OAuth2 or OpenID Connect, put [OAuth2 Proxy](/doc/manage/request-flow/oauth2-proxy/) in front of your website with [Request Flow](/doc/manage/request-flow/). An [Otoroshi](/doc/deploy/services/otoroshi/) gateway also manages access rules, quotas, and tokens, and the [Otoroshi challenge](/doc/manage/request-flow/otoroshi-challenge/) makes sure that requests come through it.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

If Clever Cloud serves a folder of your repository, from `CC_WEBROOT` or `cc_static_autobuilt`, the cache keeps only this folder and these files:

- The `clevercloud/` folder, a `Caddyfile` and an `sws.toml` file, at the root of the repository
- The files set in `CC_STATIC_CADDYFILE`, `CC_VARNISH_FILE`, and `SERVER_CONFIG_FILE`

On a restart from the cache, the other files are missing, such as a script your `CC_RUN_COMMAND` or a hook runs. To keep them, list in `CC_OVERRIDE_BUILDCACHE` every path the cache needs, from the root of the repository and separated by `:`. It replaces the default content:

```bash
clever env set CC_OVERRIDE_BUILDCACHE "public:scripts"
```

## Static site generators (SSG) auto-build

If you don't set `CC_BUILD_COMMAND`, Clever Cloud looks for the configuration file of a static site generator, at the root of your project, in the order of this table. It runs the build command of the first one it finds:

| Generator  | Configuration file                               | Build command                                                   |
| ---------- | ------------------------------------------------ | --------------------------------------------------------------- |
| Astro      | `astro.config.mjs`, `.ts`, `.js`, or `.cjs`      | `npm i && npm run astro build -- --outDir <out-dir>`            |
| Docusaurus | `docusaurus.config.js` or `.ts`                  | `npm i && npm run docusaurus build -- --out-dir <out-dir>`      |
| Hugo       | `hugo.toml`, `hugo.yaml`, or `hugo.json`         | `hugo --gc --minify --destination <out-dir>`                    |
| mdBook     | `book.toml`                                      | `mdbook build --dest-dir <out-dir>`                             |
| MkDocs     | `mkdocs.yml`                                     | `uvx mkdocs build --site-dir <out-dir>`                         |
| Nuxt       | `nuxt.config.ts`                                 | `npm i && npm run generate && mv .output/public <out-dir>`      |
| Storybook  | `.storybook/main.js` or `.ts`                    | `npm i && npm run build-storybook -- --output-dir <out-dir>`    |
| VitePress  | `.vitepress/config.js`, `.ts`, `.mjs`, or `.mts` | `npm i && npm run docs:build -- --outDir <out-dir>`             |
| Zola       | `zola.toml`                                      | `zola build --minify --output-dir <out-dir>`                    |

By default, the generator writes the website in the `cc_static_autobuilt` folder, which Clever Cloud then serves. If you set `CC_WEBROOT`, it writes the website there instead, and Clever Cloud serves this folder.

`CC_STATIC_AUTOBUILD_OUTDIR` sets another output folder, without changing the served folder. Set `CC_WEBROOT` to the same folder, or to a parent folder to serve the website under a path. For instance, to serve it under `/blog`:

```bash
clever env set CC_STATIC_AUTOBUILD_OUTDIR public/blog
clever env set CC_WEBROOT /public
```

Set this path in the configuration of the generator too, such as `baseURL = "/blog/"` for Hugo, so that the links of the website include it.

With `APP_FOLDER`, the generator runs from this folder, but `CC_WEBROOT` starts from the root of the repository. For a website in `site`:

```bash
clever env set APP_FOLDER site
clever env set CC_STATIC_AUTOBUILD_OUTDIR public
clever env set CC_WEBROOT /site/public
```

### Hugo version {#hugo}

Clever Cloud provides [Hugo Extended](https://gohugo.io/installation/linux/#editions), the edition that compiles Sass with its embedded LibSass. Set `CC_HUGO_VERSION` to {{% runtime_versions_list hugo %}} to select its version. Clever Cloud only provides a few recent versions of Hugo. To use an older one, declare it in a [`mise.toml` file](/doc/manage/mise/), with the same edition:

```toml {filename="mise.toml"}
[tools]
hugo-extended = "0.150.1"
```

## Static Site Generators (SSG) guides {#-static-site-generators-ssg-guides}

{{% include "shared/static-guides" %}}

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Put Varnish or Redirection.io in front of your website" icon="traffic-light" >}}
{{< /cards >}}
