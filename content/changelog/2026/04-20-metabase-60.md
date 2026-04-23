---
title: "Metabase 60 is available, with Metabot, MCP server and split panel charts"
description: Metabot, MCP server integration, Slack querying, metrics explorer, split panel charts, frozen columns, transform inspector and more
date: 2026-04-20
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

The `x.60` branch of Metabase is now available on Clever Cloud. It brings Metabot with "bring your own key" support for Anthropic models, an official MCP server to connect Claude, Cursor and other tools, and a Slack integration to query data directly from a channel. It also introduces a metrics explorer to edit and compare metric definitions, split panel charts to display multiple series as faceted panels, frozen columns and rows in tables, a transform inspector for diagnostics, one-click model-to-transform migration, OpenID authentication, remote sync beyond GitHub and multiple enhancements and bug fixes.

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `0.60` or `1.60` for the enterprise edition (EE) and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.60
```

This new branch is not yet the default if you use `community-latest`, we'll move to it in the next few weeks.

- [Learn more about Metabase 60](https://www.metabase.com/changelog/60#metabase-601)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)
