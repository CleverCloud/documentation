---
type: docs
linkTitle: Static with Apache
title: Static with Apache runtime
description: Deploy static websites and single-page applications on Clever Cloud with Apache and .htaccess files, a build hook, cache headers, and Git, FTP, or SFTP
keywords:
- apache
- ftp
- htaccess
- sftp
- single page application
- spa
- static apache hosting
- static files
aliases:
- /doc/applications/static-apache
---

## Overview

Static with Apache serves the files of your website with [Apache](https://httpd.apache.org) 2.4. Use it when your website relies on `.htaccess` files, to rewrite URLs, set headers, or control access, or to send your files over [FTP](#deploy-with-ftp) instead of Git. Its instances start with the `nano` size.

For other static websites, prefer the [Static](/doc/deploy/applications/static/) runtime. Unlike Static with Apache, it:

- Starts with the smaller `pico` instance size
- Serves your files with Static Web Server or Caddy, instead of Apache
- Runs your build command, or the one of the static site generator it detects, such as Hugo or Astro

## Create your Static with Apache application

To create a new Static with Apache application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type static-apache
```

The [getting started guide](/doc/getting-started/) describes each step of the creation of an application.

## Configure your Static with Apache application

### Mandatory needs

A Static with Apache application serves the `index.html` file at the root of the webroot, the folder of your website, as its home page. Its other pages, styles, and images sit next to it, as in this minimal website:

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

The webroot is the root of your repository, or the folder set in `CC_WEBROOT`. Set its path from the root of your repository, starting with a `/` and without `..`. For instance, to serve the `dist` folder that the build of your website writes:

```bash
clever env set CC_WEBROOT /dist
```

Apache serves every file of the webroot: keep notes, scripts, configuration files, and secrets out of it. Without `CC_WEBROOT`, it serves your whole repository, with its source code and its configuration: set this variable to keep them private.

### Build phase

Clever Cloud doesn't detect any build tool: build your website in the pre-build or the post-build [hook](/doc/manage/build-hooks/). For instance, to build a single-page application (SPA) with Vite, and serve the folder it writes:

```bash
clever env set CC_POST_BUILD_HOOK "npm ci && npm run build"
clever env set CC_WEBROOT /dist
```

The image includes Node.js and npm, and `CC_NODE_VERSION` sets the version of Node.js, such as `24`. To install another tool, declare it in a [`mise.toml` file](/doc/manage/mise/): Clever Cloud installs it before the build. For instance, [Pagefind](https://pagefind.app), which indexes your website for its search:

```toml {filename="mise.toml"}
[tools]
"github:Pagefind/pagefind" = "1.6.0"
```

### Serve a single-page application

An SPA handles its routes in the browser: when a visitor reloads a page such as `/account`, Apache finds no file to serve. To answer with `index.html` instead, add these rules to the `.htaccess` file at the root of the webroot:

```apache {filename="public/.htaccess"}
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} !\.[a-z0-9]+$ [NC]
RewriteRule ^ index.html [L]
```

The paths that end with an extension keep their `404` error, such as a missing `app.js` file, or a route with a dot, such as `/users/jane.doe`. With a build, put the `.htaccess` file in the folder that it copies unchanged, such as `public` for Vite.

### Set cache headers

Apache compresses its HTML, CSS, and JavaScript answers with gzip. To let browsers keep the files that Vite names after their content, in the `assets` folder, and check the pages at each visit, add these directives to your `.htaccess` file:

```apache {filename="public/.htaccess"}
<If "%{REQUEST_URI} =~ m#^/assets/#">
  Header set Cache-Control "public, max-age=31536000, immutable"
</If>
<FilesMatch "\.html$">
  Header set Cache-Control "no-cache"
</FilesMatch>
```

### Prerender your pages at build time

Google and Bing run the JavaScript of an SPA, but social network previews and some AI crawlers don't, and get an empty page. Prerender your routes at build time instead, with the static output of your framework, such as Astro, Nuxt `generate`, or SvelteKit `adapter-static`.

The build then writes an `index.html` file for each route, which Apache serves, while your SPA rules answer the other paths. A route such as `/about` becomes a folder: to keep HTTPS when Apache adds its trailing slash, see the [Apache page](/doc/deploy/applications/php/apache/#redirections-of-folders).

### Other Apache settings

The [Apache page](/doc/deploy/applications/php/apache/) applies to Static with Apache too. It explains how to ask for a password with `CC_HTTP_BASIC_AUTH`, remove headers, or raise the size limit of the request headers with `CC_APACHE_HEADERS_SIZE`.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit, with the whole folder of your application. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

Clever Cloud doesn't keep the dependencies of your hooks between commits: they install them again at each new commit.

## Deploy with FTP

To send your files over FTP instead of Git, create the application from the [Console](https://console.clever-cloud.com), and choose FTP as its deployment method. Clever Cloud then creates an [FS Bucket](/doc/deploy/storage/fs-bucket/) add-on with the ID of your application, which holds its files.

The **Dashboard** of this add-on, in the Console, shows the host, the user, and the password of the bucket. Connect to it with an SFTP client, or with an FTP client over TLS (FTPS), as the [FS Bucket page](/doc/deploy/storage/fs-bucket/#access-your-files) explains.

Send your files to the root of the bucket, or to the folder set in `CC_WEBROOT`. The application doesn't start on its own: once your files are on the bucket, start it from the Console, or with `clever restart`. Apache then serves each new or changed file right away, without a new deployment.

You can't move an FTP application to another region, nor delete its FS Bucket on its own: deleting the application deletes its bucket.

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/php/apache" title="Apache" subtitle="Configure the web server with .htaccess, authentication, and timeouts" icon="feather" >}}
  {{< card link="/developers/doc/deploy/storage/fs-bucket" title="FS Buckets" subtitle="Reach the files of an FTP application, over FTP or SFTP" icon="fsbucket" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
  {{< card link="/developers/doc/deploy/applications/static" title="Static" subtitle="Build a website with a static site generator, and serve it" icon="static" >}}
{{< /cards >}}
