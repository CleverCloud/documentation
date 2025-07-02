---
type: docs
linkTitle: V (Vlang)
title: V (Vlang) application runtime
description: Build and deploy your V (Vlang) based API and applications
type: docs
---

## Overview

[V](https://vlang.io) is a very simple modern language, similar to Go. It's a statically typed compiled programming language designed for building maintainable software. Its design has also been influenced by Oberon, Rust, Swift, Kotlin, and Python. One of its forces is it comes with [a strong standard library](https://modules.vlang.io/), built-in modules and a package manager. Thus, it includes a web server easy to use in V applications : [Veb](https://modules.vlang.io/veb.html).

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

V (Vlang) runtime only requires a working application listening on `0.0.0.0:8080`.

* [Learn more about environment variables on Clever Cloud](/developers/doc/reference/reference-environment-variables/)

### Build phase

During the build phase, the V (Vlang) application is built with the `v . -prod` command. To compile without the `-prod` flag, set `ENVIRONMENT=development`. You can choose a custom output binary name with the `CC_V_BINARY` environment variable, default is `${APP_HOME}/v_bin_${APP_ID}`.

- [Deploy an example V application on Clever Cloud](https://github.com/CleverCloud/v-example)

### V (Vlang) version and tools

The currently deployed version of V (Vlang) on Clever Cloud is `0.4.11`.

## V scripts (.vsh), Clever Tasks

V (Vlang) can be used to execute [shell scripts (.vsh)](https://docs.vlang.io/other-v-features.html#cross-platform-shell-scripts-in-v). On Clever Cloud, to run such workloads as Clever Tasks, configure an application as Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/developers/doc/cli/applications/#tasks):

```bash
clever create --type v --task "./your-script.vsh --and arguments"
clever deploy # or clever restart if there is no code change
```

- [Learn more about Clever Tasks](/developers/doc/develop/tasks/)

{{< content "redirectionio" >}}
{{< content "varnish" >}}
