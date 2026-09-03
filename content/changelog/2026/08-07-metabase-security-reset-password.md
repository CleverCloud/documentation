---
title: "Metabase critical security update, password reset endpoint blocked"
description: Metabase 0.58.24, 0.59.21, 0.60.17, 0.61.11, 0.62.9 and 0.63.5 are available on Clever Cloud, requests to /api/session/reset_password are blocked on outdated instances
date: 2026-08-07
tags:
  - addons
  - metabase
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Metabase [published a security advisory](https://www.metabase.com/blog/security-update) about a critical vulnerability affecting the `x.58` branch and above. It could be exploited through the unauthenticated `POST /api/session/reset_password` endpoint, which allows an attacker to get an authenticated session on a vulnerable instance. Branches below `x.58` are not affected. Technical details are available in the [GHSA-vwf4-m7j8-wcjf advisory](https://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf).

Metabase versions `0.58.24`, `0.59.21`, `0.60.17`, `0.61.11`, `0.62.9` and `0.63.5` fix this vulnerability. They're available on Clever Cloud (versions starting with `1` for the enterprise edition). Update your add-on as soon as possible, through its dashboard in the [Clever Cloud Console](https://console.clever-cloud.com), by setting `CC_METABASE_VERSION` of the underlying Java application to the latest patch of your branch and rebuilding it, or with [Clever Tools](/doc/manage/cli/operators/):

```bash
clever features enable operators

clever metabase version check yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId
clever metabase version update yourMetabaseNameOrId 0.63
```

## Requests to the vulnerable endpoint are blocked

As long as your Metabase add-on runs an affected version, Clever Cloud blocks requests to `/api/session/reset_password`. Your instance stays protected against this attack, but users can't ask for a password reset email until you update. Once your add-on runs a patched version, requests reach Metabase again.

You can control this behavior with the `CC_METABASE_BLOCK_RESET_PASSWORD` environment variable of the underlying Java application. Set it to `true` to keep blocking the endpoint, even on a patched version, or to `false` to allow requests on a version that's not up to date. Restart the application for the change to take effect. Keep the default behavior unless you have a specific reason to change it.

## Detect an attack in your access logs

The attack pattern described by Metabase is a call to `POST /api/session/reset_password` answered with a `400` status code, immediately followed by a call to `GET /api/user/current` answered with a `200` status code, from the same IP address. You can look for this sequence in the access logs of the Java application of your Metabase add-on, kept for 7 days:

```bash
clever accesslogs --app yourMetabaseJavaAppId --since 7d --format json-stream \
  | jq -r 'select(.http.request.path == "/api/session/reset_password" or .http.request.path == "/api/user/current")
           | "\(.date) \(.source.ip) \(.http.request.method) \(.http.request.path) \(.http.response.statusCode)"'
```

Access logs are also available in the [Clever Cloud Console](https://console.clever-cloud.com). A `200` on `/api/user/current` right after a rejected password reset means the attacker got a valid session on your instance: consider it compromised and apply the steps below.

## What to do after the update

Metabase recommends the following actions once your instance runs a patched version:

- Revoke all active sessions by deleting the rows of the `core_session` table in the PostgreSQL database of your add-on
- Review your API keys and delete the ones you don't recognize
- Review administrator accounts and check that they weren't modified
- Rotate the credentials of every database connected to your Metabase instance
- Review the logs of your data warehouses to detect unauthorized access
- Review Metabase activity and query history to detect unexpected queries or exports

## Users on an XS Java instance

If your add-on uses `community-latest` as its `CC_METABASE_VERSION` and still runs on an XS Java instance, you must move to a S instance to update. Metabase requires at least 2 GB of RAM starting for releases after x.59.9, as detailed in [a previous changelog entry](/changelog/2026/05-06-metabase-60-ram/): 1 GB provided by the XS instance is no longer enough for recent versions. Update your add-on to a patched version x.60 or above, it will automatically move to a S instance.

If you need help with these database actions, contact the [Clever Cloud support team](https://console.clever-cloud.com/ticket-center-choice).

- [Learn more about Metabase on Clever Cloud](/doc/deploy/services/metabase/)
