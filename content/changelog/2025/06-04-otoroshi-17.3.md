---
title: "Otoroshi 17.3 is available, with LLM agentic workflows"
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
description: Use Biscuits, end-to-end
excludeSearch: true
---

[Otoroshi v17.3.0](https://github.com/MAIF/otoroshi/releases/tag/v17.3.0) is available with multiple improvements, bug fixes and a new canary mode plugin with autonomous rollout. LLM extension is updated to [0.0.47 release](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.47) which brings new OVHcloud endpoints, user provided data for ecological/cost tracking, support of multiple models for audio (speech-to-text, text-to-speech), image generation and moderation.

To update just set `CC_OTOROSHI_VERSION` of the add-on's Java application to `v17.3.0_XXX` and rebuild it.

- [Learn more about Otoroshi with LLM on Clever Cloud](/developers/doc/addons/otoroshi/)
