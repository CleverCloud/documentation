---
title: "PHP: a warning message when a deprecated version is used"
date: 2024-04-24
tags:
  - php
  - applications
  - information
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Please, update!
aliases:
- /changelog/2024-04-24-php-deprecate-warning
excludeSearch: true
---

PHP ecosystem is evolving at a steady pace with a clear lifecycle: 1 version per year, 2 years of active support, plus 1 year of security support. PHP 8.2 is actively supported, while 8.1 is in its security support window. ALL previous releases are considered end-of-life (EOL) by PHP Team. PHP 5.x branch is EOL since 2019, 7.x branch since the end of 2022.

As we still see a lot of applications using deprecated versions, the new PHP image we'll release next week will start to better inform our users about this. When PHP 8.0 or a previous release is used, a warning will be shown during deployment, asking to set `CC_PHP_VERSION` to `8` (latest 8.x), `8.2` currently on Clever Cloud. In the coming month, we'll extend such informative warnings to other runtimes. We'll also explore ways to show them in other interfaces and send emails about it.

 There is no short term plan to cut access to supported versions such as PHP 5.6 or 7.x, but you do it at your own risks.

* Learn more about [PHP releases lifecycle](https://www.php.net/supported-versions.php)
