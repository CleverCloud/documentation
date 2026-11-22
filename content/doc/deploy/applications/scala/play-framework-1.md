---
type: docs
linkTitle: Play 1
title: Play Framework 1
description: Deploy Play Framework 1 applications on Clever Cloud, with the Play and Java versions of your choice and a configuration for Clever Cloud in application.conf
keywords:
- java web framework
- play 1
- play framework
- play framework 1
aliases:
- /doc/applications/java/play-framework-1
- /doc/applications/scala/play-framework-1
- /doc/deploy/application/java/by-framework/play-framework-1
- /doc/deploy/application/scala/tutorials/play-framework-1
- /doc/java/play-framework-1
- /doc/play-framework
- /doc/scala/play-framework-1
- /guides/play-framework-1
---

## Overview

[Play Framework 1](https://github.com/playframework/play1) is a Java web framework with its own build tool and command line. Clever Cloud installs the Play 1 version of your choice, and precompiles your application. It then starts it with the `clevercloud` framework ID, with which `application.conf` can set the production mode. For Play 2 and 3, built with sbt, see [Play Framework 2 and 3](/doc/deploy/applications/scala/play-framework-2/).

## Create your Play 1 application

To create a new Play 1 application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type play1
```

The [getting started guide](/doc/getting-started/) describes each step of the creation of an application.

## Configure your Play 1 application

### Mandatory needs

A Play 1 application needs the folders that `play new` creates: `app` for the code, and `conf` for `application.conf` and `routes`. Play listens on every interface, and Clever Cloud sets its port: you have nothing to change. For instance, a minimal application:

```text {filename="conf/routes"}
GET     /       Application.index
```

```java {filename="app/controllers/Application.java"}
package controllers;

import play.mvc.Controller;

public class Application extends Controller {

    public static void index() {
        renderText("Hello from Play 1 on Clever Cloud");
    }
}
```

```properties {filename="conf/application.conf"}
application.name=hello
application.mode=dev
%clevercloud.application.mode=prod
application.secret=${APPLICATION_SECRET}
```

`${APPLICATION_SECRET}` takes the value of this [environment variable](/doc/manage/environment-variables/), to keep the secret out of your repository. Set a random secret:

```bash
clever env set APPLICATION_SECRET "$(openssl rand -base64 32)"
```

Then choose the Play and Java versions: the default ones fail to build, as the next section explains.

### Play and Java versions

With the default versions, Play {{< runtime_version play1 >}} and Java 21, the build fails: Play 1.7 can't precompile the templates of your application with Java 21, `Unsupported class file major version 65`. Use a recent version of Play, such as 1.11:

```bash
clever env set CC_PLAY1_VERSION 1.11
```

Or keep Play 1.7, with Java 17:

```bash
clever env set CC_JAVA_VERSION 17
```

`CC_PLAY1_VERSION` accepts these versions. The legacy forms without the dot, such as `17` or `111`, also work:

{{< runtimes_versions play1 >}}

### Configuration for Clever Cloud

Clever Cloud starts Play with the `clevercloud` framework ID. In `application.conf`, a key prefixed with `%clevercloud.` only applies on Clever Cloud, and replaces the same key without prefix. In the example above, the application runs in production mode on Clever Cloud only.

Combine the prefix with a variable, such as `%clevercloud.db.user=${POSTGRESQL_ADDON_USER}`, for a linked add-on.

### Build and start

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/), then resolves the dependencies and precompiles:

```bash
play dependencies
play precompile --%clevercloud
```

Clever Cloud then starts the precompiled application on the port it sets, 8080 by default:

```bash
play start -Dprecompiled=true --%clevercloud --http.port=8080
```

### HTTPS

The load balancers of Clever Cloud handle HTTPS, and reach your application over HTTP: `request.secure` is `false`. [Force HTTPS](/doc/manage/#force-https), enabled by default, redirects HTTP requests to HTTPS. To read the protocol and the address of the client, see the headers of the [load balancers](/doc/network/load-balancers/).

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/scala/play-framework-2" title="Play Framework 2 and 3" subtitle="Deploy a Play 2 or 3 application built with sbt" icon="playframework" >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/network/load-balancers" title="Load balancers" subtitle="Read the address and the protocol of your clients" icon="server-stack" >}}
{{< /cards >}}
