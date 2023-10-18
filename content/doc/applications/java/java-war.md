---
type: docs
title: Java War/Ear deployment
position: 4
shortdesc: In JEE, applications modules are packaged as EAR and WAR based on their functionality.
tags:
- deploy
keywords:
- java
- war
str_replace_dict:
  "@application-type@": "Java + WAR"
type: docs
---

## Overview

Clever Cloud allows you to run WAR or EAR applications. You can deploy these projects without changing your code. We just need a configuration file with your targeted container.

In <abbr title="Java Enterprise Edition">JEE</abbr>, application modules are packaged as EAR and WAR based on their purpose.

* <abbr title="Web Archive">WAR</abbr>: Web modules which contains Servlet class files, JSP FIles, supporting files, GIF and HTML files are packaged as JAR file with *.war* extension.

* <abbr title="Enterprise Archive">EAR</abbr>: *.war* and *.jar* files are packaged as JAR file with .ear extension and deployed into Application Server. EAR file contains configuration such as application security role mapping, EJB reference mapping and context root url mapping of web modules.

Note : like other runtimes, Java application needs to listen on `0.0.0.0:8080`

## Available containers

Clever Cloud supports many servlet containers.
The supported containers are listed below:

<table id="containers" class="table table-bordered table-striped">
   <thead>
      <tr>
         <th>Apache</th>
         <th>Jetty</th>
         <th>Jboss</th>
         <th>Glassfish</th>
         <th>Payara</th>
         <th>Resin</th>
         <th>Wildfly</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>Apache Tomcat 4.1 (TOMCAT4)</td>
         <td>Jetty 6.1 (JETTY6)</td>
         <td>Jboss 6.1 (JBOSS6)</td>
         <td>Glassfish 3.1 (GLASSFISH3)</td>
         <td>Payara 4.1 (PAYARA4)</td>
         <td>Resin 3.1 (RESIN3)</td>
         <td>WildFly 9.0.2 (WILDFLY9)</td>
      </tr>
      <tr>
         <td>Apache Tomcat 5.5 (TOMCAT5)</td>
         <td>Jetty 7.6 (JETTY7)</td>
         <td>Jboss AS 7.1 (JBOSS7)</td>
         <td>Glassfish 4.1 (GLASSFISH4)</td>
         <td></td>
         <td></td>
         <td>WildFly 17.0.1 (WILDFLY17)</td>
      </tr>
      <tr>
         <td>Apache Tomcat 6.0 (TOMCAT6)</td>
         <td>Jetty 8.1 (JETTY8)</td>
         <td></td>
         <td></td>
         <td></td>
         <td></td>
         <td>WildFly 23.0.2 (WILDFLY23)</td>
      </tr>
      <tr>
         <td>Apache Tomcat 7.0 (TOMCAT7)</td>
         <td>Jetty 9.0 (JETTY9)</td>
         <td></td>
         <td></td>
         <td></td>
         <td></td>
         <td>WildFly 24.0.1 (WILDFLY24)</td>
      </tr>
      <tr>
         <td>Apache Tomcat 8.8 (TOMCAT8)</td>
         <td></td>
         <td></td>
         <td></td>
         <td></td>
         <td></td>
         <td></td>
      </tr>
   </tbody>
</table>

{{< readfile file="/content/partials/create-application.md" >}}

{{< readfile file="/content/partials/set-env-vars.md" >}}

{{< readfile file="/content/partials/java-versions.md" >}}

## Configure your Java application

{{< callout type="warning" >}}
<p>You <strong>must</strong> provide a <code>clevercloud/war.json</code> file in your application repository.</p>
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
      "container": "TOMCAT8",
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

### Ok, but what does all this configuration mean?

#### Let's start with the mandatory part

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
         <td>
            <span class="label label-danger">Required</span>
         </td>
         <td><strong>container</strong></td>
         <td>Name of the container to use. Should contain one of the values inside parentheses in the <a href="#available-containers">containers table</a> (in uppercase and all).</td>
      </tr>
      <tr>
         <td>
            <span class="label label-danger">Required</span>
         </td>
         <td><strong>file</strong></td>
         <td>Should contain the path of the war/ear file relative to your application root.</td>
      </tr>
      <tr>
         <td>
            <span class="label label-default">Optional</span>
         </td>
         <td><strong>context</strong></td>
         <td>
            <ul>
               <li>Must start with a slash (/), can be "/".</li>
               <li>Defines the base path you want your app to be under. If your app has a /foobar endpoint, it will be available under the <code>/{my-context}/foobar</code> path.</li>
               <li>Not needed for an <code>ear</code> file.</li>
               <li>The default value for a war is the name of the war without the extensions: helloworld-1.0.war will be deployed under the <code>/helloworld-1.0</code> context.</li>
            </ul>
         </td>
      </tr>
      <tr>
         <td>
            <span class="label label-default">Optional</span>
         </td>
         <td><strong>checkMe</strong></td>
         <td>
            <ul>
               <li>This field is recommended</li>
               <li>A path to GET in order to test if the application is really running.</li>
               <li>By default we will consider that the application is up if the container is up.</li>
               <li>With this option, we will try to <code>GET /{checkMe}</code> for each one of your wars and consider the app down until every single checkMe path that replies a 200.</li>
            </ul>
         </td>
      </tr>
   </tbody>
