---
title: "Clever Tools 5.1: instances listing, SSH to a given instance and access logs drains"
date: 2026-10-02
description: Clever Tools 5.1 lists the instances of an application, connects through SSH to a given instance, including build instances, and forwards access logs to drains
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

[Clever Tools 5.1.0](https://github.com/CleverCloud/clever-tools/releases/tag/5.1.0) is available. It adds a command to list the instances of an application, lets `clever ssh` target a given instance without any prompt, and creates drains that forward access logs.

## List the instances of an application

`clever instances` lists the running instances of an application, with their creation date, state, number, flavor, ID and deployment ID. Add `--all` to include instances in any state, including deleted ones. You can also select the instances that existed during a period with `--after` and `--before`, or the ones created by a deployment with `--deployment-id`, whatever their state. It lists up to 100 instances by default, and up to 1,000 with `--limit`:

```bash
clever instances
clever instances --all
clever instances --after 1d --format json
```

## SSH to a given instance

`clever ssh` gets an `--instance` option, which accepts an instance ID, an instance number or `any`. It skips the interactive selection, so you can now run commands through SSH from a script or a CI job, even when your application runs several instances:

```bash
clever ssh --instance 0 --command hostname
clever ssh --instance any --command hostname
```

During a rolling deployment, the instance going away and the one replacing it share the same number: Clever Tools prefers the one that is `UP`. Build instances are now part of the selection: they show up as `build` in the output of `clever instances`, and you can use their ID to connect to them and inspect a running build:

```bash
clever ssh --instance INSTANCE_ID
```

## Access logs drains

Every `clever drain create` subcommand accepts a `--kind` option. Set it to `ACCESSLOG` to forward the access logs of an application, instead of its output. `LOG` remains the default, and `clever drain` and `clever drain get` now display the kind of each drain:

```bash
clever drain create raw-http https://logs.example.com/clever-cloud --kind ACCESSLOG
```

## Other changes

The `--after` and `--before` options of `clever logs`, `clever accesslogs` and `clever instances` now accept a plain number of seconds as a duration, and so does `--expiration` in `clever tokens create`. Commands managing Kubernetes clusters, Materia KV, Network Groups and operators, such as `clever keycloak`, now report an ambiguous name like other commands do, with the list of matching resources to pick one by ID. The Docker image now includes `git`, required since system Git became the default backend in [Clever Tools 5.0](/changelog/2026/09-11-clever-tools-5.0/).

## How to upgrade

To upgrade Clever Tools, follow the [update guide](/doc/manage/cli/install/update/) for the installation method you use. For example with `npm`:

```bash
npm install -g clever-tools
clever version
```

- [Learn more about SSH access with Clever Tools](/doc/manage/cli/applications/deployment-lifecycle/#ssh)
- [Learn more about logs drains](/doc/manage/cli/logs-drains/#access-logs-drains)
