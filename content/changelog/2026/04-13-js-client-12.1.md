---
title: 'JS Client 12.1: new features for Keycloak, Matomo, Metabase and Otoroshi'
description: Clever Cloud JS client 12.1 adds commands to manage Keycloak, Matomo, Metabase and Otoroshi add-ons, plus dev mode support for events
date: 2026-04-13
tags:
  - client
  - javascript
authors:
  - name: Florian Sanders
    link: https://github.com/florian-sanders-cc
    image: https://github.com/florian-sanders-cc.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Cloud JS client 12.1](https://github.com/CleverCloud/clever-client.js/releases/tag/12.1.0) is available. This release extends the new client structure introduced in v12 with dedicated commands for four managed add-ons: [Keycloak](/doc/addons/keycloak/), [Matomo](/doc/addons/matomo/), [Metabase](/doc/addons/metabase/) and [Otoroshi](/doc/addons/otoroshi/).

## New add-on commands

You can now manage the lifecycle of these services directly from the client. For Matomo, the release adds `RebootMatomoCommand` and `RebuildMatomoCommand` to reboot the add-on or rebuild it without cache, and exposes the associated Materia KV identifier through `resource.kvId` in the `GetMatomoInfoCommand` output. Keycloak, Metabase and Otoroshi each get their own dedicated command set on the same model.

```javascript
import { CcApiClient } from "@clevercloud/client/cc-api-client.js";
import { GetMatomoInfoCommand } from "@clevercloud/client/cc-api-commands/matomo/get-matomo-info-command.js";

const client = new CcApiClient({
  authMethod: {
    type: 'api-token',
    apiToken: process.env.CLEVER_API_TOKEN,
  },
});

const info = await client.send(new GetMatomoInfoCommand({ id: 'addon_xxxxxxxx' }));
console.log(info.resource.kvId);
```

## Bug fixes

- **Events**: the events client now uses `ws://` when the API host is served over `http://`, restoring support for local development setups.
- **Matomo**: `GetMatomoInfoCommand` no longer sorts available versions, preserving the order returned by the API.

## How to upgrade

Add or update `@clevercloud/client` in your project:

```bash
npm install @clevercloud/client@12.1.0
```

Refer to the [new client documentation](https://github.com/CleverCloud/clever-client.js/blob/master/NEW_CLIENT.md) for usage details and share your feedback on the [GitHub repository](https://github.com/CleverCloud/clever-client.js/issues).
