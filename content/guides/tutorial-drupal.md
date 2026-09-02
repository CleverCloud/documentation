---
type: docs
linkTitle: Drupal
title: Deploy a Drupal website
description: Deploy Drupal on Clever Cloud with Composer, PHP, MySQL and persistent file storage
keywords:
- cms
- composer
- drupal
- mysql
- php
aliases:
- /doc/deploy/application/php/tutorials/tutorial-drupal
- /doc/php/tutorial-drupal
- /php/tutorial-drupal
---

{{< hextra/hero-subtitle >}}
  Deploy Drupal on Clever Cloud with a managed MySQL database and persistent public files.
{{< /hextra/hero-subtitle >}}

[Drupal](https://www.drupal.org/) runs on Clever Cloud's [PHP runtime](/developers/doc/applications/php/). This guide follows Drupal's recommended Composer layout, where the public document root is the `web` directory.

This guide was tested with Drupal 11.4.5 and PHP 8.4. Check the [Drupal system requirements](https://www.drupal.org/docs/getting-started/system-requirements) before selecting versions for a different release.

## Prepare Drupal

Install [Composer](https://getcomposer.org/download/) and create the project using the current supported Drupal branch:

```bash
composer create-project drupal/recommended-project:^11.4 myDrupal
cd myDrupal
git init
```

Commit `composer.lock` so deployments install the versions you tested.

Create `web/sites/default/settings.php` with the database, proxy and security configuration:

```php {filename="web/sites/default/settings.php"}
<?php

$databases['default']['default'] = [
  'database' => getenv('MYSQL_ADDON_DB'),
  'username' => getenv('MYSQL_ADDON_USER'),
  'password' => getenv('MYSQL_ADDON_PASSWORD'),
  'host' => getenv('MYSQL_ADDON_HOST'),
  'port' => getenv('MYSQL_ADDON_PORT'),
  'driver' => 'mysql',
  'namespace' => 'Drupal\\mysql\\Driver\\Database\\mysql',
  'autoload' => 'core/modules/mysql/src/Driver/Database/mysql/',
  'prefix' => '',
];

$settings['hash_salt'] = getenv('DRUPAL_HASH_SALT');
$settings['reverse_proxy'] = TRUE;
$settings['reverse_proxy_addresses'] = array_filter(array_map('trim', explode(',', getenv('CC_REVERSE_PROXY_IPS') ?: '')));

$trusted_host = getenv('DRUPAL_TRUSTED_HOST_PATTERN');
if ($trusted_host) {
  $settings['trusted_host_patterns'] = [$trusted_host];
}
```

Keep generated dependencies and persistent files out of Git. The recommended project already provides suitable ignore rules; verify that they include at least `vendor`, `web/core`, contributed extensions and `web/sites/*/files`.

## Create the application and services

Install [Clever Tools](/developers/doc/cli/), log in, then create a PHP application and a linked MySQL add-on:

```bash
npm i -g clever-tools
clever login

clever create -t php -a myDrupal
clever addon create mysql-addon myDrupalDatabase -p xs_sml --link myDrupal
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link a resource.

You can display your application's URL or add a custom domain. A custom domain also requires [DNS configuration](/developers/doc/administrate/domain-names/):

```bash
clever domain
clever domain add your.website.tld
```

Set the public directory, PHP version and a stable random salt. Drupal's Composer scaffold is implemented by Composer scripts, so override the PHP runtime's default `--no-scripts` flag:

```bash
clever env set CC_WEBROOT /web
clever env set CC_PHP_VERSION 8.4
clever env set DRUPAL_HASH_SALT "$(openssl rand -base64 48)"
clever env set -- CC_PHP_COMPOSER_FLAGS "--no-interaction --no-progress --optimize-autoloader"
```

Do not change `DRUPAL_HASH_SALT` after the site starts using hashes and one-time links.

For an exact custom domain, add a trusted host pattern. Escape dots because Drupal expects a regular expression:

```bash
clever env set DRUPAL_TRUSTED_HOST_PATTERN '^your\.website\.tld$'
```

Create and link an FS Bucket for public files, then mount it into the absent `web/sites/default/files` directory:

```bash
clever addon create fs-bucket myDrupalFiles --link myDrupal

FS_BUCKET_HOST="$(clever env -F json | jq -er 'first(.fromAddons[] | select(.addonName == "myDrupalFiles") | .env[] | select(.name == "BUCKET_HOST") | .value)')"
clever env set CC_FS_BUCKET "/web/sites/default/files:${FS_BUCKET_HOST}"
unset FS_BUCKET_HOST
```

The name lookup expects the add-on name to be unique. If several add-ons use that name, retrieve the host with `clever addon env ADDON_ID -F json` and the ID returned when the add-on was created. Do not create or commit the mount target, because an existing non-empty directory prevents the FS Bucket from being mounted.

You can also create and link these resources from the [Clever Cloud Console](https://console.clever-cloud.com/).

## Deploy and install Drupal

Commit and deploy the project:

```bash
git add .
git commit -m "Deploy Drupal"

clever deploy
clever open
```

Composer installs Drupal and generates the `web` directory during the build. The browser then opens Drupal's installer. Choose a language and installation profile. The database screen reads its host, name, user and port from `settings.php`; enter `MYSQL_ADDON_PASSWORD`, available in the application's environment variables or the linked MySQL add-on, then continue with the site and administrator settings.

After installation, the database contains Drupal configuration and content while the FS Bucket contains public uploads and generated CSS or JavaScript aggregates. Both remain available when an application instance is replaced.

## Update Drupal

Update the project locally with Composer, review the changes and commit the updated lock file:

```bash
composer update "drupal/core-*" --with-all-dependencies
git add composer.json composer.lock
git commit -m "Update Drupal"

clever deploy
```

Follow Drupal's [update procedure](https://www.drupal.org/docs/updating-drupal) and apply pending database updates after deploying compatible code. Back up the database and persistent files before a major upgrade.

## Learn more

{{< cards >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://www.drupal.org/docs/getting-started/installing-drupal" title="Drupal installation" subtitle="Install and configure a Drupal website" icon="drupal" >}}
  {{< card link="/developers/doc/applications/php/" title="PHP applications" subtitle="Configure and deploy PHP applications" icon="php" >}}
  {{< card link="/developers/doc/addons/mysql/" title="MySQL" subtitle="Create and administer a managed database" icon="mysql" >}}
  {{< card link="/developers/doc/addons/fs-bucket/" title="FS Buckets" subtitle="Mount persistent file storage in an application" icon="fsbucket" >}}
{{< /cards >}}
