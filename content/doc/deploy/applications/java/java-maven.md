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

Note: Clever Cloud passes the port of your application as the `http.port` system property: `8080`, or `9000` with [Request Flow](/doc/manage/request-flow/). Your application listens on `0.0.0.0`, on this port. [Learn more about the port of your application](/doc/manage/#listen-on-the-right-port).

Maven is essentially a project management and comprehension tool and as such provides a way to help with managing:

- Builds
- Documentation
- Reporting
- Dependencies
- SCMs
- Releases
- Distribution

## Configure your Java application

### About Cargo

To run your app, you can, for example, use plugins like cargo ([Find it here](https://codehaus-cargo.github.io/cargo/Maven+3+Plugin.html)).
Your application must listen on the port of the `http.port` system property.

{{% include "shared/java-versions" %}}

{{< runtimes_versions java >}}

(`graalvm-ce` for GraalVM 21.0.0.2, based on OpenJDK 11.0)

### Mandatory configuration

Unless you set `CC_RUN_COMMAND`, define the goal that starts your application in `CC_MAVEN_DEPLOY_GOAL`, for example `CC_MAVEN_DEPLOY_GOAL="spring-boot:run"` for a Spring Boot application with `spring-boot-maven-plugin`. The former `MAVEN_DEPLOY_GOAL` name remains supported as an alias.

### Build goal

By default, Clever Cloud builds your application with `mvn package`. To use another goal, set `CC_MAVEN_BUILD_GOAL`, for example `CC_MAVEN_BUILD_GOAL="clean install -DskipTests"`.

To build with Ant, a `clevercloud/maven.json` file is the only way: set `ant` in `build.type`, and the target in `build.goal`.

### Custom Maven settings

To use your own Maven configuration, such as credentials for a private repository or a mirror, commit a `clevercloud/settings.xml` file. Clever Cloud copies it to `~/.m2/settings.xml` before the build. This applies to every Java build, whatever the build system, so dependencies Maven resolves on behalf of another tool use it too.

### Specifying a profile

To activate a Maven profile, set it in `CC_MAVEN_PROFILES`, such as `CC_MAVEN_PROFILES="prod"`, or add `-P` to a goal, such as `CC_MAVEN_BUILD_GOAL="-Pprod package"` for the build.

 {{% include "shared/new-relic" %}}

{{% include "shared/java-env-injection" %}}

## Custom run command

If you need to run a custom command
you can specify it through the `CC_RUN_COMMAND` environment variable.
This will override the default `maven run` we use to run your application.

Example:

```bash
CC_RUN_COMMAND="java -jar somefile.jar <options>"
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
