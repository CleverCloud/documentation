---
title: Deploying Scala apps with SBT
shortdesc: Scala is an object-functional programming and scripting language that runs on the Java platform…
tags:
- scala
---

Clever Cloud allows you to deploy Scala (and Java) applications built with
<acronym title="Simple Build Tool">SBT</acronym>. This document will explain
you how to set up your app to run on our service.

If you're looking to deploy a [Play Framework](https://www.playframework.com)
application, you can have a look at our dedicated [deployment guide for play
framework applications](/doc/scala/play-framework-2/)

## Create an application

Create an application of type "SBT + Scala". Please have a look at [Deploy an
application on Clever Cloud](/doc/clever-cloud-overview/add-application/) for
more information on creating applications on Clever Cloud.

## Requirements

Your application has to listen on port `8080` for worldwide connections
(`0.0.0.0`). We set the system variable `http.port` to `8080` for you so in
many cases (like for play applications) you don't have anything to do.

We rely on `sbt-native-packager` to run applications. This plugin provides a
`stage` task which is run during deployment.

### Install `sbt-native-packager`

If your project doesn't already use `sbt-native-packager`, you need to add it
to `project/plugins.sbt`. Please make sure you use an up-to-date version.

In `project/plugins.sbt`:

```scala
addSbtPlugin("com.typesafe.sbt" % "sbt-native-packager" % "1.2.0-M9")
```

Then you need to configure the package type:

In `build.sbt`:

```scala
enablePlugins(JavaAppPackaging)

# Disable javadoc packaging
mappings in (Compile, packageDoc) := Seq()
```

For more information, please have a look at [documentation for
sbt-native-packager](http://www.scala-sbt.org/sbt-native-packager/index.html)

## Environment injection

Clever Cloud can inject environment variables that are defined in the
dashboard and by add-ons linked to your application.

To get an env variable from your code, you can use the
`System.getenv("MY_VARIABLE")` method. Be aware that it can return null.

### HOCON users

If you're using
[HOCON](https://github.com/typesafehub/config/blob/master/HOCON.md#hocon-human-optimized-config-object-notation)
configuration files, then you can have direct acces to environment variables
from the configuration file:

```
application.secret=${APPLICATION_SECRET}
```

## Custom sbt goal

By default, the deployment system runs `sbt stage`. If you want to run another
goal, you can specify it with the `SBT_DEPLOY_GOAL` environment variable.

## Multi-module build

If you have a single repository with multiple modules (and no top-level `stage`
task), then you can specify which module to build with `SBT_DEPLOY_GOAL`.

For instance, if you want to deploy the `service1` module, then add
`SBT_DEPLOY_GOAL=service1/stage` in the application's environment variables.

## Hooks

If you need to run specific tasks during deployment, you can specify hooks that
will be run during the build. Please have a look at [documentation on
hooks](/doc/clever-cloud-overview/hooks/)

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via Git. Follow [these
steps](/doc/clever-cloud-overview/add-application/) to deploy your application.
