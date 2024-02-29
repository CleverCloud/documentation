---
type: docs
title: PHP
shortdesc: PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML.
tags:
- php
- deploy
str_replace_dict:
  "@application-type@": "PHP"
type: docs
aliases:
- /doc/deploy/application/php
- /doc/deploy/application/php/php-apps
- /doc/getting-started/by-language/php
- /doc/partials/language-specific-deploy/php
---

## Overview

PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded
into HTML.

PHP is available on our platform with the branches 5.6, 7.2, 7.3, 7.4, 8.0, 8.1 and 8.2. You can use FTP or Git to deploy your applications.

The HTTP server is [Apache 2](https://httpd.apache.org/), and the PHP code is executed by [PHP-FPM](https://php-fpm.org/).

{{% content/create-application %}}

{{% content/set-env-vars %}}

{{< readfile file="language-specific-deploy/php.md" >}}

{{% content/new-relic %}}

{{% content/blackfire %}}

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via **Git or FTP**.

{{% content/deploy-git %}}

{{% content/deploy-ftp %}}

## ProxySQL

{{% content/proxysql %}}

You can learn more about ProxySQL on the [dedicated documentation page]({{< ref "/guides/proxysql" >}})

{{% content/more-config %}}

{{% content/url_healthcheck %}}

