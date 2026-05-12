---
title: "Network Groups are now available in the Console"
description: Create, browse and delete Network Groups directly from the Clever Cloud Console, link applications and add-ons, inspect members and peers without leaving the browser.
date: 2026-05-12
tags:
  - console
  - network-groups
  - wireguard
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Network Groups](/doc/develop/network-groups/) — our [WireGuard](https://www.wireguard.com/)-based private networks between Clever Cloud resources — are now first-class citizens in the [Clever Cloud Console](https://console.clever-cloud.com). Until now, creating and managing them required the [public API](/api/v4/#network-groups) or [Clever Tools](/doc/cli/network-groups/). The same operations are now available directly in the Console.

From the Network Groups section of your organisation, you can create a new group with its label, description and tags, browse the groups already in place, and delete the ones you don't need anymore. Opening a group shows its CIDR, the members linked to it (applications, add-ons or external resources) and the peers currently connected, with domain name and IP inside the private network.

Linking resources is also done from the Console: pick an application or an add-on from your organisation and add it as a member of the group in a few clicks. Removing a member works the same way, and the change is reflected immediately on the peers list as instances reconnect to the network.

This rounds out the Network Groups experience across all our interfaces — API, CLI, and now the Console — so you can pick the one that fits your workflow. Share your feedback and feature requests on our [GitHub Community](https://github.com/CleverCloud/Community/discussions/156).

- [Learn more about Network Groups](/doc/develop/network-groups/)
- [How to use Network Groups from Clever Tools](/doc/cli/network-groups/)
- [Share your feedback on Network Groups in the Console](https://github.com/CleverCloud/Community/discussions/156)
