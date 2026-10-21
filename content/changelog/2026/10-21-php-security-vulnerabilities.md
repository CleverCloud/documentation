---
title: PHP 8.2.35, 8.3.36, 8.4.27 and 8.5.12 are available (Security update)
description: New PHP versions fix the critical vulnerabilities CVE-2026-109618 and CVE-2026-109619, Clever Cloud applies mitigations and limits FrankenPHP to version 1.13
date: 2026-10-21
tags:
  - frankenphp
  - images
  - php
  - security
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The [CERT-EU security advisory 2026-018](https://cert.europa.eu/publications/security-advisories/2026-018/) describes two critical vulnerabilities affecting PHP, [CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618) and [CVE-2026-109619](https://www.cve.org/CVERecord?id=CVE-2026-109619). With a CVSS v4 score of 9.2, both can allow unauthenticated remote code execution on PHP installations serving web requests. The [PHP security advisory](https://www.php.net/archive/2026.php#2026-10-21-5) gives the technical details and the mitigations available until you update.

We set up an analysis team on the evening of 20 October 2026 to follow the issue and apply fixes as they become available. Affected customers received an alert through the [Console](https://console.clever-cloud.com) on the morning of 21 October 2026, followed by an email.

A [dedicated maintenance on the status page](https://www.clevercloudstatus.com/schedules/3a899921-b728-4f63-943a-223fb4e361a5) shares updates on the fixes.

## Active mitigations

Before the release of the new PHP versions, we set `session.upload_progress.enabled` to `Off` on all our customers' PHP with Apache instances, following the [PHP security team recommendations](https://www.php.net/archive/2026.php#2026-10-21-5). This setting only disables upload progress tracking in sessions. We didn't block `multipart/form-data` requests, as this could break your applications. The PHP security team [validated this attack path against `mod_php`](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w), but hasn't demonstrated a complete exploit against PHP-FPM, which our PHP instances use.

PHP 8.2.35, 8.3.36, 8.4.27 and 8.5.12 are now available on Clever Cloud, and we are redeploying your PHP applications so they use them automatically. If your application uses one of these branches, you have nothing to do.

PHP 8.1 and earlier [reached end of life](https://www.php.net/supported-versions.php) and no longer receive updates from the PHP project. We are studying a backport of the fixes to these versions. They nevertheless remain end of life and affected by many other vulnerabilities, so we recommend that you migrate without delay to a [supported version](https://www.php.net/supported-versions.php) such as PHP 8.3, 8.4 or 8.5 (PHP 8.2 reaches its end of life on 31 December 2026).

## FrankenPHP 1.13 is now the only supported version

FrankenPHP 1.13 is now the only version supported on Clever Cloud, whatever the value of `CC_PHP_VERSION`. Major vulnerabilities affect all earlier versions, and FrankenPHP maintainers [consider the 1.12 branch as end of life](https://github.com/php/frankenphp/issues/2732#issuecomment-6316479790).

The available release, [FrankenPHP 1.13.1](https://github.com/php/frankenphp/releases/tag/v1.13.1), includes the fixes.

## Managed Matomo add-ons

We moved every managed [Matomo](/doc/deploy/services/matomo/) add-on that ran PHP 8.1 or 8.2 to PHP 8.3.

If you have any questions or need help, contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).

- [Learn more about PHP on Clever Cloud](/doc/deploy/applications/php/)
- [Learn more about FrankenPHP on Clever Cloud](/doc/deploy/applications/frankenphp/)
