---
type: docs
title: Laravel
shortdesc: This article shows you how to deploy a Laravel application on Clever Cloud.
tags:
- deploy
keywords:
- php
- laravel
str_replace_dict:
  "@application-type@": "PHP"
aliases:
- /doc/deploy/application/php/tutorials/tutorial-laravel
- /doc/php/tutorial-laravel
---

{{< hextra/hero-subtitle >}}
  Laravel is a PHP web application framework with expressive, elegant syntax. This guide walks you through the minimal requirements to successfully deploy your app.
{{< /hextra/hero-subtitle >}}

## Overview

Deploying a Laravel application on Clever Cloud requires:

- [PHP application](../../doc/applications/php)
- A database add-on: ([MySQL](../../doc/addons/mysql) or [PostgreSQL](../../doc/addons/postgresql))
- An [FS Bucket](../../doc/addons/fs-bucket) for persistent storage.

The following sections explain how to set up each instance step by step:

## Configure your Laravel Application

{{% steps %}}

### Create a PHP application

From the Clever Cloud Console, create a new PHP application and choose your deployment method: [git, GitHub or FTP](../../doc/quickstart/#choose-how-to-deploy).

### Add `DocumentRoot` variable

Add the following environment variable in the Console: `CC_WEBROOT="/public"`.

Or set it with the Clever Cloud CLI:

  ```bash
  clever env set CC_WEBROOT /public
  ```

### Add your application key variable

Make sure `config/app.php` contains the following line:

```php
  'key' => env('APP_KEY'),
```

Locally, run `php artisan key:generate`. It should output something like `base64:tQbFzxwUfOfKKqNlbjXuduwaUFDQUy+NL8DBfgb3o3s=`.

Copy this value and add an environment variable named `APP_KEY`, with this value.

### Configure monolog to use syslog

Make sure `config/logging.php` contains the following line:

```php
  'default' => env('LOG_CHANNEL', 'stack'),
```

In your environment variables, add the `LOG_CHANNEL=syslog` environment variable. This allows you to read your application logs directly from the console or the [CLI](../../doc/cli) tool.

### Optional: configure the front-end build

If you need to build your frontend assets (eg. JavaScript or CSS files), you can either add it as a step in your composer file, or you can add a post build hook with the `CC_PRE_RUN_HOOK` environment variable.

For example: `CC_PRE_RUN_HOOK="npm install && npm run prod"`.

This step is necessary if you are building your Laravel application with [Blade](https://laravel.com/docs/10.x/blade), for example.

### Connect a database

Edit `config/database.php` to set the correct environment variable names. For example, replace `DB_xxx` by `MYSQL_ADDON_xxx` for a MySQL database.

For instance for MySQL:

```php{linenos=table}
   // …
   'connections' => [
     // …
        'mysql' => [
            'driver' => 'mysql',
            'host' => env('MYSQL_ADDON_HOST', '127.0.0.1'),
            'port' => env('MYSQL_ADDON_PORT', '3306'),
            'database' => env('MYSQL_ADDON_DB', 'forge'),
            'username' => env('MYSQL_ADDON_USER', 'forge'),
            'password' => env('MYSQL_ADDON_PASSWORD', ''),
            'unix_socket' => env('DB_SOCKET', ''),
            'charset' => 'utf8mb4',
            'collation' => 'utf8mb4_unicode_ci',
            'prefix' => '',
            'strict' => true,
            'engine' => null,
        ],
    // …
    ]
  // …
```

Create a database add-on (either MySQL or PostgresSQL) and link it to your application. If your add-on already exists, use the **Service Dependencies > Link add-ons** dropdown menu in your application options, to select the name of the add-on you want to link and use the add button to finish the process.

### Optional: automatically run migrations upon deployment

If you want to have database migrations automatically run during each deployment, add this hook instruction to the application's environment variables `CC_POST_BUILD_HOOK=php artisan migrate --force`

### Configure storage

Create a FS Bucket add-on and link it to your application. Note its host (you can see it from the add-on configuration panel, or in the environment variables exported by the add-on). It looks like `bucket-01234567-0123-0123-0123-012345678987-fsbucket.services.clever-cloud.com`.

Create a new environment variable called `CC_FS_BUCKET` and set `/storage/app:<bucket-host>` as its value.

{{% /steps %}}

## Optional Further Configuration

### Task scheduling

If your app uses [task scheduling](https://laravel.com/docs/scheduling), you need to configure a cron to run the scheduling process:

1. Create a `clevercloud/cron.json` file in your project, containing:

```json
[
    "* * * * * $ROOT/clevercloud/cron.sh"
]
```

This installs a cron to run `clevercloud/cron.sh` every minute.

2. Create a `clevercloud/cron.sh` file in your project (with execute permissions), containing:

```bash
#!/bin/bash -l
set -euo pipefail

pushd "$APP_HOME"
php artisan schedule:run >> /dev/null 2>&1
```

Note: the PHP CLI process uses a `memory_limit` configuration value that depends on the instance's size (you can verify this value by connecting to your app using SSH and running `php -i`).

If one of your scheduled tasks needs to allocate more memory than this limit, the `php artisan schedule:run` process is going to silently crash.

To allow it to use more memory, you can call [`ini_set()`](https://www.php.net/manual/en/function.ini-set) inside a `php_sapi_name() === 'cli'` condition from an early hook to the app's lifecycle (like the `AppServiceProvider`).

See [this Gist](https://gist.github.com/dsferruzza/e57dd3db957efe7a649325868f0024a4) for an example implementation.

### Trusted Proxy

To ensure Laravel correctly handles HTTP requests when using the Clever Cloud HTTP reverse proxy (Sōzu), add the following code to the `config/trustedproxy.php` file:

```php{linenos=table}
<?php
return [
    'proxies' => env('CC_REVERSE_PROXY_IPS'),
];
```

This environment variable exists in any Clever Cloud instance. This configuration specifies to trust Clever Cloud proxies, allowing Laravel to seamlessly recognize HTTP requests in the presence of a proxyhugo server.

{{< content "more-config" >}}

## Go Further

{{< cards >}}
  {{< card link="../../doc/metrics/new-relic" title="Monitor your App with New Relic" subtitle="Connect your application to New Relic." icon="new-relic" >}}
  {{< card link="../../doc/addons/fs-bucket" title="FS Bucket" subtitle="External File System for your apps" icon="fsbucket" >}}
  {{< card link="../../doc/develop/build-hooks" title="Deployment hooks" subtitle="Learn about custom commands used in this guide." icon="rocket-launch" >}}
  {{< card link="https://laravel.com/docs/10.x/deployment" title="Laravel Documentation" subtitle="Read Laravel documentation on deployments." icon="laravel" >}}
{{< /cards >}}
