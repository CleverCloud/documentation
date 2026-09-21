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

Note : like other runtimes, Java application need listen on `0.0.0.0:8080`

{{% content "create-application" %}}

{{% content "set-env-vars" %}}

{{% content "java-versions" %}}

Accepted values are the following:

{{< runtimes_versions java >}}

(`graalvm-ce` for GraalVM 21.0.0.2, based on OpenJDK 11.0)

## Configure your Java application

Unless you set `CC_RUN_COMMAND`, you *must* tell Clever Cloud how to run your application, either with the `CC_GRADLE_DEPLOY_GOAL` environment variable [described below](#configure-goals-with-environment-variables), or with a `clevercloud/gradle.json` file (gradle.json file in clevercloud folder which is at the root of your repository) that contains at least the following:

```json
{
  "deploy": {
    "goal": "grails:run"
  }
}
```

That is the only option you really need to supply.

### Optional configuration

The full configuration can look like the following:

```json
{
  "build": {
    "type": "<string>",
    "goal": "<string>"
  },
  "deploy": {
    "goal": "<string>"
  }
}
```

You can use the following properties:

| Usage    | Field             | Description                                                                                                                          |
| -------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Optional | **build → type**  | can be maven, gradle or ant                                                                                                          |
| Optional | **build → goal**  | is the target you want to use to build your project                                                                                  |
| Required | **deploy → goal** | the goal/target and options you want to execute to deploy/run you project, unless `CC_GRADLE_DEPLOY_GOAL` or `CC_RUN_COMMAND` is set |

### Configure goals with environment variables

You can set the goals with environment variables instead of the `clevercloud/gradle.json` file. They take precedence over its fields:

- `CC_GRADLE_BUILD_GOAL`: the task that builds your project, `assemble` by default
- `CC_GRADLE_DEPLOY_GOAL`: the task and options that run your project, such as `bootRun`

```bash
CC_GRADLE_BUILD_GOAL="clean assemble"
CC_GRADLE_DEPLOY_GOAL="bootRun"
```

The former `GRADLE_BUILD_GOAL` and `GRADLE_DEPLOY_GOAL` names remain supported as aliases.

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

## The Gradle Wrapper

Since Gradle can come in many versions, Clever Cloud automatically support the [Gradle Wrapper ↗](https://www.gradle.org/docs/current/userguide/gradle_wrapper.html).

Just create and commit the `gradlew` file and the wrapper `jar` and `properties` files. Your working repository should look like this:

{{< filetree/container >}}
  {{< filetree/folder name="." >}}
    {{< filetree/folder name="clevercloud" >}}
      {{< filetree/file name="gradle.json" >}}
    {{< /filetree/folder >}}
    {{< filetree/file name="gradlew" >}}
    {{< filetree/folder name="graddle" >}}
      {{< filetree/folder name="wrapper" >}}
        {{< filetree/file name="gradle-wrapper.jar" >}}
        {{< filetree/file name="gradle-wrapper.properties" >}}
      {{< /filetree/folder >}}
    {{< /filetree/folder >}}
    {{< filetree/folder name="src" >}}
    {{< /filetree/folder >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

 {{% content "deploy-git" %}}

{{% content "more-config" %}}

{{% content "url_healthcheck" %}}
{{% content "request-flow" %}}
