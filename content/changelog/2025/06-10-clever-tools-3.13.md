---
date: 2025-06-10
title: 'Clever Tools 3.13: emails, operators, SSH keys, better UX'
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
description: Manage more things in a better way
excludeSearch: true
---

[Clever Tools 3.13](https://github.com/CleverCloud/clever-tools/releases/tag/3.13.0) is available. It includes some bug fixes and a new interface for application management commands. Our goal here is to start making Clever Tools more user-friendly with more useful information, tips and a better look. It paves the way for next major releases. [Let us know what you think](https://github.com/CleverCloud/clever-tools/issues) about it to help us to design the future of Clever Tools.

The `clever tokens` command is not experimental anymore, as [API tokens are now available](/developers/changelog/2025/06-05-api-tokens-console-tips/) through the Clever Cloud Console.

![New clever create command](/images/changelog/clever-tools-new-create.webp)

## Operators

The `operators` experimental feature adds direct commands for services deployed and managed through our Operators, such as Keycloak, Matomo, Metabase and Otoroshi. You can now get useful information about these services once deployed, restart, rebuild or update them, open their dashboard or web management interface, activate features such as Network Groups, etc.

```bash
clever features enable operators

clever keycloak get myKeycloak
clever keycloak enable-ng myKeycloak

clever matomo open webui myMatomo
clever metabase rebuild metabase_id
clever otoroshi version update otoroshi_id
```

- [Learn more about Operators commands in Clever Tools](/developers/doc/cli/operators/)

![Check Metabase Version command](/images/changelog/clever-tools-metabase-version-check.webp)

## Emails and public SSH keys

Manage your Clever Cloud account's emails and public SSH keys with the new `clever emails` and `clever ssh-keys` commands:

```
clever emails
clever ssh-keys -F json

clever emails add email@example.com
clever emails primary email@example.com
clever ssh-keys add myNewPublicKey ~/.ssh/id_ecdsa.pub

clever emails remove-all
clever ssh-keys remove-all
```

- [Learn more about emails and ssh-keys commands in Clever Tools](/developers/doc/cli/#emails)

## Application configuration as Clever Task

You can also use `clever config` to set an application as a [Clever Task](/developers/doc/develop/tasks/) after its creation of get this option configuration:

```
clever config get task
clever config set task true
clever config set task false
clever config update --name "My new task name" --enable-task
```

- [Learn more about config command in Clever Tools](/developers/doc/cli/applications/configuration/)

## How to upgrade

To upgrade Clever Tools, [use your favorite package manager](/developers/doc/cli/install/). For example with `npm`:

```
npm update -g clever-tools
clever version
```
