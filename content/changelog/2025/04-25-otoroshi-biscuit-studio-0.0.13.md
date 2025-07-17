---
title: "Otoroshi update with Biscuit Studio 0.0.13"
date: 2025-04-25
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

[Otoroshi v17.0.0](https://github.com/MAIF/otoroshi/releases/tag/v17.0.0) is available with Biscuit Studio [0.0.13](https://github.com/cloud-apim/otoroshi-biscuit-studio/releases/tag/0.0.13) which enhance `BiscuitUserExtractor` plugin capabilities.

To update just set `CC_OTOROSHI_VERSION` of the add-on's Java application to `v17.0.0_1745325312` and rebuild it. You can also delete `CC_OTOROSHI_APIM_VERSION`, `CC_OTOROSHI_SECRET` variables from the Java application, they are not used anymore.

- [Learn more about Otoroshi with LLM on Clever Cloud](/developers/doc/addons/otoroshi/)
