---
type: docs
title: Scala
shortdesc: Scala is an object-functional programming and scripting language that runs on the Java platform…
tags:
- deploy
keywords:
- scala
str_replace_dict:
  "@application-type@": "SBT + Scala"
type: docs
aliases:
- /developers/doc/scala/scala
- /doc/getting-started/by-language/scala
- /doc/deploy/application/scala
- /doc/deploy/application/scala/scala
- /doc/partials/language-specific-deploy/scala
- /doc/scala/scala
comments: false
---

## Overview

Clever Cloud allows you to deploy Scala (and Java) applications built with SBT. This document will explain you how to set up your app to run it on our service.

If you're looking to deploy a [Play Framework](https://www.playframework.com) application, you can have a look at our dedicated [deployment guide for play framework applications]({{< ref "/guides/play-framework-2" >}})

{{< content "create-application" >}}

{{< content "set-env-vars" >}}

## Configure your Scala application

### Mandatory configuration

Your application has to listen on port `8080` for worldwide connections (`0.0.0.0`). We set the system variable `http.port` to `8080` for you so in many cases (like for play applications) you don't have anything to do.
You need to use the [sbt-native-packager](#the-sbt-native-packager) in your project.

### The sbt-native-packager

We rely on `sbt-native-packager` to run applications. This plugin provides a `stage` task which is run during deployment.

If your project doesn't already use [sbt-native-packager](https://GitHub.com/sbt/sbt-native-packager), you need to add it to `project/plugins.sbt`. Please make sure you use an up-to-date version.

In `project/plugins.sbt`:

```scala
addSbtPlugin("com.typesafe.sbt" % "sbt-native-packager" % "1.7.0")
```

Then you need to configure the package type:

In `build.sbt`:

```scala
enablePlugins(JavaAppPackaging)

# Disable javadoc packaging
mappings in (Compile, packageDoc) := Seq()
```

For more information, please have a look at the [documentation for sbt-native-packager](https://www.scala-sbt.org/sbt-native-packager/index.html)

#### Custom sbt goal

By default, the deployment system execute `sbt stage` and runs the first binary found into `/target/universal/stage/bin`. If you want to run another goal, you can specify it with the `SBT_DEPLOY_GOAL` [environment variable](#setting-up-environment-variables-on-clever-cloud).

#### Multi-module build

If you have a single repository with multiple modules or want to build a specific module in a monorepo (and no top-level `stage` task), then you can specify the sbt task with `SBT_DEPLOY_GOAL`.

`CC_SBT_TARGET_DIR` must be set to the relative path of the module and `CC_SBT_TARGET_BIN` to the name of the binary to run.

For instance, if you want to deploy a module named `service1` that produce a binary named "my-binary", you have to define the following variables:

```shell
SBT_DEPLOY_GOAL=service1/stage
CC_SBT_TARGET_DIR=service1
CC_SBT_TARGET_BIN=my-binary
```

Check details on [environment variables](#setting-up-environment-variables-on-clever-cloud).

Our engine will execute the `sbt service1/stage` and will run `service1/target/universal/stage/bin/my-binary`

**Note:** even when `CC_RUN_COMMAND` is configured `CC_SBT_TARGET_DIR` and `CC_SBT_TARGET_BIN` should be set to the correct values.

### HOCON users

If you're using
[HOCON](https://GitHub.com/typesafehub/config/blob/master/HOCON.md#hocon-human-optimized-config-object-notation) configuration files, then you can have direct acces to environment variables from the configuration file:

```shell
application.secret=${APPLICATION_SECRET}
```

{{< content "new-relic" >}}

{{< content "env-injection" >}}

To access environment variables from your code, just get them from the environment with `System.getenv("MY_VARIABLE")`. Be aware that it can return null.

{{< content "deploy-git" >}}

{{< content "link-addon" >}}

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}
