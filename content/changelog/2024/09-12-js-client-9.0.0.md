---
title: 'JS Client 9.0 is available'
date: 2024-09-12
tags:
  - client
  - javascript
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
description: A must have for next packaging of clever tools
aliases:
- /changelog/2024-09-12-js-client-9.0.0
excludeSearch: true
---

We released [Clever Cloud JS client 9.0.0](https://github.com/CleverCloud/clever-client.js/blob/master/CHANGELOG.md#900-2024-09-11). It computes OAuth v1 signature with Web Crypto for all platforms (Browser, Node.js, Deno, Bun, CF workers, etc.) instead of relying on `node:crypto`. This will simplify usage of the client with a bundler.