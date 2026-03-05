---
title: "Metabase security patches for versions 54 to 58"
description: Metabase v0.54.20, v0.55.20, v0.56.20, v0.57.13 and v0.58.7 are available on Clever Cloud, fixing CVEs
date: 2026-02-20
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

Metabase versions `0.54.20`, `0.55.20`, `0.56.20`, `0.57.13` and `0.58.7` are now available on Clever Cloud. These releases fix security vulnerabilities (CVEs) and should be applied as soon as possible.

If you use `community-latest` as your `CC_METABASE_VERSION`, you have nothing to do or simply need to restart your instance to get the latest patched version. If you use a specific version, update `CC_METABASE_VERSION` of the underlying Java application to the latest patch for your branch and rebuild it.

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com), or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
```

- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)
