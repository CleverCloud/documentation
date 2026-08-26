---
type: docs
linkTitle: Networking and IP
title: Networking and IP addresses ranges
description: Understand Clever Cloud IP ranges for external service filtering, whitelist configuration, and unique IP services
keywords:
- network
- ip
- range
- outgoing
- security
---

Some services external to Clever Cloud require filtering their clients' source IPs. They
may call it "whitelist" or "allowlist". Since your applications may be deployed
"somewhere" inside your chosen zones, you cannot predict the IP they are going to
come from.

Here's a bit more insight on the subject:

## Custom network services

### Unique IP service

For each region, we provide a unique IP service.
This service allows your queries to some external services to come from a fixed and unique IP.

This service does not appear in the Console at the moment.
The best is to ask the support team that will set it up for you and provide you with the needed information.
For pricing details, contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).
The price does not change with the number of applications that will use it.

The IP depends on the zone, so ask the support about it.

### VPN service

Some external services, customers or providers may propose/require a encrypted Virtual Private Network between Clever
Cloud's regions and their datacenter to secure the traffic.

We provide three kinds of VPN technologies:

- [WireGuard](https://www.wireguard.com/): our favorite VPN technology. Has been adopted
  by most major "off-the-shelf" VPNs (like the ones that sponsor Youtubers 😉).
- [IPSec](https://www.wikiwand.com/fr/IPsec): used by a lot of companies. It might be
  their only available VPN technology.
- [OpenVPN](https://openvpn.net/): less used by companies, but still quite common.

If you are interested, please ask the support / your sales contact for a quote.

### Dedicated load balancers

By default, incoming traffic to your applications goes through Clever Cloud's shared load balancers, powered by [Sōzu](https://www.sozu.io/). For workloads that need isolated capacity, fixed inbound IP addresses or additional redundancy, you can request **dedicated load balancers**.

Dedicated load balancers are especially relevant if you need to:

- **Isolate your traffic** from other customers
- **Use fixed inbound IP addresses** for allowlists or compliance requirements
- **Handle high traffic volumes** without sharing load balancer capacity with other organisations
- **Add redundancy** to the network entry point of critical architectures

Two configurations are available:

- **Single load balancer**: one load balancer dedicated to your organisation.
- **High availability**: two dedicated load balancers make the network entry layer redundant, so it doesn't depend on a single load balancer. This configuration is recommended for critical architectures.

This is a custom, quote-based option. To discuss your requirements and pricing, contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) with your use case and target region.

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
