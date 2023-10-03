---
type: docs
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
type: docs
---

Clever Cloud allows you to define environment variables that will be
injected in your application's environment.

## How are variables defined?

Variables are defined on a per-application basis. They are defined in four ways:

* By provisioned add-ons linked to applications. The variables names
  are listed in the add-on's information panel.

* By linked applications with exposed configuration.

* By adding variables yourself in the "Environment variables" panel of your application.

* Some environment variables are added automatically for each application.

Please note that if you define or modify environment variables, you will
need to redeploy your application to make it use the new variables.

Check out our [environment variable reference]({{< ref "doc/reference/reference-environment-variables.md" >}}).

## Special environment variables

Some variables are injected to the environment of your application when you deploy it,
to inform you about the current context of your application and about the application itself.

They can be accessed as classic environment variables.

* `APP_ID`: the ID of the application. Each application has a unique identifier used to
  identify it in our system. This ID is the same than the one you can find in the information
  section of your application.

* `INSTANCE_ID`: the ID of the current instance (scaler) of your application. It's unique for each
  instance of your application and changes every time you deploy it.

* `INSTANCE_TYPE`: The type of the instance (scaler). Its value can be `build` or `production`.
  `build` is when your application is being built on a [dedicated instance][dedicated-instance].

* `COMMIT_ID`: the commit ID used as a base to deploy your application. As we remove
  the `.git` directory before the deployment (to avoid security problems), it can be used
  to know which version of your application is running on the server.

* `APP_HOME`: The absolute path of your application on the server. Can be used to
  create absolute links in your application (e.g. `${APP_HOME}/foo/bar`).

* `CC_PRETTY_INSTANCE_NAME`: A random string name generated for each instance using pokemon names.

* `INSTANCE_NUMBER`: See below

[dedicated-instance]: {{< ref "doc/administrate/apps-management.md#edit-application-configuration" >}}

### What is the `INSTANCE_NUMBER` variable used for?

This variable allows your application to differentiate each running node on the application level.

It will contain a different number for each instance of your application.

For example, if three instances are running, it will contain `0` for the first,
`1` for the second and `2` for the third.
It's handy if you want to only run crons on 1 instance (e.g. only on instance 0).

## Settings you can define using environment variables

We use environment variables for some settings:

* `IGNORE_FROM_BUILDCACHE`: allows you to specify paths to ignore when the build
  cache archive is created. Must be relative to your application root.
  (e.g. `foo/bar:foo/baz` where `bar` or `baz` can be either a directory or a file)

* `CC_OVERRIDE_BUILDCACHE`: allows you to specify paths that will be in the build cache.
  Only those files/directories will be cached
  (e.g. `foo/bar:foo/baz` where `bar` or `baz` can be either a directory or a file).

## Environment variables rules and formats

You will find below a list of rules applied to our environment variables keys and
examples of the formats available on our different modes.

### Rules

* Letters (ASCII only, upper and lower case)
  * Valid: `user_id`, `USER_ID`, `UsERId`, `userid`, `USERID`
  * Invalid: `user_id?`, `?userid`, `user.id`, `user id`
* Digits (but not for first character)
  * Valid: `user2id`, `userid42`
  * Invalid: `2userid`, `1user_Id`
* Underscores
  * Valid: `user_id`, `all_user_id`, `_user_id`, `_user_id__`
* Everything else is not allowed

#### Java properties rules exception

In case of a Java application you can also use:

* Dashes
  * Valid: `spring-boot`, `spring-boot-database`, `--spring-boot`, `--spring`
* Dots
  * Valid: `spring.boot`, `spring.datasource.url`, `.spring.url`

### Format

