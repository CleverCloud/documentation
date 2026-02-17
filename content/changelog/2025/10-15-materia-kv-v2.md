---
title: "Materia KV is now Beta: Hash support, Set is coming"
description: After months of heavy development, lots of new features and improvements are coming to Materia KV
date: 2025-10-15
tags:
  - addons
  - materia
  - kv
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Last year](/changelog/2024/06-11-materia-kv-public-alpha/), we introduced [Materia KV](/doc/addons/materia-kv/) as an Alpha add-on to provide a simple, distributed, scalable key-value store for your applications. Since then, we've been working hard to enhance its capabilities: [TTL (Time To Live) commands support](/changelog/2024/10-01-materia-kv-ttl-layer-update/) and [KV Explorer](/changelog/2024/11-28-kv-explorer-available/), included in the [Clever Cloud Console](https://console.clever-cloud.com). Last march, we added [support for JSON GET/SET/DEL commands](https://www.clever.cloud/developers/changelog/2025/03-12-materia-kv-json/).

Since then, we were focused on a major overhaul of the Redis® compatibility layer, to bring more data structures support, better performance and reliability. It's now available, and Materia KV in Beta stage.

It's still free to use, but now with more commands and `Hash` support. `Set` support is next to come. You can also [use Materia for your PHP sessions](/doc/applications/php/sessions-emails/#use-materia-kv-or-redis-to-store-php-sessions) more easily, as TLS transport is now supported during application deployment. There nothing more to do than to link a Materia KV to your application.

- [Learn more about Materia KV](/doc/addons/materia-kv/)
- [Learn more about Materia KV supported commands](/doc/addons/materia-kv/#supported-types-and-commands)
