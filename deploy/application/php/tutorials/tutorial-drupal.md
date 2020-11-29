---
title: Deploying a Drupal website
shortdesc: This article shows you how to deploy a Drupal-based website on Clever Cloud.
tags:
- php
---

## Create an application

You can find in [this article](/doc/clever-cloud-overview/add-application/#create-an-application) the process to create an application.

## Two choices for deployment

During the creation of a PHP application, it is asked if you want to deploy it via FTP or via Git. These two techniques have their own pros and cons but have the same end result.

## Deploy via FTP

1. Download the Drupal source files on [drupal.org](http://drupal.org)
2. [Add a MySQL database add-on](/doc/addons/clever-cloud-addons/) and link it to your application
3. [Send these Drupal files via FTP](/doc/clever-cloud-overview/add-application/#ftp-deployment) using the FTP credentials from the addon dashboard.
4. When finished, launch the application with the url that you can find in the *domains* panel in the left sidebar.
5. Follow the Drupal installation steps.
6. When asked for database informations, fill them with the ones displayed in the database addon dashboard.
  * database name
  * database username
  * database password
  * database host, for example `bj79c949bvl2deb6.mysql.services.clever-cloud.com`
  * database port

*Note: You can also make use of environnement variables. But any env update will require a re-deploy of the app*


## Deploy via Git

1. Download the Drupal source files on [drupal.org](http://drupal.org)
2. [Add a MySQL database add-on](/doc/addons/clever-cloud-addons/) and link it to your application
3. Open `.gitignore` file and delete `sites/*/settings*.php` line
4. Copy the file `sites/default/default.settings.php` to `sites/default/settings.php`
5. Open `sites/default/settings.php` and line 213, replace

    ```php
    $databases = array();
    ```

    <br/>
    by

    ```php
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
6. Replace the line `$settings['hash_salt'] = ''` (`$drupal_hash_salt` for Drupal 7) with `$settings['hash_salt'] = getenv('DRUPAL_SALT')`. You can generate salts with [this link](http://www.passwordtool.hu/). Add a new `DRUPAL_SALT` [environment variable](/doc/php/php-apps/#environment-injection) to the application with the salt you have generated.
7. As mentioned in this [article](/doc/addons/fs_buckets/), with Git deployments, files that are uploaded by users must be
persisted in a File System Bucket. In order to do so, [add a File Bucket](/doc/addons/fs_buckets/) via the console.
8. At the root of your application, create a `clevercloud/buckets.json` file (create a `clevercloud`
folder in which you create a `buckets.json` file).
9. Copy the `bucket.json` content from the FS bucket addon dashboard (make sure to edit the `folder` field):

```javascript
[
   {
      "bucket_host": "<bucket-id>-fsbucket.services.clever-cloud.com",
      "folder": "/sites/default/files"
   }
]
```

10. Send these Drupal files via Git. Read this [article](/doc/clever-cloud-overview/add-application/#git-deployment) if you need more information about it.
11. When finished, get the url that you can find in the *domains* panel in the left sidebar. Then open the following link:

`http://yourapplication.cleverapps.io/install.php`

Do not forget the **/install.php** page otherwise installation will not happen.
Follow the steps and you're done!