</table>

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
         <td>
            <span class="label label-danger">Required</span>
         </td>
         <td><strong>type</strong></td>
         <td>
            <ul>
               <li>The tool you want to use to build your app</li>
               <li>Can be "maven", "gradle", "sbt" or "ant"</li>
            </ul>
         </td>
      </tr>
      <tr>
         <td>
            <span class="label label-danger">Required</span>
         </td>
         <td><strong>goal</strong></td>
         <td>
            <ul>
               <li>The goal you want the tool to execute.</li>
               <li>Basically, for maven, you want to put "package" in here.</li>
            </ul>
         </td>
      </tr>
   </tbody>
</table>

## Available containers

Here's the list of the configuration values for the "container" field in `war.json`:

<table class="table table-bordered table-stripped">
   <thead>
      <tr>
         <th>Value</th>
         <th>Description</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>GLASSFISH3</td>
         <td>Use Glassfish 3.x (see <a href="https://glassfish.java.net/">https://glassfish.java.net/</a>)</td>
      </tr>
      <tr>
         <td>GLASSFISH4</td>
         <td>Use Glassfish 4.x (see <a href="https://glassfish.java.net/">https://glassfish.java.net/</a>)</td>
      </tr>
      <tr>
         <td>JBOSS6</td>
         <td>Use JBoss AS 6.x (see <a href="https://www.jboss.org/jbossas">https://www.jboss.org/jbossas</a>)</td>
      </tr>
      <tr>
         <td>JBOSS7</td>
         <td>Use JBoss AS 7.x (see <a href="https://www.jboss.org/jbossas">https://www.jboss.org/jbossas</a>) </td>
      </tr>
      <tr>
         <td>RESIN3</td>
         <td>Use Resin AS 3.x (see <a href="https://www.caucho.com/resin-3.1/doc/">https://www.caucho.com/resin-3.1/doc/</a>)</td>
      </tr>
      <tr>
         <td>RESIN4</td>
         <td>Use Resin AS 4.x (see <a href="https://www.caucho.com/resin-4/doc/">https://www.caucho.com/resin-4/doc/</a>)</td>
      </tr>
      <tr>
         <td>JETTY6</td>
         <td>Use Jetty servlet container 6.x (see <a href="https://jetty.codehaus.org/jetty/">https://jetty.codehaus.org/jetty/</a>)</td>
      </tr>
      <tr>
         <td>JETTY7</td>
         <td>Use Jetty servlet container 7.x (see <a href="https://www.eclipse.org/jetty/">https://www.eclipse.org/jetty/</a>)</td>
      </tr>
      <tr>
         <td>JETTY8</td>
         <td>Use Jetty servlet container 8.x (see <a href="https://www.eclipse.org/jetty/">https://www.eclipse.org/jetty/</a>)</td>
      </tr>
      <tr>
         <td>JETTY9</td>
         <td>Use Jetty servlet container 9.x (see <a href="https://www.eclipse.org/jetty/documentation/current/">https://www.eclipse.org/jetty/documentation/current/</a>)</td>
      </tr>
      <tr>
         <td>TOMCAT4</td>
         <td>Use Tomcat servlet container 4.x (see <a href="https://tomcat.apache.org/">https://tomcat.apache.org/</a>)</td>
      </tr>
      <tr>
         <td>TOMCAT5</td>
         <td>Use Tomcat servlet container 5.x (see <a href="https://tomcat.apache.org/">https://tomcat.apache.org/</a>)</td>
      </tr>
      <tr>
         <td>TOMCAT6</td>
         <td>Use Tomcat servlet container 6.x (see <a href="https://tomcat.apache.org/">https://tomcat.apache.org/</a>)</td>
      </tr>
      <tr>
         <td>TOMCAT7</td>
         <td>Use Tomcat servlet container 7.x (see <a href="https://tomcat.apache.org/">https://tomcat.apache.org/</a>)</td>
      </tr>
      <tr>
         <td>TOMCAT8</td>
         <td>Use Tomcat servlet container 8.x (see <a href="https://tomcat.apache.org/">https://tomcat.apache.org/</a>)</td>
      </tr>
      <tr>
         <td>PAYARA4</td>
         <td>Use Payara servlet container 4.x (see <a href="https://www.payara.fish/">https://www.payara.fish/</a>)</td>
      </tr>
      <tr>
         <td>WILDFLY9</td>
         <td>Use Wildfly servlet container 9.x (see <a href="https://wildfly.org/">https://wildfly.org/</a>)</td>
      </tr>
      <tr>
         <td>WILDFLY17</td>
         <td>Use Wildfly servlet container 17.x (see <a href="https://wildfly.org/">https://wildfly.org/</a>)</td>
      </tr>
      <tr>
         <td>WILDFLY23</td>
         <td>Use Wildfly servlet container 23.x (see <a href="https://wildfly.org/">https://wildfly.org/</a>)</td>
      </tr>
   </tbody>
</table>

## Custom run command

If you need to run a custom command
you can specify it through the `CC_RUN_COMMAND` environment variable.
This will override the default way of running your application.

Example:

```bash
CC_RUN_COMMAND="java -jar somefile.jar <options>"
```

{{< readfile file="/content/partials/new-relic.md" >}}

{{< readfile file="/content/partials/deploy-git.md" >}}

{{< readfile file="/content/partials/link-addon.md" >}}

{{< readfile file="/content/partials/more-config.md" >}}
