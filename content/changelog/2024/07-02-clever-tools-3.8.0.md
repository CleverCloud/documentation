---
title: 'Clever Tools 3.8: "Big Summer Update" is available'
date: 2024-07-02
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
description: Better manage your apps, lots of new features
aliases:
- /changelog/2024-07-02-clever-tools-3.8.0
excludeSearch: true
---

[Clever Tools 3.8](https://github.com/CleverCloud/clever-tools/releases/tag/3.8.0) is now available. It's an important release, as we've worked on some of its features for several weeks.

## Brand new application management

It introduces a complete new way to use our CLI with `--app` option, available to every application-related commands. It allows you to target any application available from your account, by its ID or its name. You can for example restart an application this way:

```bash
clever restart --app app_id
clever restart --app my_app_name
clever restart --app my_app_name --org my_org_name
```
`clever applications list` new command can be used from any folder of your system. It prints details about applications across your organisations. You can filter the result with `--org` or `-o` option. It includes IDs, names and local aliases (if available) in a table.

## More (consistent) options

For most commands, you can now get a result in the format of your choice with `--format` or `-F` option. In most cases, you can use `human` (default) or `json`, but sometimes `json-stream` or `shell` are available too (for example).

You can now define when to stop logs streaming during a `clever deploy` or a `clever restart` with `exit-on` option. Available values are: `deploy-start`, `deploy-end` and `never` (default: `deploy-end`). Thus, the `--follow` option is now deprecated.

Of course, you can combine these new options:

```bash
# We show ID and name of all applications in JSON format
clever applications list --org my_org_name --format json | jq '.[].applications[] | {app_id, name}'

# We check status of an application
clever status --app app_id_or_name -F json | jq '.status'

# If it's running, we restart it and stop the logs streaming when the deployment starts
clever restart --app app_id_or_name --exit-on deploy-start
```

These changes are available thanks to a `cliparse` update [introducing private options](https://github.com/CleverCloud/cliparse-node/commit/023bd72ddce66337c5b0716ddb3c2a103ff252a8).

## Lots of new features

Multiple new features are also available in this "Big Summer Update". Access Logs feature now uses `v4` API. It's faster and more reliable, only available for applications and as an alpha test for now. It's available through `clever accesslogs` command.

`--no-color` or `--color true|false` global option is available. It's used by default when the output is not a terminal. `clever console` now opens the [Console](https://console.clever-cloud.com) even if your not in a folder with a linked application. [3.8.1 release](https://github.com/CleverCloud/clever-tools/releases/tag/3.8.1) comes with some minor fixes.

To upgrade Clever Tools, [use your favorite package manager](/developers/doc/cli/install)

```
npm update -g clever-tools
clever version
```

Note that we reintroduced [Nix support](/developers/doc/cli/install/#nix-package-manager) with this release.
