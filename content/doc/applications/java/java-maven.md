---
type: docs
title: Maven
position: 3
shortdesc: Maven is essentially a project management and comprehension tool…
tags:
- deploy
keywords:
- java
- maven
str_replace_dict:
  "@application-type@": "Java + Maven"
aliases:
- /doc/deploy/application/java/java-maven
- /doc/deploy/application/java/
type: docs
---

## Overview

Clever Cloud offers you to run your Java Maven projects. You can deploy this kind of project without changing your code, but running it on Clever Cloud needs specific environment variables or configuration files, to add parameters like your targeted container for instance.

Note : like other runtimes, Java application needs to listen on `0.0.0.0:8080`

Maven is essentially a project management and comprehension tool and as such provides a way to help with managing:

* Builds
* Documentation
* Reporting
* Dependencies
* SCMs
* Releases
* Distribution

{{< content "create-application" >}}

{{< content "set-env-vars" >}}

## Configure your Java application

### About Cargo

To run your app, you can, for example, use plugins like cargo ([Find it here](https://codehaus-cargo.github.io/cargo/Maven+3+Plugin.html)).
Your application must be set to listen on the port 8080.

{{< content "java-versions" >}}

{{< runtimes_versions java >}}

(`graalvm-ce` for GraalVM 21.0.0.2, based on OpenJDK 11.0)

### Mandatory configuration

#### Option 1: JSON file in repository

The `clevercloud/maven.json` (maven.json file in clevercloud folder which is at the root of your repository) file must contain the _goal_ field to indicate how to start your application:

```json
  {
    "deploy": {
      "goal": "yourgoal"
    }
  }
```

An example of what can be found as a goal value is:

```txt
"-Dtest.active=false -Dexec.mainClass=\"com.example.Main\" assembly:jar-with-dependencies exec:java"
```

#### Option 2: Environment variable

If you don't want to add a file to your repository, or if you're using a monorepo with multiple applications in directories configured with the `APP_FOLDER` environment variable, you'll probably prefer to use an environment variable for deployment configuration.

Simply define `MAVEN_DEPLOY_GOAL="yourgoal"` and it's OK

Eg. `MAVEN_DEPLOY_GOAL="spring-boot:run"` for a Spring Boot application with spring-boot-maven-plugin

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

| Usage    | Field             | Description                                                               |
|----------|-------------------|---------------------------------------------------------------------------|
| Optional | **build → type**  | can be `maven`, `gradle` or `ant`                                         |
| Optional | **build → goal**  | is the target you want to use to build your project                       |
| Required | **deploy → goal** | the goal/target and options you want to execute to deploy/run you project |

### Specifying a profile

If you need to specify a maven profile (either for the `build` or the `deploy` goal, you can add it in the `goal` section:

```txt
"-Pmyprofile package"
```

Or use the `CC_MAVEN_PROFILES` environment variable.

Eg. `CC_MAVEN_PROFILES="prod"`.

## Custom run command

If you need to run a custom command
you can specify it through the `CC_RUN_COMMAND` environment variable.
This will override the default `maven run` we use to run your application.

Example:

```bash
CC_RUN_COMMAND="java -jar somefile.jar <options>"
```

 {{< content "new-relic" >}}

 {{< content "deploy-git" >}}

 {{< content "link-addon" >}}

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}
