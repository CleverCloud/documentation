---
type: docs
linkTitle: Network Groups
title: Network Groups
description: Configure and manage Network Groups using Clever Tools CLI for secure application communication and network isolation policies
keywords:
- network-groups
- security
- cli
- communication
- isolation
- wireguard
aliases:
- /doc/manage/cli/network-groups
- /doc/cli/network-groups
- /doc/cli/operators/ng.md
---

[Network Groups](/doc/network/network-groups/) (NG) link applications, dedicated add-ons, and external machines of an organisation in a private network, built with [WireGuard](https://www.wireguard.com/). This page lists the commands of Clever Tools to manage them. To learn how members reach each other, which add-ons join a group, and how to set up an external machine, see the [Network Groups](/doc/network/network-groups/) page.

A Network Group has an ID (`ngId`), a label, and optionally a description and tags. Its members are applications, add-ons, or external peers. Each running instance of a member is a peer, with a private IP address from the range of the group. An application or add-on member has a domain name of the form `<memberID>.m.<ngID>.cc-ng.cloud`, which resolves inside Clever Cloud instances.

Share your feedback and feature requests in [the Network Groups section of the GitHub Community](https://github.com/CleverCloud/Community/discussions/categories/network-groups).

## Prerequisites

Activate `ng` feature flag to manage Network Groups:

```console
clever features enable ng
```

Then, check it works with the following command:

```console
clever ng
```

In the following examples, target an organisation with `--org` or `-o`. A Network Group and its members belong to the same organisation.

## Create a Network Group

Create a Network Group with a label:

```console
clever ng create myNG
```

You can create it declaring its members:

```console
clever ng create myNG --link app_xxx,postgresql_xxx
```

You can add a description and tags:

```console
clever ng create myNG --description "My first NG" --tags test,ng
```

## Delete Network Groups

You can delete a Network Group through its ID or label, even if it still has members. Their instances leave the group and keep running:

```console
clever ng delete ngId
clever ng delete ngLabel
```

## List Network Groups

Once created, you can list your Network Groups:

```console
clever ng

┌─────────┬───────-┬─────────-─┬───────────────┬─────────┬───────┐
| (index) │ ID     │ Label     │ Network CIDR  │ Members │ Peers │
├─────────┼────────┼───────────┼───────────────┼─────────┼───────┤
│ 0       │ 'ngId' │ 'ngLabel' │ '10.x.0.0/16' │ X       │ Y     │
└─────────┴────────┴──────────-┴───────────────┴─────────┴───────┘
```

A `json` formatted output is available with the `--format/-F json` option.

## (Un)Link a resource to a Network Group

To (un)link an application or an add-on to a Network Group:

```console
clever ng link app_xxx ngIdOrLabel
clever ng unlink redis_xxx ngIdorLabel
```

Both commands take effect on running instances within seconds, without a restart.

> [!TIP] Add-on IDs
> To link add-ons to a Network Group, use their real IDs, such as `mysql_xxx`, `postgresql_xxx`, or `redis_xxx`. Only dedicated plans of the Elasticsearch, MongoDB, MySQL, PostgreSQL, and Redis add-ons are reachable through a group, on port `8080`. See [Link add-ons](/doc/network/network-groups/#link-add-ons).

## Manage external peers

To create an external peer in a Network Group, provide a label, the Network Group, and the WireGuard public key of the machine:

```console
clever ng create external myExternalPeer myNG wg_public_key
```

To delete an external peer from a Network Group:

```console
clever ng delete external peerIdOrLabel myNG
```

## Get information of a Network Group, a member or a peer

To get information about a Network Group or a resource (a `json` formatted output is available):

```console
clever ng get ngIdOrLabel -F json
clever ng get resourceIdOrName
```

You can specify the type of resource to look for with the `--type` option (`NetworkGroup`, `Member`, `CleverPeer`, `ExternalPeer`):

```console
clever ng get resourceIdOrName --type ExternalPeer
```

You can also search for Network Groups, members or peers:

```console
clever ng search text_to_search -F json
clever ng search text_to_search --type Member
```

> [!NOTE] Search and exact matches
> The search command is case-insensitive and will return all resources containing the search string. The get command looks for an exact match and will return an error if multiple resources are found.

## Get the WireGuard configuration of a Peer

To print the WireGuard configuration of an external peer, provide its ID or label and the Network Group:

```console
clever ng get-config peerIdOrLabel myNG
```

Replace `<%PrivateKey%>` with the private key of the machine. The configuration lists the current instances of the group: get it again after a restart, a deployment, or a change of scaling, and insert the private key again. To follow these changes, see [Follow configuration changes](/doc/network/network-groups/#follow-configuration-changes).

## Demos & examples

You can find ready to deploy projects using Network Groups in the following repositories:

- <https://github.com/CleverCloud/network-groups-example>

Share your projects in [the Network Groups discussion](https://github.com/CleverCloud/Community/discussions/categories/network-groups)
