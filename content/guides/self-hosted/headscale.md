---
type: docs
linkTitle: Headscale
title: Deploy a Headscale control server
description: Deploy Headscale, an open source Tailscale control server, on Clever Cloud with the Linux runtime and PostgreSQL, then connect your devices and applications to it
keywords:
- headscale
- tailscale
- tailnet
- control server
- wireguard
- vpn
- linux
- mise
- postgresql
---

{{< hextra/hero-subtitle >}}
  An open source Tailscale control server, to run your own private network without a Tailscale account.
{{< /hextra/hero-subtitle >}}

In a Tailscale network, a tailnet, the control server registers the machines and shares their keys and addresses. The machines then connect to each other directly, over WireGuard. [Headscale](https://headscale.net) replaces the control server of Tailscale, and works with the same Tailscale clients.

This guide deploys Headscale with the [Linux runtime](/doc/deploy/applications/linux/) and [Mise](/doc/manage/mise/), and stores its data in [PostgreSQL](/doc/deploy/databases/postgresql/). You then connect your devices to it, and your Clever Cloud applications with their built-in [Tailscale support](/doc/manage/tailscale/).

## Prepare the project

You need [Git](https://git-scm.com/downloads), [OpenSSL](https://openssl-library.org/), [Clever Tools](/doc/tools/cli/), and a [Clever Cloud account](https://console.clever-cloud.com). Create a project and initialize its Git repository:

```bash
mkdir my-headscale
cd my-headscale
git init
```

The `mise.toml` file installs Headscale, and passes it the credentials of the PostgreSQL add-on, as Headscale reads a setting from a variable prefixed with `HEADSCALE_`. It also defines the `run` task, which the Linux runtime [runs to start the application](/doc/deploy/applications/linux/#build-and-run-commands):

```toml {filename="mise.toml"}
[tools]
"github:juanfont/headscale" = "0.29.7"

[env]
HEADSCALE_DATABASE_TYPE = "postgres"
HEADSCALE_DATABASE_POSTGRES_HOST = "{{ env.POSTGRESQL_ADDON_HOST }}"
HEADSCALE_DATABASE_POSTGRES_PORT = "{{ env.POSTGRESQL_ADDON_PORT }}"
HEADSCALE_DATABASE_POSTGRES_NAME = "{{ env.POSTGRESQL_ADDON_DB }}"
HEADSCALE_DATABASE_POSTGRES_USER = "{{ env.POSTGRESQL_ADDON_USER }}"
HEADSCALE_DATABASE_POSTGRES_PASS = "{{ env.POSTGRESQL_ADDON_PASSWORD }}"
HEADSCALE_DATABASE_POSTGRES_SSL = "require"

[tasks.run]
run = '''
#!/usr/bin/env bash
set -euo pipefail

: "${HEADSCALE_SERVER_URL:?Set HEADSCALE_SERVER_URL before deploying}"
: "${HS_NOISE_PRIVATE_KEY:?Set HS_NOISE_PRIVATE_KEY before deploying}"
mkdir -p data
printf '%s' "$HS_NOISE_PRIVATE_KEY" > data/noise_private.key
chmod 600 data/noise_private.key

headscale serve -c config.yaml
'''
```

The task stops the deployment with an error if `HEADSCALE_SERVER_URL` or `HS_NOISE_PRIVATE_KEY`, which you set below, is missing. It then writes the private key of the server in `data/noise_private.key`, readable only by the application, and starts Headscale with `config.yaml`. This key comes from an environment variable, so that it stays the same across deployments: your machines keep trusting the server.

The `config.yaml` file holds the other settings of Headscale, which [its documentation](https://headscale.net/stable/ref/configuration/) describes:

```yaml {filename="config.yaml"}
listen_addr: 0.0.0.0:8080
metrics_listen_addr: 127.0.0.1:9090
grpc_listen_addr: 127.0.0.1:50443
unix_socket: ./data/headscale.sock
unix_socket_permission: "0770"
noise:
  private_key_path: ./data/noise_private.key
node:
  ephemeral:
    inactivity_timeout: 30m
prefixes:
  v4: 100.64.0.0/10
  v6: fd7a:115c:a1e0::/48
derp:
  server:
    enabled: false
  urls:
    - https://controlplane.tailscale.com/derpmap/default
disable_check_updates: true
dns:
  magic_dns: true
  base_domain: tailnet.internal
  override_local_dns: false
  nameservers:
    global:
      - 1.1.1.1
```

Headscale listens on port `8080`, behind the load balancers of Clever Cloud, which handle HTTPS. Its metrics and the socket of its command line stay local. It reads the private key that the `run` task writes, and gives machines addresses in the `prefixes` ranges.

An ephemeral machine stays registered for 30 minutes after it disconnects, instead of 2 by default, so that your applications stay in your network while Headscale redeploys, which takes a few minutes.

With `dns`, the machines name each other in the `tailnet.internal` domain, and keep their own DNS servers. When they can't connect directly, they go through the public Designated Encrypted Relay for Packets (DERP) servers of Tailscale. An application can't receive the UDP traffic, on port 3478, that the relay built into Headscale needs to work.

## Create the application and its database

Create a Linux application, which runs on a single instance by default, as Headscale needs, then show its domain:

```bash
clever create --type linux my-headscale
clever domain
```

Your machines keep the URL of the server. To use your own domain, add it now, and [configure its DNS](/doc/manage/domain-names/):

```bash
clever domain add headscale.example.com
```

Set the public URL of your server, with your domain or the `cleverapps.io` one, then generate its private key:

```bash
HEADSCALE_URL="https://headscale.example.com"
clever env set HEADSCALE_SERVER_URL "$HEADSCALE_URL"
clever env set HS_NOISE_PRIVATE_KEY "privkey:$(openssl rand -hex 32)"
```

Headscale recommends SQLite, and keeps PostgreSQL in maintenance mode. This guide uses PostgreSQL: the disk of an instance doesn't persist across deployments, and an [FS Bucket](/doc/deploy/storage/fs-bucket/#limits) doesn't suit SQLite, as two instances can run during a [blue/green deployment](/doc/manage/#bluegreen-deployment). Create the add-on, linked to the application. The `dev` plan suits a test: choose a larger [plan](/doc/deploy/databases/postgresql/) for production.

```bash
clever addon create postgresql-addon my-headscale-pg --plan dev --link my-headscale
```

## Deploy Headscale

Commit the project, then deploy it:

```bash
git add .
git commit -m "Deploy Headscale"
clever deploy
```

Check that Headscale answers on its `/health` path, with the URL of your server:

```bash
curl "$HEADSCALE_URL/health"
```

## Create users and auth keys

Manage Headscale with its command line, on the instance, through [SSH](/doc/manage/ssh-access/). Create a user, then list the users to get its ID:

```bash
clever ssh --command 'cd "$APP_HOME" && headscale -c config.yaml users create my-team'
clever ssh --command 'cd "$APP_HOME" && headscale -c config.yaml users list'
```

Then create a reusable and ephemeral auth key for this user, here with the ID `1`, as instances change with each deployment:

```bash
clever ssh --command 'cd "$APP_HOME" && headscale -c config.yaml preauthkeys create --user 1 \
  --reusable --ephemeral --expiration 90d'
```

The command returns the key, which starts with `hskey-auth-`.

## Connect your machines

Without an access policy, every machine of your network reaches the others, whatever their user: define a [policy](https://headscale.net/stable/ref/policy/) to restrict access.

On a device, install the [Tailscale client](https://tailscale.com/download), then join your network as the [Headscale documentation](https://headscale.net/stable/usage/getting-started/) explains:

```bash
tailscale up --login-server https://headscale.example.com --auth-key hskey-auth-…
```

For a device you keep, create its key without `--ephemeral`, so that it stays in your network while it's offline.

To connect a Clever Cloud application, here `my-app`, set its [Tailscale variables](/doc/manage/tailscale/#use-your-own-control-server), not the ones of Headscale:

```bash
clever env set --app my-app TAILSCALE_LOGIN_SERVER "$HEADSCALE_URL"
clever env set --app my-app TAILSCALE_AUTH_KEY "hskey-auth-…"
clever restart --app my-app
```

List the connected machines from the folder of your Headscale project:

```bash
clever ssh --command 'cd "$APP_HOME" && headscale -c config.yaml nodes list'
```

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/manage/tailscale" title="Headscale/Tailscale support" subtitle="Connect your applications to a tailnet" icon="lock-closed" >}}
  {{< card link="/developers/doc/deploy/applications/linux" title="Linux applications" subtitle="Deploy any application" icon="simple:linux" >}}
  {{< card link="/developers/doc/deploy/databases/postgresql" title="PostgreSQL" subtitle="Store data in a managed database" icon="simple:postgresql" >}}
  {{< card link="https://headscale.net" title="Headscale documentation" subtitle="Configure users, access rules and DNS" icon="book-open" >}}
{{< /cards >}}
