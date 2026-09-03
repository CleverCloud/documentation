---
type: docs
weight: 141
linkTitle: Dedicated load balancers
title: Dedicated load balancers
description: Request load balancers dedicated to your organisation for isolated capacity, fixed inbound IP addresses and redundancy
keywords:
- load balancer
- sozu
- inbound ip
- redundancy
- high availability
aliases:
- /doc/load-balancers
- /doc/network/load-balancers
---

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
