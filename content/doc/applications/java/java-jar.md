---
type: docs
title: Jar
position: 1
shortdesc: Deploy a jar on Clever Cloud…
keywords:
- deploy
tags:
- java
str_replace_dict:
  "@application-type@": "Java + JAR"
aliases:
- /doc/deploy/application/java/java-jar
type: docs
---

## Overview

Clever Cloud offers you to run any Java ARchive file. You do not need to change your code, but running it on Clever Cloud needs some configuration files or environment variable to specify the JAR path.

Note : like other runtimes, Java application needs to listen on `0.0.0.0:8080`

{{< content "create-application" >}}

{{< content "set-env-vars" >}}

{{< content "java-versions" >}}

{{< runtimes_versions java >}}

(`graalvm-ce` for GraalVM 21.0.0.2, based on OpenJDK 11.0)

## Configure your Java application

You *must* either have the `CC_JAR_PATH` environment variable containing the
path to your jar or provide a `clevercloud/jar.json` file (jar.json file in
clevercloud folder which is at the root of your repository) that
contains at least the following:

```json
{
  "deploy": {
    "jarName": "path/to/jar"
  }
}
```

That is the least you need to do. Note that `path/to/jar` *must not* start with a `/` and that the path should be relative to your repository's root.

### Build options

You do not need to build and commit a JAR. Instead you can push your
sources and build them with either gradle, ant or maven. Here is the
configuration you need to provide in the `clevercloud/jar.json` file:

```json
{
  "build": {
    "type": "maven"|"gradle"|"ant",
    "goal": "package"
  }
}
```

The `goal` field is what will be asked to the build command, like `mvn package` for a `maven` build with the `package` goal.

An configuration example with a maven build that generates a JAR with
embedded dependencies is:

```json
{
  "build": {
    "type": "maven",
    "goal": "package"
  },
  "deploy": {
    "jarName": "target/myproject-1.0-jar-with-dependencies.jar"
  }
}
```

### An example of full configuration

You can pass extra arguments to the `java` command by using the environment
variable `CC_EXTRA_JAVA_ARGS` and to your JAR by using `CC_JAR_ARGS`

The full configuration can look like the following:

```json
{
  "build": {
    "type": "<string>",
    "goal": "<string>"
  },
  "deploy": {
    "goal": "<string>",
    "jarName": "<string>"
  }
}
```

You can use the following properties:

| Usage    | Field               | Description                                                               |
|----------|---------------------|---------------------------------------------------------------------------|
| Optional | **build → type**    | can be `maven`, `gradle` or `ant`                                         |
| Optional | **build → goal**    | is the target you want to use to build your project                       |
| Optional | **deploy → goal**   | the goal/target and options you want to execute to deploy/run you project |
| Required | **build → jarName** | jar file name of your application                                         |

 {{< content "new-relic" >}}

## Custom run command

If you need to run a custom command (or just pass options to the program),
you can specify it through the `CC_RUN_COMMAND` environment variable.
This will override the default way of running your application.

Example:

```bash
CC_RUN_COMMAND="java -jar somefile.jar <options>"
```

### Environment injection

Clever Cloud can inject environment variables that are defined in the
dashboard and by add-ons linked to your application.

For Java applications, the environment is injected in the `System.getProperties()` object.

So, to use a variable, you just need `System.getProperties().getProperty("MY_VARIABLE")`.

For Groovy applications, just use the `System.getProperty("MY_VARIABLE")`.

 {{< content "deploy-git" >}}

 {{< content "link-addon" >}}

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}
