---
title: "Images update: PHP 8.4 is now default, some cleanup"
date: 2025-05-06
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Node.js 18 and Ruby 3.1 are now EOL
excludeSearch: true
---

We updated all our images. Deployment is in progress for all our users.

* **Common:**
  * Linux kernel 6.14.4
  * Mise 2025.5.0
  * Redis 8.0.0
  * Tailscale 1.82.5
* **Go:**
  * Update to 1.24.2
* **Node.js:**
  * Update to 22.15 (npm 10.9.2)
* **Python:**
  * uv 0.7.2

As previously announced, Python 3.8 [is not available in our images anymore](/developers/changelog/2025/03-25-python-3.8-eol/) and PHP 8.4 [is now used as default](https://www.clever-cloud.com/developers/changelog/2025/03-21-php-version-management-update/) for `CC_PHP_VERSION=8`. As Node.js 18 and Ruby 3.1 are now end-of-life, you'll get a warning if you use them.

- [Learn more about Node.js release cycle](https://nodejs.org/en/about/releases/)
- [Learn more about PHP release cycle](https://www.php.net/supported-versions.php)
- [Learn more about Python release cycle](https://devguide.python.org/versions/#python-release-cycle)
- [Learn more about Ruby release cycle](https://www.ruby-lang.org/en/downloads/branches/)
