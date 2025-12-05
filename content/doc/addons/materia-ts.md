---
type: docs
linkTitle: Materia TS
title: Materia TS
description: Deploy Materia Time Series store distributed across 3 datacenters, storage-based, resilient and compatible with Warp 10 ecosystem
keywords:
- materia ts
- time series
- warp 10
- serverless database
- distributed storage
- high availability
---

Materia is a new serverless databases offering by Clever Cloud. A whole range of services meeting the needs expressed by our customers in recent years, with an open and resilient approach. It includes deployment across multiple availability zones, compatibility with existing protocols, clients, and pay-as-you-go billing. It's built on the [FoundationDB](https://www.foundationdb.org/) open source transactional engine. A distributed and robust solution, notably thanks to its high simulation capacity.

Materia TS is the time series database of this family. It comes with simplicity in mind. You have no instance size to choose, no storage capacity to worry about. We simply provide you with a host address, a port and a token: you’re ready to go! Once our servers send a reply message, your data is durable: it's synchronously replicated over 3 data centers in Paris.

You don't have to configure leaders, followers: high availability is included, by design.

> [!NOTE] Materia TS is in private access
> Ask for activation to your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice)

{{% content "warp10-concepts" %}}

## Create a Materia TS add‑on

To create a Materia TS add-on, use the [Console](https://console.clever-cloud.com) or the following command in Clever Tools:

```bash
clever addon create ts myTS --org <your_org_id>
```

The add-on is immediately created and you can start using it with provided tokens.

## Using your Materia TS add-on

Materia TS uses Warp10 time series engine and WarpsScript query language. It
provides PromQL and Prometheus Ingestion gateway in addition to warp10 endpoints. You can also use [Time Series Language (TSL)](https://github.com/ovh/tsl/) previously written by OVHcloud Metrics team.

| Endpoint | Description |
| -------- | ----------- |
| `https://materiats.eu-fr-1.services.clever-cloud.com:443/api/v0/update` | Warp10 compatible Ingestion endpoint |
| `https://materiats.eu-fr-1.services.clever-cloud.com:443/api/v0/exec` | WarpScript query language endpoint |
| `https://catalyst-materiats.eu-fr-1.services.clever-cloud.com:443/` | Prometheus Ingestion gateway |
| `https://prometheus-materiats.eu-fr-1.services.clever-cloud.com:433` | PromQL endpoint |

For complete technical documentation on Warp 10 and its query language,
see our [Warp 10 documentation](/doc/metrics/warp10/).

> [!TIP] HTTP headers to pass tokens
> Warp 10 related endpoints expects a `X-warp10-token` HTTP header containing
the read or write token of your add-on. Prometheus related endpoints expects
your tokens inside the `Authorization` HTTP header.

{{% content "warp10-content" %}}
