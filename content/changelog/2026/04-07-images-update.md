---
title: "Images update: mdBook 0.5, Static Web Server 2.42, OAuth2Proxy 7.15.1, Tailscale 1.96.3"
description: Many tool updates, check your mdBook configuration for the 0.5 release
date: 2026-04-07
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

We updated all our images, except PHP. Deployment is in progress for all our users.

* **Common:**
  * Linux kernel 6.19.11
  * nginx 1.28.3
  * OAuth2Proxy 7.15.1
  * Tailscale 1.96.3
* **Python:**
  * uv 0.11.2
* **Ruby:**
  * Update to 3.3.11
  * Update to 4.0.2
* **Static:**
  * mdBook 0.5.2
  * Static Web Server 2.42.0
* **V (Vlang):**
  * Update to 0.5.1

## mdBook 0.5

mdBook 0.5 introduces some breaking changes. If your configuration is not yet compatible, follow the [migration guide](https://github.com/rust-lang/mdBook/blob/master/CHANGELOG.md#05-migration-guide).
