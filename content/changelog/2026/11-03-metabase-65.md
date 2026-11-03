---
title: "Metabase 65 is available, with a research mode, data apps and session management"
description: New Metabase release with a Metabot research mode, data apps in beta, timeline events on dashboards, new AI providers and session management for administrators
date: 2026-11-03
tags:
  - addons
  - metabase
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The `x.65` branch of Metabase is now available on Clever Cloud with version `0.65.2`. It isn't a Long Term Support (LTS) release: Metabase supports it until January 1, 2027 according to its [version support policy](https://www.metabase.com/version-support). [Metabase 64 LTS](/changelog/2026/10-29-metabase-64-default/) stays the default version.

This release adds timeline events to time-series charts on dashboards, a dashboards section in the Library of Data Studio, and query actions that no longer require a model. Subscriptions accept a custom email subject, charts get a separate label for the right y-axis, and the column picker of the query builder gains a search box for tables with at least 10 columns. Transform tests created with the Metabase CLI now run in Data Studio, and you can opt in to faster pivot tables with `MB_USE_NATIVE_PIVOT_TABLES`.

On the AI side, Metabot introduces a research mode, from **+ New > AI exploration > Research**, and supports Ollama, xAI, Google Cloud Model Garden endpoints and Amazon Bedrock inference profiles. On Pro and Enterprise plans, data apps (beta) let you build React applications on the semantic layer, administrators can restrict MCP tools by group, and the Monitor area gains content diagnostics, API key usage and session management pages.

## Breaking changes

Metabot now reads query results by default and sends them to the AI provider you configured. To opt out, turn off **Allow Metabot to read query results** in **Admin > AI > Metabot settings**. Metabase also removes `MB_LLM_MAX_TOKENS` and ignores it if you set it. The MCP endpoint no longer accepts sessions or API keys for authentication, and `POST /api/llm/generate-sql` and `POST /api/product-feedback` now return `404`. Creating or retargeting a transform onto an existing table returns `409 Conflict` instead of `403 Forbidden`.

Only administrators can create actions, and users subject to row or column-level security can no longer run them. Remote sync now syncs only the Library by default, and serialized YAML files use a lighter format: the previous one still imports, but your first export after the update changes most files.

## How to update

This branch isn't used by default if you use `latest`. You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `0.65`, or `1.65` for the enterprise edition (EE), then rebuild it without the build cache. With [Clever Tools](/doc/manage/cli/operators/), run:

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId --target 0.65
```

- [Learn more about Metabase 65](https://www.metabase.com/changelog/65)
- [Learn more about Metabase on Clever Cloud](/doc/deploy/services/metabase/)
