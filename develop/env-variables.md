---
title: Environment variables
position: 8
shortdesc: How to setup and configure environment variables for apps and add-ons
tags:
- dashboard-setup
- apps
- develop
keywords:
- env
- variables
- environment variables
---

Clever Cloud allows you to define environment variables that will be
injected in your application's environment.

## How are variables defined?

Variables are defined on a per-application basis. They are defined in four ways:

 * By provisioned add-ons linked to applications. The variables names
   are listed in the add-on's information panel

 * By linked applications with exposed configuration

 * By adding variables yourself in the "Environment variables" panel of
   your application.

 * Some environment variables are added automatically for each application.

Please note that if you define or modify environment variables, you will
need to redeploy your application to make it use the new variables.

## Special environment variables

Some variables are injected to the environment of your application when you deploy it,
to inform you about the current context of your application and about the application itself.

They can be accessed as classic environment variables.

 * `APP_ID`: the ID of the application. Each application has a unique identifier used to
 identify it in our system. This ID is the same than the one you can find in the information
 section of your application.

 * `INSTANCE_ID`: the ID of the current instance (scaler) of your application. It's unique for each
 instance of your application and changes every time you deploy it.

 * `INSTANCE_TYPE`: The type of the instance (scaler). Its value can be `build` or `production`. `build` is when
 your application is being built on a [dedicated instance]({{< ref "administrate/apps-management.md#edit-application-configuration" >}}).

 * `COMMIT_ID`: the commit ID used as a base to deploy your application. As we remove
 the `.git` directory before the deployment (to avoid security problems), it can be used
 to know which version of your application is running on the server.

 * `APP_HOME`: The absolute path of your application on the server. Can be used to
 create absolute links in your application (e.g. ${APP_HOME}/foo/bar).

 * `CC_PRETTY_INSTANCE_NAME`: A random string name generated for each instance using pokemon names.

 * `INSTANCE_NUMBER`: See below

### What is the `INSTANCE_NUMBER` variable used for?

This variable allows your application to differentiate each running node on the application level.

It will contain a different number for each instance of your application.

For example, if three instances are running, it will contain `0` for the first, `1`
for the second and `2` for the third.
It's handy if you want to only run crons on 1 instance (e.g. only on instance 0)

## Settings you can define using environment variables

We use environment variables for some settings:

 * `IGNORE_FROM_BUILDCACHE`: allows you to specify paths to ignore when the build
 cache archive is created. Must be relative to your application root.
 (ex: `foo/bar:foo/baz` where `bar` or `baz` can be either a folder or a file)

* `CC_OVERRIDE_BUILDCACHE`: allows you to specify paths that will be in the build cache. Only those files / directories will be cached. (ex: `foo/bar:foo/baz` where `bar` or `baz` can be either a folder or a file)

## Variable definition constraints

*Spaces are not allowed* in the name of the variables.

## How do I use these variables?

Depending on the type of your application, you will need to use
different ways. You can find the various ways in the specific instances
documentations.

<table class="table table-bordered table-striped dataTable">
<tr>
<th>language</th>
<th>use case</th>
</tr>
<tr>
<td>[Go]({{< ref "deploy/application/golang/go#environment-injection" >}}) </td>
<td>Os.Getenv["MY\_VAR"]</td>
</tr>
<tr>
<td>[Haskell]({{< ref "deploy/application/haskell/haskell#environment-injection" >}})  </td>
<td>getEnv "MY\_VAR"</td>
</tr>
<tr>
<td>[Node.js]({{< ref "deploy/application/javascript/by-framework/nodejs#environment-injection" >}})  </td>
<td>process.env["MY\_VAR"]</td>
</tr>
<tr>
<td>[Java WAR]({{< ref "deploy/application/java/java-war#environment-injection" >}}) </td>
<td>System.getProperties().getProperty("MY\_VAR")</td>
</tr>
<tr>
<td>[PHP]({{< ref "deploy/application/php/php-apps#environment-injection" >}})</td>
<td>getenv("MY\_VAR")</td>
</tr>
<tr>
<td>[Play! Framework 1]({{< ref "deploy/application/java/by-framework/play-framework-1#environment-injection" >}})
& [Play! Framework 2]({{< ref "deploy/application/java/by-framework/play-framework-2#environment-injection" >}})</td>
<td>System.getenv("MY\_VAR") or ${MY\_VAR} in application.conf</td>
</tr>
<tr>
<td>[Python]({{< ref "deploy/application/python/python_apps#environment-injection" >}})</td>
<td>os.getenv("MY\_VAR")</td>
</tr>
<tr>
<td>[Ruby]({{< ref "deploy/application/ruby/ruby-rack#environment-injection" >}})</td>
<td>ENV["MY\_VAR"]<br></td>
</tr>
<tr>
<td>[Rust]({{< ref "deploy/application/rust/rust#environment-injection" >}})</td>
<td>std::env::var("MY\_VAR")<br></td>
</tr>
<tr>
<td>[Scala]({{< ref "deploy/application/scala/scala#environment-injection" >}}) </td>
<td>System.getenv("MY\_VAR")</td>
</tr>
</table>

Please note that the variables are available at build-time, for
runtimes that support build-time instructions, such as
[Java WAR]({{< ref "deploy/application/java/java-war#environment-injection" >}}),
[Play! Framework 1]({{< ref "deploy/application/java/by-framework/play-framework-1#environment-injection" >}}),
[Play! Framework 2]({{< ref "deploy/application/java/by-framework/play-framework-2#environment-injection" >}})
or [Scala]({{< ref "deploy/application/scala/scala#environment-injection" >}}).
