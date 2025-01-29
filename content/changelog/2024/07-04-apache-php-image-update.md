---
title: PHP 8.2.21 and 8.3.9 image update
date: 2024-07-04
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Apache 2.4.60 and Composer 2.7.7 also included
aliases:
- /changelog/2024-07-04-apache-php-image-update
excludeSearch: true
---

We've updated our PHP image to support versions [8.2.21](https://www.php.net/ChangeLog-8.php#8.2.21) and [8.3.9](https://www.php.net/ChangeLog-8.php#8.3.9):
* They fix a bug [introduced](https://github.com/api-platform/core/issues/6416) in 8.2.20 and 8.3.8 which we had previously patched
* This image includes a fix for GnuPG extension
* PHP info apps are up-to-date: [8.2](https://php82info.cleverapps.io) and [8.3](https://php83info.cleverapps.io)

Over the past few weeks, we have also included [Apache 2.4.60](https://dlcdn.apache.org/httpd/CHANGES_2.4.60), fixing CVE-2024-36387, 38472, 38473, 38474, 38475, 38476, 38477, 39573 and [Composer 2.7.7](https://github.com/composer/composer/releases/tag/2.7.7), fixing CVE-2024-35241, 35242.

* Learn more about [PHP on Clever Cloud](/developers/doc/applications/php/)
