---
type: docs
linkTitle: Java
title: Java application runtime
description: Build and deploy Java applications on Clever Cloud with Maven or Gradle, or from a JAR or WAR file, with the Java version and JVM options of your choice
keywords:
- gradle
- java
- java app hosting
- jar deployment
- jvm
- maven
- quarkus
- spring boot
aliases:
- /applications/java
- /applications/java/java-jar
- /deploy/application/java/java-jar
- /doc/applications/java
- /doc/applications/java/java-jar
- /doc/deploy/application/java
- /doc/deploy/application/java/by-framework
- /doc/deploy/application/java/java
- /doc/deploy/application/java/java-jar
- /doc/deploy/applications/java/java-jar
- /doc/develop/java/
- /doc/getting-started/by-language/java
- /doc/java
- /doc/java-hosting
- /doc/java/java-jar
- /doc/java/select-java-version
- /doc/partials/language-specific-deploy/java
---

## Overview

[Java](https://dev.java) is a statically typed language that runs on the Java virtual machine (JVM). Clever Cloud builds your [Maven](/doc/deploy/applications/java/java-maven/) or [Gradle](/doc/deploy/applications/java/java-gradle/) project. It then starts the JAR it produces, a task of your build tool, or a [WAR file](/doc/deploy/applications/java/java-war/) in a servlet container. It works with frameworks such as [Spring Boot](https://spring.io/projects/spring-boot), [Quarkus](https://quarkus.io), or [Micronaut](https://micronaut.io). For Scala and sbt, see the [Scala page](/doc/deploy/applications/scala/). For Play Framework, see the [Play 2 and 3](/doc/deploy/applications/scala/play-framework-2/) or [Play 1](/doc/deploy/applications/scala/play-framework-1/) page.

## Create your Java application

To create a new Java application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/), here for a Maven project:

```bash
clever create --type maven
```

The `gradle`, `jar`, and `war` types work the same way. The [getting started guide](/doc/getting-started/) describes each step of the creation of an application.

## Configure your Java application

### Mandatory needs

A Java application needs:

- A Maven or Gradle project, or a JAR file, at the root of the project or of the folder set in `CC_APP_FOLDER`
- A way to start it: the path of a JAR in `CC_JAR_PATH`, a goal of your build tool, or a `CC_RUN_COMMAND`
- A web server listening on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port)

A [WAR or EAR application](/doc/deploy/applications/java/java-war/) needs a `clevercloud/war.json` file instead, which sets its container and its packages.

