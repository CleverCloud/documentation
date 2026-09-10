---
type: docs
weight: 233
linkTitle: Consumption
title: Consumption
description: Understand Clever Cloud billing calculation, credit consumption metrics, and how application scaling affects your monthly costs
keywords:
- billing
- consumption
- analytics
- metrics
- costs
- grafana
aliases:
- /doc/account/consumption
- /doc/admin-console/analytics-consumption
- /doc/billing/analytics-consumption
- /doc/consumption
---

Clever Cloud's billing is based on several types of products: applications (Java, PHP, Jenkins, etc.), managed services (MySQL, PostgreSQL, etc.), storage services (via FTP with FS Buckets, or via the S3 protocol with Cellar) and other services (Heptapod, Pulsar, etc).

## Billing calculation

The calculation of consumption is based on the second of running. Once your monthly bill has been generated, you can refer to it to find out by service:

- the size of the instances used
- the execution time
- the unit price per second
- the total monthly amount

To find your consumption history, it is visible in the **Metrics in Grafana** service via a specific Grafana dashboard. This is called the **Uptime Service**.

![Grafana dashboard](/images/analytics.png "The Uptime Service dashboard in Grafana")

## Upscale & Downscale Impacts

If the auto-scalability option is activated, it is possible that the size of the instances of your applications will vary during the month. This variation will not be systematically identical from one month to the next, which explains the variation in the amount of your bills.

Most of our cutomers apps running with auto-scaling enabled have less than a ±5% variation between consecutive months in their invoice. Especially because upscale events don't last for long before a downscale occurs, usually after 2-3 hours. High traffic is most of the time temporary (a newsletter sendings, a TV show appearance, Techcrunch effect etc.).

In the end, auto-scaling is pretty useful to avoid applications slowdown without a significant impact on your billing.

## Credit provisioning

Clever Cloud uses a credit provision system to cover the consumption of the upcoming billing period.

At the beginning of each month, when the monthly invoice is generated, Clever Cloud calculates the amount of resources consumed during the current billing period. This consumption is used as an estimate for the following period.

Based on this estimate, the required amount of prepaid credits is added to the invoice to provision the account for the upcoming month.

### Example

The **Current credit** is the amount of prepaid credits provisioned during the previous billing cycle, as well as any other sources (free credits, partnership credits etc...). It is used to pay for the actual consumption of the current period.

The **Total paid** amount corresponds to the amount required to cover the current consumption and provision the account for the following period, taking the current credit into account.

For example, in February:

- €100 of current credit is available from the January provisioning.
- February's actual consumption is €120.
- €120 of credits is provisioned for March.
- The amount to be paid is therefore **€120 - €100 + €120 = €140**.

| Period | Current credit | Actual consumption | Provision for next period | Total paid |
|--------|---------------:|-------------------:|--------------------------:|-----------:|
| January (first invoice of the account) | €0 | €100 | €100 | €200 |
| February | €100 | €120 | €120 | €140 |
| March | €120 | €80 | €80 | €40 |