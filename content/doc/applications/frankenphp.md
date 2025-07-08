---
type: docs
linkTitle: FrankenPHP
title: FrankenPHP application runtime
description: Deploy your applications with FrankenPHP, the modern PHP server based on Caddy, written in Go
type: docs
---

## Overview

[FrankenPHP](https://frankenphp.dev) is a fast and modern server for PHP developed by [Kevin Dunglas](https://github.com/dunglas) built on top of the [Caddy web server](https://caddyserver.com/docs/). It's a seamless drop-in replacement for PHP-FPM or Apache with `mod_php`, designed to enhance your PHP applications with advanced capabilities.

It comes with many extensions and features such as early hints (HTTP 103), real-time capabilities with its built-in Mercure hub. FrankenPHP can also make your Laravel and Symfony projects faster than ever through their official integrations with the [worker mode](#worker-mode). Deploying PHP applications with FrankenPHP on Clever Cloud is straightforward and requires no complex configuration, nor Docker container.

> [!NOTE] FrankenPHP is a new runtime. Help us to improve it by reporting any issue or suggestion on the [Clever Cloud Community](https://github.com/CleverCloud/Community/discussions/categories/frankenphp)

## Create your FrankenPHP application

To create a new FrankenPHP application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type frankenphp
```
* [Learn more about Clever Tools](/developers/doc/cli/)
* [Learn more about Clever Cloud application deployment](/developers/doc/quickstart/#create-an-application-step-by-step)

> [!NOTE] FrankenPHP applications can't be deployed on a pico instance, XS is the default instance type

## Configure your FrankenPHP application

### Mandatory needs

FrankenPHP runtime only requires a working web application, with an `index.php` or `index.html` file. If you need to serve files from a specific directory, set the `CC_WEBROOT` environment variable, relative to the root of your project (default: `/`).

* [Learn more about environment variables on Clever Cloud](/developers/doc/reference/reference-environment-variables/)

### FrankenPHP version and tools

FrankenPHP currently deployed version on Clever Cloud is `1.8.0` based on PHP `8.4.10` and Caddy server `2.10.0`. Virtual machine image includes multiple tools from the PHP ecosystem such as Composer or Symfony CLI.

- [FrankenPHP PHP info](https://frankenphpinfo.cleverapps.io/)

### Composer native support

If a `composer.json` file is detected at the root of your project, it will be used to install dependencies during building phase with `--no-interaction --no-progress --no-scripts --no-dev` flags. To use your own, set the `CC_PHP_COMPOSER_FLAGS`environment variable.

To install development dependencies, set the `CC_PHP_DEV_DEPENDENCIES` environment variable to `install`.

> [!TIP] To use a local Composer to install dependencies, put the `composer.phar` file at the root of your project

## Custom PHP configuration

To load your own PHP configuration directives, put a `php.ini` file at the root of your project. FrankenPHP will automatically use it.

## FrankenPHP and Materia KV

Materia KV is Clever Cloud's distributed serverless key-value store based on FoundationDB, compatible with existing ecosystems such as Redis®, with TTL for sessions support and JSON commands.

To manage Materia KV data with FrankenPHP, use the included `redis` extension in your PHP code and configure it with your add-on URL, port and token as password. For now, you need to use the `tcp` mode and `6378` port.

- [Learn more about Materia KV](/developers/doc/addons/materia-kv)
- [Materia KV and FrankenPHP demo](https://github.com/CleverCloud/frankenphp-kv-json-example)

### Worker mode

With FrankenPHP worker mode, a script of your project is kept in memory to handle incoming requests in a few milliseconds. Define the path to this script, relative to the root of your project, with the `CC_FRANKENPHP_WORKER` environment variable (e.g. `/worker/script.php`). It's supported by design by Laravel Octane and Symfony Runtime projects.

* [Learn more about FrankenPHP worker mode](https://frankenphp.dev/docs/worker/#standalone-binary)
* [Learn more about Laravel Octane](https://laravel.com/docs/master/octane#frankenphp)
* [Learn more about Symfony Runtime](https://symfony.com/doc/current/components/runtime.html)

## Configurable port

By default, FrankenPHP listens on port `8080`. If you want to change it, set the `CC_FRANKENPHP_PORT` environment variable to your desired port. This is useful if you want to run a service in front of FrankenPHP, such as [Redirection.io](/developers/doc/reference/reference-environment-variables/#use-redirectionio-as-a-proxy) for example.

## Custom FrankenPHP run command

Use your own command to run your FrankenPHP application to define flags such as `--debug`, `--mercure` or `--no-compress`. To do so, set the `CC_RUN_COMMAND` environment variable, starting with `frankenphp php-server --listen 0.0.0.0:8080`.

You can also use this to load [a custom Caddyfile](https://frankenphp.dev/docs/config/#caddyfile-config), starting `CC_RUN_COMMAND` with `frankenphp run --config /path/to/Caddyfile`.

## Use FrankenPHP to execute PHP scripts as Clever Tasks

FrankenPHP can be used to execute PHP scripts. On Clever Cloud, to run such workloads as Clever Tasks, configure an application as Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/developers/doc/cli/applications/#tasks):

```bash
clever create --type frankenphp --task "frankenphp php-cli path/to/task.php"
clever deploy # or clever restart if there is no code change
```

- [Learn more about Clever Tasks](/developers/doc/develop/tasks/)

## Included extensions

FrankenPHP on Clever Cloud comes with a set included PHP extensions: `amqp`,`apcu`,`ast`,`bcmath`,`brotli`,`bz2`,`calendar`,`ctype`,`curl`,`dba`,`dom`,`exif`,`fileinfo`,`filter`,`ftp`,`gd`,`gmp`,`gettext`,`iconv`,`igbinary`,`imagick`,`intl`,`ldap`,`lz4`,`mbregex`,`mbstring`,`mysqli`,`mysqlnd`,`opcache`,`openssl`,`parallel`,`pcntl`,`pdo`,`pdo_mysql`,`pdo_pgsql`,`pdo_sqlite`,`pgsql`,`phar`,`posix`,`protobuf`,`readline`,`redis`,`session`,`shmop`,`simplexml`,`soap`,`sockets`,`sodium`,`sqlite3`,`ssh2`,`sysvmsg`,`sysvsem`,`sysvshm`,`tidy`,`tokenizer`,`xlswriter`,`xml`,`xmlreader`,`xmlwriter`,`xz`,`zip`,`zlib`,`yaml`,`zstd`

{{< content "url_healthcheck" >}}
