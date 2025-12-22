---
title: "Images update: Docker 29, Elixir clean up, Static Web Server for llms.txt"
description: Lots of new versions and features and some cleanup of old Elixir/Erlang versions
date: 2025-12-17
tags:
  - images
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

We updated all our images except FrankenPHP and PHP. Deployment is in progress for all our users.

* **Common:**
  * Linux kernel 6.17.12
  * Anubis 1.23.1
  * Clever Tools 4.4.1
  * Git 2.52.0
  * Mise 2025.12.1
  * Nano 8.7
  * Poppler 25.12.0
  * Postgresql-client 18.1
  * Redis 8.4
  * Rust 1.92.0
  * Tailscale 1.90.9
  * Tmux 3.6
* **Docker:**
  * Docker 29.0.2
  * Docker Buildx 0.30.1
* **Elixir:**
  * Update to 1.19.4
  * Erlang 26.2.5.16
  * Erlang 27.3.4.6
  * Erlang 28.2
* **Go:**
  * Update to 1.25.5
* **Node.js:**
  * Update to 24.11.1 (npm 11.6.1)
  * Bun 1.3.4
  * Yarn 4.12.0
* **Python:**
  * Update to 3.9.25
  * Update to 3.12.0
  * Update to 3.13.11
  * uv 0.9.17
* **Ruby:**
  * Update to 3.3.10
  * Update to 3.4.7
* **Static:**
  * Static Web Server 2.40.1

## Elixir support

Starting with this release, we don't support end-of-life Elixir versions from 1.8 to 1.13 anymore. They were no longer used by our customers. Thus, we also removed Erlang versions from 22 to 24.

## Static Web Server for llms.txt

Static Web Server 2.40.1 includes a new feature we contributed to, allowing to serve Markdown version of a web page when it exists and the request contains the `Accept: text/markdown` header. This is useful to serve documentation to LLMs following the [llms.txt proposal](https://llmstxt.org/). It can be combined with Hugo [transform.HTMLToMarkdown](https://gohugo.io/functions/transform/htmltomarkdown/) function for example, as we do on this documentation.

To enable this feature, just set `SERVER_ACCEPT_MARKDOWN` environment variable to `true` in your Static Web Server application.
