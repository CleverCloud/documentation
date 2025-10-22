---
title: New Keycloak dashboard is available with Secured Multi Instances easy to enable
description: Better manage your Keycloak on Clever Cloud, with Secured Multi Instances based on WireGuard Network Groups
date: 2025-10-07
tags:
  - addons
  - keycloak
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

When you deploy Keycloak on Clever Cloud, you now have access to a better dashboard to manage it. This dashboard provides direct access to Keycloak admin panel, useful information such as deployed version, underlying resources, initial user/password, edit name, tags, etc. You can easily rebuild/restart your Keycloak instance with [Blue/Green deployment](/doc/best-practices/blue-green/), access the Grafana dashboard, transparently update Keycloak to a new version when available:

![Keycloak Dashboard](/images/keycloak-dashboard.webp)

## Secured Multi Instances

The Keycloak dashboard also makes Secured Multi Instances directly available from the Console, and not only through [API](/api) or [Clever Tools](/doc/cli). It adds a second Java application instance to your Keycloak which brings more resiliency and availability to your identity management solution. As communication through such cluster use an unencrypted Infinispan connection, a Network Group is automatically created and used to isolate this traffic through a private, encrypted, [WireGuard](https://www.wireguard.com/) network.

If you also need a more resilient database, contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).

- [Learn more about Network Groups](/doc/develop/network-groups/)
- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
