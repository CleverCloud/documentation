---
title: "Metabase 64 LTS is available, with a Monitor area, metric dimensions and a revamped MCP server"
description: Long Term Support release with a new Monitor area, metric dimensions, an index manager, a revamped MCP server, more Metabot providers and enforced two-factor authentication
date: 2026-10-09
tags:
  - addons
  - metabase
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The `x.64` branch of Metabase is now available on Clever Cloud with version `0.64.1`. It's a Long Term Support (LTS) release, supported by Metabase until December 1, 2027 according to its [version support policy](https://www.metabase.com/version-support). Clever Cloud keeps offering this branch as long as Metabase officially supports it.

This release introduces a Monitor area that gathers content diagnostics, logs, background tasks and AI auditing in one place. Data Studio gains an index manager for tables created by transforms, one-click reruns of upstream or downstream dependencies, and incremental transforms can now look back in time to catch late-arriving data. Metrics can now expose curated breakout dimensions, and administrators on Pro and Enterprise plans can enforce two-factor authentication enrollment with a deadline. Some other features of this release also require these plans.

On the AI side, the revamped MCP server, available at `/api/metabase-mcp`, brings new tools, least-privilege OAuth scopes and a glossary tool. If you use an existing MCP v1 connector, remove it and add it again with this endpoint. Metabot adds Google Gemini, Mistral, DeepSeek, Moonshot, Z.AI and self-hosted vLLM models, saves conversations so you can resume or fork them, and displays reasoning on supported models.

## Breaking changes

Metabot environment variables such as `MB_METABOT_CHAT_SYSTEM_PROMPT`, `MB_METABOT_NLQ_SYSTEM_PROMPT` and `MB_METABOT_SQL_SYSTEM_PROMPT` no longer exist: configure these prompts from the administration settings instead. Custom visualizations built with SDK v1.x need an update to SDK v2.0 before you upgrade, and endpoints that pre-fill action forms now expect parameters in the POST body instead of the query string. Metabot also no longer generates transforms.

## How to update

This branch isn't used by default yet if you use `latest`. You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `0.64` or `1.64` for the enterprise edition (EE) and rebuild it without the build cache, or use [Clever Tools](/doc/manage/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId --target 0.64
```

- [Learn more about Metabase 64](https://www.metabase.com/changelog/64)
- [Learn more about Metabase on Clever Cloud](/doc/deploy/services/metabase/)
