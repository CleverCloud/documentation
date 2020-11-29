---
title: Analytics and consumption
position: 6
shortdesc: How credit consumption and add-on billing works.
tags:
- billing
keywords:
- billing
- consumption
---

Clever Cloud billing is based on two kind of products: apps and add-ons. Running apps consume credits within the organization, whereas add-ons are directly billed for the coming month.

## Applications Bill Calculation

Apps credit consumption is done on a 10 minute basis per scaler (instance). If you have one application running on two scalers, you will be billed each month like this: `Price per month = Number of running x instance price per 10min x 144 x 30`

In the console, the consumption of each apps is displayed 

<br/>

{{< image "/images/analytics.png" "analytics"  >}}

## Upscale & Downscale Impacts

If your apps is experiencing upscale and downscale frequently, like several times per month, your monthly invoice amount will not be exactly the same each month, if auto-scalability is enabled (in your app preferences, tab "Scaling").

Most of our cutomers apps running with auto-scaling enabled have less than a ±5% variation between consecutive months in their invoice. Especially because upscale events don't last for long before a downscale occurs, usually after 2-3 hours. High trafic is most of the time temporary (a newsletter sendings, a TV show appearence, Techcrunch effect etc.).

In the end, auto-scaling is pretty useful to avoid applications slowdown with a significant impact on your billing.
