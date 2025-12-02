---
title: "Otoroshi 17.9 is available with new plugins: Swagger UI, llms.txt Accept Markdown"
description: Simplify your API documentation with Swagger UI and markdown responses for LLMs
date: 2025-12-03
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

[Otoroshi v17.9](https://github.com/MAIF/otoroshi/releases/tag/v17.9.0) is available with multiple improvements and bug fixes and two new plugins we've contributed to:
- LLMs.txt Accept Markdown: proxies requests with `Accept: text/markdown` header according to [llms.txt proposal](https://llmstxt.org/)
- Swagger UI: serves a Swagger UI page from a configurable OpenAPI specification URL

Release 17.9.2 brings routes templates and a fix to reduce excessive CPU usage. You can update through add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.9.2_1764753761` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.9.2_1764753761
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
