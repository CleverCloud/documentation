---
title: "Otoroshi 17.10 is available with updated MCP support, a plugin to detect and block React2Shell attacks"
description: Protect your applications from React2Shell attacks and use latest MCP features
date: 2025-12-09
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

[Otoroshi v17.10](https://github.com/MAIF/otoroshi/releases/tag/v17.10.0) is available with multiple improvements, bug fixes and a new plugin to detect and block React2Shell attacks. To use it, add the `React2Shell detector` plugin to your routes and activate blocking if needed.

This release comes with [LLM extension 0.6.6](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.66) which [supports](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.65) latest versions of Model Context Protocol (MCP) with official Streamable HTTP transport implementation. MCP Connectors can now be used in Workflows.

You can update through add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.10.0_1765204068` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.10.0_1765204068
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
