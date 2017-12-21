---
title: Java Maven
position: 3
shortdesc: Maven is essentially a project management and comprehension tool...
tags:
- java
---

# Deploy Java Maven projects

Clever Cloud offers you to run your Java Maven projects. You can deploy this kind of project without changing your code, but running it on Clever Cloud needs some configuration files, to add parameters like your targeted container for instance.

Note : like other runtimes, Java application need listen on `0.0.0.0:8080`

## Overview
Maven is essentially a project management and comprehension tool and as such provides a way to help with managing:

* Builds
* Documentation
* Reporting
* Dependencies
* SCMs
* Releases
* Distribution


## About Cargo
To run your app, you can, for example, use plugins like cargo
(<a href="https://codehaus-cargo.github.io/cargo/Maven2+plugin.html">Find it here</a>).
Your application must be set to listen on the port 8080.

## Create an application

Refer to the page [Deploy an application on Clever Cloud](/doc/clever-cloud-overview/add-application/).

## Necessary information

The `clevercloud/maven.json` (maven.json file in clevercloud folder which is at the root of you application) file must contain the _goal_ field to indicate how to start your application:

```javascript
  {
    "deploy": {
      "goal": "yourgoal"
    }
  }
```

An example of what can be found as a goal value is:  

```haskell
"-Dtest.active=false -Dexec.mainClass=\"com.example.Main\" assembly:jar-with-dependencies exec:java"
```

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

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via Git. Follow [these steps](/doc/clever-cloud-overview/add-application/) to deploy your application.

## Specifying a profile

If you need to specify a maven profile (either for the `build` or the `deploy` goal, you can add it in the `goal` section:

```haskell
"-Pmyprofile package"
```