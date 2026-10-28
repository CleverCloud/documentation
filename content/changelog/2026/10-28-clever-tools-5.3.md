---
title: "Clever Tools 5.3: drain list command, Sekoia.io support and Terraform import blocks"
date: 2026-10-28
description: Clever Tools 5.3 adds the clever drain list command, creates Sekoia.io drains, removes ANSI codes from logs and generates Terraform import blocks
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

[Clever Tools 5.3.0](https://github.com/CleverCloud/clever-tools/releases/tag/5.3.0) is available. It adds the `clever drain list` command, forwards logs to Sekoia.io, cleans ANSI codes from logs and generates Terraform `import` blocks for your existing resources.

## New `drain list` command

`clever drain list` lists the drains of every application and add-on of your organisations, grouped by organisation, with the resource each drain belongs to. Target a single organisation with `--org` and filter by type with `--type`. With `--format json`, each drain carries the ID and name of its organisation:

```bash
clever drain list
clever drain list --org my-organisation --type datadog
```

`clever drain` and `clever drain list` now display drains in a bordered table. A single `STATUS` column combines the status of the drain and of its execution, and the recipient appears as `TARGET URL`.

## Sekoia.io drains

`clever drain create sekoia` forwards logs to the `/jsons` endpoint of a [Sekoia.io](https://docs.sekoia.com/integration/ingestion_methods/https/overview/) HTTPS intake. The drain sends the intake key in a header, never in the URL. For a self-hosted intake behind a private certificate authority, add `--tls-verification trustful`, which skips certificate and hostname verification:

```bash
clever drain create sekoia https://intake.sekoia.io/jsons --intake-key "$SEKOIA_INTAKE_KEY"
```

Sekoia.io has no built-in intake format for Clever Cloud logs: create the intake with a custom format that parses the fields of the forwarded logs.

## ANSI codes and colors in logs

`clever logs` gets a `--strip-ansi` option, which removes the ANSI codes contained in log messages, in any output format. In the `human` format, Clever Tools also removes them when colors are disabled. Clever Tools disables colors when its output isn't a terminal, so add `--color true` to keep them in a pager:

```bash
clever logs --since 1h --until now --format json --strip-ansi > logs.json
clever logs --since 15m --until now --color true | less -R
```

`--color`, `FORCE_COLOR` and `NO_COLOR` now apply consistently, including when the output isn't a terminal and with the `--color=false` syntax. `FORCE_COLOR=0` also disables the colors of the update notifier.

## Generate Terraform import blocks

`clever terraform generate` writes the `import` blocks of the applications and add-ons of your personal space or of an organisation, ready for the [Terraform provider](/doc/tools/terraform/). Filter them with `--app` or `--tag`. The command skips the resources it identifies as managed by another add-on, such as the Kibana application of an Elasticsearch add-on. It's an experimental feature, so enable it first:

```bash
clever features enable terraform
clever terraform generate --org my-organisation > imports.tf
terraform plan -generate-config-out=generated.tf
```

## Other changes

The standalone binaries now embed Node.js 24.22.1, a security release, and Clever Tools updates its `simple-git`, `undici` and `zod` dependencies. `clever env import-vars` now accepts a comma-separated list of names, instead of reading its input character by character. `clever deploy` no longer crashes when you combine `--quiet` with `--exit-on never`.

## How to upgrade

To upgrade Clever Tools, follow the [update guide](/doc/manage/cli/install/update/) for the installation method you use. For example with `npm`:

```bash
npm install -g clever-tools
clever version
```

- [Learn more about logs drains](/doc/manage/cli/logs-drains/)
- [Learn more about the Terraform provider](/doc/tools/terraform/)
