---
type: docs
linkTitle: Gradle
title: Gradle
description: Build Java applications with Gradle on Clever Cloud, with the Gradle Wrapper or the Gradle version of your choice, and the task or the JAR to start
keywords:
- build.gradle
- gradle
- gradle wrapper
- gradlew
- java
- spring boot
aliases:
- /doc/applications/java/java-gradle
- /doc/deploy/application/java/java-gradle
- /doc/java/java-gradle
- /java/java-gradle
---

## Overview

[Gradle](https://gradle.org) builds a Java project from its `build.gradle` file, which declares the plugins, the dependencies, and the tasks of the project. Clever Cloud builds it with `gradle assemble`, then starts the JAR it produces or a task of Gradle. The [Java page](/doc/deploy/applications/java/) describes what all Java applications share: the Java version, the memory, the variables, and the caches.

## Create your Gradle application

To create a new Gradle application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type gradle
```

## Build with Gradle

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/), then the `assemble` task of Gradle:

```bash
gradle assemble
```

To run other tasks, set them in `CC_GRADLE_BUILD_GOAL`, such as `clean assemble`.

### Gradle version

The [Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html) sets the version of Gradle in your project. Run `gradle wrapper`, then commit the `gradlew` script, executable, and the `gradle/wrapper` folder: Clever Cloud runs `./gradlew` instead of `gradle`. Clever Cloud detects Gradle from `build.gradle` or `gradlew`: commit the wrapper with a Kotlin build script, `build.gradle.kts`.

Without the wrapper, Clever Cloud uses Gradle {{< runtime_version gradle >}} by default. To use Gradle 9, set `CC_GRADLE_VERSION`:

```bash
clever env set CC_GRADLE_VERSION 9
```

## Start your application

Set the JAR that the build produces in `CC_JAR_PATH`, as the [Java page](/doc/deploy/applications/java/#start-command) explains. Its pattern must match a single file: the Spring Boot plugin builds a `-plain.jar` next to the executable JAR, and `build/libs/*.jar` then matches both. Build only the executable JAR with the `bootJar` task:

```bash
clever env set CC_GRADLE_BUILD_GOAL bootJar
clever env set CC_JAR_PATH "build/libs/*.jar"
```

You can also start a task of Gradle, such as `bootRun`, set in `CC_GRADLE_DEPLOY_GOAL`. Gradle then stays in memory next to your application, which runs in another JVM: a JAR uses less memory.

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/java" title="Java" subtitle="Java version, memory, variables, caches, and tasks" icon="java" >}}
  {{< card link="/developers/doc/deploy/applications/java/java-maven" title="Maven" subtitle="Build with Maven or its wrapper, and start a JAR or a goal" icon="simple:apachemaven" >}}
  {{< card link="/developers/doc/deploy/applications/java/java-war" title="WAR and EAR" subtitle="Deploy a WAR or an EAR in Tomcat, Jetty, WildFly, or Payara" icon="java" >}}
{{< /cards >}}
