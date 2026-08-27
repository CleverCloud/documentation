---
type: docs
linkTitle: EKG and StatsD
title: Export Haskell metrics with ekg-statsd
description: Send EKG runtime and WAI request metrics from a Haskell application to the Clever Cloud StatsD endpoint
keywords:
- haskell
- ekg-statsd
- statsd
- metrics
- monitoring
aliases:
- /doc/deploy/application/haskell/tutorials/ekg-statsd-haskell-metrics.md
---

Use [EKG](https://hackage.haskell.org/package/ekg-core) to collect runtime metrics and [`ekg-statsd`](https://hackage.haskell.org/package/ekg-statsd) to send them to the [StatsD endpoint available to Clever Cloud applications](/doc/metrics/#publish-your-own-metrics). Applications built on WAI can also use [`wai-middleware-metrics`](https://hackage.haskell.org/package/wai-middleware-metrics) to record request counts, response status codes and latency distributions.

## Configure metrics

Add these packages to the executable's `build-depends` in your [Cabal file](/doc/applications/haskell#dependencies):

- ekg-core
- ekg-statsd
- scotty
- wai-middleware-metrics

Enable the runtime statistics required by `registerGcMetrics` in the executable configuration:

```cabal
ghc-options: -threaded -rtsopts -with-rtsopts=-N -with-rtsopts=-T
```

Create the metric store, start the StatsD reporter and install the WAI middleware:

```haskell
{-# LANGUAGE OverloadedStrings #-}
import           Control.Monad                   (when)
import           Data.Maybe                      (fromMaybe)
import           Network.Wai.Metrics             (WaiMetrics, metrics,
                                                  registerWaiMetrics)
import           System.Environment              (lookupEnv)
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
    _ <- forkStatsd defaultStatsdOptions store
    pure ()
  pure waiMetrics

main :: IO ()
main = do
  waiMetrics <- handleMetrics
  port <- read . fromMaybe "8080" <$> lookupEnv "PORT"
  scotty port $ do
    middleware $ metrics waiMetrics
    get "/" $ html "Hello world"
```

Enable reporting in the application environment, then deploy:

```bash
clever env set ENABLE_METRICS true
clever deploy
```

The reporter's default host and port match the local StatsD endpoint exposed to the application, so no endpoint configuration is required.
