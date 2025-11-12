---
title: Otoroshi 17.7 is available, with many fixes and improvements
description: Lots of small changes here and there to make Otoroshi even better
date: 2025-10-31
tags:
  - addons
  - otoroshi
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Otoroshi v17.7](https://github.com/MAIF/otoroshi/releases/tag/v17.7.0) is available with multiple improvements and bug fixes. It comes with [LLM extension 0.0.54](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.54).

To update just set `CC_OTOROSHI_VERSION` of the add-on's Java application to `v17.7.0_1762500043` and rebuild it. You can also use [the new Clever Tools commands](/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.7.0_1762500043
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)

