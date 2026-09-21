---
type: docs
linkTitle: Scala
title: Scala
description: Deploy Scala applications on Clever Cloud using the object-functional programming language that runs on the Java platform runtime
keywords:
- scala app hosting
- scala cloud
- jvm language
- functional programming
- java platform
- sbt
- type safety
aliases:
- /applications/scala
- /deploy/application/scala/scala
- /doc/applications/scala
- /doc/deploy/application/scala
- /doc/deploy/application/scala/scala
- /doc/developers/doc/scala-hosting
- /doc/getting-started/by-language/scala
- /doc/partials/language-specific-deploy/scala
- /doc/play-framwork
- /doc/sbt
- /doc/scala
- /doc/scala-hosting
- /doc/scala/scala
- /scala/scala
---

## Overview

Clever Cloud allows you to deploy Scala (and Java) applications built with SBT. This document will explain you how to set up your app to run it on our service. If you're looking to deploy a [Play Framework](https://www.playframework.com) application, you can have a look at our dedicated [documentation page](/doc/deploy/applications/scala/play-framework-2).

{{% content "create-application" %}}

{{% content "set-env-vars" %}}

## Configure your Scala application

### Mandatory configuration

Your application has to listen on port `8080` for worldwide connections (`0.0.0.0`). We set the system variable `http.port` to `8080` for you so in many cases (like for play applications) you don't have anything to do.

### sbt Native Packager

We rely on [sbt-native-packager](https://github.com/sbt/sbt-native-packager) to run applications. This tool automates project build and provides a `stage` task which is run during deployment. To use it, add this line to `project/plugins.sbt` (with an up-to-date version):

```scala
addSbtPlugin("com.github.sbt" % "sbt-native-packager" % "1.11.4")
```

Then you need to enable the package in `build.sbt`:

```scala
enablePlugins(JavaAppPackaging)

// Disable javadoc packaging to speed up the build
Compile / packageDoc / mappings := Seq()
```

For more information, please have a look at the [sbt-native-packager documentation](https://www.scala-sbt.org/sbt-native-packager/index.html)

#### sbt custom goal

By default, the deployment system executes `sbt stage` and runs a binary from `target/universal/stage/bin`. When this folder holds several scripts, the choice isn't guaranteed: set `CC_SBT_TARGET_BIN` to the one you want to run. To build with another goal, set the `CC_SBT_BUILD_GOAL` [environment variable](#setting-up-environment-variables-on-clever-cloud), for example `CC_SBT_BUILD_GOAL="clean stage"`. It takes precedence over the `build.goal` field of a `clevercloud/sbt.json` file.

To pass arguments to the binary when it starts, set `CC_SBT_DEPLOY_ARGS`, for example `CC_SBT_DEPLOY_ARGS="-Dconfig.resource=clevercloud.conf"`. The former `SBT_DEPLOY_GOAL` name remains supported as an alias of `CC_SBT_DEPLOY_ARGS`, but it no longer adds goals to the build command: if you used it to build a specific module, move that goal to `CC_SBT_BUILD_GOAL`.

#### Multi-module build

If you have a single repository with multiple modules or if you want to build a specific module in a monorepo (with no top-level `stage` task), you must set `CC_SBT_BUILD_GOAL`, `CC_SBT_TARGET_DIR`, and `CC_SBT_TARGET_BIN`. For instance, if you want to deploy a module named `service1` that produces a binary named `my-binary`, configuration should be:

```shell
CC_SBT_BUILD_GOAL=service1/stage
CC_SBT_TARGET_DIR=service1
CC_SBT_TARGET_BIN=my-binary
```

The build command is `sbt service1/stage` and the application is started with `service1/target/universal/stage/bin/my-binary`.

When you set `CC_RUN_COMMAND`, Clever Cloud runs it as is and ignores `CC_SBT_TARGET_DIR` and `CC_SBT_TARGET_BIN` to start your application.

### HOCON users

If you're using
[HOCON](https://github.com/typesafehub/config/blob/master/HOCON.md#hocon-human-optimized-config-object-notation) configuration files, then you can have direct acces to environment variables from the configuration file:

```shell
application.secret=${APPLICATION_SECRET}
```

{{% content "new-relic" %}}

{{% content "env-injection" %}}

In Scala code, retrieve an environment variable with `System.getenv("MY_VARIABLE")`, it returns `null` when the variable is not defined.

{{% content "deploy-git" %}}

{{% content "link-addon" %}}

{{% content "more-config" %}}

{{% content "url_healthcheck" %}}
