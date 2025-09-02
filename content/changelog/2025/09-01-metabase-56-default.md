---
title: Metabase 56 is now used by default
description: Metabase 56 is now the default version for new and existing add-ons on Clever Cloud 
date: 2025-09-01
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

The `x.56` branch of Metabase is available on Clever Cloud [since last month](/changelog/2025/08-08-metabase-56/). It's now the default branch deployed with the [release 0.56.3](https://github.com/metabase/metabase/releases/tag/v0.56.3). It means that:
- All new add-ons will use it
- All add-ons using default configuration (`community-latest`) will use it after a rebuild

To update Metabase, you can also set `CC_METABASE_VERSION` of the add-on's Java application to `0.56` for the community edition or `1.56` for the enterprise edition (EE) or use [the new Clever Tools commands](/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.56
```

- [Learn more about Metabase 56](https://www.metabase.com/releases/metabase-56)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)

{{< youtube id="eNKSrpQjWk8" >}}
