---
title: Otoroshi 17.4 with JSON/Markdown documentation generator for Workflows
description: Do more with workflows in Otoroshi, and export usage data easily
date: 2025-07-16
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

[Otoroshi v17.4](https://github.com/MAIF/otoroshi/releases/tag/v17.4.0) is available with multiple improvements and bug fixes. It brings operators, JSON/Markdown documentation generator and a data exporter to Workflows. It comes with [LLM extension 0.0.49](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.49).

To update just set `CC_OTOROSHI_VERSION` of the add-on's Java application to `v17.4.0_1752074416` and rebuild it. You can also use [the new Clever Tools commands](/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.4.0_1752074416
```

- [Learn more about Otoroshi Workflows](https://maif.github.io/otoroshi/manual/topics/workflows.html)
- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)

