---
type: docs
linkTitle: WAR and EAR
title: WAR and EAR
description: Deploy WAR and EAR packages on Clever Cloud in Tomcat, Jetty, WildFly, or Payara, built by Clever Cloud or committed to your repository
keywords:
- ear
- jakarta ee
- jetty
- payara
- servlet container
- tomcat
- war
- wildfly
aliases:
- /deploy/application/java/java-war
- /doc/applications/java/java-war
- /doc/applications/java/war/
- /doc/deploy/application/java/java-war
- /doc/java-war
- /doc/java/java-war
---

## Overview

A WAR file packages a Java web application, with its servlets, pages, and libraries, for a servlet container. An EAR file groups several modules for an application server. Clever Cloud starts the container of your choice, Tomcat, Jetty, WildFly, or Payara, and deploys your packages in it. The [Java page](/doc/deploy/applications/java/) describes what all Java applications share: the Java version, the variables, and the caches.

## Create your WAR application

To create a new WAR application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type war
```

## Configure your WAR application

A `clevercloud/war.json` file is mandatory: it sets the container and the packages to deploy, which no environment variable replaces. For instance, a servlet packaged as a WAR by Maven:

```xml {filename="pom.xml"}
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.example</groupId>
  <artifactId>hello</artifactId>
  <version>1.0.0</version>
  <packaging>war</packaging>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <dependency>
      <groupId>jakarta.servlet</groupId>
      <artifactId>jakarta.servlet-api</artifactId>
      <version>6.0.0</version>
      <scope>provided</scope>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.5.1</version>
      </plugin>
    </plugins>
  </build>
</project>
```

```java {filename="src/main/java/com/example/hello/HelloServlet.java"}
package com.example.hello;

import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.setContentType("text/plain");
        response.getWriter().println("Hello from a WAR on Clever Cloud");
    }
}
```

Here, Maven builds the WAR, which Tomcat 10.1 serves at the root of the domain:

```json {filename="clevercloud/war.json"}
{
  "build": {
    "type": "maven",
    "goal": "package"
  },
  "deploy": {
    "container": "TOMCAT10",
    "war": [
      {
        "file": "target/hello-1.0.0.war",
        "context": "/",
        "checkMe": "/hello"
      }
    ]
  }
}
```

The container listens on the port Clever Cloud sets, with a heap size that depends on the memory of the instance.

### Build the package

With `war.json`, Clever Cloud doesn't detect the build tool from the files of your project. Its `build` object runs Maven with a goal, such as `mvn package`, after the pre-build [hook](/doc/manage/build-hooks/) and before the deployment of the WAR.

For a Gradle project, leave the `build` object out and set the task in `CC_GRADLE_BUILD_GOAL` instead, such as `war`. Without either, Clever Cloud skips the build: commit the WAR or EAR files to deploy.

### Deploy the packages

`deploy.war` lists the packages to deploy, each with these fields:

- `file`: the path of the WAR or EAR file, from the folder of your project
- `context`: the path the application answers on, such as `/` or `/app`
- `checkMe`: a path that must answer for the deployment to succeed, context included

Without `context`, a WAR answers on its name without the extension, such as `/hello-1.0.0`. Set `checkMe` to a path of your application, such as `/hello-1.0.0/hello`: the [health check](/doc/manage/healthcheck/) then waits until it answers. Deploy an EAR in WildFly or Payara, which are application servers.

### Containers

`deploy.container` accepts these values, with end-of-life (EOL) versions marked. For a new application, use Tomcat 10.1:

| Value       | Container        |
| ----------- | ---------------- |
| `JETTY9`    | Jetty 9.4 (EOL)  |
| `JETTY11`   | Jetty 11 (EOL)   |
| `PAYARA5`   | Payara 5 (EOL)   |
| `PAYARA6`   | Payara 6 (EOL)   |
| `TOMCAT8`   | Tomcat 8 (EOL)   |
| `TOMCAT9`   | Tomcat 9         |
| `TOMCAT10`  | Tomcat 10.1      |
| `WILDFLY27` | WildFly 27 (EOL) |
| `WILDFLY33` | WildFly 33 (EOL) |

Tomcat 10, Jetty 11, WildFly 27 and later, and Payara 6 use the `jakarta.*` packages of Jakarta EE 9 and later. The other containers use the former `javax.*` packages. Another value fails at start: `No enum constant com.clevercloud.cargostarter.ContainerEnum`.

## Environment variables

Your application reads its [environment variables](/doc/manage/environment-variables/) from its environment, and from the system properties of the container:

```java
String fromEnvironment = System.getenv("MY_VARIABLE");
String fromProperties = System.getProperty("MY_VARIABLE");
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/java" title="Java" subtitle="Java version, memory, variables, caches, and tasks" icon="java" >}}
  {{< card link="/developers/doc/deploy/applications/java/java-gradle" title="Gradle" subtitle="Build with Gradle or its wrapper, and start a JAR or a task" icon="simple:gradle" >}}
  {{< card link="/developers/doc/deploy/applications/java/java-maven" title="Maven" subtitle="Build with Maven or its wrapper, and start a JAR or a goal" icon="simple:apachemaven" >}}
{{< /cards >}}
