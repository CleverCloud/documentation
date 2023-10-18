---
type: docs
title: Deploy PHP applications
shortdesc: PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML.
tags:
- php
str_replace_dict:
  "@application-type@": "PHP"
type: docs
---

## Overview

PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded
into HTML.

PHP is available on our platform with the branches 5.6, 7.2, 7.3, 7.4, 8.0, 8.1 and 8.2. You can use FTP or Git to deploy your applications.

The HTTP server is [Apache 2](https://httpd.apache.org/), and the PHP code is executed by [PHP-FPM](https://php-fpm.org/).

{{< readfile file="/content/partials/create-application.md" >}}

{{< readfile file="/content/partials/set-env-vars.md" >}}

{{< readfile file="/content/partials/language-specific-deploy/php.md" >}}

{{< readfile file="/content/partials/new-relic.md" >}}

{{< readfile file="/content/partials/blackfire.md" >}}

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via **Git or FTP**.

{{< readfile file="/content/partials/deploy-git.md" >}}

{{< readfile file="/content/partials/deploy-ftp.md" >}}

## ProxySQL

{{< readfile file="/content/partials/proxysql.md" >}}

You can learn more about ProxySQL on the [dedicated documentation page]({{< ref "doc/deploy/addon/mysql/proxysql.md" >}})

{{< readfile file="/content/partials/more-config.md" >}}
