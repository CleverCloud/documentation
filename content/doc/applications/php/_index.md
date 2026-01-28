---
type: docs
linkTitle: PHP with Apache
title: PHP with Apache application runtime
description: Deploy PHP applications on Clever Cloud with Apache, PHP-FPM, Composer dependencies, and framework support
keywords:
- php hosting
- apache
- composer
- laravel
- symfony
- wordpress
aliases:
- /applications/php
- /deploy/application/php/php-apps
- /doc/deploy/application/php
- /doc/deploy/application/php/php-apps
- /doc/doc/php
- /doc/php
- /doc/php/php-apps
- /doc/doc/php/php-apps
- /doc/getting-started/by-language/php
- /doc/partials/language-specific-deploy/php
- /getting-started/by-language/php
- /php
- /php/php-apps
---

## Overview

PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded
into HTML.

The HTTP server is [Apache 2](https://httpd.apache.org/), and the PHP code is executed by [PHP-FPM](https://php-fpm.org/).

## Create your PHP application

To create a new PHP application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type php
```
- [Learn more about Clever Tools](/doc/cli/)
- [Learn more about Clever Cloud application deployment](/doc/quickstart/#create-an-application-step-by-step)

## Configure your PHP application

### Mandatory needs

PHP runtime requires a working web application. The HTTP server is Apache 2 with PHP-FPM. If you need to serve files from a specific directory, set the `CC_WEBROOT` environment variable (e.g. `/public`).

```shell
clever env set CC_WEBROOT /public
```

- [Learn more about environment variables on Clever Cloud](/doc/reference/reference-environment-variables/)

### Build phase

Composer build is supported out of the box. If a `composer.json` file is present at the root of your repository, dependencies are installed automatically during the build phase.

- [Learn more about Composer on Clever Cloud](/doc/applications/php/composer/)
- [Learn more about Deployment hooks](/doc/develop/build-hooks/)

### PHP version

Set the `CC_PHP_VERSION` environment variable to one of the following versions.

{{< runtimes_versions php >}}

All new PHP applications are created with a default `CC_PHP_VERSION`. You can change it whenever you want then redeploy your application to use the version you want. Only values based on the first two digits (`X` or `X.Y`, not `X.Y.Z`) are supported.

### Custom PHP configuration

Most PHP settings can be changed using a `.user.ini` file.

If you want the settings to be applied to the whole application, you should put this file in your `webroot`. If you did not change it, then your `webroot` is the root of the repository.

If you put the `.user.ini` file in a subdirectory, settings will be applied recursively starting from this subdirectory.

You can review the [available directives](https://www.php.net/manual/en/ini.list.php); all the `PHP_INI_USER`, `PHP_INI_PERDIR`, and `PHP_INI_ALL` directives can be set from within `.user.ini`.

- [Learn more about .user.ini](https://www.php.net/manual/en/configuration.file.per-user.php)

#### Same configuration between PHP-CLI and PHP-FPM

`.user.ini` files are not loaded by the PHP CLI by default.

However, some PHP applications may want to check for the PHP-FPM configuration pre-requisites, `post_max_size` or `upload_max_filesize` values for example.

To load the PHP-FPM `.user.ini` file during a PHP-CLI process, in a [hook](/doc/develop/build-hooks/), use the `PHP_INI_SCAN_DIR` environment variable to load the additional file.

Assuming the script runs at the root-folder of the application:

```bash
#!/usr/bin/env bash

export PHP_INI_SCAN_DIR=":."
php myscript.php
```

This appends the current directory while still loading the default configuration.

> [!NOTE]
> The `:` at the beginning of the string is mandatory. It indicates defaults files must still load.

A specific `.ini` file can be loaded with:

```bash
#!/usr/bin/env bash

export PHP_INI_SCAN_DIR=":.php-configuration/"
php myscript.php
```

This loads every `.ini` files in the `php-configuration/` directory.

#### Timezone configuration

All instances on Clever Cloud run on the UTC timezone. We recommend to handle all your dates in UTC internally, and only handle timezones when reading or displaying dates.

Additionally, you can set PHP's time zone setting with `.user.ini`. For instance, to use the french time zone, edit `.user.ini` to add this line:

```ini
date.timezone=Europe/Paris
```

#### Memory Limit

When php-fpm spawns a worker it allocates a smaller part of the application's memory to the worker, here is the allocated memory for each flavor:

 | Flavor   | Memory Limit |
 |----------|--------------|
 |Pico      | 64M          |
 |Nano      | 64M          |
 |XS        | 128M         |
 |S         | 256M         |
 |M         | 384M         |
 |L         | 512M         |
 |XL        | 768M         |
 |2XL       | 1024M        |
 |3XL       | 1536M        |
 |4XL+      | 2048M        |

To change this limit you can define `MEMORY_LIMIT` [environment variable](/doc/reference/reference-environment-variables#php).

If you define a limit exceeding the application memory it will use the default one.

## Frameworks and CMS

The following is the list of tested CMS by our team.

It's quite not exhaustive, so it does not mean that other CMS can't work on the Clever Cloud platform.

{{< cards >}}
  {{< card link="/developers/guides/tutorial-drupal" title="Drupal" subtitle= "Deploy a Drupal-based website on Clever Cloud" icon="drupal" >}}
  {{< card link="/developers/guides/tutorial-laravel" title="Laravel" subtitle= "Deploy a Laravel app on Clever Cloud" icon="laravel" >}}
  {{< card link="/developers/guides/tutorial-symfony" title="Symfony" subtitle= "Deploy a Symfony application on Clever Cloud" icon="symfony" >}}
  {{< card link="/developers/guides/tutorial-wordpress" title="WordPress" subtitle= "Deploy WordPress on Clever Cloud" icon="wordpress" >}}
  {{< card link="/developers/guides/moodle" title="Moodle" subtitle="Full Moodle installation and configuration guide" icon="moodle" >}}

{{< /cards >}}

Others PHP frameworks tested on Clever Cloud:

- Prestashop
- Dokuwiki
- Joomla
- SugarCRM
- Drupal
- Magento
- Status.net
- Symfony
- Thelia
- Laravel
- Sylius

## Configure Monolog

A lot of frameworks (including Symfony) use Monolog to handle logging. The default configuration of Monolog doesn't allow to log errors into the console.

Here is a basic configuration of Monolog to send your application's logs into our logging system and access them into the Console:

```yaml
monolog:
  handlers:
    clever_logs:
      type: error_log
      level: warning
```

You can change the level to whatever level you desire. For Symfony, the configuration file is `app/config/config_prod.yml`.

Laravel doesn't need Monolog to retrieve logs via Clever console or Clever CLI. Here, ensure that you have the following line in `config/app.php`:

```php
return [
    // …
    'log' => env('APP_LOG'),
    // …
];
```

Then, set `APP_LOG=syslog` as Clever application environment variable.

{{% content "new-relic" %}}

{{% content "blackfire" %}}

## ProxySQL

{{% content "proxysql" %}}

You can learn more about ProxySQL on the [dedicated documentation page](/guides/proxysql)

{{% content "url_healthcheck" %}}
{{% content "redirectionio" %}}
{{% content "varnish" %}}
