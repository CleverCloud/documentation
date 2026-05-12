---
title: "Metabase 60 is available, with Metabot, MCP server and split panel charts"
description: Metabot, MCP server integration, Slack querying, metrics explorer, split panel charts, frozen columns, transform inspector and more
date: 2026-05-12
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

The `x.60` branch of Metabase is now available on Clever Cloud. It brings Metabot with "bring your own key" support for Anthropic models, an official MCP server to connect Claude, Cursor and other tools, and a Slack integration to query data directly from a channel.

It also introduces a metrics explorer to compare multiple metrics side-by-side and surface trends across dimensions, split panel charts to display multiple series as faceted panels, frozen columns and rows in tables, a transform inspector to compare data before and after a transform runs, model-to-transform migration in a few clicks, OpenID Connect (OIDC) authentication, remote sync with GitLab and Bitbucket in addition to GitHub, and multiple enhancements and bug fixes.

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `0.60` or `1.60` for the enterprise edition (EE) and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.60
```

## New RAM requirements

Starting with the `x.60` branch, [Metabase requires at least 2 GB of RAM](https://github.com/metabase/metabase/issues/72942) to run. Because the XS Java instance previously used by default only provides 1 GB of RAM, the default sizing has been adapted: new Metabase add-ons are deployed on a **S Java instance**, and existing add-ons are **automatically migrated to a S Java instance** when upgrading to version 60.

This new branch is not yet the default if you use `community-latest`, we'll move to it in the next few weeks. To prepare for the automatic move to x.60, we recommend scaling the underlying Java application from XS (the current default) to a S instance now from the **Scalability** link in your Metabase add-on dashboard.

If you want to keep an XS instance, stay on the `x.59` branch by setting `CC_METABASE_VERSION` to `0.59` (or `1.59` for the Enterprise Edition) on the underlying Java application. Keep in mind that staying on x.59 means you will not receive the new features shipped with x.60 and beyond; security patches and some fixes will still be provided as long as the 0.59 branch is maintained. We recommend moving to a S instance and the latest branch as soon as possible.

- [Learn more about Metabase 60](https://www.metabase.com/releases/metabase-60)
- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)
- [Pricing of Java instances on Clever Cloud](https://www.clever-cloud.com/pricing/)

{{< youtube id="IrQeCFHHU3A" >}}
