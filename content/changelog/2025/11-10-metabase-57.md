---
title: "Metabase 57 is available, with dark mode"
date: 2025-11-10
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

The `x.57` branch of Metabase is now available on Clever Cloud. It brings dark mode, variables in SQL snippets, dynamic goals for progress bars, embedding Hub, new components in Embedded Analytics JS, multiple enhancements and bug fixes.

To update, set `CC_METABASE_VERSION` of the add-on's Java application to `0.57` for the community edition or `1.57` for the enterprise edition (EE). This new branch is not yet the default if you use `community-latest`, we'll move to it in the next few weeks.

You can also use [the new Clever Tools commands](/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.57
```

- [Learn more about Metabase 57](https://www.metabase.com/changelog/57)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)
