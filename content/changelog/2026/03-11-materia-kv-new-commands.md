---
title: "Materia KV: new commands and improved reliability"
description: Materia KV now supports GETDEL, HEXISTS, HSETNX, HINCRBY, EXPIREAT and PEXPIREAT commands, with improved scan reliability and transaction retry limits.
date: 2026-03-11
tags:
  - addons
  - materia
  - kv
authors:
  - name: Baptiste Le Morlec
    link: https://github.com/baptiste-le-m
    image: https://github.com/baptiste-le-m.png?size=40
  - name: Pierre Zemb
    link: https://github.com/pierrez
    image: https://github.com/pierrez.png?size=40
excludeSearch: true
---

[Materia KV](/doc/addons/materia-kv/) adds six new commands to its Redis-compatible layer, expanding hash, string and time to live (TTL) management capabilities:

- `GETDEL`: atomically get a string value and delete its key
- `HEXISTS`: check if a field exists in a hash
- `HSETNX`: set a hash field only if it doesn't already exist
- `HINCRBY`: increment the integer value of a hash field
- `EXPIREAT`: set key expiration using an absolute Unix timestamp in seconds
- `PEXPIREAT`: set key expiration using an absolute Unix timestamp in milliseconds

These commands are available for new and already deployed add-ons, with no additional configuration.

This update also brings reliability improvements to the underlying storage layer.

The `SCAN`, `HSCAN`, `SSCAN` and `KEYS` commands now produce more accurate results thanks to fixes in the scan boundary logic.

Transactions now enforce retry limits of 5 retries with a 5-second timeout, preventing cascading retries from overwhelming the cluster under heavy contention. Previously, transactions could retry indefinitely on conflict.

- [Learn more about Materia KV](/doc/addons/materia-kv/)
- [Learn more about Materia KV supported commands](/doc/addons/materia-kv/#supported-types-and-commands)
