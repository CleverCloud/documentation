---
type: docs
linkTitle: Jar
title: Jar
description: Deploy Java JAR applications on Clever Cloud with automatic JVM configuration, dependency management, and runtime optimization
keywords:
- java
- jar
- deployment
- jvm
- runtime
- applications
aliases:
- /deploy/application/java/java-jar
- /doc/applications/java/java-jar
- /doc/deploy/application/java/java-jar
- /applications/java/java-jar
- /doc/java/java-jar
---

## Overview

Clever Cloud offers you to run any Java ARchive file. You do not need to change your code, but running it on Clever Cloud needs some configuration files or environment variable to specify the JAR path.

Note: Clever Cloud passes the port of your application as the `http.port` system property: `8080`, or `9000` with [Request Flow](/doc/manage/request-flow/). Your application listens on `0.0.0.0`, on this port. [Learn more about the port of your application](/doc/manage/#listen-on-the-right-port).

{{% content "java-versions" %}}

{{< runtimes_versions java >}}

(`graalvm-ce` for GraalVM 21.0.0.2, based on OpenJDK 11.0)

## Configure your Java application

Set the path of your JAR, from the root of your repository and without a leading `/`, in `CC_JAR_PATH`:

```bash
clever env set CC_JAR_PATH target/myproject-1.0.jar
```

### Build options

You don't need to commit a JAR. Push your sources: Clever Cloud builds them with Gradle for a `build.gradle` file, otherwise with Maven for a `pom.xml`. For another build command, set `CC_GRADLE_BUILD_GOAL` or `CC_MAVEN_BUILD_GOAL`, and `CC_JAR_PATH` to the JAR it produces.

To select Ant, or Maven when your project also has a `build.gradle` file, set the build system in a `clevercloud/jar.json` file: `ant` or `maven` in `build.type`, and its target, such as `jar`, in `build.goal`:

```json {filename="clevercloud/jar.json"}
{
  "build": {
    "type": "ant",
    "goal": "jar"
  }
}
```

Pass extra arguments to the `java` command with `CC_EXTRA_JAVA_ARGS`, and to your JAR with `CC_JAR_ARGS`.

 {{% content "new-relic" %}}

{{% content "java-env-injection" %}}

## Custom run command

If you need to run a custom command (or just pass options to the program),
you can specify it through the `CC_RUN_COMMAND` environment variable.
This will override the default way of running your application.

Example:

```bash
CC_RUN_COMMAND="java -jar somefile.jar <options>"
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