For instance, a minimal [Spring Boot](https://spring.io/projects/spring-boot) application, built with Maven:

```xml {filename="pom.xml"}
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>4.2.0</version>
  </parent>

  <groupId>com.example</groupId>
  <artifactId>hello</artifactId>
  <version>1.0.0</version>

  <properties>
    <java.version>21</java.version>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-webmvc</artifactId>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
      </plugin>
    </plugins>
  </build>
</project>
```

```java {filename="src/main/java/com/example/hello/HelloApplication.java"}
package com.example.hello;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class HelloApplication {

    public static void main(String[] args) {
        SpringApplication.run(HelloApplication.class, args);
    }

    @GetMapping("/")
    public String hello() {
        return "Hello from Spring Boot on Clever Cloud";
    }
}
```

```properties {filename="src/main/resources/application.properties"}
server.port=${PORT:8080}
```

Set the JAR that `mvn package` builds as the one to start:

```bash
clever env set CC_JAR_PATH "target/*.jar"
```

To try it locally, run `mvn package`, then `java -jar target/hello-1.0.0.jar`: it listens on port 8080. A [Clever Task](#java-applications-as-clever-tasks) doesn't need a web server.

### Build phase

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/), then builds your project with the tool its files point to:

- `build.gradle` or `gradlew`: [Gradle](/doc/deploy/applications/java/java-gradle/), with `gradle assemble`
- `build.sbt`: [sbt](/doc/deploy/applications/scala/), with `sbt stage`
- `pom.xml` or `mvnw`: [Maven](/doc/deploy/applications/java/java-maven/), with `mvn package`

Clever Cloud checks them in this order, and uses the wrapper of your project when it has one.

To run another goal, set `CC_MAVEN_BUILD_GOAL` or `CC_GRADLE_BUILD_GOAL`. Without these files, such as for a committed JAR, Clever Cloud skips the build. A [WAR application](/doc/deploy/applications/java/java-war/) follows its `war.json` file instead of these files.

### Start command

With `CC_JAR_PATH`, Clever Cloud starts this JAR from the folder of your project. A pattern, such as `target/*.jar`, must match a single file:

```bash
java -jar target/hello-1.0.0.jar
```

Pass arguments to your application with `CC_JAR_ARGS`, and options to the JVM with `CC_EXTRA_JAVA_ARGS`. Put `--` before a value that starts with a dash, so that Clever Tools doesn't read it as an option:

```bash
clever env set CC_JAR_ARGS -- "--spring.profiles.active=production"
```

Instead of a JAR, Clever Cloud can start a goal of Maven, such as `spring-boot:run` in `CC_MAVEN_DEPLOY_GOAL`, or a task of Gradle, such as `bootRun` in `CC_GRADLE_DEPLOY_GOAL`. Your build tool then stays in memory next to your application.

To start something else, set `CC_RUN_COMMAND`: it runs from the folder of your project. Without any of them, the deployment of a Maven project fails with `goal is missing for deploying with maven`.

### Java version

Clever Cloud uses Java {{< runtime_version java >}} by default, an [Eclipse Temurin](https://adoptium.net) build of OpenJDK. Set another version in `CC_JAVA_VERSION`:

{{< runtimes_versions java >}}

Set it to the target version of your build, such as `java.version` in a Spring Boot `pom.xml`, or a more recent one. `graalvm-ce` selects [GraalVM Community Edition](https://www.graalvm.org) for Java 17: compile your project for Java 17 or earlier to run it.

### Memory and JVM options

Clever Cloud sets the heap size from the memory of the instance. It applies to a goal of Maven or Gradle, an sbt script, or a servlet container. The JVM of `CC_JAR_PATH`, or the one that `spring-boot:run` forks, keeps its default heap: 216 MB on an `XS` instance. For a JAR, raise it:

```bash
clever env set CC_EXTRA_JAVA_ARGS -- "-XX:MaxRAMPercentage=75"
```

To replace the default options of the garbage collector, set them in `CC_JAVA_GC_PARAMS`, such as `-XX:+UseZGC`.

Clever Cloud also starts an agent that collects the [metrics](/doc/observability/metrics/) of the JVM: set `CC_DISABLE_JVM_AGENT=true` to disable it. The [New Relic](/doc/observability/new-relic/) page explains how to monitor your application with its own agent.

### Environment variables

Your application reads its [environment variables](/doc/manage/environment-variables/) with `System.getenv("MY_VARIABLE")`, such as the credentials of linked add-ons. Clever Cloud also passes them to the JVM it starts as system properties, which `System.getProperty("MY_VARIABLE")` reads.

A variable whose name holds a dot or a dash, such as `my.app.mode`, only exists as a system property. With `CC_RUN_COMMAND`, or a goal of Maven or Gradle that starts another JVM, Clever Cloud doesn't forward these properties. Pass them in the configuration of your build tool, such as `systemPropertyVariables` for `spring-boot:run`, or use names without dots or dashes.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps the dependencies that Maven and Gradle download between commits, in the `.m2` and `.gradle` folders of the home directory. The next builds then skip these downloads.

## Java applications as Clever Tasks

A Java application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration. Clever Cloud builds it, then runs `CC_RUN_COMMAND` from the folder of your project, instead of starting a web server. The task stops when this command ends.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks), here for a Spring Boot application without its web server:

```bash
clever create --type maven --task "java -jar target/hello-1.0.0.jar --spring.main.web-application-type=none"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/java/java-gradle" title="Gradle" subtitle="Build with Gradle or its wrapper, and start a JAR or a task" icon="simple:gradle" >}}
  {{< card link="/developers/doc/deploy/applications/java/java-maven" title="Maven" subtitle="Build with Maven or its wrapper, and start a JAR or a goal" icon="simple:apachemaven" >}}
  {{< card link="/developers/doc/deploy/applications/java/java-war" title="WAR and EAR" subtitle="Deploy a WAR or an EAR in Tomcat, Jetty, WildFly, or Payara" icon="java" >}}
{{< /cards >}}
