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
- /doc/getting-started/by-language/scala
- /doc/deploy/application/scala
- /doc/deploy/application/scala/scala
- /doc/developers/doc/scala-hosting
- /doc/partials/language-specific-deploy/scala
- /doc/sbt
- /doc/scala
- /doc/scala/scala
- /doc/scala-hosting
- /scala/scala
---

## Overview

Clever Cloud allows you to deploy Scala (and Java) applications built with SBT. This document will explain you how to set up your app to run it on our service. If you're looking to deploy a [Play Framework](https://www.playframework.com) application, you can have a look at our dedicated [deployment guide](/guides/play-framework-2).

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

By default, the deployment system executes `sbt stage` and runs the first binary found into `/target/universal/stage/bin`. If you want to run another goal, you can specify it with the `SBT_DEPLOY_GOAL` [environment variable](#setting-up-environment-variables-on-clever-cloud).

#### Multi-module build

If you have a single repository with multiple modules or if you want to build a specific module in a monorepo (with no top-level `stage` task), you must set `SBT_DEPLOY_GOAL`, `CC_SBT_TARGET_DIR`, and `CC_SBT_TARGET_BIN`. For instance, if you want to deploy a module named `service1` that produces a binary named "my-binary", configuration should be:

```shell
SBT_DEPLOY_GOAL=service1/stage
CC_SBT_TARGET_DIR=service1
CC_SBT_TARGET_BIN=my-binary
```

The build command is `sbt service1/stage` and the application is started with `service1/target/universal/stage/bin/my-binary`.

> [!NOTE]
> Even when `CC_RUN_COMMAND` is configured, `CC_SBT_TARGET_DIR` and `CC_SBT_TARGET_BIN` should be set to the correct values.

### HOCON users

If you're using
[HOCON](https://github.com/typesafehub/config/blob/master/HOCON.md#hocon-human-optimized-config-object-notation) configuration files, then you can have direct acces to environment variables from the configuration file:

```shell
application.secret=${APPLICATION_SECRET}
```

{{% content "new-relic" %}}

{{% content "env-injection" %}}

To access environment variables from your code, just get them from the environment with `System.getenv("MY_VARIABLE")`. Be aware that it can return null.

{{% content "deploy-git" %}}

{{% content "link-addon" %}}

{{% content "more-config" %}}

{{% content "url_healthcheck" %}}
