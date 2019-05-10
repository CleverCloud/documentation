---
title: Deploying Play Framework 2 Scala
position: 2
shortdesc: Play is an open source web application framework, written in Scala and Java, which follows the model–view–controller (MVC) architectural pattern.
tags:
- scala
---

Clever Cloud supports Play! 2 applications natively. The following guide
explains how to set up your application to run on Clever Cloud. Play 2
applications use sbt.

## Create an application

Create an application of type "Java or Scala + Play! 2". Please have a look at
[Deploy an application on Clever
Cloud](/doc/clever-cloud-overview/add-application/) for more information on
creating applications on Clever Cloud.

## Necessary information

* The application must be located at the **root** of the git repository.
* Starting from **Play 2.4**, your application needs **Java 8** to run. Please read [select java version](https://www.clever-cloud.com/doc/java/select-java-version/) for more information.

Please have a look at [deploy scala apps](/doc/scala/scala) for a complete
documentation on sbt deployment options.

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
db.default.username=${POSTGRESQL_ADDON_USER}
db.default.password=${POSTGRESQL_ADDON_PASSWORD}
```

## Generate application secret

To deploy a Play! application you have to set a secret in your `conf/application.conf`  the environment variable name depends on your Play2! version:

* 2.6.x: `play.http.secret.key=${?APPLICATION_SECRET}`, to generate secret use `sbt playGenerateSecret`;
* 2.4.x -> 2.5.x: `play.crypto.secret=${?APPLICATION_SECRET}` -> `sbt playGenerateSecret`;
* 2.3.x: `application.secret=${?APPLICATION_SECRET}` -> `sbt play-generate-secret`.

Then, in your Clever Cloud application define `APPLICATION_SECRET` with the generated value.

## Custom config file

If you don't want to use the default `conf/application.conf` configuration
file, you can use the `SBT_DEPLOY_GOAL` environment variable:

```
SBT_DEPLOY_GOAL=-Dconfig.resource=clevercloud.conf
```

## HTTPS support

HTTPS is handled by Clever Cloud ahead of your application, your application
retrieves the traffic in plain http.

If you want to redirect HTTP traffic to HTTPS, please have a look at [How to
Redirect to HTTPS With Play
2.4](https://www.clever-cloud.com/blog/engineering/2015/12/01/redirect-to-https-in-play/).

## Before play 2.4

To be able to use `request.secure`, you have to add `trustxforwarded=true` in
`application.conf`.

## Multi-module project

If you have a single repository with multiple modules, then you can specify which module to run with `CC_SBT_TARGET_DIR`.

For instance, if your Sbt project contains a `shared` and `play` module and you want to execute the `play` module, then add
`CC_SBT_TARGET_DIR=play` in the application's environment variables.


## Deploy on Clever Cloud

Application deployment on Clever Cloud is via Git. Follow [these steps](/doc/clever-cloud-overview/add-application/) to deploy your application.


## Bad root server path error

The error occurs when we cannot find a bin to execute your project.


## Failed to acquire connection: Too many connections

You may run into this error during deployments:

``` scala
[error] c.j.b.h.AbstractConnectionHook - Failed to acquire connection to jdbc:<address> Sleeping for 1000ms and trying again. Attempts left: 10. Exception: null.Message:FATAL: too many connections for role "<user>"
```

By default, Play! opens a pool of 10 connections, which is more than the
connection limit allowed by DEV database plans. During a no-downtime
deployment, there are at least two instances of the application running in
parallel, so it's 20 connections.

To avoid connection exhaustion, you should limit your pool at half the number
of available connections (if you have horizontal scaling enabled, adjust
accordingly).

``` scala
# conf/application.conf

db.default.partitionCount=2
db.default.maxConnectionsPerPartition=5
db.default.minConnectionsPerPartition=5
```

## Known problems with Play! 2

Please read the following if your project fails with this error:  

`sbt.ResolveException: unresolved dependency: play#sbt-plugin;2.0: not found`

Some versions of Play2 try to retrieve a nonexistent version of
"sbt-plugin" which is required by the framework.
You have two options to fix this problem:

You can set the "play.version" environment variable in the
`/clevercloud/sbt.json` file.  
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

More info on <a target="_blank" href="http://www.playframework.com">playframework.com</a>.
