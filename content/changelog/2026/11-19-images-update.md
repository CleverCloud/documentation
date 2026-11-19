---
title: "Images update: FrankenPHP, PHP, and Ruby security fixes, Clever Tools 5.5, Hugo 0.169 by default"
description: Ruby security releases with the Ruby2Shell fix, PHP security releases, FrankenPHP 1.13.6, Apache 2.4.71, NGINX 1.30.7, Clever Tools 5.5, and Hugo 0.169 as the default version
date: 2026-11-19
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

We updated all our images, except Docker. Deployment is in progress for all our users.

- **Common:**
  - Apache 2.4.71
  - Chromium 157.0.8103.78
  - ClamAV 1.5.5
  - Clever Tools 5.5.0
  - ExifTool 13.64
  - Git 2.56.1
  - LibreOffice 26.8.2.2
  - Mise 2026.11.7
  - NGINX 1.30.7
  - OpenVPN 2.7.9
  - Tailscale 1.104.6
  - Zellij 0.46.0
- **FrankenPHP:**
  - Update to 1.13.6 (PHP 8.5.13, Caddy 2.11.9)
- **Go:**
  - Update to 1.27.4
- **Java:**
  - Update to 17.0.21.1_p2
  - Update to 21.0.13.1_p2
  - Update to 25.0.5.1_p2
  - Gradle 8.14.7 and 9.9.1
- **Node.js & Bun:**
  - Bun 1.4.5
- **PHP:**
  - Update to 8.2.36
  - Update to 8.3.37
  - Update to 8.4.28
  - Update to 8.5.13
  - Composer 2.2.32 and 2.11.2
  - MongoDB extension 2.1.12 (PHP 8.5)
  - OpenTelemetry extension 1.5.0
- **Python:**
  - uv 0.13.8
- **Ruby:**
  - Update to 3.3.14
  - Update to 3.4.13
  - Update to 4.0.10
- **Static:**
  - Static Web Server 2.44.3
  - Hugo 0.169 is now the default version

## Ruby security releases

Ruby 3.3.14, 3.4.13, and 4.0.10 fix [seven vulnerabilities](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/) in regular expressions and in the case conversion of strings. Six of them may allow remote code execution, including the heap overflow known as Ruby2Shell, [CVE-2026-132825](https://www.cve.org/CVERecord?id=CVE-2026-132825).

If your application requests a Ruby branch, such as `3.4`, it gets the fixed release at its next deployment. If `CC_RUBY_VERSION` or your `Gemfile` sets an exact version, such as `3.4.12`, your application stays on it: update it to a fixed release. Ruby 3.2 and earlier reached their end of life and don't receive these fixes: migrate to a supported version.

- [Learn more about Ruby on Clever Cloud](/doc/deploy/applications/ruby/)

## PHP security releases

PHP [8.2.36](https://www.php.net/archive/2026.php#2026-11-19-1), [8.3.37](https://www.php.net/archive/2026.php#2026-11-19-2), [8.4.28](https://www.php.net/archive/2026.php#2026-11-19-3), and [8.5.13](https://www.php.net/archive/2026.php#2026-11-19-4) are security releases. They fix vulnerabilities in PHP-FPM, sessions, SOAP, Phar, and the date extension, among others, some of which can lead to remote code execution. The PHP project [rates the most severe ones as critical](https://www.php.net/archive/2026.php#2026-11-18-1), and states that they require a non-default configuration or an uncommon setup.

PHP 8.5.13 also fixes [CVE-2026-129474](https://www.cve.org/CVERecord?id=CVE-2026-129474), a use-after-free only known to be remotely exploitable on this branch. Until this release, we set `zend.exception_ignore_args` to `On` on PHP 8.5 applications to protect them, which removed the arguments from exception stack traces. The updated images restore its previous value.

PHP 8.1 and earlier [reached end of life](https://www.php.net/supported-versions.php) and don't receive these fixes: migrate to a supported version.

- [Learn more about PHP on Clever Cloud](/doc/deploy/applications/php/)

## FrankenPHP 1.13.6

[FrankenPHP](/doc/deploy/applications/frankenphp/) 1.13.6 embeds PHP 8.5.13 and its security fixes.

This release also fixes several bugs. PHP system calls, such as `stream_select()`, no longer fail intermittently with an `EINTR` error. In worker mode, a restart of the workers requested through the admin API during a configuration reload no longer crashes FrankenPHP.

- [Read the FrankenPHP 1.13.6 release notes](https://github.com/php/frankenphp/releases/tag/v1.13.6)

## Hugo 0.169 by default

[Static](/doc/deploy/applications/static/#hugo) applications now use Hugo 0.169 when you don't set `CC_HUGO_VERSION`, instead of 0.163, [as announced](/changelog/2026/11-04-hugo-0.169-default/).

From December 1, 2026, Hugo 0.168 will be the minimum supported version. If your application sets `CC_HUGO_VERSION` to an older version, set it to `0.168` or `0.169`, or remove it to use the default, then redeploy.

## Other changes

- NGINX 1.30.7 fixes the [NGINX2Root vulnerabilities](/changelog/2026/11-19-nginx2root/)
- Bun 1.4.5 includes [security fixes](https://bun.com/blog/bun-v1.4.5) for HTTP/3, TLS, and DNS
- The Node.js version included in our images is its latest [security release](https://nodejs.org/en/blog/release/v26.13.1)
- The Java 17, 21, and 25 releases are the ones announced [to fix Java4Shell](/changelog/2026/11-19-java-security-releases/)
- Apache 2.4.71 fixes [three vulnerabilities](https://httpd.apache.org/security/vulnerabilities_24.html), including a critical one in `mod_http2`
- Go 1.27.4 includes [security fixes](https://go.dev/doc/devel/release#go1.27.4) to cgo, the `go` command, the compiler, the linker, and the `net/http` package

## Linux Kernel

Kernel is [now updated independently](/changelog/2026/05-12-linux-kernel-7.0.6). Current version is 7.3.5.
