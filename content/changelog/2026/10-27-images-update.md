---
title: "Images update: FrankenPHP, Java, PHP, Python and Ruby security fixes, rebar3 3.28"
description: Java security updates, Ruby regular expression fixes, FrankenPHP 1.13.4, CVE-2023-0662 fix for PHP 5.6 to 7.3, eMudhra distrust follow-up in certifi, Python and rebar3, Bun, libheif and Redis fixes, and new Rust build options
date: 2026-10-27
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
  - Anubis 1.28.2
  - libheif 1.23.7
  - Mise 2026.10.19
  - Nano 9.3
  - Otoroshictl 0.0.20
  - Redis 8.10.3
- **Erlang/Elixir:**
  - rebar3 3.28.0
- **FrankenPHP:**
  - Update to 1.13.4 (PHP 8.5.12, Caddy 2.11.7)
- **Java:**
  - Update to 17.0.21_p9
  - Update to 21.0.13_p9
  - Update to 25.0.5_p8
- **Node.js & Bun:**
  - Bun 1.4.4
- **PHP:**
  - CVE-2023-0662 fix for 5.6, 7.0, 7.1, 7.2 and 7.3
- **Python:**
  - Update to 3.13.17
  - Update to 3.14.9
  - certifi 2026.10.23
  - uv 0.13.5
- **Ruby:**
  - Update to 3.3.13
  - Update to 3.4.12
  - Update to 4.0.9
- **Rust:**
  - rustup 1.29.2

## Java security updates

Our images ship the [Eclipse Temurin](https://adoptium.net/temurin/releases/) builds of Java. The 17.0.21, 21.0.13 and 25.0.5 releases include the [OpenJDK fixes of October 2026](https://openjdk.org/groups/vulnerability/advisories/2026-10-20). Its risk matrix lists 48 vulnerabilities, with CVSS 3.1 scores up to 7.0, in components such as networking, TLS, XML processing and image decoding.

## Ruby regular expression fixes

Ruby 3.3.13, 3.4.12 and 4.0.9 fix [memory corruption bugs in the regular expression engine](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves/), which GitLab showed could lead to remote code execution. Your application is exposed if it compiles regular expressions from untrusted input, for example with `Regexp.new` or by interpolating user input into a pattern. Neither `Regexp.timeout` nor length limits protect against these bugs.

If your application requests Ruby 3.3, 3.4 or 4.0 without a patch level, it gets the fixed release at its next deployment. A version pinned to its patch level, such as `4.0.7`, stays on it until you update it.

- [Learn more about Ruby on Clever Cloud](/doc/deploy/applications/ruby/)

## FrankenPHP 1.13.4

[FrankenPHP 1.13.4](https://github.com/php/frankenphp/releases/tag/v1.13.4) is a security release. It fixes a high-severity issue affecting worker mode in FrankenPHP 1.13.2, shipped by the [previous release](/changelog/2026/10-21-images-update/): a single unauthenticated request could crash the whole process. It also fixes use-after-free issues and leaks of data between requests, mostly in worker mode, such as per-request environment variables visible to later requests.

## PHP 5.6 to 7.3 security fixes

Our [patched builds of PHP 5.6 to 7.3](/changelog/2026/10-21-php-eol-security-backport/) now also include the fix for [CVE-2023-0662](https://www.cve.org/CVERecord?id=CVE-2023-0662), which PHP 8.0.28 introduced with the `max_multipart_body_parts` directive. Without it, a form upload made of a very large number of parts could exhaust CPU resources or fill the disk with log entries. PHP now parses at most `max_input_vars` plus `max_file_uploads` parts per request by default. Our PHP 7.4, 8.0 and 8.1 builds already include this fix.

These branches remain end of life and affected by many other vulnerabilities, so we recommend that you migrate without delay to a [supported version](https://www.php.net/supported-versions.php) such as PHP 8.3, 8.4 or 8.5.

## eMudhra certificate authorities distrust follow-up

Following the [eMudhra certificate authorities distrust](/changelog/2026/10-21-images-update/#emudhra-certificate-authorities-distrust) of the previous release, more tools now align with the system trust store:

- Anubis 1.28.2 is built with Go 1.27.3, which rejects certificate chains containing the affected intermediates
- certifi 2026.10.23, used by the system Python, also drops the emSign Root CA - C1 and emSign ECC Root CA - C3 roots
- Python 3.13.17 and 3.14.9 bundle pip 26.2.2 with certifi 2026.10.19, which drops the emSign ECC Root CA - G3 root, as do the managed CPython 3.11 and later builds that uv 0.13.5 installs
- rebar3 3.28.0 no longer bundles its own certificates and uses the system trust store
- rustup 1.29.2 updates its certificate validation to reject the affected intermediates
- uv 0.13.5 rejects certificate chains containing the affected intermediates

If your dependencies pin `certifi`, update it to 2026.10.23 or later.

## Other security fixes

- Bun 1.4.4 fixes [CVE-2026-111497](https://www.cve.org/CVERecord?id=CVE-2026-111497), also known as Node2Shell, in its own copy of the Brotli library. The [previous release](/changelog/2026/10-21-images-update/#nodejs-security-releases) already fixed it in Node.js and in the system Brotli library.
- libheif 1.23.7 fixes 14 high-severity vulnerabilities in HEIF and AVIF image processing, including a heap use-after-free that only affected version 1.23.6, shipped by the previous release.
- Mise 2026.10.19 tightens its trust checks: fewer actions now implicitly trust the configuration of a project, and safe mode blocks more operations.
- Redis 8.10.3 fixes a heap buffer overflow when a cluster propagates a `PUBLISH` or `SPUBLISH` message larger than 4 GB.

## Rust build improvements

[Rust](/doc/deploy/applications/rust/) applications now honor the `default-run` field of `Cargo.toml` to select the binary to start, when your project builds several of them. Clever Cloud only looks for binaries in the default members of your workspace, the ones `cargo build` builds. `CC_RUST_BIN` still takes precedence, and the undocumented `CARGO_BIN` alias is no longer supported.

Set `CC_RUST_INSTALL=true` to build your application with `cargo install` instead of `cargo build`. Clever Cloud then removes the build artifacts, which keeps your build cache smaller. The build now vendors your dependencies with `cargo vendor` when possible, and the dependencies cache then stores their sources instead of the whole `target/release` folder.

## Linux Kernel

Kernel is [now updated independently](/changelog/2026/05-12-linux-kernel-7.0.6). Current version is 7.2.13.
