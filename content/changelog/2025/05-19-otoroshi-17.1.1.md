---
title: "Otoroshi 17.1 is available, audio and image models supported by LLM extension"
date: 2025-05-19
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
aliases:
- /changelog/2025/19-05-otoroshi-17.1.1/
---

[Otoroshi v17.1](https://github.com/MAIF/otoroshi/releases?q=v17.1&expanded=true) is available with multiple improvements, bug fixes and a new canary mode plugin with autonomous rollout. LLM extension is updated to [0.0.46 release](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.46) which brings new OVHcloud endpoints, user provided data for ecological/cost tracking, support of multiple models for audio (speech-to-text, text-to-speech), image generation and moderation.

To update just set `CC_OTOROSHI_VERSION` of the add-on's Java application to `v17.1.1_1747324564` and rebuild it.

- [Learn more about Otoroshi with LLM on Clever Cloud](/developers/doc/addons/otoroshi/)
