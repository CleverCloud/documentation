---
title: "Clever Tools 4.8: OAuth consumers and drains for add-ons"
date: 2026-04-09
description: Clever Tools 4.8 introduces commands to manage OAuth consumers and extends drain management to add-ons
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
excludeSearch: true
---

[Clever Tools 4.8.0](https://github.com/CleverCloud/clever-tools/releases/tag/4.8.0) is available. This release adds a new `oauth-consumers` command set to manage OAuth consumers from the CLI and extends `clever drain` to operate on add-ons.

## OAuth consumers management

You can now create and manage [OAuth consumers](/api/howto/#create-an-oauth-consumer) directly from the CLI. The new `clever oauth-consumers` command set covers the full lifecycle: list, create, get details, update, open in the Console and delete. Consumers can be referenced by name (when unambiguous) or by their consumer key, and the `get` command supports a `--with-secret` flag when you need to retrieve the consumer secret for application configuration.

```bash
# List OAuth consumers
clever oauth-consumers list

# Create a new consumer with rights and callback URL
clever oauth-consumers create my-app \
  --description "My application" \
  --url https://my-app.example.com \
  --base-url https://my-app.example.com/oauth/callback \
  --rights access-personal-information,access-organisations

# Get details, including the secret
clever oauth-consumers get my-app --with-secret

# Update an existing consumer
clever oauth-consumers update my-app --description "Updated description"

# Open the consumer page in the Console
clever oauth-consumers open my-app

# Delete a consumer
clever oauth-consumers delete my-app --yes
```

These commands target the current profile's organisation by default. The `create` command accepts the `--org` option to specify the consumer's organisation. For other commands, the consumer key is enough to identify the resource.

- [Learn more about OAuth consumers](/api/howto/#create-an-oauth-consumer)

## Drains on add-ons

The `clever drain` commands now accept an `--addon` option to manage [log drains](/doc/administrate/log-management/) on add-ons, in addition to applications. All drain subcommands (`create`, `enable`, `disable`, `get`, `remove` and the top-level listing) accept this new option, which resolves either an add-on ID or its real ID. The `--addon` option is mutually exclusive with `--app` and `--alias`.

```bash
# List drains on an add-on
clever drain --addon postgresql_xxxxxxxx

# Create a drain on an add-on
clever drain create --addon postgresql_xxxxxxxx raw-http https://logs.example.com

# Get a specific drain
clever drain get --addon postgresql_xxxxxxxx <DRAIN-ID>

# Remove a drain
clever drain remove --addon postgresql_xxxxxxxx <DRAIN-ID>
```

## Bug fixes

- **Network groups** commands have been adapted to the `@clevercloud/client` v12 API change for peer configuration, restoring proper peer handling.

## How to upgrade

To upgrade Clever Tools, [use your favourite package manager](/doc/cli/install/). For example with `npm`:

```
npm update -g clever-tools
clever version
```
