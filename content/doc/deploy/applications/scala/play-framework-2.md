---
type: docs
linkTitle: Play 2 and 3
title: Play Framework 2 and 3
description: Deploy Play Framework 2 and 3 applications on Clever Cloud with sbt, with an application secret, the allowed hosts, and a database pool sized for your plan
keywords:
- java web framework
- pekko
- play 2
- play 3
- play framework
- sbt
- scala
aliases:
- /doc/applications/java/play-framework-2
- /doc/applications/scala/play-framework-2
- /doc/deploy/application/java/by-framework/play-framework-2
- /doc/deploy/application/scala/tutorials/play-framework-2
- /doc/java/play-framework-2
- /doc/scala/play-framework-2
- /guides/play-framework-2
- /java/play-framework-2
- /scala/play-framework-2
---

## Overview

[Play Framework](https://www.playframework.com) is a web framework for Scala and Java. Play 3 runs on [Apache Pekko](https://pekko.apache.org), and Play 2 on Akka. Clever Cloud builds a Play project with sbt, as a [Scala application](/doc/deploy/applications/scala/). The sbt plugin of Play includes sbt-native-packager, which creates the start script. This page applies from Play 2.6, which named the secret `play.http.secret.key` and enables the allowed hosts filter by default.

## Create your Play application

To create a new Play application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type play2
```

The [getting started guide](/doc/getting-started/) describes each step of the creation of an application.

## Configure your Play application

### Mandatory needs

A Play application needs:

- The sbt plugin of Play, in `project/plugins.sbt`
- An application secret, in `play.http.secret.key`
- The domains of the application, in `play.filters.hosts.allowed`

Play listens on every interface, on the port of the `http.port` system property, which Clever Cloud sets. A minimal Play 3 application in Scala:

```properties {filename="project/build.properties"}
sbt.version=1.13.1
```

```scala {filename="project/plugins.sbt"}
addSbtPlugin("org.playframework" % "sbt-plugin" % "3.0.12")
```

```scala {filename="build.sbt"}
name := "hello-play"
scalaVersion := "3.3.8"
libraryDependencies += guice
lazy val root = (project in file(".")).enablePlugins(PlayScala)
Compile / doc / sources := Seq.empty
```

```text {filename="conf/routes"}
GET     /       controllers.HomeController.index()
```

```scala {filename="app/controllers/HomeController.scala"}
package controllers

import javax.inject.Inject
import play.api.mvc.*

class HomeController @Inject() (cc: ControllerComponents) extends AbstractController(cc):
  def index() = Action {
    Ok("Hello from Play on Clever Cloud")
  }
```

```text {filename="conf/application.conf"}
play.http.secret.key = ${?APPLICATION_SECRET}
play.filters.hosts.allowed = [".cleverapps.io", "localhost"]
```

The last line of `build.sbt` skips the Scaladoc, which Play adds to the staged application. On the default `XS` instance, generating it runs out of memory, and the build fails or stalls, even for this minimal application.

### Application secret

In production, Play refuses to start without a secret: `The application secret has not been set, and we are in prod mode`.

In `application.conf`, `${?APPLICATION_SECRET}` takes the value of this [environment variable](/doc/manage/environment-variables/), which keeps the secret out of your repository. Generate a random secret, and set it on your application:

```bash
clever env set APPLICATION_SECRET "$(openssl rand -base64 32)"
```

### Allowed hosts

Play answers `400 Bad Request` to the requests for a domain it doesn't allow: `Host not allowed: app-xxx.cleverapps.io`. In `play.filters.hosts.allowed`, a leading dot allows a domain and its subdomains, such as `.cleverapps.io`, and `"."` allows every domain. Add your own domains too, such as `.example.com`.

The [health check](/doc/manage/healthcheck/) of Clever Cloud accepts this answer: the deployment succeeds, but your users get this error.

### Database connections

The `jdbc` module of Play opens a pool of connections to the database. This pool can take all the connections of a small plan. A `DEV` PostgreSQL add-on allows five, and a deployment runs the old and the new instances side by side. Limit the pool to half the connections of your plan, divided by the number of instances. Here, with a linked PostgreSQL add-on:

```scala {filename="build.sbt"}
libraryDependencies ++= Seq(jdbc, "org.postgresql" % "postgresql" % "42.7.14")
```

```text {filename="conf/application.conf"}
db.default.driver = org.postgresql.Driver
db.default.url = "jdbc:postgresql://"${?POSTGRESQL_ADDON_HOST}":"${?POSTGRESQL_ADDON_PORT}"/"${?POSTGRESQL_ADDON_DB}
db.default.username = ${?POSTGRESQL_ADDON_USER}
db.default.password = ${?POSTGRESQL_ADDON_PASSWORD}
db.default.hikaricp.maximumPoolSize = 2
```

With the default pool, the new instance gets `FATAL: too many connections for role`, and the deployment doesn't finish.

### HTTPS

The load balancers of Clever Cloud handle HTTPS, and reach your application over HTTP: `request.secure` is `false`, and `request.remoteAddress` holds the address of a load balancer. [Force HTTPS](/doc/manage/#force-https), enabled by default, redirects HTTP requests to HTTPS. To read the protocol and the address of the client, see the headers of the [load balancers](/doc/network/load-balancers/).

### Build, versions, and start

Clever Cloud builds and starts a Play application as any sbt project. The [Scala page](/doc/deploy/applications/scala/) describes the build, the Java version, the start command, and the caches. Play 3.0 builds with sbt 1 only. A project with `PlayJava` instead of `PlayScala` deploys the same way. For Play 2, the plugin is `"com.typesafe.play" % "sbt-plugin"`, and an older version of Play can need an older Java, such as `CC_JAVA_VERSION=8` for Play 2.6.

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/scala/play-framework-1" title="Play Framework 1" subtitle="Deploy a Play 1 application with the Play version of your choice" icon="playframework" >}}
  {{< card link="/developers/doc/deploy/applications/scala" title="Scala" subtitle="Build, Java version, start command, and caches of sbt projects" icon="simple:scala" >}}
  {{< card link="/developers/doc/deploy/databases/postgresql" title="PostgreSQL" subtitle="Create a PostgreSQL add-on and connect to it" icon="simple:postgresql" >}}
  {{< card link="/developers/doc/network/load-balancers" title="Load balancers" subtitle="Read the address and the protocol of your clients" icon="server-stack" >}}
{{< /cards >}}
