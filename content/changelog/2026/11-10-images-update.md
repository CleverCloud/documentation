---
title: "Images update: FrankenPHP and Python security fixes, Chromium 157, Clever Tools 5.4, Gradle 9.9, CC_APP_FOLDER"
description: FrankenPHP 1.13.5 and Python security releases, Chromium 157, Clever Tools 5.4, Gradle 9.9, Hugo 0.168 and 0.169, the CC_APP_FOLDER variable, Zola auto-build with zola.toml, and a fix for workers
date: 2026-11-10
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

- **Common:**
  - Chromium 157.0.8103.38
  - Clever Tools 5.4.0
  - ExifTool 13.61
  - Mise 2026.11.2
  - OAuth2 Proxy 7.15.6
  - OpenSSH 10.6_p2
  - Poppler 26.11.0
  - ProxySQL 2.7.4
  - rsync 3.5.2
  - Subversion 1.15.0
  - Tailscale 1.104.5
- **Docker:**
  - Update to 29.9.3
  - Buildx 0.38.2
  - OpenVPN 2.7.9
- **FrankenPHP:**
  - Update to 1.13.5 (PHP 8.5.12, Caddy 2.11.9)
- **Java:**
  - Update to 1.8.0.512_p09
  - Update to 11.0.33_p10
  - Gradle 9.9.0
- **Node.js & Bun:**
  - nvm 0.41.0
- **PHP:**
  - MongoDB extension 1.21.12 (PHP 8.1 to 8.4)
  - xdebug extension 3.5.3
- **Python:**
  - Update to 3.11.18
  - Update to 3.12.16
  - Update to 3.13.18
  - Update to 3.14.10
  - pip 26.3
  - uv 0.13.7
- **Rust:**
  - rustup 1.29.3
- **Static:**
  - Caddy 2.11.9
  - Hugo 0.168.0 and 0.169.0 are now available

## FrankenPHP 1.13.5

[FrankenPHP](/doc/deploy/applications/frankenphp/) 1.13.5 is a security release that fixes 17 vulnerabilities. The most severe one let `php_server` run an uploaded file as PHP when its path contained a PHP extension, such as `/uploads/photos.php.php/avatar.jpg`. Others include an open redirect, a `Host` spoofing over HTTP/2, a crash a client could trigger, and slow request bodies blocking every PHP thread.

In worker mode, FrankenPHP now only resets between requests the state built from the HTTP request. The values of `error_get_last()`, `strtok()`, `http_get_last_response_headers()`, and the libxml errors persist again. Call `error_clear_last()`, `libxml_clear_errors()`, or `http_clear_last_response_headers()` if you need a clean state.

FrankenPHP now answers `400` to requests that are ambiguous about the script they run. A client header can no longer override a variable set with `env`. This release embeds Caddy 2.11.9, also used by [Static](/doc/deploy/applications/static/) applications. Since 2.11.8, Caddy validates its configuration more strictly, and rejects some settings it silently accepted before.

- [Read the FrankenPHP 1.13.5 release notes](https://github.com/php/frankenphp/releases/tag/v1.13.5)
- [Read the Caddy 2.11.8 release notes](https://github.com/caddyserver/caddy/releases/tag/v2.11.8)
- [Read the Caddy 2.11.9 release notes](https://github.com/caddyserver/caddy/releases/tag/v2.11.9)

## Python security releases

Python 3.11.18, 3.12.16, 3.13.18, and 3.14.10 are [expedited security releases](https://blog.python.org/2026/10/python-3152-31410-31318-31216-31118). They distrust the compromised intermediate certificates of the [eMudhra certificate authority](/changelog/2026/10-21-images-update/#emudhra-certificate-authorities-distrust). They also make the `tarfile` extraction filters reject links that replace their destination. Python 3.11, 3.12, and 3.13 also update the bundled Expat library to 2.9.0.

If your application requests a Python branch, such as `3.13`, it gets the fixed release at its next deployment.

- [Learn more about Python on Clever Cloud](/doc/deploy/applications/python/)

## CC_APP_FOLDER

`CC_APP_FOLDER` replaces `APP_FOLDER` to deploy an application from a folder of your repository. The previous name still works, with a deprecation warning in the deployment logs. If you set both, the deployment fails: keep only the new one.

Clever Cloud now uses this folder more consistently:

- Clever Cloud reads `mise.toml`, or the file set in `CC_MISE_FILE_PATH`, from this folder
- Linux applications read the Makefile of their build and run commands from this folder
- FrankenPHP and Static applications look for `CC_WEBROOT` in this folder first, then at the root of the repository

In FrankenPHP and Static applications, the deployment now fails when the `CC_WEBROOT` folder doesn't exist after the build, or when its path has a `..` segment. In Static applications, the build command is the last step that can create this folder.

## Zola auto-build with zola.toml

The [auto-build](/doc/deploy/applications/static/#static-site-generators-ssg-auto-build) of Static applications now detects a [Zola](https://www.getzola.org) project from its `zola.toml` file, in addition to `config.toml`.

The first images update after December 1, 2026 will stop detecting `config.toml`, to avoid conflicts with other tools that use this file name. If your Zola website relies on the auto-build, rename this file to `zola.toml` before this date.

## Other changes

- Clever Cloud now deletes the `.nvmrc` file on every runtime, [as announced](/changelog/2026/11-05-nvmrc-all-runtimes/): set the version with `CC_NODE_VERSION`
- [Workers](/doc/manage/workers/) no longer start on dedicated build instances, nor with Clever Tasks: they only run next to your application
- A Ruby application without a `Gemfile.lock` or `gems.locked` file now fails at the start of its deployment
- The `memcache` extension is now loaded with PHP 8.5

## Linux Kernel

Kernel is [now updated independently](/changelog/2026/05-12-linux-kernel-7.0.6). Current version is 7.2.15.
