---
title: Otoroshi 17.3 introduces AI and Biscuit in Workflows
description: Secret vault expressions with multiple values, streaming for tool calls, and many enhancements
date: 2025-06-04
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

[Otoroshi v17.3](https://github.com/MAIF/otoroshi/releases/tag/v17.3.0) is available with multiple improvements and bug fixes. It brings more enhancements to Workflows and data extraction from API keys. Secret vault expression can now have multiple values using the `||` and `&&` operators.

This release is shipped with [LLM extension 0.0.47](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.47) with enhancements in responses, streaming for tool calls for Ollama, multiple access token per provider. It also introduces AI oriented set of functions for Otoroshi Workflows. [Biscuit Studio 0.0.15](https://github.com/cloud-apim/otoroshi-biscuit-studio/releases/tag/0.0.15) provides attenuation, forge and verify functions to workflows.

To update just set `CC_OTOROSHI_VERSION` of the add-on's Java application to `v17.3.1_1749049547` and rebuild it. You can also use [the new Clever Tools commands](/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.3.1_1749049547
```

- [Learn more about Otoroshi Workflows](https://maif.github.io/otoroshi/manual/topics/workflows.html)
- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)

