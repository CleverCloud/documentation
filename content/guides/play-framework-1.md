---
type: docs
title: Play Framework 1.x Scala
position: 1
shortdesc: Play is an open source web application framework, written in Scala and Java, which follows the model–view–controller (MVC) architectural pattern.
tags:
- deploy
keywords:
- scala
- play
str_replace_dict:
  "@application-type@": "Scala"
aliases:
- /doc/deploy/application/java/by-framework/play-framework-1
- /doc/applications/java/play-framework-1

type: docs
---

## Overview

Clever Cloud supports Play 1.x applications natively. The present guide explains how to set up your application to run on Clever Cloud.

{{< content "create-application" >}}

 {{< content "set-env-vars" >}}

## Configure your Scala + Play! 1 application

### Select Play! 1.x version

Clever Cloud supports Play! **1.2**, **1.3**, **1.4**, **1.5**. You can select the Play! version for your application by setting the `PLAY1_VERSION` [environment variable](#setting-up-environment-variables-on-clever-cloud) (or by putting it in a file named `clevercloud/play1_version`).

The `PLAY1_VERSION` environment variable can contain one of the following values:

* `1.2` or `12` for **Play! 1.2**.
* `1.3` or `12` for **Play! 1.3**.
* `1.4` or `14` for **Play! 1.4**.
* `1.5` or `15` for **Play! 1.5**.

### Play! configuration with application.conf

By default, your application will run on Clever Cloud with the option `--%clevercloud`.
It means that you can define special keys in your `application.conf` file that will be used only on Clever Cloud.

You can for example:

* set production mode so the files are compiled at startup time and the errors are logged in a file:

    ```bash
    %clevercloud.application.mode=prod
    ```

* set up a mysql database (using environment variables)

    ```bash
    %clevercloud.db.url="jdbc:mysql://"${MYSQL_ADDON_HOST}"/"${MYSQL_ADDON_DB}
    %clevercloud.db.driver=com.mysql.jdbc.Driver
    %clevercloud.db.user=${MYSQL_ADDON_USER}
    %clevercloud.db.pass=${MYSQL_ADDON_PASSWORD}
    ```

More information on [playframework.com](https://www.playframework.com).

### HTTPS support

HTTPS is handled by Clever Cloud ahead of your application, your application retrieves the traffic in plain http. To be able to use `request.secure`, you have to add `XForwardedSupport=all` in `application.conf`.

 {{< content "new-relic" >}}

 {{< content "env-injection" >}}

To access the environment variables from your code, you need to add `my.option=${MY_VARIABLE}` in your `application.conf` file, and then use the configuration item `my.option` in your application. e.g `%clevercloud.db.url="jdbc:mysql://"${MYSQL_ADDON_HOST}"/"${MYSQL_ADDON_DB}`

 {{< content "deploy-git" >}}

 {{< content "link-addon" >}}

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}
