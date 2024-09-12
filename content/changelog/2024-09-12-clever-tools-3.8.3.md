---
title: 'Clever Tools 3.8.3 is available'
date: 2024-09-12
tags:
  - clever-tools
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
description: Last minors updates before a big change
excludeSearch: true
---

After two minor releases fixing issues with drains, [Clever Tools 3.8.3](https://github.com/CleverCloud/clever-tools/releases/tag/3.8.3) is available. It fixes Nix support, `update-notifier` and enhances the add-on deletion command. It will now only need the add-on ID or name if it's in an organization linked to your account.

To upgrade Clever Tools, [use your favorite package manager](https://github.com/CleverCloud/clever-tools/blob/master/docs/setup-systems.md#how-to-install-clever-tools). For example with npm:

```
npm update -g clever-tools
clever version
```
