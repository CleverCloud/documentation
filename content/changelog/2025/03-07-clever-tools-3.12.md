---
title: 'Clever Tools 3.12, with API Tokens and Network Groups'
date: 2025-03-07
tags:
  - clever-tools
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
description: Two new big features to play with
excludeSearch: true
---

[Clever Tools 3.12](https://github.com/CleverCloud/clever-tools/releases/tag/3.12.0) is available. It includes some bug fixes and two new experimental features, available through feature flags.

## API Tokens
First is `clever tokens`, which allows you to create and manage API tokens, and use them to request the Clever Cloud API:

```bash
clever features enable tokens

clever tokens create "CI job Foobar"
clever tokens create "Quick local test" --expiration 1h
```
You can also list or revoke tokens:

```bash
clever tokens -F json
clever tokens revoke api_tokens_xxx
```

Once created, API tokens must be used through the bridge URL:

```bash
curl https://api-bridge.clever-cloud.com/v2/self -H "Authorization: Bearer [API_TOKEN]"
```
- [Clever Cloud API Documentation](/developers/api)
- [Give your feedback about API Tokens](https://github.com/CleverCloud/Community/discussions/categories/api-tokens)

## Network Groups

The second feature is `clever ng`, to manage the long awaited Network Groups. Use them to link resources over a [Wireguard-based](https://www.wireguard.com/) private and secure network. It can be applications, add-ons or external systems (a local machine, a third-party server, etc.).

```bash
clever features enable ng

clever ng create myNg
clever ng link app_id myNg
clever ng unlink app_id myNg

clever ng create anotherNg --link app_id1,app_id2
clever ng get anotherNg
clever ng get app_id1

clever ng
clever ng search Ng

clever ng delete myNg
clever ng delete anotherNg
```

Once linked to a Network Groups, resources can communicate with each other directly, on any port. Each resources is identified as a "Member" with a dedicated domain name. Each instance of a resource is a "Peer" with a unique IP address inside the Network Group.

- [Network Group demo application](https://github.com/CleverCloud/network-groups-example)

We've natively integrated Network Groups to our Keycloak and Otoroshi operators. Thus, you can (de)activate a high-availability Keycloak service with two instance synced over a Network Group. It just needs one API call (and soon one Clever Tools command):

```bash
curl -XPOST -H "Authorization: Bearer [API_TOKEN]" \
  https://api-bridge.clever-cloud.com/v4/addon-providers/addon-keycloak/addons/keycloak_id/networkgroup

curl -XDELETE -H "Authorization: Bearer [API_TOKEN]" \
  https://api-bridge.clever-cloud.com/v4/addon-providers/addon-keycloak/addons/keycloak_id/networkgroup
```

{{< callout type="info" >}}
If you activate multi-instances Keycloak feature, you'll be billed for two Java instances. Network Groups are free of charge.
{{< /callout >}}

With Otoroshi, activating a Network Group links the underlying Java application to it. Thus, you can easily add other applications to the same Network Group and use Otoroshi as a gateway to protect the access to your applications through API keys, Biscuits, WAF, etc.

```bash
curl -XPOST -H "Authorization: Bearer [API_TOKEN]" \
  https://api-bridge.clever-cloud.com/v4/addon-providers/addon-otoroshi/addons/otoroshi_id/networkgroup

curl -XDELETE -H "Authorization: Bearer [API_TOKEN]" \
  https://api-bridge.clever-cloud.com/v4/addon-providers/addon-otoroshi/addons/otoroshi_id/networkgroup
```

As this beta feature evolves, we'll add demos, documentations and videos to help you to fully take advantage of Network Groups.

- [Learn more about Network Groups](/developers/doc/develop/network-groups/)
- [Give your feedback about Network Groups](https://github.com/CleverCloud/Community/discussions/categories/network-groups)

## How to upgrade
To upgrade Clever Tools, [use your favorite package manager](/developers/doc/cli/install). For example with `npm`:

```
npm update -g clever-tools
clever version
```
