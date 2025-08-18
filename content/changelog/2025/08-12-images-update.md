---
title: "Images update: Gradle 9, Rust 1.89"
date: 2025-08-12
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: No holidays for greatest changes!
excludeSearch: true
---

We updated all our images. Deployment is in progress for all our users.

* **Common:**
  * Tailscale 1.86.4
* **Go:**
  * Update to 1.24.6
* **Java:**
  * Gradle 9.0.0
* **Node.js & Bun:**
  * Bun 1.2.20
* **Python:**
  * 3.13.6
  * pip 25.2
  * uv 0.8.8
* **Rust:**
  * Update to 1.89.0

In the [Bun & Node.js runtime](/doc/applications/nodejs), you can now set `CC_NODE_BUILD_TOOL` to `pnpm` or `yarn-berry`.
