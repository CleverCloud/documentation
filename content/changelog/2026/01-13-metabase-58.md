---
title: Metabase 58 is available with Documents and Guest Embeds
date: 2026-01-13
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
description: Dark mode, variables in SQL snippets, dynamic goals for progress bars, embedding Hub, new components in Embedded Analytics JS, and more
excludeSearch: true
---

The `x.58` branch of Metabase is now available on Clever Cloud. It brings multiple improvements and bug fixes, Modular Embedding, [Guest Embeds](https://www.metabase.com/docs/latest/embedding/guest-embedding), but also [Documents](https://www.metabase.com/docs/latest/documents/introduction). They let you blend charts and metrics with narrative text using Markdown or a rich text editor. Collaborate with comments, mentions, and emoji reactions—like a Notion doc meets Metabase, or a lightweight Jupyter notebook.

To update, set `CC_METABASE_VERSION` of the add-on's Java application to `0.58` for the community edition or `1.58` for the enterprise edition (EE). This new branch is the default if you use `community-latest`.

You can update through add-on’s dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `0.58` or `1.58` for the enterprise edition (EE) and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.58
```

- [Learn more about Metabase 58](https://www.metabase.com/changelog/58)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)

{{< youtube id="Qc8Zsoam9Dc" >}}
