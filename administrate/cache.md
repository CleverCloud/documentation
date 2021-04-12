---
title: Varnish as HTTP Cache
position: 3
shortdesc: Configuring Varnish on Clever Cloud
tags:
- administrate
keywords:
- varnish
- caching
- cache
---

## Overview

[Varnish](https://www.varnish-cache.org/) is a HTTP proxy-cache, which works as a reverse proxy between your application
and the client. Following rules defined by the user, Varnish will cache the data of an application to reduce the load on its server. We use **Varnish 4**

## Limitations

{{< alert "warning" >}}
<p>Varnish is only available on PHP and Go applications. Support for other applications is in discussion.</p> 
<p>For more information about it, contact us at <a href="mailto:support@clever-cloud.com">support@clever-cloud.com</a>.</p>
{{< /alert >}}

## Enable Varnish for your application

To enable it, you just have to create a `varnish.vcl` file in the `/clevercloud` folder.
This file describes how Varnish caches your applications and how it decides to return a cached resource or not.

{{< alert "warning" >}}
<p>The <code>vcl 4.0;</code> and backend section of the `varnish.vcl` configuration file are not necessary as they are already handled by Clever Cloud.</p>
<p>If you have a PHP FTP application or if your `varnish.vcl` file is on an FS Bucket, make sure you redeploy the application for the changes to take effect.</p>
{{< /alert >}}

To know how to write your `varnish.vcl` file, please have a look at the [Varnish 4.0 book](https://book.varnish-software.com/4.0/).

## Varnish 3 to 4 migration

If you already have a configuration file written for varnish 3, you can use [varnish3to4](https://GitHub.com/fgsch/varnish3to4) to convert it to varnish 4 in order to use it on Clever Cloud.

## Example files

We provide some [examples of Varnish configuration files](https://GitHub.com/CleverCloud/varnish-examples) that you can
use for your application. Create a `/clevercloud` folder at the root of your application if it does not exist,
rename the file to `varnish.vcl` and move it in the `/clevercloud` folder.
