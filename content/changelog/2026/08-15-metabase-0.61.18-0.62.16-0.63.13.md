---
title: "Metabase 0.61.18, 0.62.16 and 0.63.13 are available (security update)"
description: Metabase 0.61.18, 0.62.16 and 0.63.13 are available on Clever Cloud with security hardening for the supported 61, 62 and 63 branches
date: 2026-08-15
tags:
  - addons
  - metabase
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Metabase versions `0.61.18`, `0.62.16` and `0.63.13` are now available on Clever Cloud. These patch releases harden security on the supported `x.61`, `x.62` and `x.63` branches and should be applied as soon as possible. Versions starting with `1` provide the same updates for the enterprise edition.

If you use `latest` as your `CC_METABASE_VERSION`, restart your instance to deploy the latest patched version. If you use a specific branch, update `CC_METABASE_VERSION` of the underlying Java application to its latest patch and rebuild it.

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com), or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.63
```

- [Read the Metabase security-focused release announcement](https://www.metabase.com/blog/security-focused-release-announcement-2026-08-12)
- [Read the Metabase 61 changelog](https://www.metabase.com/changelog/61)
- [Read the Metabase 62 changelog](https://www.metabase.com/changelog/62)
- [Read the Metabase 63 changelog](https://www.metabase.com/changelog/63)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)
