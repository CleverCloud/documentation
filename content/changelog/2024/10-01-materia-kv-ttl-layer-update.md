---
title: 'Materia KV: layer update, with TTL support'
date: 2024-10-01
tags:
  - Materia KV
  - TTL
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Get ready for more commands and layers soon
aliases:
- /changelog/2024-10-01-materia-kv-ttl-layer-update
excludeSearch: true
---

After the first release of our [Materia KV add-on](/developers/doc/addons/materia-kv), we discussed with users and what they wanted to see in the next version. A major milestone for us was to add support for `TTL` (Time To Live) command, and those related to it such as `EXPIRE`, `PEXPIRE`, `PTTL`, `SET EX`. It's now available and will helps us, for example, to bring Materia KV support to PHP sessions.

This new release of our Redis API compatible layer brings a new design, helping us to better support more commands in the future. In the meantime, we've retired hash and list commands, to enhance them. They will be back soon. Some others are added, like `CLIENT ID`, `DECRBY`, `INCRBY`,`GETBIT`, `SETBIT`, etc.

If you have any questions or feedback, let's discuss it on our [GitHub Community](https://github.com/CleverCloud/Community/discussions/categories/materia).

- [The full Materia KV commands list](/developers/doc/addons/materia-kv/#supported-types-and-commands).
