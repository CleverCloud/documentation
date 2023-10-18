---
type: docs
title: Play Framework 1.x 
position: 1
shortdesc: Play is an open source web application framework, written in Scala and Java, which follows the model–view–controller (MVC) architectural pattern.
tags:
- deploy
keywords:
- java
- play
str_replace_dict:
  "@application-type@": "Java + Play! 1"
type: docs
aliases:
- /doc/deploy/application/java/by-framework/play-framework-1

---

## Overview

Clever Cloud supports Play 1.x applications natively. This guide explains how to set up your application to run
on Clever Cloud.

[Play](https://www.playframework.com) is an open source web application framework, written in Scala and Java, which follows the model–view–controller (MVC) architectural pattern. It aims at optimizing developer productivity by using convention over configuration, hot code reloading and display of errors in the browser.

{{< readfile file="/content/partials/create-application.md" >}}

{{< readfile file="/content/partials/set-env-vars.md" >}}

## Configure your Java + Playframework 1 application

### Mandatory configuration

* The application must be located at the **root** of the git repository.
* The application needs listen on `0.0.0.0:8080`

### Select Play! version

Clever Cloud supports Play! **1.2**, **1.3**, **1.4** and **1.5**. You can select the Play! version for your application by creating a `play1_version` file in the `/clevercloud` folder (you must create it at the root of your application's folder).

The `play1_version` file can contain one of the following values:

* `1.2` or `12` for **Play! 1.2**.
* `1.3` or `13` for **Play! 1.3**.
* `1.4` or `14` for **Play! 1.4**.
* `1.5` or `15` for **Play! 1.5**.

### Play! configuration

By default, your application will run on Clever Cloud with the option `--%clevercloud`.  
It means that you can define special keys in your `application.conf` file that will be used only on Clever Cloud.

You can for example:

* set production mode so the files are compiled at startup time and the errors are logged in a file:

```conf
%clevercloud.application.mode=prod
```

* set up a mysql database

```conf
%clevercloud.db.url=jdbc:mysql://{yourcleverdbhost}/{dbname}
%clevercloud.db.driver=com.mysql.jdbc.Driver
%clevercloud.db.user={yourcleveruser}
%clevercloud.db.pass={yourcleverpass}
```

More information on [playframework.com](https://www.playframework.com).

### HTTPS support

HTTPS is handled by Clever Cloud ahead of your application, your application retrieves the traffic in plain http. To be able to use `request.secure`, you have to add `XForwardedSupport=all` in `application.conf`.

{{< readfile file="/content/partials/env-injection.md" >}}

To access environment variables from your code, you need to reference them in your application.conf file with `my.option=${MY_VARIABLE}` and then use the configuration item `my.option` in your application.

{{< readfile file="/content/partials/new-relic.md" >}}

{{< readfile file="/content/partials/deploy-git.md" >}}

{{< readfile file="/content/partials/link-addon.md" >}}

{{< readfile file="/content/partials/more-config.md" >}}
