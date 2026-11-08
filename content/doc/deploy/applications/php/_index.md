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
- /doc/applications/php
- /doc/applications/php-with-apache
- /doc/applications/php/php
- /doc/deploy/application/php
- /doc/deploy/application/php/php-apps
- /doc/deploy/php-with-apache
- /doc/develop/php-with-apache
- /doc/doc/php
- /doc/doc/php/php-apps
- /doc/getting-started/by-language/php
- /doc/partials/language-specific-deploy/php
- /doc/php
- /doc/php-hosting
- /doc/php/php-apps
- /doc/runtimes/php
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

- [Learn more about Clever Tools](/doc/tools/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

## Configure your PHP application

### Mandatory needs

PHP runtime requires a working web application. The HTTP server is Apache 2 with PHP-FPM. If you need to serve files from a specific directory, set the `CC_WEBROOT` environment variable to its absolute path from the root of your project (e.g. `/public`). The deployment fails if this path is relative or contains `..`.

```shell
clever env set CC_WEBROOT /public
```

- [Learn more about environment variables on Clever Cloud](/doc/manage/environment-variables/reference/)

### Build phase

Composer build is supported out of the box. If a `composer.json` file is present at the root of your repository, dependencies are installed automatically during the build phase.

- [Learn more about Composer on Clever Cloud](/doc/deploy/applications/php/composer/)
- [Learn more about Deployment hooks](/doc/manage/build-hooks/)

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

To load the PHP-FPM `.user.ini` file during a PHP-CLI process, in a [hook](/doc/manage/build-hooks/), use the `PHP_INI_SCAN_DIR` environment variable to load the additional file.

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

All instances on Clever Cloud run in the UTC time zone. Handle your dates in UTC internally, and convert them to a time zone only when you read or display them.

Additionally, you can set PHP's time zone setting with `.user.ini`. For instance, to use the french time zone, edit `.user.ini` to add this line:

```ini
date.timezone=Europe/Paris
```

This setting doesn't change when [CRON jobs](/doc/manage/cron/) run: to schedule them in a local time zone, add a [`CRON_TZ` line](/doc/manage/cron/#choose-the-time-zone) to `clevercloud/cron.json`.

#### Memory limit

Clever Cloud configures PHP's [`memory_limit`](https://www.php.net/manual/en/ini.core.php#ini.memory-limit) directive, which limits how much memory each PHP script can allocate. For web requests, this limit applies independently within each PHP-FPM worker; memory is not reserved when workers start. Both the default limit and the maximum value accepted through `MEMORY_LIMIT` depend on the application's available memory, which excludes memory reserved for the system:

| Flavor | Default `memory_limit` | Maximum `MEMORY_LIMIT` |
| ------ | ---------------------: | ---------------------: |
| Nano   | 91 MiB                 | 358 MiB                |
| XS     | 161 MiB                | 859 MiB                |
| S      | 249 MiB                | 1683 MiB               |
| M      | 406 MiB                | 3579 MiB               |
| L      | 658 MiB                | 7523 MiB               |
| XL     | 1051 MiB               | 15496 MiB              |
| 2XL    | 1377 MiB               | 23503 MiB              |
| 3XL    | 1666 MiB               | 31525 MiB              |

To change the limit, set [`MEMORY_LIMIT`](/doc/manage/environment-variables/reference#php) to a positive integer interpreted in MiB, without a unit suffix.

For example, to allow each PHP script to allocate up to 128 MiB:

```bash
clever env set MEMORY_LIMIT 128
```

If `MEMORY_LIMIT` exceeds the maximum value for the selected flavor, Clever Cloud keeps the automatically calculated limit and logs a warning during deployment. Clever Cloud also calculates the number of PHP-FPM workers automatically.

On XS and larger flavors, setting [`CC_CONFIGURATION_PM_MAX_CHILDREN`](/doc/manage/environment-variables/reference#php) can lower the calculated memory limit. On Nano, the platform always uses six workers. If you also set a valid `MEMORY_LIMIT`, it takes precedence over the adjustment based on the number of workers.

#### Session upload progress

Clever Cloud sets [`session.upload_progress.enabled`](https://www.php.net/manual/en/session.configuration.php#ini.session.upload-progress.enabled) to `Off` when it deploys your application, following the [PHP security team recommendations](https://www.php.net/archive/2026.php#2026-10-21-5). This setting only disables upload progress tracking in sessions: file uploads and `multipart/form-data` requests keep working.

### Configuration reference

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/php/apache" title="Apache" subtitle="Configure the web server, headers and authentication" icon="feather" >}}
  {{< card link="/developers/doc/deploy/applications/php/composer" title="Composer" subtitle="Manage PHP dependencies and private repositories" icon="php" >}}
  {{< card link="/developers/doc/deploy/applications/php/extensions" title="Extensions" subtitle="Review and configure available PHP extensions" icon="puzzle" >}}
  {{< card link="/developers/doc/deploy/applications/php/sessions-emails" title="Sessions and emails" subtitle="Configure session storage and email delivery" icon="mail" >}}
{{< /cards >}}

## Frameworks and CMS

The following is the list of tested CMS by our team.

It's quite not exhaustive, so it does not mean that other CMS can't work on the Clever Cloud platform.

{{< cards >}}
  {{< card link="/developers/guides/self-hosted/drupal" title="Drupal" subtitle="Deploy a Drupal website on Clever Cloud" icon="drupal" >}}
  {{< card link="/developers/guides/frameworks/laravel" title="Laravel" subtitle="Deploy a Laravel application on Clever Cloud" icon="simple:laravel" >}}
  {{< card link="/developers/guides/self-hosted/moodle" title="Moodle" subtitle="Deploy and configure a Moodle learning platform on Clever Cloud" icon="moodle" >}}
  {{< card link="/developers/guides/frameworks/symfony" title="Symfony" subtitle="Deploy a Symfony application on Clever Cloud" icon="simple:symfony" >}}
  {{< card link="/developers/guides/self-hosted/wordpress" title="WordPress" subtitle="Deploy a WordPress website on Clever Cloud" icon="simple:wordpress" >}}

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

{{% include "shared/new-relic" %}}

### Monitor your application with Blackfire

You can use [Blackfire](https://www.blackfire.io/) to monitor your application on Clever Cloud.

Please refer to our [Blackfire documentation](/doc/observability/blackfire) to configure it for your application.

{{% include "shared/proxysql" %}}

You can learn more about ProxySQL on the [dedicated documentation page](/guides/databases/proxysql)

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
