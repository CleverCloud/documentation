---
title: Clever Tools 3.6.0 is available
date: 2024-04-16
tags:
  - clever-tools
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
description: Lots of new features included!
excludeSearch: true
---

Clever Tools 3.6 is now available, with some minor fixes and a new feature: the support of SD-PARAMS ([RFC 5424](https://www.rfc-editor.org/rfc/rfc5424.html)) for UDP and TCP drains with `clever drain create --sd-params "SD_PARAMS_STRING"`.

To upgrade Clever Tools, [use your favorite package manager](https://github.com/CleverCloud/clever-tools/blob/master/docs/setup-systems.md#how-to-install-clever-tools). For example with npm:

```
npm update -g clever-tools
clever version
```
