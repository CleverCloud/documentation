---
title: Gradle deployment
position: 3
shortdesc: Gradle is a project automation tool that builds…
tags:
- java
---

Clever Cloud offers you to run your Gradle projects. You can deploy this kind of project
without changing your code, but running it on Clever Cloud needs some configuration files,
to add parameters like your gradle task for example.

Note : like other runtimes, Java application need listen on `0.0.0.0:8080`

## Overview

Gradle is a project automation tool that builds upon the concepts of
Apache Ant and Apache Maven and introduces a Groovy-based
domain-specific language (DSL) instead of the more traditional XML form
of declaring the project configuration.

## Create an application

Refer to the page [Deploy an application on Clever Cloud](/doc/clever-cloud-overview/add-application/).

## Necessary information

You *must* provide a `clevercloud/gradle.json` file (gradle.json file in
clevercloud folder which is at the root of you application) that
contains at least the following:

```javascript
{
    "deploy": {
        "goal": "grails:run"
    }
}
```

That is the only option you really need to supply.

## Optional configuration

The full configuration can look like the following:

```javascript
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
      <td>**build -&gt; type**</td>
      <td>can be ``"maven"``, ``"gradle"`` or ``"ant"``</td>
    </tr>
    <tr>
      <td><span class="label label-default">Optional</span></td>
      <td>**build -&gt; goal**</td>
      <td>is the target you want to use to build your project</td>
    </tr>
    <tr>
      <td><span class="label label-danger">Required</span></td>
      <td>**deploy -&gt; goal**</td>
      <td>the goal/target and options you want to execute to deploy/run you project</td>
    </tr>
  </tbody>
</table>

## The Gradle Wrapper

Since Gradle can come in many versions, Clever Cloud automatically support the
[Gradle Wrapper|http://www.gradle.org/docs/current/userguide/gradle_wrapper.html]:
Just create and commit the `gradlew` file and the wrapper `jar` and
`properties` files:

```haskell
./
	clevercloud/
		gradle.json
	gradlew
	gradle/wrapper/
		gradle-wrapper.jar
		gradle-wrapper.properties
	src/
```

## Custom run command

If you need to run a custom command
you can specify it through the `CC_RUN_COMMAND` environment variable.
This will override the default way of runing your application.

Example:

```
CC_RUN_COMMAND=java -jar somefile.jar <options>
```


## Environment injection

Clever Cloud can inject environment variables that are defined in the
dashboard and by add-ons linked to your application.

For Java applications, the environment is injected in the
`System.getProperties()` object. So, to use a variable, you just do
`System.getProperties().getProperty("MY_VARIABLE")`.

For Groovy applications, just use the `System.getProperty("MY_VARIABLE")`.
