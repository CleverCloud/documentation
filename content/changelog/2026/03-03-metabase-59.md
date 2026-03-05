---
title: "Metabase 59 is available, with Data Studio, AI and box-and-whisker plots"
description: Data Studio, box-and-whisker plots, conditional colors for big numbers, AI text-to-SQL for open source, Agent API, and more
date: 2026-03-03
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

The `x.59` branch of Metabase is now available on Clever Cloud. It introduces Data Studio, a comprehensive toolkit for data governance including a semantic layer library, dependency graphs, diagnostic tools and data transforms. It also brings box-and-whisker plots, conditional colors for big number displays, AI-powered text-to-SQL for open source users via Anthropic API, a new Agent API, multiple enhancements and bug fixes.

You can update through the add-on’s dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `0.59` or `1.59` for the enterprise edition (EE) and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.59
```

This new branch is not yet the default if you use `community-latest`, we'll move to it in the next few weeks.

- [Learn more about Metabase 59](https://www.metabase.com/changelog/59)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)
