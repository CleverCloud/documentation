---
title: 'JS Client 11.3: stream logs in real time'
description: Clever Cloud JS client 11.3 adds Server-Sent Events support and commands to stream application and add-on logs
date: 2025-11-14
tags:
  - client
  - javascript
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Cloud JS client 11.3](https://github.com/CleverCloud/clever-client.js/releases/tag/v11.3.0) is available. The new client structure introduced in 11.1 now supports Server-Sent Events (SSE): `client.stream()` opens a real-time stream from a stream command, reconnects automatically when the connection drops and resumes from the last event received.

This release uses it to stream [logs](/doc/observability/logs/). `StreamApplicationRuntimeLogCommand` and `StreamAddonRuntimeLogCommand` deliver the runtime logs of an application or an add-on, `StreamApplicationAccessLogCommand` the [access logs](/doc/observability/logs/#api) of an application. They accept a time range (`since`, `until`), a `limit`, and for runtime logs a deployment, instances or a text `filter` to narrow the output:

```javascript
import { CcApiClient } from '@clevercloud/client/cc-api-client.js';
import { StreamApplicationRuntimeLogCommand } from '@clevercloud/client/cc-api-commands/log/stream-application-runtime-log-command.js';

const client = new CcApiClient({
  authMethod: {
    type: 'api-token',
    apiToken: process.env.CLEVER_API_TOKEN,
  },
});

const stream = await client.stream(
  new StreamApplicationRuntimeLogCommand({ applicationId: 'app_xxxxxxxx', filter: 'error' }),
);
stream.onLog((log) => console.log(log.message));
await stream.start();
```

Release 11.2.1 also fixes the resume position of a stream, which an event without an ID could reset. To upgrade, run:

```bash
npm install @clevercloud/client@11.3.0
```
