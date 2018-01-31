---
title: Metrics
shortdesc: Gather metrics on your applications
tags:
- apps
---

<div class="panel panel-warning">
  <div class="panel-heading">
    <h4>Warning:</h4>
  </div>
  <div class="panel-body">
    Clever Cloud Metrics is still in beta.
  </div>
</div>

In addition to logs, you can have access to metrics to know how your application
behaves. By default, system metrics like CPU and RAM use are available, as well
as application-level metrics when available (apache or nginx status for instance).

You can also publish your own metrics if you want (via `statsd`).

## Activate metrics

To enable metrics on your application you need to add `ENABLE_METRICS=true` to
its [environment variables](/doc/admin-console/environment-variables/) and restart
the application.
Once it's done, metrics will automatically be gathered and displayed in the console.

## Display metrics

For each application, there is a `Metrics` tab in the console.

### Overview pane

To get a quick overview of the current state of your scalers, the overview pane
displays the current CPU, RAM, Disk and Network activity. On supported platforms,
you can also have access to requests / second, and GC statistics.

### Advanced pane

Advanced metrics allow you to access all gathered metrics,
on a specified time range.

### Custom queries

All metrics are stored in [Warp10](http://www.warp10.io/), so you explore data directly with
the quantum interface, with [WarpScript](http://www.warp10.io/reference/). For instance,
you can derive metrics over time, do custom aggregations or combine metrics.

## Custom metrics

You can expose custom metrics via [`statsd`](https://github.com/etsy/statsd#usage).
These metrics will be gathered and displayed in advanced view as well.
On some platforms, standard metrics published over `statsd` are even integrated on the overview pane.

Metrics published over `statsd` are prefixed with `statsd`.

### statsd socket

To publish custom metrics, configure to use your client to push to `localhost:8125`
(it's the default host and port, so it should work with default settings as well).

### NodeJS example

You can use `node-statsd` to publish metrics

```javascript
// npm install node-statsd

const StatsD = require('node-statsd'),
      client = new StatsD();

// Increment: Increments a stat by a value (default is 1)
client.increment('my_counter');

// Gauge: Gauge a stat by a specified amount
client.gauge('my_gauge', 123.45);
```

### Haskell example

<!-- Maybe this should be put in haskell documentation? -->

In Haskell, metrics are usually gathered with [EKG](https://hackage.haskell.org/package/ekg).
The package `ekg-statsd` allows to push EKG metrics over `statsd`.

If you're using [warp](https://hackage.haskell.org/package/warp), you can use
`wai-middleware-metrics` to report request distributions (request count,
responses count aggregated by status code,
responses latency distribution).

EKG allows you to have access to GC metrics, make sure you compile your application
with `"-with-rtsopts=-T -N"` to enable profiling.

```haskell
{-# LANGUAGE OverloadedStrings #-}

-- you need the following packages
-- ekg-core
-- ekg-statsd
-- scotty
-- wai-middleware-metrics

import           Control.Monad                   (when)
import           Network.Wai.Metrics             (WaiMetrics, metrics,
                                                  registerWaiMetrics)
import           System.Metrics                  (newStore, registerGcMetrics)
import           System.Remote.Monitoring.Statsd (defaultStatsdOptions,
                                                  forkStatsd)
import           Web.Scotty

handleMetrics :: IO WaiMetrics
handleMetrics = do
  store <- newStore
  registerGcMetrics store
  waiMetrics <- registerWaiMetrics store
  sendMetrics <- maybe False (== "true") <$> lookupEnv "ENABLE_METRICS"
  when sendMetrics $ do
    putStrLn "statsd reporting enabled"
    forkStatsd defaultStatsdOptions store
    return ()
  return waiMetrics

main = do
  waiMetrics <- handleMetrics
  scotty 8080 $ do
     middleware $ metrics waiMetrics
     get "/" $
       html $ "Hello world"
```
