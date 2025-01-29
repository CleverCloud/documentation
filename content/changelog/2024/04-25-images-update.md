---
title: "Images: April 2024 update"
date: 2024-04-25
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Kernel 6.8.6, security fixes and action executor
aliases:
- /changelog/2024-04-25-images-update
excludeSearch: true
---

We've updated all our images and deployed them without any impact for our users. They include our new action executor, which will help to make some features available soon. They also include the following changes:

* **Common:**
  * Linux kernel 6.8.6
  * glibc security fix (CVE-2024-2961)
  * Node.js 20.12.2 as default version
* **Ruby:**
  * Update to 3.0.7, 3.1.5, 3.2.4 and 3.3.1 (CVE-2024-27282, CVE-2024-27281 et CVE-2024-27280)
* **Erlang / Elixir:**
  * Update to 21.16.2, 22.3.4.27, 23.3.4.20, 24.3.4.17, 25.3.2.11, 26.2.4
* **.NET:**
  * Update to 8.0.103, 8.0.3

We had to delay the release of PHP image with 8.3 version support, to better support some extensions and include latest security fixes. It will start to deploy next week and include an informative message when a deprecated version of PHP is used.

* Learn more about the [message for deprecated PHP versions](../04-24-php-deprecate-warning/).
