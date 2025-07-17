---
title: 'JS Client 11.0 is available'
date: 2025-07-02
tags:
  - client
  - javascript
authors:
  - name: Pierre De Soyres
    link: https://github.com/pdesoyres-cc
    image: https://github.com/pdesoyres-cc.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Some cleaning before big changes
excludeSearch: true
---

[Clever Cloud JS client 11.0](https://github.com/CleverCloud/clever-client.js/blob/master/CHANGELOG.md#1101-2025-06-30) is available. It adds API call analysis scripts, uses native WebSocket support and OAuth plaintext instead of HMAC512. Thus, we removed `oauth-1.0a` dependency. Note that if you use the event API, you need Node.js 21+.
