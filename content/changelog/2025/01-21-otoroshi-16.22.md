---
title: "Otoroshi v16.22 is available"
date: 2025-01-21
tags:
  - addons
  - Otoroshi
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Make the AI enterprise-grade
excludeSearch: true
---

The release `16.22.0` of Otoroshi is available on Clever Cloud for new add-ons. [It fixes](https://github.com/MAIF/otoroshi/releases/tag/v16.22.0) some bugs and adds some features such as a plugin to add very simple basic auth, without complex user management, plugins to provide information (metrics, health, etc.) as user endpoint. LLM Extension also contains multiple fixes. To upgrade, edit `CC_OTOROSHI_VERSION` to `v16.22.0`, `CC_OTOROSHI_APIM_VERSION` to `1737449369` in the Java application and rebuild it.

- [Learn more about Otoroshi with LLM on Clever Cloud](/developers/doc/addons/otoroshi/)
