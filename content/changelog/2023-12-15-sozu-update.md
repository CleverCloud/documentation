---
title: Sozu update
date: 2023-12-15
tags:
  - sozu
excludeSearch: true
description: Sozu updated to version 0.15.18 
---

This release v0.15.18 of Sozu has been issue for performance and various bugfixes:

* Fix 502 following a 304 response with a body that does not respect RFCs
* Fix of a panic when upgrading from HTTP to WS or from HTTPs to WSs
* Fix encryption issues when reusing TLS sessions (bump rustls)
* Added `--json` flag to all commands
