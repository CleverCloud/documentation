---
title: Otoroshi 17.11 is available with Data Exporters, OpenFGA Authorizations, Websocket Mirroring
description: Data exporters, OpenFGA authorizations, websocket mirroring, workflow for websocket messages and new load balancing strategies
date: 2026-01-05
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

[Otoroshi v17.11](https://github.com/MAIF/otoroshi/releases/tag/v17.11.0) is available with multiple improvements and bug fixes. It brings `Datadog` and `New Relic` data exporters, fine-grained authorizations through OpenFGA API, a plugin to mirror websocket traffic to another target, workflow support for websocket message transformations and 3 new load balancing strategies: `HeaderHash`, `CookieHash` and `QueryHash`.

This release comes with [LLM extension 0.0.67](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.67) which supports Cloud Temple as new provider, Nano Banana as Image model provider and Azure OpenAI as embedding model provider.

You can update through add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.11.0_1767272929` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.11.0_1767272929
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
