---
title: "Metabase 0.61.19, 0.62.17 and 0.63.14 are available (security update)"
description: Metabase 0.61.19, 0.62.17 and 0.63.14 harden security and introduce breaking changes to API parameters, dependency permissions and serialization
date: 2026-08-21
tags:
  - addons
  - metabase
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Metabase versions [0.61.19](https://github.com/metabase/metabase/releases/tag/v0.61.19), [0.62.17](https://github.com/metabase/metabase/releases/tag/v0.62.17) and [0.63.14](https://github.com/metabase/metabase/releases/tag/v0.63.14) are now available on Clever Cloud. These releases focus on hardening Metabase security and include the changes from private patch releases published for each branch. Versions starting with `1` provide the same updates for the enterprise edition.

## Breaking changes

These security measures introduce breaking changes. Metabase no longer supports undocumented API usage, and the `/api/card/{card-id}/query/{export-format}` endpoint now requires a non-blank `id` for each item in the `parameters` array. Users also need **View** collection permissions for every question dependency, including models, metrics and nested questions. Database secrets are no longer included in serialization exports, but existing exports containing secrets can still be imported.

## `community-latest` on XS instances

All Metabase add-ons that used `community-latest` on an XS Java instance have been pinned to `0.59.9`, the latest version that can start with the 1 GB of RAM provided by this instance size. Metabase `0.60` and later require at least 2 GB of RAM, as detailed in the previous changelog entries about [the new RAM requirements](/changelog/2026/05-06-metabase-60-ram/) and [the availability of Metabase 60](/changelog/2026/05-12-metabase-60/). To upgrade, set `CC_METABASE_VERSION` to `latest` and rebuild the underlying Java application. The update automatically resizes it from XS to S because `latest` resolves to a version newer than `0.60`. Keep `latest` afterward so each new deployment uses the most recent Metabase version available on Clever Cloud.

Back up your Metabase application database and review your API integrations and collection permissions before updating. If you use `latest` on an S instance or larger, restart your instance to get the latest version. If you use a specific branch, update `CC_METABASE_VERSION` of the underlying Java application to its latest patch and rebuild it.

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com), or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.63
```

- [Read the Metabase 61 changelog](https://www.metabase.com/changelog/61)
- [Read the Metabase 62 changelog](https://www.metabase.com/changelog/62)
- [Read the Metabase 63 changelog](https://www.metabase.com/changelog/63)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)
