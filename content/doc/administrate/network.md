---
type: docs
title: Networking and IP addresses ranges
linkTitle: Networking and IP
position: 3
shortdesc: What are my application's outgoing IP?
keywords:
- network
- ip
- range
- outgoing
- security
tags:
- administrate
type: docs
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

- [Wireguard](https://www.wireguard.com/): our favorite VPN technology. Has been adopted
  by most major "off-the-shelf" VPNs (like the ones that sponsor Youtubers 😉).
- [IPSec](https://www.wikiwand.com/fr/IPsec): used by a lot of companies. It might be
  their only available VPN technology.
- [OpenVPN](https://openvpn.net/): less used by companies, but still quite common.

If you are interested, please ask the support / your sales contact for a quote.

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
