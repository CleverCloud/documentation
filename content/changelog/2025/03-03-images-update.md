---
title: "Multiple images update"
date: 2025-03-03
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Releases are getting bigger
excludeSearch: true
---

We deployed and updated all our images, except Docker, Go, Java, Node and Ruby, with no impact for our users.

* **Common:**
  * Linux kernel 6.13.5
* **.Net:**
  * Update to 8.0.108
* **Elixir:**
  * Update to 1.18.2
  * Erlang 27.2.2
* **Haskell:**
  * Stack 2.15.7
* **PHP:**
  * Update to 8.4.4
  * Composer 2.8.6
  * `CC_APACHE_HEADERS_SIZE` [environment variable](/developers/doc/reference/reference-environment-variables/)
* **Python:**
  * Update to 3.13.2
  * pip 24.3.1
  * uv 0.6.3
* **Rust:**
  * Update to 1.85.0

All these images include [Mise and Redirection.io easy setup](/developers/changelog/2025/01-15-node-22-lts-image-update/).
