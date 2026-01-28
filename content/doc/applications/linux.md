---
type: docs
linkTitle: Linux
title: Linux application runtime
description: Build and deploy any application with Mise and your favorite tools on Clever Cloud using flexible Linux runtime environment
keywords:
- linux app hosting
- linux cloud
- mise package manager
- mise deployment
- versatile
- flexible runtime
- makefile
aliases:
- /doc/deploy/application/other
- /doc/deploy/not-supported
---

## Overview

Clever Cloud platform provides a multi-runtime environment, including many tools to deploy and run your applications. The Linux runtime is a versatile solution to build and deploy any kind of application. The Mise package manager helps you to install and manage any supported dependencies Clever Cloud doesn't provide by default such as Dart, Gleam, Zig for example.

> [!NOTE] Linux is a new runtime
> Help us to improve it by reporting any issue or suggestion on the [Clever Cloud Community](https://github.com/CleverCloud/Community/discussions/categories/paas-runtimes)

## Create your Linux application

To create a new Linux application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type linux
```
- [Learn more about Clever Tools](/doc/cli/)
- [Learn more about Clever Cloud application deployment](/doc/quickstart/#create-an-application-step-by-step)

## Configure your Linux application

### Mandatory needs

Linux runtime requires a run command (through `CC_RUN_COMMAND`, a Mise `run` task, or a Makefile `run:` target) and a working web application listening on `0.0.0.0:8080`.

- [Learn more about environment variables on Clever Cloud](/doc/reference/reference-environment-variables/)

### Build and run commands

Build and run commands are resolved in this priority order:

1. `CC_BUILD_COMMAND` and `CC_RUN_COMMAND` environment variables
2. [Mise](https://mise.jdx.dev/tasks/) `build` and `run` tasks (from `mise.toml` or [File Tasks](https://mise.jdx.dev/tasks/#tasks-in-mise-toml-files))
3. Makefile `build:` and `run:` targets (searches `GNUmakefile`, `Makefile`, `makefile` or the file defined in `CC_MAKEFILE`)

Each level fills in only the commands not already defined by a higher priority source. For example, you can define `CC_BUILD_COMMAND` and let Mise or a Makefile provide the `run` command.

- [Learn more about Deployment hooks](/doc/develop/build-hooks/)

## Clever Task and Multi-runtime approach

Linux runtime is perfect fit to run on-demand workloads on Clever Cloud: configure an application as Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/cli/applications/#tasks):

```bash
clever create --type linux --task "your-task-command --and arguments"
clever deploy # or clever restart if there is no code change
```

- [Learn more about Clever Tasks](/doc/develop/tasks/)

## Expand your toolbox with Mise package manager

{{% content "mise" %}}

### Mise configuration examples

- [Deploy a Dart application with Mise](https://github.com/CleverCloud/dart-with-mise-example)
- [Deploy a Swift application with Mise](https://github.com/CleverCloud/swift-hello-world-example)
- [Deploy a Zig application with Mise](https://github.com/CleverCloud/zig-with-mise-example)

{{% content "url_healthcheck" %}}
{{% content "request-flow" %}}
