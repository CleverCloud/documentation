---
type: docs
linkTitle: Linux
title: Linux application runtime
description: Build and deploy any application with Mise and your favorite tools
type: docs
---

## Overview

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

## Clever Task and Multi-runtime strategy


## Expand your toolbox with Mise package manager

{{% content/mise %}}

- [Deploy a Dart application with Mise and Linux runtime]()
- [Deploy a Zig application with Mise and Linux runtime]()
