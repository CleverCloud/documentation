---
title: "Clever Tools 5.5: organisations and members management, rebuild command"
date: 2026-11-19
description: Clever Tools 5.5 adds commands to manage organisations and their members, and clever rebuild to redeploy without the build cache
tags:
  - clever-tools
  - cli
authors:
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Tools 5.5.0](https://github.com/CleverCloud/clever-tools/releases/tag/5.5.0) is available. It adds the `clever orgs` and `clever members` commands, to manage your organisations and their members from a terminal, and `clever rebuild`, which redeploys an application without its build cache.

## Manage organisations

`clever orgs list` shows your organisations, your Personal Space first, with their ID and your role in each. `clever orgs get` details one of them: its description, its number of members and admins, its billing information, and its support level. Target an organisation by its ID or its exact name, and add `--format json` to use the result in a script:

```bash
clever orgs list
clever orgs get my-organisation
clever orgs get my-organisation --format json | jq -r '.billingEmail'
```

`clever orgs update` changes the name, the description, and the billing details of an organisation. Only the options you give change. An empty value clears a field, but the name and the description can't be empty. A value-added tax (VAT) number requires a company:

```bash
clever orgs update my-organisation --billing-email billing@example.com
clever orgs update my-organisation --company "My Company" --vat-number FR12345678901
clever orgs update my-organisation --company "" --vat-number ""
```

Without any option, in a terminal, the command asks for each field: press Enter to keep its value, or type `-` to clear it.

## Manage members

`clever members list` shows the members of an organisation with their role, name, email, ID, and whether they enabled two-factor authentication (2FA). Filter them with `--role`, or with `--without-2fa` to find the accounts to secure:

```bash
clever members list my-organisation
clever members list my-organisation --without-2fa --format json | jq -r '.[].email'
```

Invite someone by email with a role: `admin`, `manager`, `developer`, or `accounting` for the Accountant role. Then change their role or remove them, by email or by ID. `clever members remove` asks for confirmation, which `--yes` skips. To leave an organisation, remove yourself:

```bash
clever members invite my-organisation giulia.rossi@example.com --role developer
clever members update my-organisation giulia.rossi@example.com --role manager
clever members remove my-organisation giulia.rossi@example.com
```

Inviting, updating, and removing other members require the Admin or Manager role, and a Manager only assigns the Manager and Developer roles. Any member can leave, except the last admin of an organisation. Your Personal Space has no members, so these commands refuse it.

## New `rebuild` command

`clever rebuild` redeploys an application without its build cache, as `clever restart --without-cache` does, with the other options of `clever restart`. It uses the commit the application already has on Clever Cloud, or the one you give with `--commit`, not your local changes:

```bash
clever rebuild
clever rebuild --app my-application --quiet
```

## Other changes

`clever logout --alias` no longer announces a profile switch when `CLEVER_TOKEN` and `CLEVER_SECRET` define the active profile.

## How to upgrade

To upgrade Clever Tools, follow the [update guide](/doc/tools/cli/install/update/) for the installation method you use. For example with `npm`:

```bash
npm install -g clever-tools
clever version
```

- [Learn more about organisations and members in Clever Tools](/doc/tools/cli/organisations/)
- [Learn more about the roles of an organisation](/doc/security/iam-roles/#roles-and-privileges)
