---
title: 'Clever Tools 3.9, with domain diagnostics and overview'
date: 2024-10-23
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
description: Better manage your apps, lots of new features
aliases:
- /changelog/2024-10-21-clever-tools-3.9.0
excludeSearch: true
---

[Clever Tools 3.9](https://github.com/CleverCloud/clever-tools/releases/tag/3.9.0) is available. It's the first minor release since our [Big Summer Update](../07-02-clever-tools-3.8.0/). Over the past few months, we've revamped many things under the hood, to clean the code and prepare next big changes we're working on.

## List and diagnose your domains
This new version brings two new features to manage domains. First is `clever domain overview`, allowing you to list domains linked to your account, across all the organisations you manage. List only domains containing a specific text string in their name thanks to the `--filter` option. Use the `json` output (`--format`/`-F`) and tools such as [jless](https://jless.io/) to navigate through long lists easily.

This feature uses a new "short" link for the Console, which doesn't require organisation or user ID:

```bash
# The id can be an app_id, an addon_id or a real_id
https://console.clever-cloud.com/goto/id
```

The `clever domain diag` command allows you to check domains' configuration for an application, locally linked or targeted with the `--app` option. If some DNS records are wrong or missing, it will help you to know how to fix them. There is a `--filter` option to get only domains containing a specific text string in their name and a `--format`/`-F` option to output the result in `human` or `json`.

## Post-creation instructions for add-ons and fixes

This release also provides bug fixes, the token expiry date/time in `clever profile` and a better experience with add-ons like [Keycloak](/developers/doc/addons/keycloak/), [Matomo](/developers/doc/addons/matomo) or [Metabase](/developers/doc/addons/metabase/). Once created, you get post-creation instructions such as management/Console URL, temporary credentials and a link to the add-on's documentation.

To upgrade Clever Tools, [use your favorite package manager](/developers/doc/cli/install). For example with `npm`:

```
npm update -g clever-tools
clever version
```
