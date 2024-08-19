---
type: docs
title: Varnish as HTTP Cache
position: 3
shortdesc: Configuring Varnish on Clever Cloud
tags:
- administrate
keywords:
- varnish
- varnish-modules
- caching
- cache
type: docs
---

## Overview

[Varnish](https://www.varnish-cache.org/) is a HTTP proxy-cache, which works as a reverse proxy between your application
and the client. Following rules defined by the user, Varnish will cache the data of an application to reduce the load on its server. We use **Varnish 6.6.0 and varnish-modules 0.18.0**.

## Limitations

Varnish is only available on **PHP**, **Go** and **Node.js** applications. Support for other applications is in discussion.

For more information about it, contact us at [support@clever-cloud.com](mailto:support@clever-cloud.com).

## Enable Varnish for your application

To enable it, you just have to create a `varnish.vcl` file in the `/clevercloud` folder.
This file describes how Varnish caches your applications and how it decides to return a cached resource or not.

{{< callout type="warning" >}}
The `vcl 4.1;` and backend section of the `varnish.vcl` configuration file are not necessary as they are already handled by Clever Cloud.
If you have a PHP FTP application or if your `varnish.vcl` file is on an FS Bucket, make sure you redeploy the application for the changes to take effect.
{{< /callout >}}

To know how to write your `varnish.vcl` file, have a look at the [Varnish 6 book](https://info.varnish-software.com/resources/varnish-6-by-example-book).

## Listen on the right port

Once varnish is enabled, your application should no longer listen on port **8080**, but on port **8081**. Because it's Varnish that will listen on port **8080**, and it will have in its configuration your application as backend.

## Configure the cache size

You can change the storage size specified in the varnish.params file with the `CC_VARNISH_STORAGE_SIZE` environment variable (the default value is `1G`).

```bash
CC_VARNISH_STORAGE_SIZE=2G
```

## Varnish 6 migration

If you already have a configuration for an older version of varnish, you can read this [guide](https://varnish-cache.org/docs/6.0/whats-new/upgrading-6.0.html) to upgrade to version 6.

## Example files

We provide some [examples of Varnish configuration files](https://GitHub.com/CleverCloud/varnish-examples) that you can
use for your application. Create a `/clevercloud` folder at the root of your application if it does not exist,
rename the file to `varnish.vcl` and move it in the `/clevercloud` folder.

## Varnish with a monorepo

If you use a monorepo, you may want to use Varnish for only some of the applications inside it.  
If you have a `/clevercloud/varnish.vcl` file at the root of your monorepo, all of your applications automatically start using Varnish.

To resolve this issue, you can create a symlink during the deployments.  

1. Put your `varnish.vcl` file anywhere but at the root of your monorepo.  
2. Create a symlink inside a `CC_PRE_BUILD_HOOK`.
  
Here is an example :

```bash
CC_PRE_BUILD_HOOK="mkdir $APP_HOME/clevercloud; ln -s $APP_HOME/path/to/your/file/varnish.vcl $APP_HOME/clevercloud/varnish.vcl"
```

This way, you only need to add the `CC_PRE_BUILD_HOOK` when you want your app to use Varnish. If you don't, the application won't use it.
