---
type: docs
linkTitle: Laravel
title: Deploy a Laravel application
description: Deploy a Laravel PHP application on Clever Cloud with a managed database, migrations, logs, scheduled tasks, and persistent file storage
keywords:
- laravel
- php
- mysql
- postgresql
- artisan
aliases:
- /deploy/application/php/tutorials/tutorial-laravel
- /doc/deploy/application/php/tutorials/tutorial-laravel
- /doc/php/tutorial-laravel
- /tutorial-laravel
---

{{< hextra/hero-subtitle >}}
  Deploy a Laravel application on Clever Cloud with a managed MySQL or PostgreSQL database.
{{< /hextra/hero-subtitle >}}

[Laravel](https://laravel.com/) applications run on Clever Cloud's [PHP runtime](/developers/doc/applications/php/), which installs Composer dependencies and serves the application's public directory through NGINX.

## Prepare the application

This guide assumes that your Laravel application works locally and contains a `composer.json` file. Commit `composer.lock` so that Clever Cloud installs the same dependency versions you tested locally.

Laravel uses its standard `DB_*` variables, while linked Clever Cloud add-ons expose provider-specific variables. Configure the MySQL connection in `config/database.php` as follows:

```php {filename="config/database.php"}
'mysql' => [
    'driver' => 'mysql',
    'host' => env('MYSQL_ADDON_HOST', '127.0.0.1'),
    'port' => env('MYSQL_ADDON_PORT', '3306'),
    'database' => env('MYSQL_ADDON_DB', 'laravel'),
    'username' => env('MYSQL_ADDON_USER', 'root'),
    'password' => env('MYSQL_ADDON_PASSWORD', ''),
    'unix_socket' => env('DB_SOCKET', ''),
    'charset' => env('DB_CHARSET', 'utf8mb4'),
    'collation' => env('DB_COLLATION', 'utf8mb4_unicode_ci'),
    'prefix' => '',
    'prefix_indexes' => true,
    'strict' => true,
    'engine' => null,
],
```

For PostgreSQL, map the corresponding connection values to `POSTGRESQL_ADDON_HOST`, `POSTGRESQL_ADDON_PORT`, `POSTGRESQL_ADDON_DB`, `POSTGRESQL_ADDON_USER`, and `POSTGRESQL_ADDON_PASSWORD` instead.

## Create and configure the application

Install [Clever Tools](/developers/doc/cli/), log in, initialize Git if needed, then create a PHP application with an alias:

```bash
npm i -g clever-tools
clever login

git init
clever create -t php -a myLaravelApp
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link a resource.

You can display your application's URL or add a custom domain. A custom domain also requires [DNS configuration](/developers/doc/administrate/domain-names/):

```bash
clever domain
clever domain add your.website.tld
```

Create a MySQL add-on and link it to the application. You can use a [PostgreSQL add-on](/developers/doc/addons/postgresql/) instead if the application is configured for PostgreSQL:

```bash
clever addon create mysql-addon myLaravelDatabase -p xs_sml --link myLaravelApp
```

You can also create and link these resources from the [Clever Cloud Console](https://console.clever-cloud.com/).

Set the public directory, PHP version, application key, log destination, and database driver. Generate a different `APP_KEY` for each application environment and do not change it after encrypted data has been stored:

```bash
clever env set CC_WEBROOT /public
clever env set CC_PHP_VERSION 8.4
clever env set APP_KEY "base64:$(openssl rand -base64 32)"
clever env set LOG_CHANNEL stderr
clever env set DB_CONNECTION mysql
clever env set CC_POST_BUILD_HOOK "php artisan migrate --force"
```

The post-build hook applies pending [database migrations](https://laravel.com/docs/migrations) before the new instance replaces the previous one. Review destructive migrations and use an application-specific deployment strategy when a schema change is not backward-compatible.

### Build frontend assets

If the application uses Vite or another frontend build tool, run it during the build phase. Put multiple post-build operations in an executable script rather than setting several `CC_POST_BUILD_HOOK` values. For example:

```bash {filename="clevercloud/post_build.sh"}
#!/bin/bash
set -euo pipefail

npm ci
npm run build
php artisan migrate --force
```

```bash
chmod +x clevercloud/post_build.sh
clever env set CC_POST_BUILD_HOOK "./clevercloud/post_build.sh"
```

The PHP runtime can use the platform's Node.js version selectors and package managers when building frontend assets. See [environment variables](/developers/doc/reference/reference-environment-variables/) for the available controls.

## Deploy Laravel

Commit the application and deploy it:

```bash
git add .
git commit -m "Deploy Laravel"

clever deploy
clever open
```

The first deployment installs Composer dependencies and runs every pending migration. Follow its progress and inspect application logs with:

```bash
clever activity --follow
clever logs
```

## Persist uploaded files

Application instances are replaced during deployments, so files written to their local filesystem are not persistent. Prefer object storage for user uploads when the application supports it. For code that requires a local filesystem, create and link an [FS Bucket](/developers/doc/addons/fs-bucket/), then mount it into a directory that does not already exist in the repository.

For example, mount a bucket as `storage/persistent`:

```bash
clever addon create fs-bucket myLaravelFiles --link myLaravelApp

FS_BUCKET_HOST="$(clever env -F json | jq -er 'first(.fromAddons[] | select(.addonName == "myLaravelFiles") | .env[] | select(.name == "BUCKET_HOST") | .value)')"
clever env set CC_FS_BUCKET "/storage/persistent:${FS_BUCKET_HOST}"
unset FS_BUCKET_HOST
```

The name lookup expects the add-on name to be unique. If several add-ons use that name, retrieve the host with `clever addon env ADDON_ID -F json` and the ID returned when the add-on was created.

Declare a dedicated Laravel disk whose root matches the mounted directory:

```php {filename="config/filesystems.php"}
'persistent' => [
    'driver' => 'local',
    'root' => storage_path('persistent'),
    'throw' => false,
],
```

Use `Storage::disk('persistent')` for data that must survive deployments. Do not commit the `storage/persistent` directory, because an existing non-empty target prevents the FS Bucket from being mounted.

## Run scheduled tasks

If the application uses Laravel's [task scheduler](https://laravel.com/docs/scheduling), create the following cron configuration:

```json {filename="clevercloud/cron.json"}
[
  "* * * * * $ROOT/clevercloud/cron.sh"
]
```

Add the executable script called by the cron:

```bash {filename="clevercloud/cron.sh"}
#!/bin/bash -l
set -euo pipefail

cd "$APP_HOME"
php artisan schedule:run
```

```bash
chmod +x clevercloud/cron.sh
```

The [PHP CLI memory limit](/developers/doc/applications/php/#memory-limit) depends on the application instance size. Monitor scheduled jobs and scale the application if they need more memory.

## Learn more

{{< cards >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://laravel.com/docs/deployment" title="Laravel deployment" subtitle="Prepare and optimize a Laravel application for production" icon="laravel" >}}
  {{< card link="/developers/doc/applications/php/" title="PHP applications" subtitle="Configure and deploy PHP applications" icon="php" >}}
  {{< card link="/developers/doc/develop/build-hooks/" title="Deployment hooks" subtitle="Run commands during build and deployment phases" icon="rocket-launch" >}}
  {{< card link="/developers/doc/addons/fs-bucket/" title="FS Buckets" subtitle="Mount persistent file storage in an application" icon="fsbucket" >}}
{{< /cards >}}
