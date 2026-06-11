---
title: "Metabase 62 is available, with custom visualizations, schema viewer and a CLI"
description: Custom visualizations, schema viewer, Metabase CLI, centralized alert management, subcollections, new MCP server tools and more
date: 2026-06-11
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

The `x.62` branch of Metabase is now available on Clever Cloud. It brings custom visualizations with built-in drills and tooltips, a schema viewer to display entity-relationship diagrams of your databases, a Metabase CLI built on the API to create dashboards, transforms and metrics from the terminal or an AI agent, centralized alert management, and subcollections in the Library to organize tables and metrics with inherited permissions. Some of these features require the enterprise edition (EE).

On the AI side, this release adds official connectors for the OpenAI Codex and Claude marketplaces, new MCP server tools to read entities, create collections and execute SQL, and interactive Metabase charts rendered directly in AI clients. The official Claude connector only works with Metabase Cloud instances: for a Metabase running on Clever Cloud, add a custom Claude connector pointing to your instance's MCP server URL. Embedding security improves with JWT tokens passed via POST instead of GET, programmatic filter control through a new `parameters` prop, and a streamlined embedding wizard. This release also includes multiple enhancements and bug fixes.

This branch is not the default for now if you use `community-latest`. You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `0.62` or `1.62` for the enterprise edition (EE) and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.62
```

- [Learn more about Metabase 62](https://www.metabase.com/changelog/62)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)
