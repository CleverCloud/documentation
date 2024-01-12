---
title: Redis updated to v7.2.4
date: 2024-01-11
tags:
  - redis
authors:
  - name: sardemff7
    link: https://github.com/sardemff7
    image: https://github.com/sardemff7.png?size=40
  - name: BlackYoup
    link: https://github.com/BlackYoup
    image: https://github.com/BlackYoup.png?size=40
excludeSearch: true
description: Pulsar version 3.2.0 is deployed
author:
  -
---
A new version of Redis™  (`7.2.4`) is now available for each new instancied Redis.

## Security fixes

* (CVE-2023-41056) In some cases, Redis may incorrectly handle resizing of memory
* buffers which can result in incorrect accounting of buffer sizes and lead to
* heap overflow and potential remote code execution.

## Bug fixes

*¨Fix crashes of cluster commands clusters with mixed versions of 7.0 and 7.2 (#12805, #12832)
*¨Fix slot ownership not being properly handled when deleting a slot from a node (#12564)
*¨Fix atomicity issues with the RedisModuleEvent_Key module API event (#12733)
