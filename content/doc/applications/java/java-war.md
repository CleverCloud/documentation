---
type: docs
linkTitle: War/Ear
title: War/Ear
description: Deploy WAR and EAR Java Enterprise (JEE) applications on Clever Cloud with support for various containers and servlet technologies
keywords:
- java
- war
- ear
- jee
- containers
- deployment
aliases:
- /deploy/application/java/java-war
- /doc/deploy/application/java/java-war
- /doc/java/java-war
- /doc/java-war
---

## Overview

Clever Cloud allows you to run WAR or EAR applications. You can deploy these projects without changing your code. We just need a configuration file with your targeted container.

In {{< tooltip title="JEE">}}JEE{{< /tooltip >}}, application modules are packaged as EAR and WAR based on their purpose.

* {{< tooltip title="WAR" >}}WAR{{< /tooltip >}}: Web modules which contains Servlet class files, JSP FIles, supporting files, GIF and HTML files are packaged as JAR file with *.war* extension.

* {{< tooltip title="EAR" >}}EAR{{< /tooltip >}}: `*.war` and `*.jar` files are packaged as JAR file with `.ear` extension and deployed into Application Server. EAR file contains configuration such as application security role mapping, EJB reference mapping and context root URL mapping of web modules.

Note: like other runtimes, your Java application needs to listen on `0.0.0.0:8080`.

{{% content "create-application" %}}

{{% content "set-env-vars" %}}

{{% content "java-versions" %}}

{{< runtimes_versions java >}}

(`graalvm-ce` for GraalVM 21.0.0.2, based on OpenJDK 11.0)

## Configure your Java application

{{< callout type="warning" >}}
You **must** provide a `clevercloud/war.json` file in your application repository.
{{< /callout >}}

### Full configuration example

Here's what your configuration file can look like:

```json
{
   "build": {
      "type": "maven",
      "goal": "package"
   },
   "deploy": {
      "container": "TOMCAT10",
      "war": [
         {
            "file": "target/my-app-1.0-SNAPSHOT.war",
            "context": "/app1",
            "checkMe": "/app1/ping"
         },
         {
            "file": "my-second-app.war",
            "context": "/app2",
            "checkMe": "/app2/web/foobar"
         }
      ]
   }
}
```

### Breaking down the configuration

#### Requirements

Here are the mandatory fields:

```json
{
   "deploy": {
      "container":"<string>",
      "war": [
         {
            "file": "<string>",
            "context": "/<string>",
            "checkMe": "/<string>"
         }
      ]
   }
}
```

|Usage     |Field   |Description|
|----------|--------|------------------------------------------------------------------------|
|Required  |**container**|Name of the container to use. Should contain one of the values inside parentheses in the containers table (uppercase).|
|Required  |file         |Should contain the path of the war/ear file relative to your application root.|
| Optional |context      |- Must start with a slash (/), can be "/" <br>- Defines the base path you want your app to be under. If your app has a /foobar endpoint, it will be available under the `/{my-context}/foobar` path. <br>- Not needed for an `ear` file. <br>- The default value for a war is the name of the war without the extensions: helloworld-1.0.war will be deployed under the `/helloworld-1.0` context.|
| Optional |checkMe      |- This field is recommended. <br>- A path to GET in order to test if the application is really running. <br>- By default we will consider that the application is up if the container is up. <br>- With this option, we will try to GET `/{checkMe}` for each one of your wars and consider the app down until every single checkMe path that replies a 200.|

#### Let Clever Cloud build your application

The mandatory part alone is enough… if you directly push a dry war file to deploy. You
might want to just push your code to Clever Cloud and let us build the app and generate
the war.

That you can do, by setting the "build" field object in the `war.json` file:

```json
{
  "build": {
    "type": "<string>",
    "goal": "<string>"
  }
}
```

| Usage                           | Field | Description                                    |
|---------------------------------|-------|------------------------------------------------|
|Required | **type**  |- The tool you want to use to build your app. <br>- Can be "maven", "gradle", "sbt" or "ant" |
|Required | **goal**  |- The goal you want the tool to execute.<br>- Basically, for maven, you want to put "package" in here. |

## Available containers for war.json

Here's the list of the configuration values for the "container" field in `war.json` (with **End Of Life** versions tagged as `EOL`):

| Value      | Description                                                                                  | EOL |
|------------|----------------------------------------------------------------------------------------------|-----|
| JETTY9     | Use Jetty servlet container 9.x (see <https://jetty.org/download.html#version-history>)      | EOL |
| JETTY11    | Use Jetty servlet container 11.x (see <https://jetty.org/download.html#version-history>)     | EOL |
| PAYARA5    | Use Payara servlet container 5.x (see <https://www.payara.fish/>)                            | EOL |
| PAYARA6    | Use Payara servlet container 6.x (see <https://www.payara.fish/>)                            | EOL |
| TOMCAT8    | Use Tomcat servlet container 8.x (see <https://tomcat.apache.org/>)                          | EOL |
| TOMCAT9    | Use Tomcat servlet container 9.x (see <https://tomcat.apache.org/>)                          |     |
| TOMCAT10   | Use Tomcat servlet container 10.x (see <https://tomcat.apache.org/>)                         |     |
| WILDFLY9   | Use Wildfly servlet container 9.x (see <https://wildfly.org/>)                               | EOL |
| WILDFLY27  | Use Wildfly servlet container 27.x (see <https://wildfly.org/>)                              | EOL |
| WILDFLY33  | Use Wildfly servlet container 33.x (see <https://wildfly.org/>)                              | EOL |

{{% content "url_healthcheck" %}}
{{% content "request-flow" %}}

## Custom run command

If you need to run a custom command
you can specify it through the `CC_RUN_COMMAND` environment variable.
This will override the default way of running your application.

Example:

```bash
CC_RUN_COMMAND="java -jar somefile.jar <options>"
```

 {{% content "new-relic" %}}

 {{% content "deploy-git" %}}

 {{% content "link-addon" %}}

{{% content "more-config" %}}
