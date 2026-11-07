---
type: docs
linkTitle: Tailscale
title: Connect applications to a Tailscale network
description: Connect the instances of your Clever Cloud applications to your Tailscale network, or to a compatible control server such as Headscale, with environment variables
keywords:
- tailscale
- tailnet
- headscale
- magicdns
- private network
- wireguard
- vpn
---

[Tailscale](https://tailscale.com) builds a private network between your devices and servers over [WireGuard](https://www.wireguard.com): a tailnet. Clever Cloud runs the Tailscale client on the instances of your application: each instance joins your tailnet, where it reaches your machines, and they reach it.

The tailnet comes from your Tailscale account, or from a compatible control server such as [Headscale](https://headscale.net). Your application keeps its public address. To link applications, add-ons, and external machines in a private network managed by Clever Cloud, use [Network Groups](/doc/network/network-groups/).

## Connect your application

Your instances join your tailnet with an [auth key](https://tailscale.com/docs/features/access-control/auth-keys). Create it in the admin console of Tailscale:

1. Open **Settings**, then [**Keys**](https://console.tailscale.com/admin/settings/keys), and select **Generate auth key…** in **Auth keys**
2. Enable **Reusable**, so that every instance and every new deployment joins with the same key
3. Set its **Expiration**, up to 90 days: past it, deployments fail until you set a new key
4. Enable **Ephemeral**, so that the tailnet removes the instances that stop, such as the previous ones
5. Select **Generate key**, and copy the key, which starts with `tskey-auth-`: Tailscale shows it only once

If your tailnet requires the [approval of new devices](https://tailscale.com/docs/features/access-control/device-management/device-approval), also enable **Pre-approved**.

Set this key in the `TAILSCALE_AUTH_KEY` environment variable of your application, from the Console or with [Clever Tools](/doc/tools/cli/), then restart it:

```bash
clever env set TAILSCALE_AUTH_KEY "tskey-auth-…"
clever restart
```

Before the build, each instance starts the Tailscale client and joins your tailnet. It then reaches the other machines by their [MagicDNS](https://tailscale.com/docs/features/magicdns) name or their `100.x.y.z` address, and they reach your application the same way, on the port it listens on, if your access rules allow it.

## Name of the instances

Each instance joins your tailnet as `cc-<application name>-<instance number>`, in lowercase, such as `cc-myapp-0` for the first instance of `myapp`. This name must follow the naming rules of Tailscale, or the deployment fails:

- Only letters, digits, and hyphens: no spaces or underscores
- 63 characters at most, for the complete name

A deployment starts new instances while the previous ones still run, so a new instance can join with a suffix, such as `cc-myapp-0-1`. Check the names of your instances in the **Machines** page of the admin console. Tailscale removes the previous ones about an hour after they stop.

## Options

| Name                      | Description                                                                                                           | Default |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------- |
| `TAILSCALE_ACCEPT_DNS`    | Set to `false` to keep the DNS settings of the instance: MagicDNS names then don't resolve, `100.x.y.z` ones do       | `true`  |
| `TAILSCALE_ACCEPT_ROUTES` | Set to `true` to use the [subnet routes](https://tailscale.com/docs/features/subnet-routers) other machines advertise | `false` |
| `TAILSCALE_AUTH_KEY`      | Auth key that connects the instances to your tailnet                                                                  |         |
| `TAILSCALE_LOGIN_SERVER`  | URL of another control server, such as Headscale                                                                      |         |

## Use your own control server

[Headscale](https://headscale.net) is an open source implementation of the Tailscale control server. To connect your application to it, set its URL in `TAILSCALE_LOGIN_SERVER`, and a reusable pre-authentication key it generates in `TAILSCALE_AUTH_KEY`:

```bash
clever env set TAILSCALE_LOGIN_SERVER "https://headscale.example.com"
```

Tailscale doesn't support other control servers: check the compatibility of your server with the version of the client.
