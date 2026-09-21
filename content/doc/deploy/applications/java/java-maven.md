---
type: docs
linkTitle: Maven
title: Maven
description: Deploy Java applications using Maven build system on Clever Cloud with automatic dependency management and build lifecycle
keywords:
- java
- maven
- build-system
- dependencies
- deployment
- lifecycle
aliases:
- /deploy/application/java/java-maven
- /doc/applications/java/java-maven
- /doc/deploy/application/java/java-maven
- /doc/deploy/application/java/old_java-maven
- /doc/java/java-maven
---

## Overview

Clever Cloud offers you to run your Java Maven projects. You can deploy this kind of project without changing your code, but running it on Clever Cloud needs specific environment variables or configuration files, to add parameters like your targeted container for instance.

Note : like other runtimes, Java application needs to listen on `0.0.0.0:8080`

Maven is essentially a project management and comprehension tool and as such provides a way to help with managing:

- Builds
- Documentation
- Reporting
- Dependencies
- SCMs
- Releases
- Distribution

{{% content "create-application" %}}

{{% content "set-env-vars" %}}

## Configure your Java application

### About Cargo

To run your app, you can, for example, use plugins like cargo ([Find it here](https://codehaus-cargo.github.io/cargo/Maven+3+Plugin.html)).
Your application must be set to listen on the port 8080.

{{% content "java-versions" %}}

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

Define the goal in the `CC_MAVEN_DEPLOY_GOAL` environment variable, for example `CC_MAVEN_DEPLOY_GOAL="spring-boot:run"` for a Spring Boot application with `spring-boot-maven-plugin`. The former `MAVEN_DEPLOY_GOAL` name remains supported as an alias.

### Build goal

By default, Clever Cloud builds your application with `mvn package`. To use another goal, set `CC_MAVEN_BUILD_GOAL`, for example `CC_MAVEN_BUILD_GOAL="clean install -DskipTests"`. It takes precedence over the `build.goal` field of the `clevercloud/maven.json` file.

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

| Usage    | Field             | Description                                                                                                                         |
| -------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Optional | **build → type**  | can be `maven`, `gradle` or `ant`                                                                                                   |
| Optional | **build → goal**  | is the target you want to use to build your project                                                                                 |
| Required | **deploy → goal** | the goal/target and options you want to execute to deploy/run you project, unless `CC_MAVEN_DEPLOY_GOAL` or `CC_RUN_COMMAND` is set |

When `build.type` is `maven`, `gradle` or `sbt`, Clever Cloud uses the same build setup as for an automatically detected project, including your Maven `settings.xml`. Any other value runs a generic build.

### Custom Maven settings

To use your own Maven configuration, such as credentials for a private repository or a mirror, commit a `clevercloud/settings.xml` file. Clever Cloud copies it to `~/.m2/settings.xml` before the build. This applies to every Java build, whatever the build system, so dependencies Maven resolves on behalf of another tool use it too.

### Specifying a profile

If you need to specify a maven profile (either for the `build` or the `deploy` goal, you can add it in the `goal` section:

```txt
"-Pmyprofile package"
```

Or use the `CC_MAVEN_PROFILES` environment variable.

Eg. `CC_MAVEN_PROFILES="prod"`.

 {{% content "new-relic" %}}

{{% content "java-env-injection" %}}

## Custom run command

If you need to run a custom command
you can specify it through the `CC_RUN_COMMAND` environment variable.
This will override the default `maven run` we use to run your application.

Example:

```bash
CC_RUN_COMMAND="java -jar somefile.jar <options>"
```

 {{% content "deploy-git" %}}

 {{% content "link-addon" %}}

{{% content "more-config" %}}

{{% content "url_healthcheck" %}}
{{% content "request-flow" %}}
