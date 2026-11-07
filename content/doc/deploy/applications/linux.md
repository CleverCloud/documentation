---
type: docs
linkTitle: Linux
title: Linux application runtime
description: Build and deploy any application on Clever Cloud with the Linux runtime, the tools Mise installs, and your own build and start commands
keywords:
- linux app hosting
- linux cloud
- mise package manager
- mise deployment
- versatile
- flexible runtime
- makefile
aliases:
- /doc/applications/linux
- /doc/deploy/application/other
- /doc/deploy/not-supported
---

## Overview

The Linux runtime deploys any application: you choose the tools it needs, and the commands that build and start it. [Mise](/doc/manage/mise/) installs these tools, such as Crystal, Dart, Gleam, Nim, Zig, or Deno, then Clever Cloud runs your commands.

Use it for a language without a dedicated runtime, for a self-hosted software, or to control each step of your deployment.

## Create your Linux application

To create a new Linux application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type linux
```

- [Learn more about Clever Tools](/doc/tools/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

## Configure your Linux application

### Mandatory needs

A Linux application needs:

- A start command, set in `CC_RUN_COMMAND`, in a `run` task of Mise, or in a `run` target of a Makefile
- A web server listening on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port)

A build command is optional, and a [Clever Task](#linux-applications-as-clever-tasks) doesn't need a web server.

[Mise](https://mise.jdx.dev) reads a `mise.toml` file at the root of your project. Its `[tools]` section lists the tools to install and their versions, and its `[tasks]` section names the commands of your project. For instance, a [Crystal](https://crystal-lang.org) web server, compiled into a `server` executable:

```toml {filename="mise.toml"}
[tools]
crystal = "1.22"

[tasks.build]
run = "crystal build --release main.cr -o server"

[tasks.run]
run = "./server"
```

```crystal {filename="main.cr"}
require "http/server"

port = ENV.fetch("PORT", "8080").to_i

server = HTTP::Server.new do |context|
  context.response.print "Hello from Linux on Clever Cloud"
end

server.bind_tcp("0.0.0.0", port)
server.listen
```

To try it locally, run `mise trust` and `mise install`, then `mise run build` and `mise run run`, and open `http://localhost:8080`.

- [Deploy a Dart application with Mise](https://github.com/CleverCloud/dart-with-mise-example)
- [Deploy a Swift application with Mise](https://github.com/CleverCloud/swift-hello-world-example)
- [Deploy a Zig application with Mise](https://github.com/CleverCloud/zig-with-mise-example)

### Build and run commands

Clever Cloud looks for the build command and the start command separately, in this order:

1. `CC_BUILD_COMMAND` and `CC_RUN_COMMAND`
2. The `build` and `run` [tasks of Mise](https://mise.jdx.dev/tasks/), in `mise.toml` or in [file tasks](https://mise.jdx.dev/tasks/file-tasks.html)
3. The `build:` and `run:` targets of a Makefile

Each source only fills in the commands that a previous one doesn't define. For instance, you can set `CC_BUILD_COMMAND` only, and let a `run` task of Mise or a `run` target of a Makefile provide the start command.

Clever Cloud looks for these files at the root of your repository, even with `APP_FOLDER`, before the pre-build [hook](/doc/manage/build-hooks/): a hook can't create them. It runs the Mise tasks from the folder of `mise.toml`, which `CC_MISE_FILE_PATH` can move. For the Makefile, it uses the first file it finds among:

- The file set in `CC_MAKEFILE`
- `GNUmakefile`, `Makefile`, then `makefile`

It checks each target with `make --dry-run`, and ignores the ones that fail. Without a start command, the deployment fails with `You must define a CC_RUN_COMMAND or a 'run' task with Makefile or Mise`.

### Build phase

Before an instance starts, Mise installs the tools of `mise.toml`. On a new build, Clever Cloud then runs the pre-build hook, the build command, and the post-build hook. `CC_BUILD_COMMAND` and the Makefile targets run from the root of your project, or from the folder set in `APP_FOLDER`.

### Start command

A `run` target of a Makefile runs from the root of your project, or from the folder set in `APP_FOLDER`. A Mise task runs from the folder of `mise.toml`. `CC_RUN_COMMAND` runs from the root of the repository, through a shell: it reads variables such as `$PORT`.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit, with your whole repository. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

Mise installs the tools again on each restart, even from the cache. With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps the files Mise downloads between commits, in the `~/.cache/mise` folder.

## Linux applications as Clever Tasks

A Linux application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration: Clever Cloud builds it, then runs `CC_RUN_COMMAND`.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks), here for a `report` task you define in `mise.toml`:

```bash
clever create --type linux --task "mise run report"
clever deploy # or clever restart if there is no code change
```

## Expand your toolbox with Mise package manager

{{% content "mise" %}}

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/mise" title="Mise Package Manager" subtitle="Install tools, map add-on credentials, and define tasks in one file" icon="cube" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
