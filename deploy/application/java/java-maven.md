---
title: Java Maven deployment
position: 3
shortdesc: Maven is essentially a project management and comprehension tool...
tags:
- deploy
keywords:
- java
- maven
str_replace_dict:
  "@application-type@": "Java + Maven"
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

{{< readfile "/content/partials/create-application.md" >}}

{{< readfile "/content/partials/set-env-vars.md" >}}

## Configure your Java application

### About Cargo

To run your app, you can, for example, use plugins like cargo ([Find it here](https://codehaus-cargo.github.io/cargo/Maven+3+Plugin.html)).
Your application must be set to listen on the port 8080.

{{< readfile "/content/partials/java-versions.md" >}}

### Mandatory configuration

The `clevercloud/maven.json` (maven.json file in clevercloud folder which is at the root of you application) file must contain the _goal_ field to indicate how to start your application:

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

### Specifying a profile

If you need to specify a maven profile (either for the `build` or the `deploy` goal, you can add it in the `goal` section:

```txt
"-Pmyprofile package"
```

## Custom run command

If you need to run a custom command
you can specify it through the `CC_RUN_COMMAND` environment variable.
This will override the default `maven run` we use to run your application.

Example:

```bash
CC_RUN_COMMAND="java -jar somefile.jar <options>"
```

{{< readfile "/content/partials/new-relic.md" >}}

{{< readfile "/content/partials/deploy-git.md" >}}

{{< readfile "/content/partials/link-addon.md" >}}

{{< readfile "/content/partials/more-config.md" >}}
