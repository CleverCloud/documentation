---
type: docs
linkTitle: Haskell
title: Haskell application runtime
description: Build and deploy Haskell applications on Clever Cloud with Stack, from a single executable to a project with several packages
keywords:
- cabal
- ghc
- haskell
- haskell app hosting
- scotty
- servant
- stack
- yesod
aliases:
- /doc/applications/haskell
- /doc/deploy/application/haskell
- /doc/deploy/application/haskell/haskell
- /doc/getting-started/by-language/haskell
- /doc/haskell
- /doc/haskell-hosting
- /doc/haskell/haskell
- /doc/partials/language-specific-deploy/haskell
- /haskell
---

## Overview

[Haskell](https://www.haskell.org) is a purely functional, statically typed language. Clever Cloud builds your [Stack](https://docs.haskellstack.org) project and starts the executable it installs. It works with web frameworks such as [Scotty](https://hackage.haskell.org/package/scotty), [Servant](https://haskell-servant.github.io), or [Yesod](https://www.yesodweb.com).

## Create your Haskell application

To create a new Haskell application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type haskell
```

- [Learn more about Clever Tools](/doc/tools/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

## Configure your Haskell application

### Mandatory needs

A Haskell application needs:

- A `stack.yaml` file, at the root of the project or of the folder set in `APP_FOLDER`
- A package described in a `.cabal` or a `package.yaml` file, with one executable
- A web server listening on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port)

[Stack](https://docs.haskellstack.org) is a Haskell build tool. In `stack.yaml`, the [snapshot](https://docs.haskellstack.org/en/stable/configure/yaml/project/#snapshot) sets the version of GHC, the compiler, and a set of libraries that build together. `packages` lists the folders of your packages, `.` for the current one.

Each package has a `.cabal` file, which lists its executables and their dependencies. A [Clever Task](#haskell-applications-as-clever-tasks) doesn't need a web server.

For instance, a minimal [Scotty](https://hackage.haskell.org/package/scotty) application:

```yaml {filename="stack.yaml"}
snapshot: lts-22.34
packages:
- .
```

```text {filename="hello.cabal"}
cabal-version: 2.4
name:          hello
version:       0.1.0

executable hello
    main-is:          Main.hs
    build-depends:    base, scotty
    default-language: Haskell2010
```

```haskell {filename="Main.hs"}
{-# LANGUAGE OverloadedStrings #-}

import System.Environment (lookupEnv)
import Web.Scotty

main :: IO ()
main = do
  port <- maybe 8080 read <$> lookupEnv "PORT"
  scotty port $ get "/" $ text "Hello from Haskell on Clever Cloud"
```

Scotty listens on every interface. Your application reads its [environment variables](/doc/manage/environment-variables/) with `lookupEnv` or `getEnv`, from `System.Environment`, such as the credentials of the add-ons you link to it.

### Build phase

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/). Stack then installs GHC, and builds your dependencies and your project:

```bash
stack setup
stack install --only-dependencies
stack install
```

`stack install` copies the executables of your project to `~/.local/bin`, which is in the `PATH`. To replace one of these commands, set `CC_HASKELL_STACK_SETUP_COMMAND`, `CC_HASKELL_STACK_INSTALL_DEPENDENCIES_COMMAND`, or `CC_HASKELL_STACK_INSTALL_COMMAND`. Clever Cloud splits their value on spaces and runs it without a shell.

The first build compiles every dependency from source: around twenty minutes for a small Scotty application. Enable the [dependencies cache](#caches) to keep them between commits, so that the next builds take a few minutes.

If a build fails for lack of memory, enable a [dedicated build instance](/doc/manage/#dedicated-build-instance), larger than your application instances:

```bash
clever scale --build-flavor M
```

### Build a single package

In a project with several packages, `stack install` builds all of them. To build only one, and the packages it depends on, set its name, from its `.cabal` file, in `CC_HASKELL_STACK_TARGET`. Clever Cloud adds it to the default `stack install` commands, not to the ones you replace:

```bash
clever env set CC_HASKELL_STACK_TARGET hello
```

### Custom run command

By default, Clever Cloud starts the executable Stack built, which it looks for in the `.stack-work/install` folder at the root of the repository. If your project is in an `APP_FOLDER`, has several executables, or needs arguments, set `CC_RUN_COMMAND`. It runs from the root of the repository: call the executable by its name, as `stack install` copies it to `~/.local/bin`. For instance, for the `site` executable of a [Hakyll](https://jaspervdj.be/hakyll/) website:

```bash
clever env set CC_RUN_COMMAND 'site server --host 0.0.0.0 --port $PORT'
```

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit, with the installed executables. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps the compiled dependencies between commits, in the Stack snapshots and the `.stack-work` folder at the repository root. Stack still installs GHC on each build, which takes a few minutes.

## Haskell applications as Clever Tasks

A Haskell application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration: Clever Cloud builds it, then runs `CC_RUN_COMMAND`.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks), here for a `worker` executable:

```bash
clever create --type haskell --task "worker --once"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
