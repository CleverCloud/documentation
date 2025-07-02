---
type: docs
title: Play Framework 2 Scala
position: 2
shortdesc: Play is an open source web application framework, written in Scala and Java, which follows the model–view–controller (MVC) architectural pattern.
tags:
- deploy
keywords:
- scala
- play
str_replace_dict:
  "@application-type@": "Java or Scala + Play! 2"
aliases:
- /developers/doc/java/play-framework-2
- /developers/doc/scala/play-framework-2
- /doc/applications/java/play-framework-2
- /doc/deploy/application/java/by-framework/play-framework-2
- /doc/java/play-framework-2
- /doc/scala/play-framework-2
type: docs
---

## Overview

Clever Cloud supports Play! 2 applications natively. The following guide explains how to set up your application to run on Clever Cloud.

{{< content "create-application" >}}

 {{< content "set-env-vars" >}}

## Configure your Scala + Play! 2 application

### Mandatory configuration

* Starting from **Play 2.4**, your application needs **Java 8** to run. Please read [select java version]({{< ref "doc/applications/java/java-war/#available-java-versions" >}} "Select Java version") for more information.
* Starting from **Play 2.4**, your application needs **Java 8** to run. Please read [select java version]({{< ref "doc/applications/java/java-war/#available-java-versions" >}} "Select Java version") for more information.

Play! 2 applications use sbt. Please have a look at [deploy Scala apps]({{< ref "doc/applications/scala" >}}) for a complete documentation on sbt deployment options.

### Generate application secret

To deploy a Play! application you have to set a secret in your `conf/application.conf`  the environment variable name depends on your Play2! version:

* 2.6.x: `play.http.secret.key=${?APPLICATION_SECRET}`, to generate secret use `sbt playGenerateSecret`;
* 2.4.x -> 2.5.x: `play.crypto.secret=${?APPLICATION_SECRET}` -> `sbt playGenerateSecret`;
* 2.3.x: `application.secret=${?APPLICATION_SECRET}` -> `sbt play-generate-secret`.

Then, in your Clever Cloud application define `APPLICATION_SECRET` [environment variable](#setting-up-environment-variables-on-clever-cloud) with the generated value.

### Custom config file

If you don't want to use the default `conf/application.conf` configuration file, you can use the `SBT_DEPLOY_GOAL` [environment variable](#setting-up-environment-variables-on-clever-cloud) `SBT_DEPLOY_GOAL=-Dconfig.resource=clevercloud.conf`

### HTTPS support

HTTPS is handled by Clever Cloud ahead of your application, your application retrieves the traffic in plain http.

If you want to redirect HTTP traffic to HTTPS, please have a look at [How to Redirect to HTTPS With Play
2.4](https://www.clever-cloud.com/blog/engineering/2015/12/01/redirect-to-https-in-play/).

#### HTTP support with Play! 2.x < 2.4

To be able to use `request.secure`, you have to add `trustxforwarded=true` in `application.conf`.

### Multi-module project

If you have a single repository with multiple modules, then you can specify which module to run with `CC_SBT_TARGET_DIR` [environment variable](#setting-up-environment-variables-on-clever-cloud).

For instance, if your Sbt project contains a `shared` and `play` module and you want to execute the `play` module, then add
`CC_SBT_TARGET_DIR=play` environment variable.

 {{< content "new-relic" >}}

 {{< content "env-injection" >}}

To access the environment variables from your code, you need to add `my.option=${MY_VARIABLE}` in your `application.conf` file, and then use the configuration item `my.option` in your application. e.g `%clevercloud.db.url="jdbc:mysql://"${MYSQL_ADDON_HOST}"/"${MYSQL_ADDON_DB}`.
You can also use the `System.getenv("MY_VARIABLE")` method. Be aware that it can return null.

 {{< content "deploy-git" >}}

 {{< content "link-addon" >}}

## Known problems with Play! 2

### sbt-plugin unresolved dependency error

If your project fails with the error `sbt.ResolveException: unresolved dependency: play#sbt-plugin;2.0: not found` this is because some versions of Play2 try to retrieve a nonexistent version of "sbt-plugin" which is required by the framework.
You have two options to fix this problem:

* You can set the "play.version" environment variable in the `/clevercloud/sbt.json` file. For example, for Play 2.0.4:

``` javascript
{
  "deploy": {
    "goal": "-Dplay.version=2.0.4"
  }
}
```

* You can modify `plugins.sbt` in the project folder of your app like the following:

``` scala
// Comment to get more information during initialization
logLevel := Level.Warn

// The Typesafe repository
resolvers += "Typesafe repository" at "https://repo.typesafe.com/typesafe/releases/"

// Use the Play sbt plugin for Play projects
addSbtPlugin("play" % "sbt-plugin" % "2.0.4") // The important part of the configuration
```

Both alternatives effectively fulfill the task at hand; you are free to select the one that best suits your preference.

More info on [playframework.com](https://www.playframework.com).

### Bad root server path error

The error occurs when we cannot find a bin to execute your project.

### Failed to acquire connection: Too many connections

You may run into this error during deployments:

``` scala
[error] c.j.b.h.AbstractConnectionHook - Failed to acquire connection to jdbc:<address> Sleeping for 1000ms and trying again. Attempts left: 10. Exception: null.Message:FATAL: too many connections for role "<user>"
```

By default, Play! opens a pool of 10 connections, which is more than the connection limit allowed by DEV database plans. During a no-downtime deployment, there are at least two instances of the application running in parallel, so it's 20 connections.

To avoid connection exhaustion, you should limit your pool at half the number of available connections (if you have horizontal scaling enabled, adjust accordingly).

``` scala
# conf/application.conf

db.default.partitionCount=2
db.default.maxConnectionsPerPartition=5
db.default.minConnectionsPerPartition=5
```

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}
