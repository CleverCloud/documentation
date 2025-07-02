---
type: docs
linkTitle: Linux
title: Linux application runtime
description: Build and deploy any application with Mise and your favorite tools
type: docs
---

## Overview

Clever Cloud platform provides a multi-runtime environment, including many tools to deploy and run your applications. The Linux runtime is a versatile solution to build and deploy any kind of application. The Mise package manager helps you to install and manage any supported dependencies Clever Cloud doesn't provide by default such as Dart, Gleam, Zig for example.

> [!NOTE] Linux is a new runtime. Help us to improve it by reporting any issue or suggestion on the [Clever Cloud Community](https://github.com/CleverCloud/Community/discussions/categories/paas-runtimes)

## Create your Linux application

To create a new Linux application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type linux
```
* [Learn more about Clever Tools](/developers/doc/cli/)
* [Learn more about Clever Cloud application deployment](/developers/doc/quickstart/#create-an-application-step-by-step)

## Configure your Linux application

### Mandatory needs

Linux runtime only requires a `CC_RUN_COMMAND` to execute, with a working web application listening on `0.0.0.0:8080`.

* [Learn more about environment variables on Clever Cloud](/developers/doc/reference/reference-environment-variables/)

### Build phase

During the build phase, Clever Cloud will run the `CC_BUILD_COMMAND` if provided. You can use it to install dependencies, compile your code, or any other task you need to perform before running your application.

- [Learn more about Deployment hooks](/developers/doc/develop/build-hooks/)

>[!TIP] Use Mise package manager to define build/run commands
> If you define `build` and `run` tasks in the `mise.toml` file [or as File Tasks](https://mise.jdx.dev/tasks/#tasks-in-mise-toml-files), Clever Cloud will automatically use them. `CC_BUILD_COMMAND` and `CC_RUN_COMMAND` have precedence over the `build` and `run` tasks defined by Mise.

## Clever Task and Multi-runtime approach

Linux runtime is perfect fit to run on-demand workloads on Clever Cloud: configure an application as Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/developers/doc/cli/applications/#tasks):

```bash
clever create --type linux --task "your-task-command --and arguments"
clever deploy # or clever restart if there is no code change
```

- [Learn more about Clever Tasks](/developers/doc/develop/tasks/)

## Expand your toolbox with Mise package manager

{{< content "mise" >}}

### Mise configuration examples

- [Deploy a Dart application with Mise](https://github.com/CleverCloud/dart-with-mise-example)
- [Deploy a Swift application with Mise](https://github.com/CleverCloud/swift-hello-world-example)
- [Deploy a Zig application with Mise](https://github.com/CleverCloud/zig-with-mise-example)

{{< content "redirectionio" >}}
{{< content "varnish" >}}
