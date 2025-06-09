---
type: docs
linkTitle: V (Vlang)
title: V (Vlang) application runtime
description: Build and deploy your V (Vlang) based API and applications
type: docs
---

## Overview

> [!NOTE] V (Vlang) is a new runtime. Help us to improve it by reporting any issue or suggestion on the [Clever Cloud Community](https://github.com/CleverCloud/Community/discussions/categories/paas-runtimes)

## Create your V (Vlang) application

To create a new V (Vlang) application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type v
```
* [Learn more about Clever Tools](/developers/doc/cli/)
* [Learn more about Clever Cloud application deployment](/developers/doc/quickstart/#create-an-application-step-by-step)

## Configure your V (Vlang) application

### Mandatory needs

V (Vlang) runtime only requires a working web application listening on `0.0.0.0:8080`.

* [Learn more about environment variables on Clever Cloud](/developers/doc/reference/reference-environment-variables/)

### Build phase

During the build phase, the V (Vlang) application is built with the `v . -prod` command. You can compile without the `-prod` flag by setting `ENVIRONMENT=development`. You can set a custom output binary name with the `CC_V_BINARY` environment variable, default is `$APP_HOME/v_bin_appId`.

### Cache dependencies

Modules in `~/.vmodules/` are added to the dependencies cache. If `VMODULES` is set, it's used as cache dependencies directory.

### V (Vlang) version and tools

The currently deployed version of V (Vlang) on Clever Cloud is `0.4.10`.

## Vshell, Clever Tasks

