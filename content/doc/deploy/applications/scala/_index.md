---
type: docs
linkTitle: Scala
title: Scala application runtime
description: Build and deploy Scala applications on Clever Cloud with sbt and sbt-native-packager, from a single project to a build with several modules, with the Java version of your choice
keywords:
- cask
- http4s
- jvm language
- pekko
- play framework
- sbt
- sbt-native-packager
- scala
- scala app hosting
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

[Scala](https://www.scala-lang.org) is a statically typed language that combines object-oriented and functional programming, and runs on the Java virtual machine (JVM). Clever Cloud builds your [sbt](https://www.scala-sbt.org) project, then starts the script that [sbt-native-packager](https://www.scala-sbt.org/sbt-native-packager/) creates. It works with web frameworks such as [Cask](https://com-lihaoyi.github.io/cask/), [http4s](https://http4s.org), [Pekko HTTP](https://pekko.apache.org/docs/pekko-http/current/), or [Play Framework](/doc/deploy/applications/scala/play-framework-2/).

## Create your Scala application

To create a new Scala application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type sbt
```

The [getting started guide](/doc/getting-started/) describes each step of the creation of an application.

## Configure your Scala application

### Mandatory needs

A Scala application needs:

- A `build.sbt` file, at the root of the project or of the folder set in `CC_APP_FOLDER`
- The sbt-native-packager plugin, enabled with `JavaAppPackaging`
- A web server listening on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port)

sbt is the most common build tool for Scala. `build.sbt` declares the Scala version and the dependencies of your project, `project/build.properties` the version of sbt, and `project/plugins.sbt` the plugins of your build.

The `stage` task of sbt-native-packager gathers your application, its dependencies, and a start script in `target/universal/stage`. Without this plugin, the build fails with `Not a valid key: stage`.

For instance, a minimal [Cask](https://com-lihaoyi.github.io/cask/) application:

```properties {filename="project/build.properties"}
sbt.version=1.13.1
```

```scala {filename="project/plugins.sbt"}
addSbtPlugin("com.github.sbt" % "sbt-native-packager" % "1.13.0")
```

```scala {filename="build.sbt"}
name := "hello"
scalaVersion := "3.10.1"
libraryDependencies += "com.lihaoyi" %% "cask" % "0.11.3"
enablePlugins(JavaAppPackaging)
```

```scala {filename="src/main/scala/Main.scala"}
object Main extends cask.MainRoutes:
  override def host = "0.0.0.0"
  override def port = sys.env.getOrElse("PORT", "8080").toInt

  @cask.get("/")
  def hello() = "Hello from Scala on Clever Cloud"

  initialize()
```

To try it locally, run `sbt stage`, then `target/universal/stage/bin/hello`: it listens on port 8080. A [Clever Task](#scala-applications-as-clever-tasks) doesn't need a web server.

Your application reads its [environment variables](/doc/manage/environment-variables/), such as the credentials of linked add-ons, with `sys.env`. In the `application.conf` files of Play 2 and 3 and Pekko, `${?MY_VARIABLE}` takes the value of a variable.

### Build phase

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/), then the `stage` task, with a `-mem` limit that depends on the size of the instance:

```bash
sbt stage
```

The image provides the sbt launcher: it downloads the version of sbt set in `project/build.properties`, then the Scala version of `scalaVersion` and the dependencies of your project. `CC_SBT_BUILD_GOAL` replaces `stage`: keep a staging task in it, such as `clean stage`.

The `stage` task also generates the Scaladoc of your project. To skip it and save memory during the build, add this line to `build.sbt`:

```scala {filename="build.sbt"}
Compile / doc / sources := Seq.empty
```

### Java version

Clever Cloud uses Java {{< runtime_version java >}} by default. To use another version, set `CC_JAVA_VERSION` to one of these values:

{{< runtimes_versions java >}}

### Build with sbt 2

sbt 2 needs Java 17 or later. The launcher of the image runs it through its thin client, which fails to start the build. Add `--server` to `CC_SBT_BUILD_GOAL`: the launcher then runs the build in its own JVM, without the thin client:

```bash
clever env set CC_SBT_BUILD_GOAL -- "--server stage"
```

sbt 2 also stages your application in `target/out`. Stage it where Clever Cloud looks for its script, with this line in `build.sbt`:

```scala {filename="build.sbt"}
Universal / sbt.Keys.stagingDirectory := baseDirectory.value / "target" / "universal" / "stage"
```

### Start command

By default, Clever Cloud runs the script of `target/universal/stage/bin` from the folder of your project. It sets the heap size of the JVM in `JAVA_OPTS`, which the script reads, and passes the port in the `http.port` system property, which Play reads. A [health check](/doc/manage/healthcheck/) makes sure that your application answers on this port before it gets any traffic.

With several main classes, such as a `worker` next to your web server, set the main class of your web server in `build.sbt`:

```scala {filename="src/main/scala/Worker.scala"}
@main def worker(args: String*): Unit =
  println(s"Worker done: ${args.mkString(" ")}")
```

```scala {filename="build.sbt"}
Compile / mainClass := Some("Main")
```

sbt-native-packager names its script after the `name` setting, here `hello`, and adds one for each other main class, such as `worker`. Without `CC_SBT_TARGET_BIN`, Clever Cloud starts one of these scripts, which may not be the one of `mainClass`. Set the name of the script to start:

```bash
clever env set CC_SBT_TARGET_BIN hello
```

To pass arguments to the script, set `CC_SBT_DEPLOY_ARGS`. The script hands `-D` system properties and the JVM options prefixed with `-J` to the JVM, and other arguments to your `main` method. Put `--` before a value that starts with a dash, so that Clever Tools doesn't read it as an option:

```bash
clever env set CC_SBT_DEPLOY_ARGS -- "-Dapp.mode=production -J-Xss2m"
```

Your application reads these properties with `sys.props`. To start something else, set `CC_RUN_COMMAND`: Clever Cloud runs it from the same folder, and ignores `CC_SBT_TARGET_DIR`, `CC_SBT_TARGET_BIN`, and `CC_SBT_DEPLOY_ARGS`.

### Build a module

In a build with several modules, the `stage` task of the root project stages the modules it aggregates. Each module that enables `JavaAppPackaging` gets its own folder, such as `api/target/universal/stage`. Here, `api` holds the web server and depends on `core`:

```scala {filename="build.sbt"}
ThisBuild / scalaVersion := "3.10.1"

lazy val core = project

lazy val api = project
  .dependsOn(core)
  .enablePlugins(JavaAppPackaging)
  .settings(libraryDependencies += "com.lihaoyi" %% "cask" % "0.11.3")

lazy val root = (project in file(".")).aggregate(core, api)
```

`lazy val api = project` keeps the sources of the module in the `api` folder, such as `api/src/main/scala`. Set the folder of your web server module in `CC_SBT_TARGET_DIR`, relative to your project, so that Clever Cloud starts its script. To build only this module and the ones it depends on, also set its `stage` task in `CC_SBT_BUILD_GOAL`:

```bash
clever env set CC_SBT_TARGET_DIR api
clever env set CC_SBT_BUILD_GOAL api/stage
```

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit, with the staged application. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

`CC_CACHE_DEPENDENCIES=true` keeps the `.ivy2`, `.m2`, and `.coursier` folders of the home directory, but sbt downloads to `.cache/coursier` and `.sbt`. Add them with `CC_CACHE_DEPENDENCIES_EXTRA_PATHS`, from the root of your repository:

```bash
clever env set CC_CACHE_DEPENDENCIES true
clever env set CC_CACHE_DEPENDENCIES_EXTRA_PATHS "../.cache/coursier:../.sbt"
```

The next builds skip these downloads, but fetch the cache archive instead: about 270 MB for the minimal application. The build gets faster, but a small application can deploy slower: enable it when downloads take most of your build time.

## Scala applications as Clever Tasks

A Scala application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration. Clever Cloud builds it, then runs `CC_RUN_COMMAND` from the folder of your project, instead of starting a web server. The task stops when this command ends.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks), here for the `worker` script of a second main class:

```bash
clever create --type sbt --task "target/universal/stage/bin/worker nightly"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/scala/play-framework-1" title="Play Framework 1" subtitle="Deploy a Play 1 application with the Play version of your choice" icon="playframework" >}}
  {{< card link="/developers/doc/deploy/applications/scala/play-framework-2" title="Play Framework 2 and 3" subtitle="Deploy a Play 2 or 3 application built with sbt" icon="playframework" >}}
{{< /cards >}}
