---
title: "Images update: PHP 8.6, FrankenPHP 1.14, Rust 1.100, Chromium 158, Docker 29.10, Ruby built on demand"
description: PHP 8.6 and FrankenPHP 1.14, Rust 1.100, Chromium 158, Docker 29.10 with BuildKit secrets and SSH commands, Ruby versions built on demand with security fixes, and the removal of Java 7 and Play 1.2 to 1.6
date: 2026-11-26
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
  - Chromium 158.0.8127.88
  - FFmpeg 9.1
  - Mise 2026.11.12
  - NGINX 1.30.8
  - PostgreSQL client 19.0
  - Tailscale 1.104.7
- **Docker:**
  - Update to 29.10.1
  - Buildx 0.39.1
- **Erlang/Elixir:**
  - Erlang 27.3.4.20
  - Erlang 28.5.0.9
  - Erlang 29.1.3
- **FrankenPHP:**
  - FrankenPHP 1.14.0 (PHP 8.6.0, Caddy 2.11.9)
- **Java:**
  - Update to 1.8.0.514_p01
  - Update to 11.0.33.1_p1
  - Gradle 8.14.8 and 9.9.2
  - Java 7 is no longer available
  - Play 1.2 to 1.6 are no longer available
- **Node.js & Bun:**
  - Corepack 0.36.0
  - Yarn 4.19.0
- **PHP:**
  - PHP 8.6.0
  - Composer 2.2.33 and 2.11.3
  - Symfony CLI 5.23.0
  - Blackfire extension 2026.11.2
  - Event extension 3.2.0
  - MaxMind DB extension 1.15.0
  - SQLSRV and PDO_SQLSRV extensions 5.14.0 (PHP 8.4 and later)
  - Tideways extension 5.48.0
- **Python:**
  - uv 0.13.9
  - uWSGI 2.0.31
- **Rust:**
  - Update to 1.100.0

## PHP 8.6

