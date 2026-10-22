---
title: Matomo 5.14.2 is available (security update)
description: Matomo warns installations running a PHP version affected by CVE-2026-109618 and CVE-2026-109619, and updates its CA certificates bundle
date: 2026-10-22
tags:
  - addons
  - matomo
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Our [Matomo](https://matomo.org/) add-on has been updated to version `5.14.2` which is now used by default. This urgent release warns administrators when their installation runs a PHP version affected by the critical vulnerabilities [CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618) and [CVE-2026-109619](https://www.cve.org/CVERecord?id=CVE-2026-109619). It also updates the CA certificates bundle Matomo uses for outgoing HTTPS requests to `composer/ca-bundle` 1.6.0.

Updating Matomo alone doesn't fix these PHP vulnerabilities. On Clever Cloud, we already moved every managed Matomo add-on that ran PHP 8.1 or 8.2 to PHP 8.3, as described in our [PHP security update](/changelog/2026/10-21-php-security-vulnerabilities/).

You can deploy this release from our [Console](https://console.clever-cloud.com) or [Clever Tools](/doc/manage/cli/). Existing customers' add-ons are already up to date.

- [Learn more about Matomo 5.14.2](https://matomo.org/changelog/matomo-5-14-2/)
- [Learn more about Matomo on Clever Cloud](/doc/deploy/services/matomo/)
