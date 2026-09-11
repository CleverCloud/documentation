---
type: docs
linkTitle: Operators
title: Operators
description: Manage Keycloak, Matomo, Metabase, and Otoroshi operators directly from Clever Tools CLI with administrative commands and configurations
keywords:
- operators
- keycloak
- metabase
- otoroshi
- cli
- management
- matomo
aliases:
- /doc/cli/operators
---

Operators allow you to deploy services as turnkey solutions on Clever Cloud. They provision resources, configure them and expose an API and tools to ease their management during their lifecycle. To add operators commands to Clever Tools, enable the `operators` feature:

```console
clever features enable operators
```

Then, you can use the commands to manage Keycloak, Matomo, Metabase and Otoroshi instances on Clever Cloud. To list deployed services:

```console
clever keycloak
clever matomo
clever metabase
clever otoroshi
```

To get information about a deployed service, use:

```console
clever keycloak get myKeycloak
clever matomo get matomo_id --format json
```

You can target a deployed service by its ID or name.

## Service management

To restart or rebuild (restart without cache) a deployed service, use:

```console
clever metabase restart myMetabase
clever otoroshi rebuild otoroshi_id
```

To open the deployed service dashboard in Clever Cloud Console, use:

```console
clever keycloak open myKeycloak
```

You can also open the service web management interface or logs of the underlying application:

```console
clever otoroshi open logs myOtoroshi
clever otoroshi open webui otoroshi_id
```

To open the Otoroshi Swagger UI, use:

```bash
clever otoroshi open swaggerui myOtoroshi
```

## Version management

Keycloak, Metabase and Otoroshi support version management. To check the version of a deployed service, use:

```console
clever otoroshi version check otoroshi_id
clever metabase version check myMetabase --format json
```

In the human output format, version checks can offer an interactive upgrade prompt. Use `--format json` to inspect versions without this prompt.

To update to a specific available version, use:

```console
clever keycloak version update myKeycloak --target 24.0.1
```

To select an available version interactively and update the service, omit `--target`:

```console
clever otoroshi version update otoroshi_id
```

## Network Groups

Keycloak and Otoroshi can be linked to a [Network Group](/doc/manage/cli/network-groups/). To enable/disable this feature, use:

```console
clever keycloak enable-ng myKeycloak
clever otoroshi disable-ng otoroshi_id
```

> [!NOTE] Keycloak clustering
> On Clever Cloud Keycloak uses Network Groups for its secure cluster feature. When you enable it, the Keycloak application is automatically scaled to 2 instances and the cluster automatically configured. When you disable the Network Group feature, the application is scaled down to 1 instance and the cluster is removed.

## Otoroshictl

You can manage Otoroshi instances with `otoroshictl`. Clever Tools exports their configuration in a compatible YAML format. With Rust and Cargo installed, use:

```bash
# Install otoroshictl and enable the operators feature
cargo install otoroshictl
clever features enable operators

clever otoroshi get-config myOtoroshi | otoroshictl config import --current --stdin
otoroshictl resources get routes
```

> [!TIP] Multiple instances
> You can add as many Otoroshi instances as you want to your `otoroshictl` configuration by repeating this command with different instance IDs or names. Add the `--current` flag to the one you want to use by default.
