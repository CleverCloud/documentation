---
title: Play Framework 1
position: 1
shortdesc: Play is an open source web application framework, written in Scala and Java, which follows the model–view–controller (MVC) architectural pattern.
tags:
- java
---

# Deploy Play Framework 1.x

Clever Cloud supports Play 1.x applications natively. The present guide explains how to set up your application to run
on Clever Cloud.

Note : like other runtimes, Java application need listen on `0.0.0.0:8080`

## Overview

Play is an open source web application framework, written in Scala and Java, which follows the model–view–controller
(MVC) architectural pattern. It aims to optimize developer productivity by using convention over configuration, hot code
reloading and display of errors in the browser.

## Create an application

Refer to the page [Deploy an application on Clever Cloud](/doc/clever-cloud-overview/add-application/).

## Necessary information

* The application must be located at the **root** of the git repository.

## Select Play! version

Clever Cloud supports Play! **1.2** and **1.3**. You can select the Play! version for your application by creating a
`play1_version` file in the `/clevercloud` folder.

The `play1_version` file can contain one of the following values:

* `1.2` or `12` for **Play! 1.2**.
* `1.3` or `12` for **Play! 1.3**.


## Play! configuration

By default, your application will run on Clever Cloud with the option `--%clevercloud`.  
It means that you can define special keys in your `application.conf` file that will be used only on Clever Cloud.

You can for example:

* set production mode so the files are compiled at startup time and the errors are logged in a file:

    ```bash
    %clevercloud.application.mode=prod
    ```

* set up a mysql database

    ```bash
    %clevercloud.db.url=jdbc:mysql://{yourcleverdbhost}/{dbname}
    %clevercloud.db.driver=com.mysql.jdbc.Driver
    %clevercloud.db.user={yourcleveruser}
    %clevercloud.db.pass={yourcleverpass}
    ```

More information on [playframework.com](http://www.playframework.com).

## Environment injection

Clever Cloud can inject environment variables that are defined in the
dashboard and by add-ons linked to your application.

To access the environment variables from your application, you need to
reference them in your application.conf file:
you just have to put `my.option=${MY_VARIABLE}` in your application.conf file, and then use
the configuration item `my.option` in your application.

So for an application using the MySQL add-on, you can set:

```bash
%clevercloud.db.url="jdbc:mysql://"${MYSQL_ADDON_HOST}"/"${MYSQL_ADDON_DB}
%clevercloud.db.driver=com.mysql.jdbc.Driver
%clevercloud.db.user=${MYSQL_ADDON_USER}
%clevercloud.db.pass=${MYSQL_ADDON_PASSWORD}
```

## HTTPS support

HTTPS is handled by Clever Cloud ahead of your application, your application
retrieves the traffic in plain http. To be able to use `request.secure`, you
have to add `XForwardedSupport=all` in `application.conf`.

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via Git. Follow [these steps](/doc/clever-cloud-overview/add-application/) to
deploy your application.
