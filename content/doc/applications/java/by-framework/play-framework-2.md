---
type: docs
title: Deploy Play Framework 2
position: 2
shortdesc: Play is an open source web application framework, written in Scala and Java, which follows the model–view–controller (MVC) architectural pattern.
tags:
- deploy
keywords:
- java
- play
str_replace_dict:
  "@application-type@": "Java or Scala + Play! 2"
type: docs
---

## Overview

Clever Cloud supports Play! 2 applications natively. The following guide explains how to set up your application to run on Clever Cloud.

Play is an open source web application framework, written in Scala and Java, which follows the model–view–controller (MVC) architectural pattern. It aims at optimizing developer productivity by using convention over configuration, hot code reloading and display of errors in the browser.

{{< readfile file="/content/partials/create-application.md" >}}

{{< readfile file="/content/partials/set-env-vars.md" >}}

## Configure your Java + Playframework 2 application
### Mandatory configuration

* The application must be located at the **root** of the git repository.
* Starting from **Play 2.4**, your application needs **Java 8** to run. Please read [Available Java Versions](#available-java-versions).
* Your Java application needs to listen on `0.0.0.0:8080`

### Configuration file

You can configure your application start command by adding a `./clevercloud/sbt.json` file with the following fields:

```json
{
  "deploy":{
    "goal": "yourgoal"
  }
}
```

You can use the following properties:
<table class="table table-bordered table-striped">
  <thead>
    <tr>
      <th>Usage</th>
      <th>Field</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="label label-danger">Required</span></td>
      <td><strong>deploy -&gt; goal</strong></td>
      <td>the goal/target and options you want to execute to deploy/run you project</td>
    </tr>
  </tbody>
</table>

{{< readfile file="/content/partials/java-versions.md" >}}

### HTTPS support

HTTPS is handled by Clever Cloud ahead of your application, your application retrieves the traffic in plain http. To be able to use `request.secure`, you have to add `trustxforwarded=true` in `application.conf`.

### Known problems with Play! 2

Please read the following if your project fails with this error:

`sbt.ResolveException: unresolved dependency: play#sbt-plugin;2.0: not found`

Some versions of Play2 try to retrieve a nonexistent version of "sbt-plugin" which is required by the framework to work.
You have two options to fix this problem:

You can set the "play.version" environment variable in the `clevercloud/sbt.json` file.
For example, for Play 2.0.4:

``` json
{
  "deploy": {
    "goal": "-Dplay.version=2.0.4"
  }
}
```

Otherwise, you can modify `plugins.sbt` in the project folder of your app like the following:

```scala
// Comment to get more information during initialization
logLevel := Level.Warn

// The Typesafe repository
resolvers += "Typesafe repository" at "https://repo.typesafe.com/typesafe/releases/"

// Use the Play sbt plugin for Play projects
addSbtPlugin("play" % "sbt-plugin" % "2.0.4") // The important part of the configuration
```

The two solutions do the job, you can pick your favorite.

{{< readfile file="/content/partials/env-injection.md" >}}

To access environment variables from your code, you need to reference them in your application.conf file with `my.option=${MY_VARIABLE}` and then use the configuration item `my.option` in your application.

You can also use the `System.getenv("MY_VARIABLE")` method. Be aware that it can return null.

{{< readfile file="/content/partials/new-relic.md" >}}

{{< readfile file="/content/partials/deploy-git.md" >}}

{{< readfile file="/content/partials/link-addon.md" >}}

{{< readfile file="/content/partials/more-config.md" >}}
