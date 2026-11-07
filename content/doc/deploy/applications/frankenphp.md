---
type: docs
linkTitle: FrankenPHP
title: FrankenPHP application runtime
description: Deploy PHP applications on Clever Cloud with FrankenPHP, the PHP application server built on Caddy, with Composer, worker mode, and Mercure
keywords:
- caddy
- framework
- frankenphp
- frankenphp cloud
- laravel
- mercure
- performance
- php app hosting
- symfony
- worker mode
aliases:
- /doc/applications/frankenphp
---

## Overview

[FrankenPHP](https://frankenphp.dev) is a PHP application server built on the [Caddy](https://caddyserver.com/docs/) web server. It runs PHP in the same process as the web server, instead of pairing a web server, such as Nginx, with PHP-FPM. Clever Cloud installs your Composer dependencies, then starts FrankenPHP.

FrankenPHP serves PHP frameworks such as [Laravel](https://laravel.com) and [Symfony](https://symfony.com). It can keep your application in memory between requests with its [worker mode](#worker-mode), and includes a [Mercure](https://mercure.rocks) hub to push real-time updates to browsers. For Apache and PHP-FPM, use the [PHP runtime](/doc/deploy/applications/php/).

## Create your FrankenPHP application

To create a new FrankenPHP application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type frankenphp
```

- [Learn more about Clever Tools](/doc/tools/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

> [!NOTE] FrankenPHP applications run on `nano` instances or larger, and use `XS` by default

## Configure your FrankenPHP application

### Mandatory needs

A FrankenPHP application needs an `index.php` file, at the root of the folder Clever Cloud serves. For instance:

```php {filename="index.php"}
<?php
echo 'Hello from FrankenPHP on Clever Cloud';
```

To try it, [install FrankenPHP](https://frankenphp.dev/docs/#getting-started), run `frankenphp php-server --listen :8080` in its folder, and open `http://localhost:8080`.

FrankenPHP serves the files that exist, such as images or styles, and sends every other request to `index.php`. This file is the front controller of frameworks such as Laravel and Symfony, which route the request themselves.

### Served folder

By default, Clever Cloud serves the root of your repository. Most frameworks serve a `public` folder instead, which keeps the code of your application out of reach. Set its path, from the root of the repository, in `CC_WEBROOT`:

```bash
clever env set CC_WEBROOT /public
```

With `APP_FOLDER`, Clever Cloud installs the dependencies and starts FrankenPHP from this folder, where it reads `composer.json`, `php.ini`, and the path of the worker. `CC_WEBROOT` still starts from the root of the repository, such as `/app/public` for a project in `app`.

### Build phase

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/). Then, if your project has a `composer.json` file at its root, it installs the dependencies listed there with [Composer](https://getcomposer.org), the package manager of PHP:

```bash
composer install --no-interaction --no-progress --no-scripts --no-dev
```

Commit the `composer.lock` file, which pins the version of each dependency: without it, Composer installs the latest versions that match `composer.json`. To use your own version of Composer, add its `composer.phar` file at the root of your project.

Two variables change this command:

- `CC_PHP_COMPOSER_FLAGS` replaces `--no-interaction --no-progress --no-scripts`
- `CC_PHP_DEV_DEPENDENCIES=install` removes `--no-dev`, to install the development dependencies

Clever Tools reads a value starting with `-` as an option: add `--` before it, as here to optimize the class loading:

```bash
clever env set CC_PHP_COMPOSER_FLAGS -- "--no-interaction --no-progress --no-scripts --optimize-autoloader"
```

{{% content "private-composer-repositories" %}}

### Composer scripts

[Composer scripts](https://getcomposer.org/doc/articles/scripts.md), such as Laravel's `post-autoload-dump` commands, don't run by default. Set them in a post-build hook instead:

```bash
clever env set CC_POST_BUILD_HOOK "php artisan package:discover"
```

The `php` command of the image runs `frankenphp php-cli`, in hooks, scripts, and Tasks. With Composer scripts, replace `@php` with `php`: Composer runs `@php` with the FrankenPHP binary and options it doesn't accept, and the build fails with `unknown shorthand flag: 'd'`.

### FrankenPHP version and tools

Clever Cloud deploys FrankenPHP `{{< runtime_version frankenphp >}}`, with PHP `{{< runtime_version frankenphp php >}}` and Caddy `{{< runtime_version frankenphp caddy >}}`, whatever the value of `CC_PHP_VERSION`. The image also includes Composer and the [Symfony CLI](https://symfony.com/download). To install other tools, declare them in a [`mise.toml` file](/doc/manage/mise/).

To change a PHP setting, such as `memory_limit`, add a `php.ini` file at the root of your project:

```ini {filename="php.ini"}
memory_limit = 256M
```

### Included extensions

FrankenPHP loads these PHP extensions:

`amqp`, `apcu`, `ast`, `bcmath`, `brotli`, `bz2`, `calendar`, `ctype`, `curl`, `dba`, `deepclone`, `dom`, `exif`, `fileinfo`, `filter`, `ftp`, `gd`, `gettext`, `gmp`, `iconv`, `igbinary`, `imagick`, `intl`, `ldap`, `lz4`, `mbstring`, `memcached`, `msgpack`, `mysqli`, `mysqlnd`, `opcache`, `openssl`, `parallel`, `pcntl`, `pdo`, `pdo_mysql`, `pdo_pgsql`, `pdo_sqlite`, `pgsql`, `phar`, `posix`, `protobuf`, `readline`, `redis`, `session`, `shmop`, `simplexml`, `soap`, `sockets`, `sodium`, `sqlite3`, `ssh2`, `sysvmsg`, `sysvsem`, `sysvshm`, `tidy`, `tokenizer`, `xlswriter`, `xml`, `xmlreader`, `xmlwriter`, `xsl`, `xz`, `yaml`, `zip`, `zlib`, `zstd`

- [See the PHP configuration of the FrankenPHP image](https://frankenphpinfo85.cleverapps.io/)

### Start command

Clever Cloud starts FrankenPHP from the root of your project, on port `8080`, or `9000` with [Request Flow](/doc/manage/request-flow/). It runs `frankenphp php-server --listen 0.0.0.0:8080`, with the served folder in `--root`, and the [worker](#worker-mode) in `--worker`.

`CC_FRANKENPHP_PORT` sets another port. With `CC_RUN_COMMAND`, Clever Cloud runs your own command instead, from the root of the repository. This command then sets the address, the served folder, and the worker itself:

```bash
clever env set CC_RUN_COMMAND 'frankenphp php-server --listen 0.0.0.0:$PORT --root public --debug'
```

With Request Flow, set `PORT=9000`, as [Clever Cloud doesn't change it](/doc/manage/#with-request-flow). To use a [Caddyfile](https://frankenphp.dev/docs/config/), start FrankenPHP with `frankenphp run`:

```text {filename="Caddyfile"}
{
    frankenphp
}

:{$PORT} {
    root * public
    php_server
}
```

```bash
clever env set CC_RUN_COMMAND "frankenphp run --config Caddyfile"
```

### Worker mode

By default, PHP starts your application again for each request. In [worker mode](https://frankenphp.dev/docs/worker/), FrankenPHP starts a script once and keeps it in memory. The script then handles requests in a loop, which saves the startup time of your framework. For instance:

```php {filename="public/index.php"}
<?php
// Runs once, when the worker starts
$count = 0;

$handler = static function () use (&$count) {
    // Runs for each request
    $count++;
    echo "Request {$count} handled by this worker";
};

while (frankenphp_handle_request($handler)) {
    gc_collect_cycles();
}
```

Set the path of the script, from the root of your project, in `CC_FRANKENPHP_WORKER`. It must be in the served folder, or the deployment fails:

```bash
clever env set CC_FRANKENPHP_WORKER /public/index.php
```

A worker keeps its state between requests: reset what a request changes, such as global variables. A script that doesn't call `frankenphp_handle_request` can't run as a worker, and the log shows `worker script has failed on restart`.

The FrankenPHP guides for [Symfony](https://frankenphp.dev/docs/symfony/) and [Laravel](https://frankenphp.dev/docs/laravel/) describe how to run their applications in worker mode.

### Real-time updates with Mercure

The `--mercure` option of `frankenphp php-server` starts the [Mercure](https://frankenphp.dev/docs/mercure/) hub of FrankenPHP, at `/.well-known/mercure`. It needs the keys that sign the tokens of publishers and subscribers, in `MERCURE_PUBLISHER_JWT_KEY` and `MERCURE_SUBSCRIBER_JWT_KEY`:

```bash
clever env set MERCURE_PUBLISHER_JWT_KEY "$(openssl rand -base64 32)"
clever env set MERCURE_SUBSCRIBER_JWT_KEY "$(openssl rand -base64 32)"
clever env set CC_RUN_COMMAND 'frankenphp php-server --listen 0.0.0.0:$PORT --root public --mercure'
```

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps the `vendor` folder of Composer between commits, at the root of the repository.

## FrankenPHP and Materia KV

[Materia KV](/doc/deploy/databases/materia-kv/) is a serverless key-value store, compatible with Redis clients. To use it from FrankenPHP, link it to your application and connect with the included `redis` extension, over TLS, with the variables of the add-on:

```php {filename="public/kv.php"}
<?php
$redis = new Redis();
$redis->connect('tls://' . getenv('KV_HOST'), (int) getenv('KV_PORT'));
$redis->auth(getenv('KV_TOKEN'));

$redis->set('greeting', 'Hello from Materia KV');
echo $redis->get('greeting');
```

- [Materia KV and FrankenPHP demo](https://github.com/CleverCloud/frankenphp-kv-json-example)

## FrankenPHP applications as Clever Tasks

A FrankenPHP application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration: Clever Cloud builds it, then runs `CC_RUN_COMMAND`.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks), here for a `bin/task.php` script:

```bash
clever create --type frankenphp --task "php bin/task.php"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
