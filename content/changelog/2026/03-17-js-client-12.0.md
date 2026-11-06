---
title: 'JS Client 12.0: log drains on API v4 and WireGuard configurations'
description: Clever Cloud JS client 12.0 returns WireGuard configurations as text, moves log drain commands to API v4 and adds a command to get a single region
date: 2026-03-17
tags:
  - client
  - javascript
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Cloud JS client 12.0](https://github.com/CleverCloud/clever-client.js/releases/tag/v12.0.0) is available. This major release changes how [Network Groups](/doc/network/network-groups/) commands return WireGuard configurations. It also wraps up the changes shipped since 11.3: log drain commands moved to API v4, and a new command gets the details of a single region.

## WireGuard configurations

`GetNetworkGroupWireguardConfigurationCommand` now requests the configuration as `text/plain` and returns it as a string, ready to write to a `.conf` file. It used to return an object holding the configuration with peer metadata, so code reading its `configuration` field must use the output directly. Release 11.5 also adds `GetNetworkGroupWireguardConfigurationUrlCommand`, which returns a pre-signed URL to download the configuration of a peer without authenticating.

## Log drains on API v4

Since 11.4.1, the [log drain](/doc/observability/drains/) commands call the API v4 endpoints. `EnableLogDrainCommand` and `DisableLogDrainCommand` replace `UpdateLogDrainCommand` and its `state` field. A drain now exposes its `status`, the `execution` status of its forwarding with the last error met, and its `backlog`. `ListLogDrainCommand` filters drains on these statuses, and these commands accept an application ID only.

## Regions

`GetZoneCommand`, added in 11.4, returns a single deployment region from its name. Pass an `ownerId` to get a region available to a specific organisation only.

## How to upgrade

Update `@clevercloud/client` in your project:

```bash
npm install @clevercloud/client@12.0.0
```
