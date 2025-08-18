---
date: 2025-07-29
title: 'Clever Tools 3.14: call it with npx'
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
description: One-off usages are now simpler
excludeSearch: true
---

[Clever Tools 3.14](https://github.com/CleverCloud/clever-tools/releases/tag/3.14.0) is available. It includes some bug fixes for operators options and `service` command. It also introduces `clever-tools` as an available binary after installation.

This allows you to use Clever Tools directly with `npx` or `npm exec`, which is useful in scripts or CI/CD pipelines:

```bash
# Set/Export CLEVER_TOKEN and CLEVER_SECRET to login with a given account
# --yes is used to skip the interactive prompts
npx --yes clever-tools@latest version
npm exec -- clever-tools@3.14 profile --format json
```

## How to upgrade

To upgrade Clever Tools, [use your favorite package manager](/doc/cli/install/). For example with `npm`:

```
npm update -g clever-tools
clever version
```
