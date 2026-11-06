---
title: 'JS Client 12.5: request metrics, live requests and scoped Warp 10 tokens'
description: Clever Cloud JS client 12.5 adds status code distribution, requests heat map and live requests commands, moves Warp 10 tokens to API v4 and merges identical concurrent requests
date: 2026-06-02
tags:
  - client
  - javascript
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Cloud JS client 12.5](https://github.com/CleverCloud/clever-client.js/releases/tag/v12.5.0) is available. It adds commands to read the HTTP traffic of your applications from the [metrics](/doc/observability/metrics/) API, and wraps up the changes shipped since 12.1 for Network Groups and request handling.

## Request metrics

Three commands cover a whole organisation, or a single application when you pass its `applicationId`. `GetStatusCodeDistributionCommand` returns the number of requests per HTTP status code, over the whole period and per time bucket. `GetHeatMapCommand` returns where requests come from, aggregated by geographic cell. `StreamRequestsCommand` opens a live stream of the same data, delivered in short batches:

```javascript
import { CcApiClient } from '@clevercloud/client/cc-api-client.js';
import { StreamRequestsCommand } from '@clevercloud/client/cc-api-commands/metrics/stream-requests-command.js';

const client = new CcApiClient({
  authMethod: {
    type: 'api-token',
    apiToken: process.env.CLEVER_API_TOKEN,
  },
});

const stream = await client.stream(new StreamRequestsCommand({ applicationId: 'app_xxxxxxxx' }));
stream.onRequests((locations) => {
  for (const { city, count } of locations) {
    console.log(`${city}: ${count} requests`);
  }
});
await stream.start();
```

`GetMetricsCommand` gains a `timestampUnit` option and now returns timestamps in milliseconds by default, to use them directly with `Date`. Set `timestampUnit: 'us'` to keep the microseconds the API returns. `GetWarpTokenCommand` now relies on the API v4 and issues time-limited tokens: replace `tokenKind` with the `applications` the token grants access to and an optional `ttl`, and pass an `applicationId` to scope it to a single application. It returns an object holding the `token`, its scope and its expiration date, instead of a bare string.

## Network Groups and requests

Release 12.2 exports `NETWORK_GROUP_SUPPORTED_ADDON_PROVIDER_IDS` and `isNetworkGroupAddonCandidate()` from the network group utilities, to list only the add-ons you can add to a [Network Group](/doc/network/network-groups/). Since 12.3, you can add an add-on as a member from its `realId`. Since 12.4, identical `GET` requests sent at the same time share a single HTTP call, and the Otoroshi commands output drops its `environment` field and gains `api.swaggerUrl`.

## How to upgrade

Update `@clevercloud/client` in your project:

```bash
npm install @clevercloud/client@12.5.0
```
