---
type: docs
linkTitle: Maven
title: Maven
description: Build Java applications with Maven on Clever Cloud, with the Maven Wrapper, profiles, a settings file, and the goal or the JAR to start
keywords:
- java
- maven
- maven wrapper
- mvnw
- pom.xml
- spring boot
aliases:
- /deploy/application/java/java-maven
- /doc/applications/java/java-maven
- /doc/deploy/application/java/java-maven
- /doc/deploy/application/java/old_java-maven
- /doc/java/java-maven
---

## Overview

[Maven](https://maven.apache.org) builds a Java project from its `pom.xml` file, which declares the dependencies, the plugins, and the packaging of the project. Clever Cloud builds it with `mvn package`, then starts the JAR it produces or a goal of Maven. The [Java page](/doc/deploy/applications/java/) describes what all Java applications share: the Java version, the memory, the variables, and the caches.

## Create your Maven application

To create a new Maven application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type maven
```

## Build with Maven

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/), then the `package` phase of Maven:

```bash
mvn package
```

To run other goals, set them in `CC_MAVEN_BUILD_GOAL`, such as `clean package -DskipTests`. When your project holds the `mvnw` script of the [Maven Wrapper](https://maven.apache.org/wrapper/), executable, Clever Cloud runs it instead of `mvn`. The build then uses the version of Maven your project sets.

### Profiles

To activate a [profile](https://maven.apache.org/guides/introduction/introduction-to-profiles.html) of your `pom.xml`, set its ID in `CC_MAVEN_PROFILES`. Clever Cloud adds it to the Maven commands:

```bash
clever env set CC_MAVEN_PROFILES production
```

### Settings and private repositories

Commit your own Maven settings, such as a mirror or the credentials of a private repository, in `clevercloud/settings.xml` at the root of your repository. Clever Cloud copies this file to `~/.m2/settings.xml` before the build, whatever the build tool. Read a password from an environment variable, such as `${env.REPOSITORY_PASSWORD}`, to keep it out of your repository:

```xml {filename="clevercloud/settings.xml"}
<settings>
  <servers>
    <server>
      <id>company</id>
      <username>deploy</username>
      <password>${env.REPOSITORY_PASSWORD}</password>
    </server>
  </servers>
  <mirrors>
    <mirror>
      <id>company</id>
      <url>https://maven.example.com/repository/public</url>
      <mirrorOf>*</mirrorOf>
    </mirror>
  </mirrors>
</settings>
```

## Start your application

Set the JAR that `mvn package` builds in `CC_JAR_PATH`, as the [Java page](/doc/deploy/applications/java/#start-command) explains. A pattern works, as long as it matches a single file: Spring Boot keeps the original JAR as `.jar.original`, which `target/*.jar` doesn't match.

```bash
clever env set CC_JAR_PATH "target/*.jar"
```

You can also start a goal of Maven, set in `CC_MAVEN_DEPLOY_GOAL`, such as `spring-boot:run`. Maven then stays in memory, and Spring Boot starts your application in another JVM, which keeps its default heap: prefer a JAR.

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/java" title="Java" subtitle="Java version, memory, variables, caches, and tasks" icon="java" >}}
  {{< card link="/developers/doc/deploy/applications/java/java-gradle" title="Gradle" subtitle="Build with Gradle or its wrapper, and start a JAR or a task" icon="simple:gradle" >}}
  {{< card link="/developers/doc/deploy/applications/java/java-war" title="WAR and EAR" subtitle="Deploy a WAR or an EAR in Tomcat, Jetty, WildFly, or Payara" icon="java" >}}
{{< /cards >}}
