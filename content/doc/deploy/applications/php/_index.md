---
type: docs
linkTitle: PHP with Apache
title: PHP with Apache application runtime
description: Deploy PHP applications on Clever Cloud with Apache and PHP-FPM, Composer, the PHP version of your choice, and frameworks such as Laravel, Symfony, or WordPress
keywords:
- apache
- composer
- laravel
- php
- php hosting
- php-fpm
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

[PHP](https://www.php.net) is a scripting language for the web. Clever Cloud serves your application with [Apache](https://httpd.apache.org) and runs its code with PHP-FPM, after it installs its dependencies with [Composer](/doc/deploy/applications/php/composer/). It works with frameworks and applications such as [Laravel](/guides/frameworks/laravel/), [Symfony](/guides/frameworks/symfony/), [WordPress](/guides/self-hosted/wordpress/), [Drupal](/guides/self-hosted/drupal/), or [Moodle](/guides/self-hosted/moodle/). To run PHP with its own web server and worker mode, see [FrankenPHP](/doc/deploy/applications/frankenphp/).

## Create your PHP application

To create a new PHP application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type php
```

The [getting started guide](/doc/getting-started/) describes each step of the creation of an application.

## Configure your PHP application

### Mandatory needs

A PHP application needs its PHP files in the webroot, the folder that Apache serves. The webroot is the root of your repository, or the folder set in `CC_WEBROOT`. Apache listens on the right port for you: your code doesn't open one.

For instance, a minimal application:

```php {filename="index.php"}
<?php
echo "Hello from PHP on Clever Cloud\n";
```

Frameworks such as Laravel and Symfony serve a `public` folder. Set its path in `CC_WEBROOT`, from the root of your repository, starting with a `/` and without `..`. Otherwise, the deployment fails with an error:

```bash
clever env set CC_WEBROOT /public
```

A [Clever Task](#php-applications-as-clever-tasks) doesn't need a webroot.

### Build phase

After the pre-build [hook](/doc/manage/build-hooks/), Clever Cloud installs the dependencies of your `composer.json` file, without the development ones:

```bash
composer install --no-dev
```

The scripts of your `composer.json` run during this install, such as `artisan package:discover` for Laravel. The [Composer page](/doc/deploy/applications/php/composer/) explains how to choose its version, install development dependencies, and reach private repositories.

### PHP version

Clever Cloud uses PHP {{< runtime_version php >}} by default. The `8` value tracks it, and moves to each new minor release of PHP a few months after it comes out. To stay on a release, set `CC_PHP_VERSION` as `X.Y`, such as `8.4`, not `X.Y.Z`:

{{< runtimes_versions php >}}

Many extensions don't support PHP 8.6 yet, such as MongoDB or Redis: check the [extensions](/doc/deploy/applications/php/extensions/) available with this version.

### PHP settings

Most PHP settings work in a `.user.ini` file at the root of the webroot. In one of its folders, it applies to this folder and the ones inside it. Use it for the [directives](https://www.php.net/manual/en/ini.list.php) of the `PHP_INI_USER`, `PHP_INI_PERDIR`, and `PHP_INI_ALL` modes, as the [PHP documentation](https://www.php.net/manual/en/configuration.file.per-user.php) explains:

```ini {filename="public/.user.ini"}
date.timezone=Europe/Paris
post_max_size=72M
upload_max_filesize=64M
```

A request can't exceed `post_max_size`, 8 MB by default, whatever `upload_max_filesize`, 32 MB by default: raise both for large uploads.

The instances run in the UTC time zone: `date.timezone` changes it for PHP only, and [cron jobs](/doc/manage/cron/#choose-the-time-zone) need a `CRON_TZ` line of their own.

The command line of PHP doesn't read `.user.ini`: add its folder to `PHP_INI_SCAN_DIR`, after a `:` that keeps the default files. For instance, to run a script with the settings of `public/.user.ini` in a hook or a task:

```bash
PHP_INI_SCAN_DIR=:public php bin/job.php
```

### Memory limit

Clever Cloud sets the [`memory_limit`](https://www.php.net/manual/en/ini.core.php#ini.memory-limit) of each PHP script, and the number of PHP-FPM workers, from the memory of the instance. To change the limit, set `MEMORY_LIMIT` in MiB, without a unit:

```bash
clever env set MEMORY_LIMIT 256
```

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

Each worker uses its limit only when a script needs it. Above the maximum of the flavor, Clever Cloud keeps its own limit and logs a warning.

`CC_CONFIGURATION_PM_MAX_CHILDREN` sets the number of workers, except on Nano instances, which run 6 workers. It can lower the default limit of each one, but not the `MEMORY_LIMIT` you set.

The [environment variables reference](/doc/manage/environment-variables/reference/#php) lists the other settings, such as `MAX_INPUT_VARS` for `max_input_vars`, or `CC_OPCACHE_MEMORY` for OPcache. Clever Cloud disables [`session.upload_progress.enabled`](https://www.php.net/manual/en/session.configuration.php#ini.session.upload-progress.enabled), as the [PHP security team recommends](https://www.php.net/archive/2026.php#2026-10-21-5): uploads still work.

### Environment variables

Your application reads its [environment variables](/doc/manage/environment-variables/) with `getenv()`, such as the credentials of a linked PostgreSQL add-on:

```php
$pdo = new PDO(
    sprintf('pgsql:host=%s;port=%s;dbname=%s', getenv('POSTGRESQL_ADDON_HOST'), getenv('POSTGRESQL_ADDON_PORT'), getenv('POSTGRESQL_ADDON_DB')),
    getenv('POSTGRESQL_ADDON_USER'),
    getenv('POSTGRESQL_ADDON_PASSWORD')
);
```

Don't expose a page that calls `phpinfo()`: it shows your environment variables with their secrets, and settings that can hold some, such as `session.save_path` with `SESSION_TYPE=redis`. Remove it once you no longer need it.

### Logs

The PHP errors, and the messages of `error_log()`, appear in the [logs](/doc/observability/logs/) of your application. Point the logger of your framework to them, such as `LOG_CHANNEL=errorlog` for Laravel, or a Monolog handler of the `error_log` type for Symfony.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit, with its `vendor` folder. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps the `vendor` folder between commits: Composer then only installs what changed.

### Monitor and connect your application

To monitor your application, use [New Relic](/doc/observability/new-relic/), [Blackfire](/doc/observability/blackfire/), or another agent of the [Extensions page](/doc/deploy/applications/php/extensions/#enable-specific-extensions).

To send traces to an [OpenTelemetry](https://opentelemetry.io/docs/zero-code/php/) collector, set `ENABLE_OPENTELEMETRY=true`. Add the SDK, its exporter, an HTTP client, and the packages that instrument your libraries, such as PHP Data Objects (PDO). Then configure the SDK with its `OTEL_*` variables:

```bash
composer require open-telemetry/sdk open-telemetry/exporter-otlp guzzlehttp/guzzle open-telemetry/opentelemetry-auto-pdo
clever env set ENABLE_OPENTELEMETRY true
clever env set OTEL_PHP_AUTOLOAD_ENABLED true
clever env set OTEL_SERVICE_NAME my-application
clever env set OTEL_EXPORTER_OTLP_ENDPOINT https://collector.example.com
```

To pool the connections to a MySQL add-on, set `CC_ENABLE_MYSQL_PROXYSQL=true`: [ProxySQL](/guides/databases/proxysql/) then runs on each instance. Connect your application to its socket, in `CC_MYSQL_PROXYSQL_SOCKET_PATH`, instead of the host and port of the add-on.

A [health check](/doc/manage/healthcheck/) checks that your application answers before it gets traffic, and [Request Flow](/doc/manage/request-flow/) chains middleware, such as Varnish, in front of it.

## PHP applications as Clever Tasks

A PHP application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration. Clever Cloud builds it, then runs `CC_RUN_COMMAND` from the root of your repository, instead of serving the webroot. The task stops when this command ends.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks), here for a script of your repository:

```bash
clever create --type php --task "php bin/job.php"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/php/apache" title="Apache" subtitle="Configure the web server with .htaccess, authentication, and timeouts" icon="feather" >}}
  {{< card link="/developers/doc/deploy/applications/php/composer" title="Composer" subtitle="Install dependencies, choose Composer, reach private repositories" icon="php" >}}
  {{< card link="/developers/doc/deploy/applications/php/extensions" title="Extensions" subtitle="Enable or disable PHP extensions" icon="puzzle" >}}
  {{< card link="/developers/doc/deploy/applications/php/sessions-emails" title="Sessions and emails" subtitle="Store sessions on an FS Bucket or Materia KV, send emails" icon="mail" >}}
{{< /cards >}}
