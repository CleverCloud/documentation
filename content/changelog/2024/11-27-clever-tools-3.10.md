---
title: 'Clever Tools 3.10 is available'
date: 2024-11-27
tags:
  - clever-tools
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
description: Some tiny changes, before the huge ones
aliases:
- /changelog/2024-11-27-clever-tools-3.10
excludeSearch: true
---

[Clever Tools 3.10](https://github.com/CleverCloud/clever-tools/releases/tag/3.10.0) is available. It includes some bug fixes on the `domain` command and supports [plugins activation](../11-27-elastic-plugins-support/) for Elasticsearch add-ons at creation (supported plugins list [is here](/developers/doc/addons/elastic/#plugins)). For example:

```bash
clever addon create es-addon --option plugins=analysis-icu,mapper-murmur3
```

To upgrade Clever Tools, [use your favorite package manager](/developers/doc/cli/install). For example with `npm`:

```
npm update -g clever-tools
clever version
```
