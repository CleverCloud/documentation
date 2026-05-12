---
title: "Clever Tools 4.10: organisation-scoped add-on providers"
date: 2026-05-07
description: Clever Tools 4.10 adds an --org option to filter add-on providers, regions and plans for a specific organisation
tags:
  - clever-tools
  - cli
  - addons
authors:
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Tools 4.10.0](https://github.com/CleverCloud/clever-tools/releases/tag/4.10.0) is available. This release makes add-on provider discovery organisation-aware, so you can see exactly which providers, regions and plans are available for a given organisation before creating a new add-on.

## Organisation-scoped add-on providers

The `clever addon providers` and `clever addon providers show` commands now accept an `--org` option. When set, results are filtered to match the providers, zones and plans exposed by the `addonproviders` API for that organisation, instead of the global catalogue.

```bash
# List add-on providers available for a specific organisation
clever addon providers --org orga_xxx

# Inspect a single provider, with org-specific plans and regions
clever addon providers show postgresql-addon --org orga_xxx
```

The `clever addon create` command also uses `--org` to validate the requested region. Without it, region availability checks were not organisation-aware, which could let creation calls through in regions not allowed for your organisation. With this fix, the CLI rejects the call up front when the target region is not available in the selected organisation.

## How to upgrade

To upgrade Clever Tools, [use your favourite package manager](/doc/cli/install/). For example with `npm`:

```bash
npm update -g clever-tools
clever version
```
