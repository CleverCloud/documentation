---
type: docs
title: Drupal
Description: This article shows you how to deploy a Drupal-based website on Clever Cloud.
tags:
- deploy
keywords:
- php
- drupal
str_replace_dict:
  "@application-type@": "PHP"
aliases:
- /developers/doc/php/tutorial-drupal
- /doc/deploy/application/php/tutorials/tutorial-drupal
- /doc/php/tutorial-drupal
---

## Overview

[Drupal](https://new.drupal.org) applications almost work out of the box on Clever Cloud, you just have a few adjustments to make.

{{< content "create-application" >}}

{{< content "set-env-vars" >}}

{{< content "new-relic" >}}

{{< content "env-injection" >}}

{{< content "link-addon" >}}

## Configure your database

Make sure you have created a MySQL database add-on in the Clever Cloud console, and that it's linked to your application. When it's done, you will be able to access all of your add-on environment variables from the application. You can use them as `DATABASE_URL=$MYSQL_ADDON_URI`.

 {{< content "deploy-git" >}}

### Git specific Drupal instructions

We at this point assume you have downloaded the source files of drupal from [drupal.org](https://new.drupal.org/download) and already have linked your MySQL add-on.

* Open `.gitignore` file and delete `sites/*/settings*.php` line
* Copy the file `sites/default/default.settings.php` to `sites/default/settings.php`
* Open `sites/default/settings.php` and line 213, replace

```php{linenos=table}
$databases = array();
```

by

```php{linenos=table}
    $databases = array (
      'default' =>
        array (
          'default' =>
          array (
            'database' => getenv('MYSQL_ADDON_DB'),
            'username' => getenv('MYSQL_ADDON_USER'),
            'password' => getenv('MYSQL_ADDON_PASSWORD'),
            'host' => getenv('MYSQL_ADDON_HOST'),
            'port' => getenv('MYSQL_ADDON_PORT'),
            'driver' => 'mysql',
            'prefix' => '',
          ),
        ),
    );
```

* Replace the line `$settings['hash_salt'] = ''` (`$drupal_hash_salt` for Drupal 7) with `$settings['hash_salt'] = getenv('DRUPAL_SALT')`. You can generate salts with [this link](https://www.passwordtool.hu/). Add a new `DRUPAL_SALT` [environment variable]({{< ref "doc/applications/php#configure-your-php-application" >}}) to the application with the salt you have generated.
* As mentioned in this [article]({{< ref "doc/addons/fs-bucket" >}}), with Git deployments, files that are uploaded by users must be
persisted in a File System Bucket. In order to do so, [add a File Bucket]({{< ref "doc/addons/fs-bucket" >}}) via the console.
* At the root of your application, create a `clevercloud/buckets.json` file (create a `clevercloud`
folder in which you create a `buckets.json` file).
* Copy the `bucket.json` content from the FS bucket addon dashboard (make sure to edit the `folder` field):

```javascript{linenos=table}
[
   {
      "bucket_host": "<bucket-id>-fsbucket.services.clever-cloud.com",
      "folder": "/sites/default/files"
   }
]
```

* Send these Drupal files via Git.
* When finished, get the url that you can find in the *domains* panel in the left sidebar. Then open the following link:

`https://yourapplication.cleverapps.io/install.php`

Do not forget the **/install.php** page otherwise installation will not happen.

{{< content "deploy-ftp" >}}

{{< content "more-config" >}}
