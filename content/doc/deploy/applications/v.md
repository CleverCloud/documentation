---
type: docs
linkTitle: V (Vlang)
title: V (Vlang) application runtime
description: Build and deploy V (Vlang) applications on Clever Cloud, from a Veb web server to V scripts run as Tasks
keywords:
- vlang
- v app hosting
- programming
- language
- web-server
- veb
aliases:
- /doc/applications/v
---

## Overview

[V](https://vlang.io) is a statically typed, compiled language, with a syntax close to Go. Its [standard library](https://modules.vlang.io/) includes a web framework, [Veb](https://modules.vlang.io/veb.html), and its package manager installs other modules. Clever Cloud installs the dependencies of your project, compiles it, then starts the executable it builds.

## Create your V (Vlang) application

To create a new V (Vlang) application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type v
```

- [Learn more about Clever Tools](/doc/tools/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

## Configure your V (Vlang) application

### Mandatory needs

A V application needs:

- A program with a `main` function, at the root of the project or of the folder set in `APP_FOLDER`
- A web server listening on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port), except for a [Clever Task](#v-vlang-applications-as-clever-tasks)

Clever Cloud compiles the `.v` files of this folder into one program. For instance, a minimal [Veb](https://modules.vlang.io/veb.html) application:

```v {filename="main.v"}
module main

import os
import veb

pub struct Context {
    veb.Context
}

pub struct App {}

pub fn (app &App) index(mut ctx Context) veb.Result {
    return ctx.text('Hello from V on Clever Cloud')
}

fn main() {
    port := os.getenv_opt('PORT') or { '8080' }.int()
    mut app := &App{}
    veb.run_at[App, Context](mut app, host: '0.0.0.0', port: port, family: .ip) or { panic(err) }
}
```

To try it locally, run `v run .`, then open `http://localhost:8080`.

- [Deploy an example V application on Clever Cloud](https://github.com/CleverCloud/v-example)

### Dependencies

A `v.mod` file describes your project as a module. Its `dependencies` list the modules to install, here [`markdown`](https://github.com/vlang/markdown):

```v {filename="v.mod"}
Module {
    name: 'hello'
    description: 'A V web server on Clever Cloud'
    version: '0.1.0'
    license: 'MIT'
    dependencies: ['markdown']
}
```

If your project has a `v.mod` file, Clever Cloud installs these modules with `v install`, in the folder set in `VMODULES`, `~/.vmodules` by default. A project that only uses the standard library doesn't need this file.

### Build phase

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/), installs the dependencies, then compiles your project in production mode, with `v . -prod`, and the path of the executable in its `-output` option.

`-prod` optimizes the executable, which takes longer to compile. With `ENVIRONMENT=development`, Clever Cloud compiles without it, faster. The executable is `v_bin_<application ID>`, at the root of the repository: set another path in `CC_V_BINARY`.

### V (Vlang) version

Clever Cloud deploys V `{{< runtime_version v >}}`.

### Start command

Clever Cloud starts the executable from the root of your project, or from the folder set in `APP_FOLDER`. With `CC_RUN_COMMAND`, it runs your own command instead, through a shell, from the root of the repository.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit, with the executable. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps the modules of the `VMODULES` folder between commits.

## V (Vlang) applications as Clever Tasks

A V application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration: Clever Cloud compiles your project, then runs `CC_RUN_COMMAND`, from the root of the repository. The project must compile, even if the Task runs another command.

A Task can run a [V script](https://docs.vlang.io/other-v-features.html#cross-platform-shell-scripts-in-v), a `.vsh` file that V compiles and runs in one step. Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks), here for a `scripts/report.vsh` script:

```bash
clever create --type v --task "v run scripts/report.vsh"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
