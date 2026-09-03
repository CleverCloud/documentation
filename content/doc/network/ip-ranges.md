---
type: docs
weight: 142
linkTitle: IP ranges
title: IP address ranges
description: Find the outbound IP address ranges used by Clever Cloud regions to configure allowlists on external services
keywords:
- network
- ip
- range
- outgoing
- allowlist
- security
aliases:
- /doc/administrate/network
- /doc/ip-ranges
- /doc/network/ip-ranges
- /doc/network/services
---

External services that filter their clients' source IPs need the ranges your applications come from. Query them from the API rather than hardcoding them. If you need a fixed outbound IP instead, see the [Unique IP service](/doc/network/unique-ip).

## PAR region (Paris)

The PAR region is owned and handled by Clever Cloud. We own or entrust the associated AS's and IP addresses ranges. The current outbound IP ranges are exposed by the public [Products zones API](/developers/api/v4/#products-zones). To list them for the Paris region:

```bash
curl -sS https://api.clever-cloud.com/v4/products/zones/par | jq -r '.outboundIPs[]'
```

Clever Cloud may change these ranges at any moment while we expand our infrastructure. If filtering source IPs is important to you, query the API regularly. If you need a fixed outbound IP address or a VPN, contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).

> [!WARNING] Shared IP ranges
> Allowing all ranges means allowing every Clever Cloud application running in the Paris region to access the service. Do not rely solely on source IP filtering to secure it.

## The other regions

The other regions we provide are hosted by other providers, such as IONOS, OVHCloud, Scaleway. We use the IPs they provide to us and have no control over the ranges.