Here are some formats that you can use when editing your variables
in our ["expert"](#expert) and [JSON](#json) modes.

#### Expert

The format of an expert variable is `VAR_NAME="VAR_VALUE"`.

Here are some examples:

* Multiple variables examples:

  ```bash
  EMPTY=""
  MULTI="line one
  line two
  line three"
  ONE="value ONE"
  TWO="value TWO"
  ```

* Multiline:

  ```bash
  MULTI="line one
  line two
  line three"
  ```

* Empty value:

  ```bash
  EMPTY=""
  ```

#### JSON

The format of a JSON variable is `{ "name": "VAR_NAME", "value": "VAR_VALUE" }`.

Note: You must put these variables in an array (see the multiple variable example to see how it goes).

Here are some examples:

* Multiline:

  ```json
  {
    "name": "MULTI",
    "value": "line one\nline two\nline three"
  }
  ```

* Empty value:

  ```json
  {
    "name": "EMPTY",
    "value": ""
  }
  ```

* Multiple variables examples:

  ```json
  [
    {
      "name": "EMPTY",
      "value": ""
    },
    {
      "name": "MULTI",
      "value": "line one\nline two\nline three"
    },
    {
      "name": "ONE",
      "value": "value ONE"
    },
    {
      "name": "TWO",
      "value": "value TWO"
    }
  ]
  ```

## How do I use these variables?

Depending on the type of your application, the code will differ.
You can find more information in the documentation pages related to your application type.

Here is a non-exhaustive summary:

{{<table "table table-bordered table-striped dataTable" >}}
| Language | Usage |
|----------|-------|
| [Go][go] | `os.Getenv("MY_VAR")`|
| [Haskell][haskell] | `Os.Getenv["MY_VAR"]` |
| [Node.js][node] | `process.env["MY_VAR"]`|
| [Java WAR][java-war] | `System.getProperties().getProperty("MY_VAR")` |
| [PHP][php] | `getenv("MY_VAR")` |
| [Play! Framework 1][play-1] & [Play! Framework 2][play-2] | `System.getenv("MY_VAR")` or `${MY_VAR}` in `application.conf` |
| [Python][python] | `os.getenv("MY_VAR")` |
| [Ruby][ruby] | `ENV["MY_VAR"]` |
| [Rust][rust] | `std::env::var("MY_VAR")` |
| [Scala][scala] | `System.getenv("MY_VAR")` |
| [.NET][dotnet] | `System.Environment.GetEnvironmentVariable("MY_VAR")` |

[go]: {{< ref "doc/deploy/application/golang/go#environment-injection.md" >}}
[haskell]: {{< ref "doc/deploy/application/haskell/haskell#environment-injection" >}}
[node]: {{< ref "doc/deploy/application/javascript/by-framework/nodejs#environment-injection" >}}
[java-war]: {{< ref "doc/deploy/application/java/java-war#environment-injection" >}}
[php]: {{< ref "doc/deploy/application/php/php-apps#environment-injection" >}}
[play-1]: {{< ref "doc/deploy/application/java/by-framework/play-framework-1#environment-injection" >}}
[play-2]: {{< ref "doc/deploy/application/java/by-framework/play-framework-2#environment-injection" >}}
[python]: {{< ref "doc/deploy/application/python/python_apps#environment-injection" >}}
[ruby]: {{< ref "doc/deploy/application/ruby/ruby-rack#environment-injection" >}}
[rust]: {{< ref "doc/deploy/application/rust/rust#environment-injection" >}}
[scala]: {{< ref "doc/deploy/application/scala/scala#environment-injection" >}}
[dotnet]: {{< ref "doc/deploy/application/dotnet/dotnet#environment-injection" >}}
{{</table>}}

{{< callout type="info" >}}
Please note that the variables are available at build time
for runtimes that support build time instructions, such as
[Java WAR]({{< ref "doc/deploy/application/java/java-war#environment-injection" >}}),
[Play! Framework 1]({{< ref "doc/deploy/application/java/by-framework/play-framework-1#environment-injection" >}}),
[Play! Framework 2]({{< ref "doc/deploy/application/java/by-framework/play-framework-2#environment-injection" >}})
or [Scala]({{< ref "doc/deploy/application/scala/scala#environment-injection" >}}).
{{< /callout >}}
