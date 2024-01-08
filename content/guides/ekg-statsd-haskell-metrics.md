---
type: docs
title: Ekg-statsd
shortdesc: This tutorial helps you configure ekg-statsd package on your Haskell application to push custom metrics
tags:
- deploy
- administrate
keywords:
- haskell
- ekg-statsd
- logs
- metrics
type: docs
aliases:
- /doc/deploy/application/haskell/tutorials/ekg-statsd-haskell-metrics.md
---

## Overview

In Haskell, metrics are usually gathered with [EKG](https://hackage.haskell.org/package/ekg).

The package `ekg-statsd` allows to push EKG metrics over `statsd`.
EKG allows you to have access to GC metrics, make sure you compile your application with `"-with-rtsopts=-T -N"` to enable profiling.

If you're using [warp](https://hackage.haskell.org/package/warp), you can use `wai-middleware-metrics` to report request distributions (request count, responses count aggregated by status code, responses latency distribution).

### Configure logs for your Haskell application

You need the following packages in your [dependencies]({{< ref "doc/applications/haskell#dependencies" >}}):

* ekg-core
* ekg-statsd
* scotty
* wai-middleware-metrics

Then add this Hello World code to your application and modify it to fit your needs:

```haskell
{-# LANGUAGE OverloadedStrings #-}
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
