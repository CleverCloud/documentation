---
title: Push custom metrics with node-statsd for Node.js
shortdesc: This tutorial helps you configure node-statsd package on your Node.js application to push custom metrics
tags:
- deploy
keywords:
- nodejs
- metrics
- logs
- node-statsd
---

## Overview

In Node.js, you can use the `node-statsd` package to push custom metrics.

### Configure metrics for your Node.js application

You only need the `node-statsd` package in your [dependencies]({{< ref "doc/deploy/application/javascript/by-framework/nodejs.md#npm-module-dependencies" >}}):

Then add this Hello World code to your application and modify it to fit your needs:

```javascript
// npm install node-statsd

const StatsD = require('node-statsd'),
      client = new StatsD();

// Increment: Increments a stat by a value (default is 1)
client.increment('my_counter');

// Gauge: Gauge a stat by a specified amount
client.gauge('my_gauge', 123.45);
```