---
title: February 2024 images update (part 2)
date: 2024-02-27
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: New .Net version, Java Elastic/APM agent update
aliases:
- /changelog/2024-02-27-images-update-part2
excludeSearch: true
---

Earlier this month, we published [a first set of updates](../02-02-images-update) for Docker, Erlang, Go, Haskell, Ruby and Rust. Some days ago, we finished this work and all images are now up-to-date. This process occurred with no impact for our users. As mentioned in a previous post, this enables [the new `healthcheck` feature](../02-26-healthcheck-for-everyone) available for all applications.

New images include security patches, Linux kernel 6.7.1, OpenSSL 3.2.1 and Node.js 20.11.0 by default. For the latter, you can set it via the `CC_NODE_VERSION` [environment variable](/developers/doc/reference/reference-environment-variables/#commons-to-all-applications). Other changes are as follows:

* **.Net:**
  * Version 8.0 support
  * `CC_DOTNET_VERSION` [environment variable](/developers/doc/reference/reference-environment-variables/#net) can be `6.0` or `8.0`
* **Java - Elastic / APM:**
  * The agent has been updated to 1.47.1
  * Java 21 support

New PHP image is next to come, with 8.3 version support, we're currently working on it. After that, we'll bring our new strategy to build images into production. We're currently testing it, and preparing enhancements for multiples runtimes. Your applications will automatically benefit from it when available. [Stay tuned](/developers/changelog/index.xml).
