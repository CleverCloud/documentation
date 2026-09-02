---
type: docs
linkTitle: WordPress
title: Deploy a WordPress website
description: Deploy WordPress on Clever Cloud with PHP, MySQL and persistent storage for media uploads
keywords:
- cms
- mysql
- php
- wordpress
aliases:
- /doc/deploy/application/php/tutorials/tutorial-wordpress
- /doc/php/tutorial-wordpress
- /php/tutorial-wordpress
- /tutorial-wordpress
- /wordpress
---

{{< hextra/hero-subtitle >}}
  Deploy WordPress on Clever Cloud with a managed MySQL database and persistent media storage.
{{< /hextra/hero-subtitle >}}

[WordPress](https://wordpress.org/) runs on Clever Cloud's [PHP runtime](/developers/doc/applications/php/). This guide uses Git deployment so the WordPress core, themes and plugins are versioned with the application while a [MySQL add-on](/developers/doc/addons/mysql/) stores content and an [FS Bucket](/developers/doc/addons/fs-bucket/) stores uploads.

This guide was tested with WordPress 7.1 and PHP 8.4. It also applies to newer compatible WordPress releases.

## Prepare WordPress

Install [Clever Tools](/developers/doc/cli/), log in, download WordPress and initialize the repository:

```bash
npm i -g clever-tools
clever login

curl -LO https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz
cd wordpress
git init
```

Copy the example configuration:

```bash
cp wp-config-sample.php wp-config.php
```

In `wp-config.php`, replace the database definitions with the variables injected by the linked MySQL add-on:

```php {filename="wp-config.php"}
define('DB_NAME', getenv('MYSQL_ADDON_DB'));
define('DB_USER', getenv('MYSQL_ADDON_USER'));
define('DB_PASSWORD', getenv('MYSQL_ADDON_PASSWORD'));
define('DB_HOST', getenv('MYSQL_ADDON_HOST') . ':' . getenv('MYSQL_ADDON_PORT'));
define('DB_CHARSET', 'utf8mb4');
define('DB_COLLATE', '');
```

Replace the eight authentication key and salt definitions with environment-backed values:

```php {filename="wp-config.php"}
define('AUTH_KEY',         getenv('WORDPRESS_AUTH_KEY'));
define('SECURE_AUTH_KEY',  getenv('WORDPRESS_SECURE_AUTH_KEY'));
define('LOGGED_IN_KEY',    getenv('WORDPRESS_LOGGED_IN_KEY'));
define('NONCE_KEY',        getenv('WORDPRESS_NONCE_KEY'));
define('AUTH_SALT',        getenv('WORDPRESS_AUTH_SALT'));
define('SECURE_AUTH_SALT', getenv('WORDPRESS_SECURE_AUTH_SALT'));
define('LOGGED_IN_SALT',   getenv('WORDPRESS_LOGGED_IN_SALT'));
define('NONCE_SALT',       getenv('WORDPRESS_NONCE_SALT'));
```

Add the following before `require_once ABSPATH . 'wp-settings.php';` so WordPress detects HTTPS through Clever Cloud's reverse proxy:

```php {filename="wp-config.php"}
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && str_contains($_SERVER['HTTP_X_FORWARDED_PROTO'], 'https')) {
    $_SERVER['HTTPS'] = 'on';
}

define('DISALLOW_FILE_MODS', true);
```

`DISALLOW_FILE_MODS` prevents changes from the administration interface that would disappear on the next deployment. Add or update WordPress core, themes and plugins in Git instead.

## Create the application and services

Create a PHP application with an alias, then create and link MySQL:

```bash
clever create -t php -a myWordPress
clever addon create mysql-addon myWordPressDatabase -p xs_sml --link myWordPress
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link a resource.

You can display your application's URL or add a custom domain. A custom domain also requires [DNS configuration](/developers/doc/administrate/domain-names/):

```bash
clever domain
clever domain add your.website.tld
```

Select PHP 8.4 and generate independent authentication secrets:

```bash
clever env set CC_PHP_VERSION 8.4

for key in AUTH_KEY SECURE_AUTH_KEY LOGGED_IN_KEY NONCE_KEY AUTH_SALT SECURE_AUTH_SALT LOGGED_IN_SALT NONCE_SALT; do
  clever env set "WORDPRESS_${key}" "$(openssl rand -base64 48)"
done
```

Do not change these values after users have signed in, because doing so invalidates every active WordPress session.

Create and link an FS Bucket for media uploads, then mount it into the absent `wp-content/uploads` directory:

```bash
clever addon create fs-bucket myWordPressFiles --link myWordPress

FS_BUCKET_HOST="$(clever env -F json | jq -er 'first(.fromAddons[] | select(.addonName == "myWordPressFiles") | .env[] | select(.name == "BUCKET_HOST") | .value)')"
clever env set CC_FS_BUCKET "/wp-content/uploads:${FS_BUCKET_HOST}"
unset FS_BUCKET_HOST
```

The name lookup expects the add-on name to be unique. If several add-ons use that name, retrieve the host with `clever addon env ADDON_ID -F json` and the ID returned when the add-on was created. The mount target must not exist in the repository, so do not commit `wp-content/uploads`.

You can also create and link these resources from the [Clever Cloud Console](https://console.clever-cloud.com/).

## Deploy WordPress

Commit and deploy the application:

```bash
git add .
git commit -m "Deploy WordPress"

clever deploy
clever open
```

The first request opens the WordPress installation form. Choose the site title and administrator credentials to initialize the database. Once installation completes, uploaded media is stored in the FS Bucket and remains available across deployments.

## Update WordPress and plugins

Apply updates locally, review them, commit the changed files and deploy again. Keeping code in Git makes deployments reproducible and prevents changes made on a replaced application instance from being lost.

If you use Composer to manage WordPress and plugins as immutable dependencies, see the [Clever WordPress example](https://github.com/CleverCloud/clever-wordpress).

## Improve performance

[Varnish](/developers/doc/develop/varnish/) is available on PHP applications for HTTP caching. Start from the [WordPress VCL example](https://github.com/CleverCloud/varnish-examples/blob/master/wordpress.vcl) and make cache exclusions match your site and plugins.

For object caching, link a [Redis add-on](/developers/doc/addons/redis/) and use a maintained WordPress Redis plugin configured with the injected `REDIS_HOST`, `REDIS_PORT` and `REDIS_PASSWORD` variables. Use a unique cache-key salt when several WordPress sites share the same Redis database.

## Learn more

{{< cards >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://developer.wordpress.org/advanced-administration/before-install/howto-install/" title="WordPress installation" subtitle="Install and configure WordPress" icon="wordpress" >}}
  {{< card link="/developers/doc/applications/php/" title="PHP applications" subtitle="Configure and deploy PHP applications" icon="php" >}}
  {{< card link="/developers/doc/addons/mysql/" title="MySQL" subtitle="Create and administer a managed database" icon="mysql" >}}
  {{< card link="/developers/doc/addons/fs-bucket/" title="FS Buckets" subtitle="Mount persistent file storage in an application" icon="fsbucket" >}}
{{< /cards >}}
