---
title: Otoroshi 17.8 is available, with budget management for AI models
description: Inline functions and usage limits for AI providers and many more improvements
date: 2025-11-07
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

[Otoroshi v17.8](https://github.com/MAIF/otoroshi/releases/tag/v17.8.0) is available with multiple improvements and bug fixes. It comes with [LLM extension 0.0.55](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.55) which introduces inline functions in all models and budget management for AI services. Thus, you can now defines limits to AI provider usage per API key, user, kind of models, etc.

You can update through add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.8.0_1762533533` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.8.0_1762533533
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
- [Learn more about Budget management for AI models in Otoroshi](https://cloud-apim.github.io/otoroshi-llm-extension/docs/cost-optimizations/budgets/)