[PHP 8.6](https://www.php.net/releases/8.6/) is available for PHP applications. It brings partial function application, and the `clamp()` function, among other features. To use it, set `CC_PHP_VERSION` to `8.6`, then redeploy:

```bash
clever env set CC_PHP_VERSION 8.6
```

PHP 8.5 stays the default version, also used when you set `CC_PHP_VERSION` to `8`. Many extensions don't have a release supporting PHP 8.6 yet. This version comes with the Blackfire, MailParse, MaxMind DB, OAuth, OpenTelemetry, SQLSRV, and PDO_SQLSRV extensions. Others, such as APCu, MongoDB, Redis, SSH2, or Xdebug, aren't available with PHP 8.6 in this release.

- [Learn more about PHP on Clever Cloud](/doc/deploy/applications/php/)
- [Read the PHP 8.6 release announcement](https://www.php.net/releases/8.6/)

## FrankenPHP 1.14

FrankenPHP 1.14.0 embeds PHP 8.6.0, with Caddy 2.11.9. FrankenPHP applications use it when you set `CC_PHP_VERSION` to `8.6`. Without this variable, or with `8` or `8.5`, they stay on FrankenPHP 1.13.6, with PHP 8.5.13.

With any other value, such as `8.4`, FrankenPHP applications run PHP 8.6. Starting with the next release, these values will make the deployment fail, as any unsupported value does: set `CC_PHP_VERSION` to `8`, `8.5`, or `8.6`, or remove it.

Unlike PHP applications on PHP 8.6, FrankenPHP 1.14 keeps the [extensions](/doc/deploy/applications/frankenphp/#included-extensions) of the previous version, except `protobuf`. The FrankenPHP project builds some of them from their development branches, such as `apcu`, `imagick`, `memcached`, or `redis`.

The `file_server` option of the `php_server` directive now accepts a block, with any option of the Caddy [`file_server`](https://caddyserver.com/docs/caddyfile/directives/file_server) directive, except `root`. With a [custom Caddyfile](/doc/deploy/applications/frankenphp/#custom-frankenphp-run-command), serving pre-compressed assets no longer needs a `handle` block, for instance:

```caddyfile {filename="Caddyfile"}
{
    frankenphp
}

:8080 {
    root public/
    php_server {
        file_server {
            precompressed zstd br gzip
        }
    }
}
```

- [Learn more about FrankenPHP on Clever Cloud](/doc/deploy/applications/frankenphp/)
- [Read the FrankenPHP 1.14.0 release notes](https://github.com/php/frankenphp/releases/tag/v1.14.0)

## Ruby versions built on demand

Our images no longer include the many Ruby versions that reached their end of life, nor every patch release of each branch, which makes them lighter for all our users. They include the latest releases of the supported Ruby branches: 3.3.14, 3.4.13, and 4.0.10.

When your application requests a specific version, such as `3.2.11` or an older patch release like `3.4.12`, Clever Cloud compiles it on demand during the build, with `rbenv`. Each new build compiles it again, and an application that restarts from its build cache reuses it.

This compilation needs memory: on an `XS` instance, it can fail. Enable a [dedicated build instance](/doc/manage/#dedicated-build-instance), such as `M`, which takes about two minutes:

```bash
clever scale --build-flavor M
```

When it compiles Ruby 2.6, 2.7, 3.1, or 3.2, Clever Cloud applies the fixes for [Ruby2Shell](/changelog/2026/11-19-images-update/#ruby-security-releases), adapted to these branches. They also cover the other regular expression and string vulnerabilities fixed in Ruby 3.3.13 and 3.3.14. These branches reached their end of life: migrate. An older patch release of a supported branch, such as `3.4.12`, doesn't get these fixes: use 3.3.14, 3.4.13, or 4.0.10.

To apply your own patches to a compiled Ruby, for security reasons for instance, set `CC_RUBY_PATCH` to the path of a patch file in your repository. For several files, use `CC_RUBY_PATCH_0`, `CC_RUBY_PATCH_1`, and so on.

To use a precompiled Ruby instead, declare it in a `mise.toml` file: [Mise](/doc/manage/mise/) downloads it in a few seconds, starting with Ruby 3.2. These builds don't include the fixes that Clever Cloud applies to the Ruby it compiles. In this case, don't set `CC_RUBY_VERSION`, and remove the `ruby` line of your `Gemfile`, or Clever Cloud also compiles this version:

```toml {filename="mise.toml"}
[tools]
ruby = "3.4"
```

`CC_RUBY_VERSION` now selects the Ruby version on every runtime except Docker, for instance for the tools that your hooks run. Without it, applications use Ruby 4.0. Ruby applications still read the `ruby` line of their `Gemfile`, when `CC_RUBY_VERSION` isn't set.

- [Learn more about Ruby on Clever Cloud](/doc/deploy/applications/ruby/)

## Docker: BuildKit secrets and better SSH

With Buildx, enabled by default with `CC_DOCKER_BUILDX`, Docker builds now receive each environment variable as a BuildKit secret, in addition to the build argument. The id of the secret is the name of the variable. A `RUN` instruction mounts it for its own duration only: the image and its history don't keep it, unless this command prints it or writes it to a file. Don't declare this variable with `ARG`, which adds it to the history:

```dockerfile {filename="Dockerfile"}
# syntax=docker/dockerfile:1
FROM node:26-alpine
WORKDIR /app
COPY package*.json .npmrc ./
RUN --mount=type=secret,id=NPM_TOKEN,env=NPM_TOKEN npm ci
```

For instance, npm reads a token from the environment with this `.npmrc` file, which holds no secret itself:

```ini {filename=".npmrc"}
//registry.npmjs.org/:_authToken=${NPM_TOKEN}
```

Nothing changes for an existing Dockerfile: build arguments stay, and BuildKit ignores the secrets it doesn't mount.

[SSH access](/doc/manage/ssh-access/#docker-applications) to Docker applications also improves. `clever ssh --command` now runs a command in the container, returns its exit code, and keeps its errors apart from its output. The session opens `bash` when the image includes it, and `/bin/sh` otherwise: an image without `bash`, such as an Alpine one, no longer prevents the connection. An application started before this release needs a restart to get these changes:

```bash
clever restart
clever ssh --command "ls -la"
```

- [Learn more about Docker on Clever Cloud](/doc/deploy/applications/docker/)

## Java 7 and Play 1.2 to 1.6 removal

Java 7 and Play 1.2 to 1.6 are no longer available. A deployment fails with `CC_JAVA_VERSION=7`, or with `CC_PLAY1_VERSION` set to one of these Play versions. Use Java 8 or later, and Play 1.7 or later. `CC_JAVA_VERSION=graalvm-ce` still selects GraalVM CE for Java 17.

Clever Cloud no longer adds `-XX:-UseBASE64Intrinsics` to Java applications, as our Temurin releases of Java 17, 21, and 25 [fix Java4Shell](/changelog/2026/11-19-java-security-releases/).

## Security updates

Several packages of this release fix vulnerabilities:

- Chromium 158 includes [204](https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_01699533288.html) and [one](https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_01734282054.html) security fixes in its two releases, seven of them critical
- Composer 2.2.33 and 2.11.3 fix a [high severity code execution flaw](https://github.com/composer/composer/security/advisories/GHSA-374h-4mh9-7rpm) with a crafted `vendor-dir` in projects you don't trust
- cryptsetup 2.8.9 fixes [three high severity flaws](https://cdn.kernel.org/pub/linux/utils/cryptsetup/v2.8/v2.8.9-ReleaseNotes) in LUKS2 metadata validation and keyring handling
- Docker 29.10.1 fixes [two vulnerabilities](https://github.com/moby/moby/releases/tag/docker-v29.10.1), one of them in `docker cp`
- Erlang 27.3.4.20, 28.5.0.9, and 29.1.3 fix [nine vulnerabilities](https://github.com/erlang/otp/security/advisories), and a critical TLS one on Erlang 28
- Expat 2.11.0 fixes [three vulnerabilities](https://github.com/libexpat/libexpat/blob/R_2_11_0/expat/Changes) in XML parsing and the `xmlwf` tool
- glibc 2.44 of the Docker image includes fixes for three vulnerabilities, such as [CVE-2026-100290](https://www.cve.org/CVERecord?id=CVE-2026-100290)
- GnuTLS 3.8.14 fixes [three low severity flaws](https://gitlab.com/gnutls/gnutls/-/raw/3.8.14/NEWS), and a buffer overrun in DSA signing
- GPGME 2.3.1 fixes a [critical double free](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) with crafted OpenPGP keys
- Gradle 8.14.8 and 9.9.2 fix [four high severity flaws](https://docs.gradle.org/9.9.2/release-notes.html), such as unverified SFTP host keys
- Java 8 and 11 releases fix five vulnerabilities of the [OpenJDK advisory](https://openjdk.org/groups/vulnerability/advisories/2026-11-17)
- libffi 3.8.2 fixes [memory corruptions](https://github.com/libffi/libffi/releases/tag/v3.8.2) on several architectures
- libseccomp 2.6.2 fixes [four flaws](https://github.com/seccomp/libseccomp/releases/tag/v2.6.2), including a high severity filter bypass
- libyaml 0.2.7 limits the [recursion depth](https://github.com/yaml/libyaml/releases/tag/0.2.6) of collections
- NGINX 1.30.8 fixes a [TLS 1.3 vulnerability](https://nginx.org/en/security_advisories.html) with `ssl_early_data`
- OpenEXR 3.5.5 fixes [five vulnerabilities](https://github.com/AcademySoftwareFoundation/openexr/security/advisories), two of them high severity
- runc 1.5.3 of the Docker image fixes a [high severity flaw](https://github.com/opencontainers/runc/releases/tag/v1.5.3) in checkpoint and restore
- shadow 4.20.4 hardens [`newuidmap` and `newgidmap`](https://github.com/shadow-maint/shadow/releases/tag/4.20.4) against symbolic links
- Tailscale 1.104.7 fixes the [TS-2026-018](https://tailscale.com/security-bulletins) vulnerability of its Kubernetes operator
- Telegraf 1.40.4 uses Go 1.27.4, and fixes a [high severity flaw](https://github.com/advisories/GHSA-mgcc-cww5-fp2q) in `go-jose`
- The Event extension 3.2.0 of PHP fixes [heap buffer overflows](https://pecl.php.net/package-changelog.php?package=event) in `EventBuffer`
- Zstandard 1.6.0 fixes [several memory safety flaws](https://github.com/facebook/zstd/releases/tag/v1.6.0), including CVE-2026-124851

## Other changes

- Lua 5.4, Tcl 8.6, Tk 8.6, and the Aerospike C and Python clients are no longer included in our images
- The SQLSRV and PDO_SQLSRV extensions are no longer available with PHP 8.1 to 8.3, as version 5.14 needs PHP 8.4
- With `CC_RAKEGOALS_SINGLE_INSTANCE=true`, a Ruby application runs its `CC_RAKEGOALS` tasks on a single instance
- The build cache now includes the Node.js version that Clever Cloud installs during the build, if any
- In front of Ruby and Python applications, NGINX keeps the `X-Forwarded-For` header sent with `Forwarded` by platform proxies
- The health check waits up to 5 seconds for each HTTP response before it retries, instead of 60
- `CC_VPN_COMP_LZO=disable` removes the `comp-lzo` directive, which prevents the OpenVPN kernel offload (DCO)

## Linux Kernel

Kernel is [now updated independently](/changelog/2026/05-12-linux-kernel-7.0.6). Current version is 7.3.6.
