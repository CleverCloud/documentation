---
title: "Metabase 55 is available"
date: 2025-06-11
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
description: Faster, with more features
excludeSearch: true
---

The `x.55` branch of Metabase is now available on Clever Cloud. It brings a new visualizer, faster and easier to use, database routing, the new search algorithm as default and many more features. To update, just set `CC_METABASE_VERSION` of the add-on's Java application to `0.55` for the community edition or `1.55` for the enterprise edition (EE).

You can also use [the new Clever Tools commands](/developers/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.55
```

- [Learn more about Metabase 55](https://www.metabase.com/releases/metabase-55)
- [Learn more about Metabase on Clever Cloud](/developers/doc/addons/metabase/)

{{< youtube id="0wKoZR0zJ6Q" >}}
