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

### Supported Versions

The supported versions are: {{< runtimes_versions PHP >}}

The HTTP server is [Apache 2](https://httpd.apache.org/), and the PHP code is executed by [PHP-FPM](https://php-fpm.org/).

{{% content/create-application %}}

{{% content/set-env-vars %}}

{{< readfile file="language-specific-deploy/php.md" >}}

{{% content/new-relic %}}

{{< readfile file="blackfire.md" >}}

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via **Git or FTP**.

{{% content/deploy-git %}}

{{% content/deploy-ftp %}}

## ProxySQL

{{< readfile file="proxysql.md" >}}

You can learn more about ProxySQL on the [dedicated documentation page]({{< ref "/guides/proxysql" >}})

{{% content/more-config %}}

{{< readfile file="url_healthcheck.md" >}}

