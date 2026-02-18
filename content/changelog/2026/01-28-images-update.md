---
title: "Images update: Docker 29.2, Gradle 9.3, Rust 1.93 and more runtimes with Request Flow"
description: PHP 8.5 is now available, Composer 2.9 introduces security features, and the default Hugo version will be updated soon
date: 2026-01-28
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

We updated all our images. Deployment is in progress for all our users.

* **Common:**
  * Clever Tools 4.5.3
  * qpdf 12.3.2
  * Mise 2026.1.8
* **Docker:**
  * Update to 29.2.0
  * Docker Buildx 0.31.0
* **Elixir:**
  * Erlang 28.3.1
* **Go:**
  * Update to 1.25.6
* **Java:**
  * Gradle 8.14.4
  * Gradle 9.3.0
  * Maven 3.9.12
* **Node.js & Bun:**
  * Bun 1.3.7
* **PHP:**
  * Update to 8.3.30
  * Update to 8.4.17
  * Update to 8.5.2
  * Composer 2.9.4
* **Python:**
  * uv 0.9.26
* **Ruby:**
  * Update to 3.2.10
* **Rust:**
  * Update to 1.93.0

## Request Flow expansion

Request Flow is now available in .NET, Elixir, Haskell and Rust applications. We plan its expansion to more runtimes in the coming weeks in three releases:
- Go and Node.js/Bun
- Java and PHP
- Python and Ruby

This feature is still in its testing phase, feel free [to test it and give us feedback](https://github.com/CleverCloud/Community/discussions/68).
