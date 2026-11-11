---
type: docs
linkTitle: Private databases
title: Private databases
description: Isolate a dedicated PostgreSQL add-on from the internet on Clever Cloud, behind a dedicated load balancer and a Network Group, so that only your own resources reach it
keywords:
- private database
- isolated database
- network isolation
- network mode
- postgresql
- dedicated load balancer
- network groups
---

By default, a dedicated database add-on is reachable from the internet, protected by its credentials. Your applications and your tools connect to it through the [proxies](/doc/network/load-balancers/#add-ons) of Clever Cloud. The server of a private database has no public port. It sits behind a [dedicated load balancer](/doc/network/load-balancers/#dedicated-load-balancers), attached to a [Network Group](/doc/network/network-groups/). This load balancer only accepts connections from the members of the group, and from the monitoring of Clever Cloud.

This feature is available for dedicated PostgreSQL add-ons, on request. A private database needs a dedicated load balancer: ask your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) for one, with your use case and region.

## Network modes

On a dedicated plan, you choose how the database is reachable when you create it, with the `network_mode` option of the add-on:

| `network_mode`     | Clients reach the database through                           | From the internet |
| ------------------ | ------------------------------------------------------------ | ----------------- |
| `shared` (default) | The proxies of Clever Cloud                                  | Yes               |
| `direct`           | The address and port of its server, without a proxy          | Yes               |
| `public`           | Your dedicated load balancer                                 | Yes               |
| `private`          | Your dedicated load balancer, from the members of your group | No                |

In `public` mode, add the `network_group` option so that the load balancer reaches the database through the encrypted tunnel of a Network Group. In `private` mode, a client outside the group can't reach the database, even with the address of its server.

## Create a private database

Before you create the add-on, create a Network Group in your organisation and note its ID, such as `ng_xxx`. Then ask Clever Cloud support to attach this group to your dedicated load balancer, and note the ID of the load balancer, such as `loadbalancer_xxx`.

Create the add-on in the organisation of the group, with a dedicated plan. Choose the region of your load balancer, and pass both IDs as options:

```bash
clever addon create postgresql-addon my-db --org <orgID> --plan <plan> --region <region> \
  --option network_mode=private \
  --option loadbalancer=loadbalancer_xxx \
  --option network_group=ng_xxx
```

The `public` and `private` modes need the `loadbalancer` option, and the `private` mode the `network_group` option too. If the group isn't attached to the load balancer, Clever Cloud refuses to create the add-on. Otherwise, it adds the database to the group: you don't link it yourself.

## Connect to a private database

[Link each application](/doc/network/network-groups/#link-applications) that uses the database to the group. To give it the variables of the add-on, also link the add-on as a [service dependency](/doc/manage/service-dependencies/#link-a-service) of the application. Then restart the application to load them:

- `POSTGRESQL_ADDON_HOST` points to your load balancer
- `POSTGRESQL_ADDON_PORT` is the port of the load balancer for this database, not `5432`

A private database has no [direct access](/doc/deploy/databases/postgresql/#direct-access) variables, such as `POSTGRESQL_ADDON_DIRECT_HOST`. To connect from a machine outside Clever Cloud, such as your computer, add it to the group as an [external peer](/doc/network/network-groups/#connect-an-external-machine).

The database also listens on port `8080` of its [domain name](/doc/network/network-groups/#how-it-works) in the group: `postgresql_xxx.m.ng_xxx.cc-ng.cloud`.

## Limits

- You choose the network mode at creation: to open a private database, create a new add-on and copy your data
- A private database doesn't support [migrations](/doc/develop/database-migration/): to update it, contact Clever Cloud support
