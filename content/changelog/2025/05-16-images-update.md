---
title: "Images update: Composer 2.8.9, Node.js 22.15.1, Rust 1.87.0"
date: 2025-05-16
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: With CC_NODE_VERSION supported in all runtimes
excludeSearch: true
---

We updated all our images. Deployment is in progress for all our users.

* **Common:**
  * Linux kernel 6.14.6 with stability fix
  * Mise 2025.5.3
  * Redis 8.0.1
  * SQLite 3.49.2
* **Node.js:**
  * Update to 22.15.1 (npm 10.9.2)
  * Bun 1.2.9
* **PHP:**
  * Composer 2.8.9
* **Ruby:**
  * Update to 3.1.7
  * Update to 3.2.8
  * Update to 3.3.8
  * Update to 3.4.3
* **Rust:**
  * Update to 1.87.0

This release introduces `CC_NODE_VERSION` support [for Node.js applications](/developers/changelog/2025/05-16-node-versions/). When an application is restarted for image update, it won't appear as `Maintenance` anymore, but as `Maintenance/ImageUpdate`

- [Learn more about Node.js on Clever Cloud](/developers/doc/applications/nodejs)
