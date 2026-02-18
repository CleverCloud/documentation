---
title: "Images update: Kernel 6.19, Request Flow in Go, Java, Node.js, PHP and Static with Apache"
description: "Use Request Flow almost everywhere, and benefit from many updates in our images"
date: 2026-02-18
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
  * Linux Kernel 6.19.2
  * ClamAV 1.5.1
  * Mise 2026.2.13
  * Otoroshictl 0.0.16
* **.NET:**
  * Update to 8.0.123
  * Update to 9.0.113
* **Elixir:**
  * Erlang 27.3.4.7
* **Node.js & Bun:**
  * Update to 24.13.1 (npm 11.8.0)
* **PHP:**
  * Update to 8.4.18
  * Update to 8.5.3
* **Rust:**
  * Update to 1.93.1

## Apache Basic Auth

`X-Robots-Tag: noindex, nofollow` header is now added to responses [with Basic Authentication](/doc/applications/php/apache/#basic-authentication) through Apache

## Request Flow extension

Request Flow is now available in Go, Java/Scala, Meteor, Node.js & Bun, PHP and Static with Apache runtimes. Python (without uv) and Ruby are coming soon. If your application currently uses Varnish in Go or Node.js, you must ask support to switch to this new release. Your application will have to move from port `8081` to `9000`.

- [Learn more about Request Flow](/doc/develop/request-flow/)
