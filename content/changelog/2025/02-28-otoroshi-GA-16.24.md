---
title: "Otoroshi in General Availability"
date: 2025-02-28
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
description: With the new Operator API
excludeSearch: true
---

Otoroshi is now in General Availability (GA), with access [to the operator API](/developers/api/v4/#operators). Deployed version is `v16.24.0_1740754279`. The LLM extension includes new models filtering tools and pre-defined context per endpoint. To update, just set `CC_OTOROSHI_VERSION` of the add-on's Java application to `v16.24.0_1740754279` and rebuild it. You can also delete `CC_OTOROSHI_APIM_VERSION`, `CC_OTOROSHI_SECRET` variables from the Java application, they are not used anymore.

- [Learn more about Otoroshi with LLM on Clever Cloud](/developers/doc/addons/otoroshi/)
