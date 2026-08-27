---
type: docs
linkTitle: Node.js metrics
title: Export Node.js metrics with hot-shots
description: Send custom application metrics to Clever Cloud from a Node.js application with the hot-shots StatsD client
keywords:
- node.js
- hot-shots
- statsd
- metrics
- monitoring
aliases:
- /doc/deploy/application/javascript/tutorials/node-statsd-nodejs-metrics
---

[Clever Cloud applications expose a StatsD endpoint](/doc/metrics/#publish-your-own-metrics) that accepts custom metrics over UDP. For Node.js applications, use the maintained [`hot-shots` client](https://github.com/brightcove/hot-shots).

Install it as an application dependency:

```bash
npm install hot-shots
```

Create a client with its default configuration, then send the metrics your application needs:

```javascript
const StatsD = require("hot-shots")

const client = new StatsD()

// Increment a counter by one
client.increment("my_counter")

// Record the current value of a gauge
client.gauge("my_gauge", 123.45)
```

The default host and port used by `hot-shots` match the StatsD endpoint available to Clever Cloud applications, so no additional environment variable is required. Use a stable metric name and add only low-cardinality tags when you need to distinguish a small number of cases.

## Learn more

{{< cards >}}
  {{< card link="/doc/metrics/" title="Clever Cloud metrics" subtitle="Collect and query application metrics" icon="chart-bar" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://github.com/brightcove/hot-shots" title="hot-shots documentation" subtitle="Configure the Node.js StatsD client" icon="github" >}}
{{< /cards >}}
