---
title: "Images update: PHP 8.5, Composer 2.9, Ruby 4.0, V (Vlang) 0.5"
description: PHP 8.5 is now available, Composer 2.9 introduces security features, and the default Hugo version will be updated soon
date: 2026-01-15
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

* **Common:**
  * Linux kernel 6.17.13
  * cURL 8.18.0
  * NGINX 1.28.1
  * OAuth2 Proxy 7.13.0
  * Otoroshictl 0.0.13
  * Poppler 26.01.0
  * Tailscale 1.92.4
* **Docker:**
  * Update to 29.1.4
* **Elixir:**
  * Update to 1.19.5
  * Erlang 28.3
* **Node.js:**
  * Update to 24.13.0 (npm 11.6.2)
  * Bun 1.3.6
* **PHP:**
  * Update to 8.1.34
  * Update to 8.2.30
  * Update to 8.3.29
  * Update to 8.4.16
  * Update to 8.5.1
  * Composer 2.9.2
  * Symfony CLI 5.16.1
  * Blackfire extension 1.92.51
  * gRPC extension 1.76.0
  * Imagick extension 3.8.1
  * Maxmind DB extension 1.13.0
  * New Relic extension 12.2.0.27
  * Protobuf extension 3.23.4, 3.25.8 and 4.33.2
  * Redis extension 6.3.0
  * Tideways extension 5.31.0 (Daemon 1.11.4)
  * YAML extension 2.3.0
* **Python:**
  * uv 0.9.24
* **Ruby:**
  * Update to 3.4.8
  * Update to 4.0.1
* **V (Vlang):**
  * Update to 0.5

## PHP 8.5 and Composer 2.9

PHP 8.5 is now available. To use it, set `CC_PHP_VERSION=8.5` as PHP 8.4 release is still the default version. We'll move to PHP 8.5 as the default version in April 2026. PHP 8.1 is now [considered as end-of-life](https://www.php.net/supported-versions.php).

[Supported extensions](/doc/applications/php/#available-extensions-and-modules) for PHP 8.5 are: `amqp`, `apcu`, `blackfire`, `event`, `excimer`, `gnupg`, `grpc`, `imagick`, `imap`, `mailparse`, `maxminddb`, `memcached`, `oauth`, `opentelemetry`, `pdo_sqlsrv`, `protobuf`, `pspell`, `rdkafka`, `redis`, `sqlsrv`, `ssh2`, `tideways`, `uploadprogress`, `yaml`, `zip`.

Composer 2.9 introduces a new default behavior: it [automatically blocks updates to packages with known security advisories](https://blog.packagist.com/composer-2-9/). As mentioned by developers, "*it prevents you from accidentally updating to vulnerable package versions. You can configure this behavior via the new audit.block-insecure config settings if needed.*"

- [Learn more about Composer Audit configuration settings](https://getcomposer.org/doc/06-config.md#audit)

## Hugo default version update

In next release, we will update the default Hugo version to `0.152` and only keep `0.150`and superior as available versions. If you need an older version, use Mise to set `hugo` or `hugo-extended` version in `mise.toml` file.

- [Learn more about Mise on Clever Cloud](/doc/reference/reference-environment-variables/#install-tools-with-mise-package-manager)
- [Learn more about Hugo on Clever Cloud](/doc/applications/static/#static-site-generators-ssg-auto-build)
