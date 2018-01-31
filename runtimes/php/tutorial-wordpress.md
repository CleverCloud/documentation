---
title: Deploying a Wordpress website
shortdesc: This article shows you how to deploy a Wordpress-based website on Clever Cloud.
tags:
- php
---

## Create an application

You can find in [this article](/doc/clever-cloud-overview/add-application/#create-an-application) the process to create an
application.


## Two choices for deployment

During the creation of a PHP application, it is asked if you want to deploy it via FTP or via Git. These two techniques
have their own pros and cons but have the same end result.

## Deploy via FTP

1. Download the Wordpress source files on [wordpress.org](http://wordpress.org).

2. [Add a MySQL database add-on](/doc/addons/clever-cloud-addons/).

3. Rename the file `wp-config-sample.php` to `wp-config.php`.

4. Replace in `wp-config.php` the host (for example: bj79c949bvl2deb6.mysql.clvrcld.net), database name, username and
password using the [environment variables](/doc/admin-console/environment-variables/) of the add-on.

3. [Send these Wordpress files via FTP](/doc/clever-cloud-overview/add-application/#ftp-deployment) using the FTP
credentials displayed in the application' information page.

6. When finished, you can launch the application with the url that you can find in the *domains* panel in the left sidebar.


## Deploy via Git

1. Download the Wordpress source files on [wordpress.org](http://wordpress.org).

2. [Add a MySQL database add-on](/doc/addons/clever-cloud-addons/).

3. Rename the file `wp-config-sample.php` to `wp-config.php`.

4. Replace in `wp-config.php` the host (for example: bj79c949bvl2deb6.mysql.clvrcld.net), database name, username and
password using the [environment variables](/doc/admin-console/environment-variables/) of the add-on.

5. As mentioned in this [article](/doc/addons/fs_buckets/), with Git deployments, files that are uploaded by users must
be persisted in a File System Bucket. In order to do so, [add a FS Bucket](/doc/addons/fs_buckets/) via the console.
You will find the bucketId in the [information](/doc/addons/clever-cloud-addons/) section of the FS Bucket add-on.

6. At the root of your application, create a `clevercloud/buckets.json` file (create a `clevercloud` folder in which
you create a `buckets.json` file).

7. Add the following lines in this file. Do not forget to replace `bucketId` by the bucketId displayed in the
[information](/doc/addons/clever-cloud-addons/) section of the FS Bucket add-on.
    ```javascript
    [
      {
        "bucket" : "bucketId",
        "folder" : "/wp-content/uploads"
      }
    ]
    ```

8. Send these Wordpress files via Git. Read this [article](/doc/clever-cloud-overview/add-application/#git-deployment)
if you need more information about it.

9. When finished, you can launch the application with the url that you can find in the *domains* panel in the left sidebar.


### Install a Wordpress plugin with Git

Wordpress plugins can be installed from the administration panel, to help the user. However, this way doesn't work with
git. Indeed, as explained above, deploying with git prevents to keep files uploaded by the user and the plugin installed
on the admin panel will be lost at the next deployment, because the code of the plugin isn't tracked by git.

To solve this problem, we recommend to install the plugin manually by copying the content of the plugin to the
`/wp-content/plugins/` folder, add the new files to git and then deploy your application.

The plugin will then be available in the **Extensions** section of your admin panel and you will be able to manage it
as others Wordpress plugins. To uninstall the plugin, the procedure is the same as before except that you have to delete
the folder corresponding to the plugin you want to delete. The extension will be automatically disabled, but we recommend
you to delete it from you admin panel before removing the file, in order to clean your database and all files that the
plugin could have created.


## Optimise and speed-up your Wordpress

There are multiple ways to optimise your Wordpress and speed-up its response time.
We provide different tools and software to help you in this task as [Varnish](/doc/php/varnish/) for the HTTP cache,
and [Redis](/doc/addons/redis/) for the object caching.


### Performance plugins

<div class="alert alert-hot-problems">
<h4>Warning:</h4>
 <p>We recommend you to <strong>not</strong> use performance plugins like W3 Total Cache or JetPack as they are
 intended to be used on a shared hosting server.<br />
 We noticed performances problems when performance plugins are enabled and we recommend to use Varnish and Redis
 if you need performance optimisations on Clever Cloud.</p>
</div>


### HTTP Cache with Varnish

Enabling [Varnish](/doc/tools/varnish/) for your application is very simple. All instances of PHP provide
[Varnish](/doc/tools/varnish/), you just have to configure your application to use it.

1. To use Varnish in your application, you have to create a `varnish.vcl` file in the `clevercloud` folder of
your application. If this folder doesn't exist, create it in the **root** of your project.

2. Copy [this code](https://raw.githubusercontent.com/CleverCloud/varnish-examples/master/wordpress.vcl) into the
`varnish.vcl` file you just created. It'll configure Varnish to work with your Wordpress.

3. To properly purge the Varnish cache of your application when a post is created/updated, a comment is posted, ...
we recommend you to install the [Varnish HTTP Purge](https://wordpress.org/plugins/varnish-http-purge/) plugin to
your Wordpress. It'll purge the Varnish cache for you and give you the possibility to purge it manually.

If you need to manually purge the Varnish cache, the plugin provides a **Purge Varnish cache** button on the top bar
of your website.


### Object cache with Redis

[Redis](/doc/addons/redis/) offers you a good way to speed-up your application by caching some of the objects of your
application, as the result of SQL queries of your application, improving the response time.

To enable [Redis](/doc/addons/redis/) for your Wordpress, you need to disable other Object Cache and Data Cache of your
application (as those provided by *W3 Total Cache* for example). Make sure they aren't enabled to avoid conflicts and
performance problems.

1. [Create a Redis add-on](/doc/addons/clever-cloud-addons/) for your application.

2. Add the following lines to your `wp-config.php` file. Make sure they are **before** the
`require_once(ABSPATH . 'wp-settings.php');` line, otherwise the Redis connexion will not work for your application and
your application will return only white pages!
```php
define('WP_CACHE_KEY_SALT', 'tvm_');
define('WP_REDIS_CLIENT', 'pecl');
define('WP_REDIS_HOST', getenv('REDIS_HOST'));
define('WP_REDIS_PORT', getenv('REDIS_PORT'));
define('WP_REDIS_PASSWORD', getenv('REDIS_PASSWORD'));
```

3. Download [this file](http://plugins.svn.wordpress.org/redis-cache/trunk/includes/object-cache.php)
who manages the connexion with Redis and Wordpress and moves it to your `/wp-content` folder. The file **must** be named
`object-cache.php`.

4. Redis should now work with your Wordpress.

### SSL Configuration

Since your website is behind a reverse proxy managed by Clever Cloud, you need to detect specific headers like **X_FORWARDED_PROTO** or **HTTP_X_FORWARDED_PROTO** to enable SSL. To do so edit `wp-config.php` and add the following code above the last `require_once` call.
```php
if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] == 'https') {
    $_SERVER['HTTPS'] = 'on';
} elseif (isset($_SERVER['X_FORWARDED_PROTO']) && $_SERVER['X_FORWARDED_PROTO'] == 'https') {
    $_SERVER['HTTPS'] = 'on';  
}
```
