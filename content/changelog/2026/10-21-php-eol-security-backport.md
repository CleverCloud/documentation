---
title: PHP 7.4.33, 8.0.30 and 8.1.34 patched for CVE-2026-109618 and CVE-2026-109619 (Security update)
description: Clever Cloud applies the fixes for the critical PHP vulnerabilities CVE-2026-109618 and CVE-2026-109619 to the end-of-life PHP 7.4, 8.0 and 8.1 branches
date: 2026-10-21
tags:
  - images
  - php
  - security
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Following the [release of PHP 8.2.35, 8.3.36, 8.4.27 and 8.5.12](/changelog/2026/10-21-php-security-vulnerabilities/), we applied the fixes for the critical vulnerabilities [CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618) and [CVE-2026-109619](https://www.cve.org/CVERecord?id=CVE-2026-109619) to the PHP 7.4, 8.0 and 8.1 branches, which [reached end of life](https://www.php.net/supported-versions.php).

Patched builds of PHP 7.4.33, 8.0.30 and 8.1.34 are now available on Clever Cloud, and we're redeploying your PHP applications so they use them automatically. If your application uses one of these branches, you have nothing to do.

These builds only fix CVE-2026-109618 and CVE-2026-109619. PHP 8.1 and earlier remain affected by many other vulnerabilities, so we recommend that you migrate without delay to a [supported version](https://www.php.net/supported-versions.php) such as PHP 8.3, 8.4 or 8.5 (PHP 8.2 reaches its end of life on December 31, 2026). To change the PHP version of your application, set the `CC_PHP_VERSION` environment variable and redeploy it:

```bash
clever env set CC_PHP_VERSION 8.5
clever restart --without-cache
```

The [dedicated maintenance on the status page](https://www.clevercloudstatus.com/schedules/3a899921-b728-4f63-943a-223fb4e361a5) keeps sharing updates on the fixes. If you have any questions or need help, contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).

- [Learn more about PHP on Clever Cloud](/doc/deploy/applications/php/)
