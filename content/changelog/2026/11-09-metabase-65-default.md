---
title: Metabase 65 is now the default version
description: Metabase add-ons using the latest keyword now run the x.65 branch with release 0.65.3, which brings a SQL parsing timeout, stricter connection checks and several fixes
date: 2026-11-09
tags:
  - addons
  - metabase
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Metabase 65](/changelog/2026/11-03-metabase-65/) has been available on Clever Cloud since November 3, 2026. It's now the default version, used when `CC_METABASE_VERSION` is `latest` or isn't set, with the release [0.65.3](https://github.com/metabase/metabase/releases/tag/v0.65.3). It isn't a Long Term Support (LTS) release: Metabase supports it until January 1, 2027, according to its [version support policy](https://www.metabase.com/version-support). [Metabase 64](/changelog/2026/10-29-metabase-64-default/) remains the LTS branch.

Add-ons that use `latest` move to Metabase 65 automatically, without downtime: review its [breaking changes](/changelog/2026/11-03-metabase-65/#breaking-changes). Add-ons pinned to a version or a branch, such as `0.64` or `1.64`, keep it until you change it. To stay on an LTS branch, pin your add-on to `0.64`, or `1.64` for the enterprise edition (EE): Metabase supports this branch until December 1, 2027.

## What's new in Metabase 65.3

Metabase 65.3 adds `MB_SQL_PARSING_TIMEOUT_MS` to bound the time spent parsing SQL queries, 30 seconds by default. Dashboards get a card-level filter interface. The password reset form now rejects the current password. Database connection details, such as the host, port, or database name, no longer accept the `?`, `&`, `;`, and `#` characters.

The native query editor no longer selects the first database automatically. Metabot stops offering SQL tools to users who can't run native queries. The **AI exploration** entry of the **+ New** menu disappears for users without AI access. Anonymous usage analytics of self-hosted instances now go to Metabase Track by default: the anonymous tracking setting still controls them.

This release also fixes several bugs. Metabase honors `MB_TRACING_ENABLED` and `MB_SEND_NEW_SSO_USER_ADMIN_EMAIL` again, and read-only ClickHouse connections work again. Query validation with connection impersonation no longer adds 10 to 40 seconds per query, and remote sync marks an existing Library as synced.

## How to update a pinned add-on

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `latest`, `0.65`, or `1.65` for the enterprise edition (EE), then rebuild it without the build cache. With [Clever Tools](/doc/tools/cli/operators/), run:

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId --target 0.65
```

- [Learn more about Metabase 65](https://www.metabase.com/releases/metabase-65)
- [Learn more about Metabase on Clever Cloud](/doc/deploy/services/metabase/)

{{< youtube list="PLPXkWwpTfNvM" >}}
