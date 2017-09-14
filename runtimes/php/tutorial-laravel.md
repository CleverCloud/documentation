---
title: Deploy a Laravel application
shortdesc: This article shows you how to deploy a laravel application on Clever Cloud.
tags:
- php
- laravel
---

# Deploy a Laravel application

Laravel applications almost work out of the box on Clever Cloud, you just have a few adjustments to make.

## Create an application

You can find in [this article](/doc/clever-cloud-overview/add-application/#create-an-application) the process to create an
application.
We strongly recommend to use git deployment for laravel applications. This tutorial assumes a git deployment.

### Configure `DocumentRoot`

Create a `php.json` file in a `clevercloud` directory at the root of your application.

```json
{
  "deploy": {
    "webroot": "/public"
  }
}
```

### Access to the laravel environment

If you already have a `.env` file in your application, please don't commit it: credentials are not meant to be committed alongside your applications. Clever Cloud allows you to inject environment in your app, so you can dynamically like databases and have separate environments with the same code base.

From the console, you can edit the application's environment variables. Click on "expert mode", you'll be able to directly paste the contents of the .env file.

From the CLI, it's even simpler: `clever env import < .env`.

### Configure your application key

On your machine, run `php artisan key:generate`. It should output something like `base64:tQbFzxwUfOfKKqNlbjXuduwaUFDQUy+NL8DBfgb3o3s=`. Copy this value and add an enviroment variable named `APP_KEY`, with this value.

Make sure `config/app.php` contains the following line:

```php
  'key' => env('APP_KEY'),
```

### Configure monolog to use syslog

In your environment variables, add the `APP_LOG` variable, with `syslog` as value. This will allow you to read your application logs directly from the console or the CLI tool.

Make sure `config/app.php` contains the following line:

```php
  'log' => env('APP_LOG', 'single'),
```

### Configure your database

Make sure you have created a database, and that it's linked to your application. When it's done, edit `config/database.php` to set the correct environment variable names (`MYSQL_ADDON_xxx` instead of `DB_xxx` for a mysql database).

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
            'username' => env('MYSQL_ADDON_USERNAME', 'forge'),
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

#### Optional: automatically run migrations upon deployment

If you want to have database migrations automatically run during each deployment, add this to the application's environment variables:

```
CC_POST_BUILD_HOOK=php artisan migrate --force
```

### Configure storage

Create a FS Bucket and link it to your application. Note its host (you can see it from the addon configuration panel, or in the environment variables exported by the addon). It looks like `bucket-01234567-0123-0123-0123-012345678987-fsbucket.services.clever-cloud.com`.

Create a new environment variable called `CC_FS_BUCKET` and set `/storage/app:<bucket-host>` as its value.

### Optional: configure the front-end build

If you need to build your frontend assets (eg. javascript or CSS files), you can either add it as a step in your composer file, or you can add a post build hook with the `CC_POST_BUILD_HOOK` environment variable.

For example, if you launch the build with `npm run prod`: `CC_POST_BUILD_HOOK=npm install && npm run prod`.