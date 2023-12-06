---
type: docs
title: Gradle
position: 2
shortdesc: Gradle is a project automation tool that builds…
tags:
- deploy
keywords:
- java
- gradle
str_replace_dict:
  "@application-type@": "Java or Groovy + Gradle" 
aliases:
- /doc/deploy/application/java/java-gradle
type: docs
---

## Overview

Clever Cloud offers you to run your Gradle projects. You can deploy this kind of project without changing your code, but running it on Clever Cloud needs some configuration files or environment variables, to add parameters like your gradle task for example.

Gradle is a project automation tool that builds upon the concepts of Apache Ant and Apache Maven and introduces a Groovy-based domain-specific language (DSL) instead of the more traditional XML form of declaring the project configuration.

Note : like other runtimes, Java application need listen on `0.0.0.0:8080`

{{< readfile file="create-application.md" >}}

{{< readfile file="set-env-vars.md" >}}

{{< readfile file="java-versions.md" >}}

## Configure your Java application

You *must* provide a `clevercloud/gradle.json` file (gradle.json file in
clevercloud folder which is at the root of your repository) that
contains at least the following:

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

<table class="table table-bordered table-striped">
  <thead>
    <tr>
      <th>Usage</th>
      <th>Field</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="label label-default">Optional</span></td>
      <td><strong>build -&gt; type</strong></td>
      <td>can be <code>maven</code>, <code>gradle</code> or <code>ant</code></td>
    </tr>
    <tr>
      <td><span class="label label-default">Optional</span></td>
      <td><strong>build -&gt; goal</strong></td>
      <td>is the target you want to use to build your project</td>
    </tr>
    <tr>
      <td><span class="label label-danger">Required</span></td>
      <td><strong>deploy -&gt; goal</strong></td>
      <td>the goal/target and options you want to execute to deploy/run you project</td>
    </tr>
  </tbody>
</table>

## Custom run command

If you need to run a custom command
you can specify it through the `CC_RUN_COMMAND` environment variable.
This will override the default way of runing your application.

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

## The Gradle Wrapper

Since Gradle can come in many versions, Clever Cloud automatically support the [Gradle Wrapper|https://www.gradle.org/docs/current/userguide/gradle_wrapper.html].

Just create and commit the `gradlew` file and the wrapper `jar` and `properties` files:

```txt
./
	clevercloud/
		gradle.json
	gradlew
	gradle/wrapper/
		gradle-wrapper.jar
		gradle-wrapper.properties
	src/
```

{{< readfile file="new-relic.md" >}}

{{< readfile file="deploy-git.md" >}}

{{< readfile file="more-config.md" >}}

{{< readfile file="url_healthcheck.md" >}}
