---
title: "Images update: PHP 8.4.5, Ruby in unified image stack"
date: 2025-03-18
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: New week, new release!
excludeSearch: true
---

We deployed and updated all our images, except Java, with no impact for our users. It now includes Ruby as part as our new unified image stack.

* **Common:**
  * Linux kernel 6.13.7
* **PHP:**
  * Update to 8.4.5
  * Apache 2.4.63
* **Python:**
  * uv 0.6.6
  * nginx 1.26.3
* **Ruby:**
  * Update to 3.4.2
  * Bundler 2.6.5
  * nginx 1.26.3

Note that Ruby 3.4 is the default only in Ruby applications. Ruby 3.2 is still default on other runtimes, use [rbenv](https://github.com/rbenv/rbenv) and `RBENV_VERSION` to switch to Ruby 3.4 for now.
