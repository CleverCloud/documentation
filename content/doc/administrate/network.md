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
At the time of writing this doc, this service was billed 30€/month.
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

### Dedicated Frontends

By default, incoming traffic to your applications goes through Clever Cloud's shared frontends (powered by [Sōzu](https://www.sozu.io/)). For use cases requiring stronger network isolation or higher availability guarantees, you can request **dedicated frontends**.

Dedicated frontends are especially relevant if you need to:

- **Isolate your traffic** from other customers (compliance, security, strict SLAs)
- **Control your inbound IPs** — useful for client-side filtering or certifications (HDS, PCI-DSS, etc.)
- **Handle very high traffic volumes** without sharing resources with other organizations
- **Guarantee the availability** of your network entry point independently from other tenants

Two configurations are available:

- **1 Dedicated Frontend**: a single load balancer dedicated to your organization.
- **2 Dedicated Frontends in high availability**: two dedicated load balancers providing fault tolerance at the network entry level, eliminating the frontend as a single point of failure. This configuration is recommended for critical architectures.

This is a custom, quote-based option. To request one, [contact our support team](https://console.clever-cloud.com/ticket-center-choice) with your use case and target region so they can assess feasibility and provide a quote.

## The "Paris" region

The Paris region is owned and handled by Clever Cloud. We own or entrust the associated AS's and
IP addresses ranges.

Here are the current two addresses ranges your application may have an outgoing IP in:

- 91.208.207.0/24
- 185.133.116.0/22

Clever Cloud may change these ranges at any moment while we expand our infrastructure. If
filtering source IPs is important to you, please check this page, or opt into our Unique
IP service or a VPN Service.

Please note that allowing all ranges means you "allow" **all Clever Cloud
applications** running in the Paris region to access that service.
This means you should not base all that service security solely on filtering source IPs!

## The other regions

The other regions we provide are hosted by other providers (OVHCloud, Scaleway, Oracle Cloud).
In this case, we use the IPs they provide to us and have no control over the ranges.
