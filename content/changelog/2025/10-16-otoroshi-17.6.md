---
title: Otoroshi 17.6 is available, with Biscuit Studio 1.0
description: Monaco editor, body size limiting and bandwidth throttling plugins
date: 2025-10-16
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

[Otoroshi v17.6](https://github.com/MAIF/otoroshi/releases/tag/v17.6.0) is available with multiple improvements and bug fixes. It now uses Monaco as code editor, brings many improvements to workflows and plugins to to limit request/response body size or throttle bandwidth. It comes with [LLM extension 0.0.53](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.53)  and [Biscuit Studio 1.0](https://github.com/cloud-apim/otoroshi-biscuit-studio/releases/tag/1.0.0) which includes features from previous releases, such as graphical inspector/tester, a sandbox to test datalog policies, support of Otoroshi expression language, etc.

You can update through add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.6.3_1760617667` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.6.3_1760617667
```

- [Learn more about Biscuit Studio](https://cloud-apim.github.io/otoroshi-biscuit-studio/docs/overview)
- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)

