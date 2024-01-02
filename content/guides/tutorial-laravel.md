---
type: docs
title: Laravel
shortdesc: This article shows you how to deploy a laravel application on Clever Cloud.
tags:
- deploy
keywords:
- php
- laravel
str_replace_dict:
  "@application-type@": "PHP"
aliases:
- /doc/deploy/applications/php/tutorials/tutorial-laravel
---

## Overview

Laravel applications almost work out of the box on Clever Cloud, you just have a few adjustments to make.

{{< readfile file="create-application.md" >}}

{{< readfile file="set-env-vars.md" >}}

## Configure your Laravel application

### Configure `DocumentRoot`

Add a new [environment variable](#setting-up-environment-variables-on-clever-cloud) called `CC_WEBROOT` and set `/public` as its value.

```
clever env set CC_WEBROOT /public 
```

### Configure your application key

Locally, run `php artisan key:generate`. It should output something like `base64:tQbFzxwUfOfKKqNlbjXuduwaUFDQUy+NL8DBfgb3o3s=`. Copy this value and add an [environment variable](#setting-up-environment-variables-on-clever-cloud) named `APP_KEY`, with this value.

Make sure `config/app.php` contains the following line:

```php
  'key' => env('APP_KEY'),
```

### Configure monolog to use syslog

In your environment variables, add the `LOG_CHANNEL=syslog` [environment variable](#setting-up-environment-variables-on-clever-cloud). This will allow you to read your application logs directly from the console or the CLI tool.

Make sure `config/logging.php` contains the following line:

```php
  'default' => env('LOG_CHANNEL', 'stack'),
```

### Optional: configure the front-end build

If you need to build your frontend assets (eg. javascript or CSS files), you can either add it as a step in your composer file, or you can add a post build hook with the `CC_POST_BUILD_HOOK` [environment variable](#setting-up-environment-variables-on-clever-cloud).

For example, if you launch the build with `npm run prod`: `CC_POST_BUILD_HOOK=npm install && npm run prod`.

{{< readfile file="new-relic.md" >}}

{{< readfile file="env-injection.md" >}}

{{< readfile file="link-addon.md" >}}

### Connect a database

Make sure you have created a database add-on in the Clever Cloud console, and that it's linked to your application. When it's done, edit `config/database.php` to set the correct environment variable names (`MYSQL_ADDON_xxx` instead of `DB_xxx` for a mysql database).

For instance for MySQL:

```php
   // ...
   'connections' => [
     // ...
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
    // ...
    ]
  // ...
```

### Optional: automatically run migrations upon deployment

If you want to have database migrations automatically run during each deployment, add this hook instruction to the application's [environment variables](#setting-up-environment-variables-on-clever-cloud) `CC_POST_BUILD_HOOK=php artisan migrate --force`

### Configure storage

Create a FS Bucket add-on and link it to your application. Note its host (you can see it from the addon configuration panel, or in the environment variables exported by the addon). It looks like `bucket-01234567-0123-0123-0123-012345678987-fsbucket.services.clever-cloud.com`.

Create a new [environment variable](#setting-up-environment-variables-on-clever-cloud) called `CC_FS_BUCKET` and set `/storage/app:<bucket-host>` as its value.

### Optional: Configure task scheduling

If your app uses [task scheduling](https://laravel.com/docs/scheduling), you need to configure a cron to run the scheduling process:

1. Create a `clevercloud/cron.json` file in your project, containing:

```json
[
    "* * * * * $ROOT/clevercloud/cron.sh"
]
```

This installs a cron that will run `clevercloud/cron.sh` every minute.

2. Create a `clevercloud/cron.sh` file in your project (with execute permissions), containing:

```bash
#!/bin/bash -l
set -euo pipefail

pushd "$APP_HOME"
php artisan schedule:run >> /dev/null 2>&1
```

Note: the PHP CLI process will use a `memory_limit` configuration value that depends on the instance's size (you can check it by connecting to your app using SSH and running `php -i`).
If one of your scheduled tasks needs to allocate more memory than this limit, the `php artisan schedule:run` process will silently crash.
To allow it to use more memory, you can call [`ini_set()`](https://www.php.net/manual/en/function.ini-set) inside a `php_sapi_name() === 'cli'` condition from an early hook to the app's lifecycle (like the `AppServiceProvider`).
See [this Gist](https://gist.github.com/dsferruzza/e57dd3db957efe7a649325868f0024a4) for an example implementation.

### Optional: Configure trusted proxy

To ensure Laravel correctly handles HTTP requests when using the Clever Cloud HTTP reverse proxy (Sōzu), add the following code to the `config/trustedproxy.php` file:

```php
<?php

return [
    'proxies' => env('CC_REVERSE_PROXY_IPS'),
];

```

This environment variable exists in any Clever Cloud instance. This configuration specifies that Clever Cloud proxies are trusted, allowing Laravel to seamlessly recognize HTTP requests in the presence of a proxy.

{{< readfile file="deploy-git.md" >}}

{{< readfile file="deploy-ftp.md" >}}

{{< readfile file="more-config.md" >}}

