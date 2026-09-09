---
type: docs
weight: 140
linkTitle: Network
title: Network
description: Configure networking on Clever Cloud with private networks, IP ranges and network services
keywords:
- network
- load balancers
- ip ranges
- network groups
- vpn
- wireguard
---

An application has no stable network identity by default: inbound traffic shares the Sōzu load balancers, outbound leaves from whichever host runs your instance. Dedicated load balancers, IP ranges and Unique IP fix one direction or the other. Network Groups link your resources into a private network that external machines can join over WireGuard, while a VPN keeps access to your services off the public internet.

{{< cards >}}
  {{< card link="/developers/doc/network/load-balancers" title="Dedicated load balancers" subtitle="Sōzu load balancers for your organisation, optionally redundant" icon="server-stack" >}}
  {{< card link="/developers/doc/network/ip-ranges" title="IP ranges" subtitle="Query current outbound ranges from the API, never hardcode them" icon="tcp-ip-service" >}}
  {{< card link="/developers/doc/network/network-groups" title="Network Groups" subtitle="WireGuard network between your resources, joinable from outside" icon="endpoints" >}}
  {{< card link="/developers/doc/network/unique-ip" title="Unique IP" subtitle="One fixed exit IP address per region" icon="map-pin" >}}
  {{< card link="/developers/doc/network/vpn" title="VPN" subtitle="Private access to your services over WireGuard, IPSec or OpenVPN" icon="lock-closed" >}}
{{< /cards >}}
