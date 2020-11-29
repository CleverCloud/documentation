---
title: Play Framework 2 deployment
position: 2
shortdesc: Play is an open source web application framework, written in Scala and Java, which follows the model–view–controller (MVC) architectural pattern.
tags:
- java
---

Clever Cloud supports Play! 2 applications natively. The following guide explains how to set up your application to run on Clever Cloud.

Note : like other runtimes, Java application need listen on `0.0.0.0:8080`

## Overview

Play is an open source web application framework, written in Scala and Java, which follows the model–view–controller (MVC) architectural pattern. It aims to optimize developer productivity by using convention over configuration, hot code reloading and display of errors in the browser.

## Create an application

Refer to the page [Deploy an application on Clever Cloud](/doc/clever-cloud-overview/add-application/).

## Necessary information

* The application must be located at the **root** of the git repository.
* Starting from **Play 2.4**, your application needs **Java 8** to run. Please read [select java version](https://www.clever-cloud.com/doc/java/select-java-version/) for more information.

## Configuration file

You can configure your application start command by adding a
`./clevercloud/sbt.json` file with the following fields:

```javascript
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
      <td>**deploy -&gt; goal**</td>
      <td>the goal/target and options you want to execute to deploy/run you project</td>
    </tr>
  </tbody>
</table>

## Environment injection

Clever Cloud can inject environment variables that are defined in the
dashboard and by add-ons linked to your application.

There are two way to access the environment variables from your application:

 * you can reference them in your application.conf file:
   you just have to put `my.option=${MY_VARIABLE}` in your application.conf file, and then use
   the configuration item `my.option` in your application.

 * you can also use the `System.getenv("MY_VARIABLE")` method. Be aware that it can return null.

 So for an application using the PostgreSQL add-on, you can set:

```bash
db.default.driver=org.postgresql.Driver
db.default.url="jdbc:postgresql://"${POSTGRESQL_ADDON_HOST}"/"${POSTGRESQL_ADDON_DB}
db.default.user=${POSTGRESQL_ADDON_USER}
db.default.password=${POSTGRESQL_ADDON_PASSWORD}
```

## Known problems with Play! 2

Please read the following if your project fails with this error:

`sbt.ResolveException: unresolved dependency: play#sbt-plugin;2.0: not found`

Some versions of Play2 try to retrieve a nonexistent version of
"sbt-plugin" which is required by the framework to work.
You have two options to fix this problem:

You can set the "play.version" environment variable in the
`clevercloud/sbt.json` file.
For example, for Play 2.0.4:

``` javascript
{
  "deploy": {
    "goal": "-Dplay.version=2.0.4"
  }
}
```

Otherwise, you can modify `plugins.sbt` in the project folder of your
app like the following:

``` scala
// Comment to get more information during initialization
logLevel := Level.Warn

// The Typesafe repository
resolvers += "Typesafe repository" at "http://repo.typesafe.com/typesafe/releases/"

// Use the Play sbt plugin for Play projects
addSbtPlugin("play" % "sbt-plugin" % "2.0.4") // The important part of the configuration
```

The two solutions do the job, you can pick your favorite.

## HTTPS support

HTTPS is handled by Clever Cloud ahead of your application, your application
retrieves the traffic in plain http. To be able to use `request.secure`, you
have to add `trustxforwarded=true` in `application.conf`.

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via Git. Follow [these steps](/doc/clever-cloud-overview/add-application/) to deploy your application.
