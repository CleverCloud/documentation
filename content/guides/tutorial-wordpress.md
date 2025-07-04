---
type: docs
title: WordPress
shortdesc: This article shows you how to deploy a WordPress-based website on Clever Cloud.
tags:
- deploy
keywords:
- php
- wordpress
str_replace_dict:
  "@application-type@": "PHP"
aliases:
- /developers/doc/php/tutorial-wordpress
- /doc/deploy/application/php/tutorials/tutorial-wordpress
- /doc/php/tutorial-wordpress
---

## Overview

[WordPress](https://WordPress.org) applications almost work out of the box on Clever Cloud, you just have a few adjustments to make.

First, you could check [our global PHP documention](/developers/doc/deploy/application/php/php-apps/).

This tutorial is mainly concerning a Git deployment. However, you can deploy using a classic FTP PHP app. Choose "FTP" when you create a new PHP app.

{{< content "create-application" >}}

 {{< content "set-env-vars" >}}

 {{< content "deploy-git" >}}

{{< content "deploy-ftp" >}}

## Configure your WordPress application

### Configuration file

Rename the file `wp-config-sample.php` to `wp-config.php`. All the PHP code for the configuration should be written in this file.

### Configure your database

Make sure you have created a MySQL database add-on in the Clever Cloud console, and that it's linked to your application. When it's done, you will be able to access all of your add-on [environment variables](#setting-up-environment-variables-on-clever-cloud) from the application. You can use them, in `wp-config.php`, as :

```php
define( 'DB_NAME', getenv("MYSQL_ADDON_DB") );
define( 'DB_USER', getenv("MYSQL_ADDON_USER") );
define( 'DB_PASSWORD', getenv("MYSQL_ADDON_PASSWORD") );
define( 'DB_HOST', getenv("MYSQL_ADDON_HOST").':'.getenv("MYSQL_ADDON_PORT") );
```

{{< callout type="warning" >}}
**Make sure you use ** in `wp-config.php` the port the add-on dashboard provides. Use the `MYSQL_ADDON_PORT` environment variable for that. We **don't** use the default MySQL port.
{{< /callout >}}

### SSL Configuration

Since your website is behind a reverse proxy managed by Clever Cloud, you need to detect specific headers like **X_FORWARDED_PROTO** or **HTTP_X_FORWARDED_PROTO** to enable SSL.
To do so edit `wp-config.php` and add the following code above the last `require_once` call.

```php{linenos=table}
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] == 'https') {
    $_SERVER['HTTPS'] = 'on';
} elseif (isset($_SERVER['X_FORWARDED_PROTO']) && $_SERVER['X_FORWARDED_PROTO'] == 'https') {
    $_SERVER['HTTPS'] = 'on';
}
```

#### Using a CDN as Cloudflare with SSL (avoid infinite loops)

As with SSL configuration, you need to detect specific headers like **X_FORWARDED_PROTO** or **HTTP_X_FORWARDED_PROTO** to enable SSL. In this case, the chained proxies might concatenate those headers. As a result, headers values can look like
```php [HTTP_X_FORWARDED_PROTO] => https, https```
The previous code snippet would not enable SSL on the Clever Cloud application, resulting in mixed content or infinite loop.

In order to avoid this, you'll need to add the following code snippet to your `wp-config.php` file (it replaces the previous code snippet). Add the following code above the last `require_once` call or at the beginning of the `wp-config.php` file.

To do so edit `wp-config.php` and add the following code above the last `require_once` call.

```php
function check_proto_set_ssl($forwarded_protocols){
  $secure = 'off';
  if ( strstr($forwarded_protocols , ",") ) {
    $previous = null;
    foreach ( explode(",", $forwarded_protocols) as $value ) {
    if ( $previous ) {
      trim($value) == $previous && trim($value) == 'https' ? $secure = 'on' : $secure = 'off';
      }
      $previous = trim($value);
    }
    $_SERVER["HTTPS"] = $secure;
  }else{
    $forwarded_protocols == 'https' ? $_SERVER["HTTPS"] = 'on' : $_SERVER["HTTPS"] = $secure = 'off';
  }
}

if (isset($_SERVER['HTTP_X_FORWARDED_PROTO'])) {
  check_proto_set_ssl($_SERVER['HTTP_X_FORWARDED_PROTO']);
} elseif (isset($_SERVER['X_FORWARDED_PROTO'])) {
  check_proto_set_ssl($_SERVER['X_FORWARDED_PROTO']);
}
```

### Configure storage

To store static files, you need to configure a FS Bucket.

Create a FS Bucket add-on and link it to your application. Note its host (you can see it from the addon configuration panel, or in the environment variables exported by the addon). It looks like `bucket-01234567-0123-0123-0123-012345678987-fsbucket.services.clever-cloud.com`.

To use the bucket in your wordpress app, there are 2 methods :

#### Environment variables

Create a new [environment variable](#setting-up-environment-variables-on-clever-cloud) called `CC_FS_BUCKET` and set `/<path-to-static-files>:<bucket-host>` as its value.

If you need to have many associated buckets with your app, you need to create en new encironment variable, with a suffix : `CC_FS_BUCKET_1`, `CC_FS_BUCKET_2`…

#### JSON

{{< callout emoji="🧹" >}}
**This method is deprecated**
We strongly recommend that you use environment variables.

If you want to switch from this method to the environment variables, you need to remove the `buckets.json` file. Otherwise, the environment variables will be ignored.
{{< /callout >}}

At the root of your application, create a `clevercloud/buckets.json` file (create a `clevercloud` folder in which you create a `buckets.json` file).
Add the following lines in this file. Do not forget to replace `bucketId` by the bucketId displayed in the [information]({{< ref "doc/addons/fs-bucket" >}}) section of the FS Bucket add-on.

```javascript
    [
      {
        "bucket" : "bucketId",
        "folder" : "/<path-to-static-files>"
      }
    ]
```

### Install a WordPress plugin with Git

If you choose git deployment over FTP, the code of your plugins won't be tracked by git. This implies that you will not be able to install plugins from the administration panel and persist them between two deployments.

To solve this problem, we recommend to install the plugin manually by copying the content of the plugin to the `/wp-content/plugins/` folder, add the new files to git and then deploy your application.

The plugin will then be available in the **Extensions** section of your admin panel and you will be able to manage it as others WordPress plugins.
To uninstall the plugin, the procedure is the same as before except that you have to delete the folder corresponding to the plugin you want to delete. The extension will be automatically disabled, but we recommend you to delete it from you admin panel before removing the file, in order to clean your database and all files that the plugin could have created.

## Optimise and speed-up your WordPress

There are multiple ways to optimise your WordPress and speed-up its response time.
We provide different tools and software to help you in this task as [Varnish]({{< ref "doc/administrate/cache.md" >}}) for the HTTP cache, and [Redis]({{< ref "doc/addons/redis" >}}) for the object caching.

### Performance plugins

{{< callout type="warning" >}}
We recommend you to **not** use performance plugins like W3 Total Cache or JetPack as they are intended to be used on a shared hosting server.
We noticed performances problems when performance plugins are enabled and we recommend to use Varnish and Redis if you need performance optimisations on Clever Cloud.
{{< /callout >}}

### HTTP Cache with Varnish

Enabling [Varnish]({{< ref "doc/administrate/cache.md" >}}) for your application is very simple. All instances of PHP provide [Varnish]({{< ref "doc/administrate/cache.md" >}}), you just have to configure your application to use it.

1. To use Varnish in your application, you have to create a `varnish.vcl` file in the `clevercloud` folder of your application. If this folder doesn't exist, create it in the **root** of your project.

2. Copy [this code](https://raw.githubusercontent.com/CleverCloud/varnish-examples/master/wordpress.vcl) into the `varnish.vcl` file you just created. It'll configure Varnish to work with your WordPress.

3. To properly purge the Varnish cache of your application when a post is created/updated, a comment is posted, … we recommend you to install the [Varnish HTTP Purge](https://WordPress.org/plugins/varnish-http-purge/) plugin to your WordPress. It'll purge the Varnish cache for you and give you the possibility to purge it manually.

If you need to manually purge the Varnish cache, the plugin provides a **Purge Varnish cache** button on the top bar of your website.

### Object cache with Redis

[Redis]({{< ref "doc/addons/redis" >}}) is an [add-on](#linking-a-database-or-any-other-add-on-to-your-application) that offers you a good way to speed-up your application by caching some of the objects of your application, as the result of SQL queries of your application, improving the response time.

To enable [Redis]({{< ref "doc/addons/redis" >}}) for your WordPress, you need to disable other Object Cache and Data Cache of your application (as those provided by *W3 Total Cache* for example). Make sure they aren't enabled to avoid conflicts and performance problems.

1. [Create a Redis add-on]({{< ref "doc/addons/redis" >}}) for your application.

2. Add the following lines to your `wp-config.php` file. Make sure they are **before** the `require_once(ABSPATH . 'wp-settings.php');` line, otherwise the Redis connexion will not work for your application and your application will return only white pages!

```php
define('WP_CACHE_KEY_SALT', 'tvm_');
define('WP_REDIS_CLIENT', 'pecl');
define('WP_REDIS_HOST', getenv('REDIS_HOST'));
define('WP_REDIS_PORT', getenv('REDIS_PORT'));
define('WP_REDIS_PASSWORD', getenv('REDIS_PASSWORD'));
```

3. Download [this file](https://plugins.svn.WordPress.org/redis-cache/trunk/includes/object-cache.php) who manages the connexion with Redis and WordPress and moves it to your `/wp-content` folder. The file **must** be named `object-cache.php`.

Redis should now work with your WordPress.

 {{< content "new-relic" >}}

## Deploy WordPress the immutable way

Discover a new way to deploy WordPress using Composer with Bedrock's boilerplate : [our tutorial on GitHub](https://github.com/CleverCloud/clever-wordpress)

<!--  {{< content "env-injection" >}} -->

<!-- {{< content "link-addon" >}}-->

{{< content "more-config" >}}
