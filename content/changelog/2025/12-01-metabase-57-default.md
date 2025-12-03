---
title: Metabase 57 is now used by default
description: Metabase 57 is now the default version for new and existing add-ons on Clever Cloud
date: 2025-12-01
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

The `x.57` branch of Metabase is available on Clever Cloud [since last month](/changelog/2025/11-10-metabase-57/). It's now the default branch deployed with the [release 0.57.4](https://github.com/metabase/metabase/releases/tag/v0.57.4). It means that:
- All new add-ons will use it
- All add-ons using default configuration (`community-latest`) will use it after a rebuild

You can update through add-on’s dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `0.57` or `1.57` for the enterprise edition (EE) and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.57
```

- [Learn more about Metabase 57](https://www.metabase.com/releases/metabase-57)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)

{{< youtube id="-Cbs-lg3rSo" >}}
