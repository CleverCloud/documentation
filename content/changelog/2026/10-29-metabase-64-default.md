---
title: Metabase 64 is now the default version
description: Metabase add-ons using the latest keyword now run the x.64 Long Term Support branch
date: 2026-10-29
tags:
  - addons
  - metabase
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Metabase 64 is available on Clever Cloud](/changelog/2026/10-09-metabase-64/) since October 9, 2026. It's now the default version, used when `CC_METABASE_VERSION` is `latest` or isn't set. It's a Long Term Support (LTS) release, supported by Metabase until December 1, 2027 according to its [version support policy](https://www.metabase.com/version-support).

Add-ons that use `latest` move to Metabase 64 automatically, without downtime. Add-ons pinned to a specific version or branch, such as `0.63` or `1.63`, keep the version they run today until you change it.

## Signed sessions for new add-ons

Every new Metabase add-on now gets a `MB_SESSION_SECRET_KEY` environment variable on its underlying Java application. With this secret, Metabase signs the session keys it stores in its application database, so database access alone is no longer enough to create or use a valid session.

Existing add-ons don't get this variable automatically. To enable it, set a value of at least 16 characters on the Java application and restart it. Setting or changing this value logs out all active sessions:

```bash
clever env set MB_SESSION_SECRET_KEY "$(openssl rand -base64 32)" --app yourMetabaseJavaApp
clever restart --app yourMetabaseJavaApp
```

- [Learn more about `MB_SESSION_SECRET_KEY`](https://www.metabase.com/docs/latest/configuring-metabase/environment-variables#mb_session_secret_key)

## How to update a pinned add-on

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_METABASE_VERSION` of the underlying Java application to `latest`, `0.64` or `1.64` for the enterprise edition (EE) and rebuild it without the build cache, or use [Clever Tools](/doc/tools/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId --target 0.64
```

- [Learn more about Metabase 64](https://www.metabase.com/releases/metabase-64)
- [Watch the Metabase 64 video playlist](https://www.youtube.com/playlist?list=PLF-FhkRU3Jto)
- [Learn more about Metabase on Clever Cloud](/doc/deploy/services/metabase/)
