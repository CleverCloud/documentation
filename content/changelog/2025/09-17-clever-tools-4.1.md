---
title: Clever Tools 4.1 is available
date: 2025-09-17
description: Better get your domains and runtime information in scripts
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
excludeSearch: true
---

[Clever Tools 4.1.0](https://github.com/CleverCloud/clever-tools/releases/tag/4.1.0) is available. It fixes  some bugs and:
- Return application runtime information in `clever status`
- Return the local alias after a successful `clever link` command
- Add JSON format with details to `clever domain` and `clever domain favourite` commands

## How to upgrade

To upgrade Clever Tools, [use your favorite package manager](/doc/cli/install/). For example with `npm`:

```
npm update -g clever-tools
clever version
```
