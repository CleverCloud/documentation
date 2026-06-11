---
title: "Metabase 61 is available, with AI governance, dashboards-as-code and Security Center"
description: AI access controls, token limits, Metabot customization, AI usage analytics, dashboards-as-code, metrics math, Security Center and more
date: 2026-05-30
tags:
  - addons
  - metabase
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The `x.61` branch of Metabase is now available on Clever Cloud. It focuses on AI governance: control which user groups can access AI features such as Metabot, SQL generation and auto-generated transforms, set token limits per instance or per user group with daily, weekly or monthly resets, customize Metabot with your own name, icon and system prompts, and track token spend and feature usage through a pre-made AI usage analytics dashboard.

It also introduces dashboards-as-code to create dashboards from an AI terminal such as Claude Code or Cursor with git-backed validation, arithmetic expressions across metrics in the metrics explorer, custom expressions written by Metabot in the query builder, and a Security Center with targeted alerts for your instance configuration. Embedded analytics gains usage analytics, guest token auto-renewal, a themes editor, mobile-optimized SDK components and a `useMetabot` React hook. Some of these features require the enterprise edition (EE).

This branch is not the default for now if you use `community-latest`. You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `0.61` or `1.61` for the enterprise edition (EE) and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.61
```

- [Learn more about Metabase 61](https://www.metabase.com/releases/metabase-61)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)

{{< youtube id="jU8ua9OHvTY" >}}
