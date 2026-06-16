---
title: Otoroshi 17.16.1 is available with web search (including Staan) and AI router support
description: A new build of Otoroshi 17.16.1 shipped with LLM extension 0.0.79, introducing search engines, AI routers, circuit breaking and OpenRouter multi-modal support
date: 2026-06-16
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

[Otoroshi v17.16.1](https://github.com/MAIF/otoroshi/releases/tag/v17.16.1) is available on Clever Cloud with the same core as the previous [release](/changelog/2026/06-04-otoroshi-17.16.1/), but with a bumped LLM extension [0.0.79](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.79).

This version introduces search engines as a first-class entity, with seven providers including [Staan](https://staan.ai/), the sovereign search engine [announced today](https://x.com/Qwant_FR/status/2066539860022718695) by Qwant, alongside Tavily, Brave Search, SearXNG, Google Custom Search and DuckDuckGo. You can use them as LLM tools, expose them through an HTTP API or call them from a workflow function.

The new AI router adds three routing strategies: a code-router that selects the cheapest model meeting a quality threshold, an auto-router that relies on a judge LLM for prompt-aware routing, and a fusion-router that synthesises responses from several candidates.

The extension also adds a per-provider circuit breaker, with configurable failure thresholds and cooldown windows for better fallback handling, and a plugin exposing call metadata such as model, provider, token usage, latency and cost through `x-otoroshi-llm-*` response headers. A mock-response decorator lets you short-circuit calls to test provider fallbacks without real API requests, OpenRouter now supports audio, image and video beyond chat, and the dashboard gains budget reset buttons.

You can update through your add-on dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.16.1_1781607455` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.16.1_1781607455
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
