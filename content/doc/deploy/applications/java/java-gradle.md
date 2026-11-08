---
type: docs
linkTitle: Gradle
title: Gradle
description: Deploy Java applications using Gradle build system on Clever Cloud with automatic dependency resolution and build automation
keywords:
- java
- gradle
- build-system
- deployment
- automation
- dependencies
aliases:
- /doc/applications/java/java-gradle
- /doc/deploy/application/java/java-gradle
- /doc/java/java-gradle
- /java/java-gradle
---

## Overview

Clever Cloud offers you to run your Gradle projects. You can deploy this kind of project without changing your code, but running it on Clever Cloud needs some configuration files or environment variables, to add parameters like your gradle task for example.

Gradle is a project automation tool that builds upon the concepts of Apache Ant and Apache Maven and introduces a Groovy-based domain-specific language (DSL) instead of the more traditional XML form of declaring the project configuration.

Note: Clever Cloud passes the port of your application as the `http.port` system property: `8080`, or `9000` with [Request Flow](/doc/manage/request-flow/). Your application listens on `0.0.0.0`, on this port. [Learn more about the port of your application](/doc/manage/#listen-on-the-right-port).

{{% content "java-versions" %}}

Accepted values are the following:

{{< runtimes_versions java >}}

(`graalvm-ce` for GraalVM 21.0.0.2, based on OpenJDK 11.0)

## Configure your Java application

Unless you set `CC_RUN_COMMAND`, you *must* tell Clever Cloud how to run your application, with the `CC_GRADLE_DEPLOY_GOAL` environment variable [described below](#configure-goals-with-environment-variables).

### Configure goals with environment variables

Set the goals with these environment variables:

- `CC_GRADLE_BUILD_GOAL`: the task that builds your project, `assemble` by default
- `CC_GRADLE_DEPLOY_GOAL`: the task and options that run your project, such as `bootRun`

```bash
CC_GRADLE_BUILD_GOAL="clean assemble"
CC_GRADLE_DEPLOY_GOAL="bootRun"
```

The former `GRADLE_BUILD_GOAL` and `GRADLE_DEPLOY_GOAL` names remain supported as aliases.

To build with Ant, a `clevercloud/gradle.json` file is the only way: set `ant` in `build.type`, and the target in `build.goal`.

 {{% content "new-relic" %}}

{{% content "java-env-injection" %}}

## Custom run command

If you need to run a custom command
you can specify it through the `CC_RUN_COMMAND` environment variable.
This will override the default way of running your application.

Example:

```bash
CC_RUN_COMMAND="java -jar somefile.jar <options>"
```

## Gradle version

Without the [Gradle Wrapper](#the-gradle-wrapper), set the major version of Gradle in `CC_GRADLE_VERSION`, `8` or `9`:

```bash
clever env set CC_GRADLE_VERSION 9
```

## The Gradle Wrapper

Since Gradle can come in many versions, Clever Cloud automatically support the [Gradle Wrapper ↗](https://www.gradle.org/docs/current/userguide/gradle_wrapper.html).

Just create and commit the `gradlew` file and the wrapper `jar` and `properties` files. Your working repository should look like this:

{{< filetree/container >}}
  {{< filetree/folder name="." >}}
    {{< filetree/file name="gradlew" >}}
    {{< filetree/folder name="gradle" >}}
      {{< filetree/folder name="wrapper" >}}
        {{< filetree/file name="gradle-wrapper.jar" >}}
        {{< filetree/file name="gradle-wrapper.properties" >}}
      {{< /filetree/folder >}}
    {{< /filetree/folder >}}
    {{< filetree/folder name="src" >}}
    {{< /filetree/folder >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
