---
title: "Metabase 56 is available"
date: 2025-08-08
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
description: Time granularity parameters, multiple values selection, Joins in custom expressions, Dashboard filters, and more
excludeSearch: true
---

The `x.56` branch of Metabase is now available on Clever Cloud. It brings [time granularity parameters](https://www.metabase.com/docs/master/questions/native-editor/time-grouping-parameters), [multiple values selection](https://www.metabase.com/docs/master/questions/native-editor/basic-sql-parameters#basic-variable-that-allows-people-to-select-multiple-values) in basic SQL variables, [joins in custom expressions](https://www.metabase.com/docs/master/questions/query-builder/join#joins-with-custom-expressions), [dashboard filters](https://www.metabase.com/docs/latest/dashboards/filters) in the dashboards' body, [more ways](https://www.notion.so/metabase/Public-Customer-Docs-for-New-Iframe-Embedding-21e69354c90180228015f4daa5ce80fd) to embed dashboards with JavaScript `<script>` tags (beta), multiple enhancements and bug fixes.

To update, set `CC_METABASE_VERSION` of the add-on's Java application to `0.56` for the community edition or `1.56` for the enterprise edition (EE). This new branch is not yet the default if you use `community-latest`, we'll move to it in the next few weeks.

You can also use [the new Clever Tools commands](/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.56
```

- [Learn more about Metabase 56](https://www.metabase.com/changelog/56)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)
