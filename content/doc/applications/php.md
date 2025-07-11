---
type: docs
title: PHP with Apache
shortdesc: Deploy PHP applications with Apache HTTP server on Clever Cloud
tags:
- php
- deploy
str_replace_dict:
  "@application-type@": "PHP"
type: docs
aliases:
- /doc/deploy/application/php
- /doc/deploy/application/php/php-apps
- /doc/getting-started/by-language/php
- /doc/partials/language-specific-deploy/php
---

## Overview

PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded
into HTML.

The HTTP server is [Apache 2](https://httpd.apache.org/), and the PHP code is executed by [PHP-FPM](https://php-fpm.org/).

{{< content "create-application" >}}

{{< content "set-env-vars" >}}

## Configure your PHP application

### Choose your PHP version

Set the `CC_PHP_VERSION` environment variable to one of the following versions.

{{< runtimes_versions PHP >}}

All new PHP applications are created with a default `CC_PHP_VERSION`. You can of course change it whenever you want then redeploy your application to use the version you want. We only support values based on the first two digits (`X` or `X.Y`, not `X.Y.Z`).

### Change the webroot

Since one of the best practices of PHP development is to take the libraries and core files outside the webroot, you may
want to set another webroot than the default one (*the root of your application*).

#### Using an environment variable

Add a new environment variable called `CC_WEBROOT` and set `/public` as its value.

```shell
clever env set CC_WEBROOT /public
```

### Change PHP settings

#### PHP settings

Most PHP settings can be changed using a `.user.ini` file.

If you want the settings to be applied to the whole application, you should put this file in your `webroot`. If you did not change it (see above), then your `webroot` is the root of the repository.

If you put the `.user.ini` file in a subdirectory; settings will be applied recursively starting from this subdirectory.

#### Same configuration between PHP-CLI and PHP-FPM.

`.user.ini` files aren't loaded by the PHP CLI by default.

However, some PHP applications may want to check for the PHP-FPM configuration pre-requisites, `post_max_size` or `upload_max_filesize` values for example.

To load the PHP-FPM `.user.ini` file during a PHP-CLI process, in a [hook](https://www.clever-cloud.com/developers/doc/develop/build-hooks/), use the `PHP_INI_SCAN_DIR` environment variable to load the additional file.

Assuming the script runs at the root-folder of the application:

```bash
#!/usr/bin/env bash

export PHP_INI_SCAN_DIR=":."
php myscript.php
```

This appends the current directory while still loading the default configuration.

**Note**: The `:` at the beginning of the string is mandatory. It indicates defaults files must still load.

A specific `.ini` file can be loaded with:

```
#!/usr/bin/env bash

export PHP_INI_SCAN_DIR=":.php-configuration/"
php myscript.php
```

This loads every `.ini` files in the `php-configuration/` directory.

##### Timezone configuration

All instances on Clever Cloud run on the UTC timezone. We recommend to handle all your dates in UTC internally, and only handle timezones when reading or displaying dates.

Additionally, you can set PHP's time zone setting with `.user.ini`. For instance, to use the french time zone, edit `.user.ini` to add this line:

```ini
date.timezone=Europe/Paris
```

##### Header injection

###### With .htaccess

To inject headers on HTTP responses, add this configuration to `.htaccess` file:

```sh
Header Set Access-Control-Allow-Origin "https://www.example.com"
Header Set Access-Control-Allow-Headers "Authorization"
```

{{< callout type="info" >}}
You can use a `.htaccess` file to create or update headers, but you can't delete them.
{{< /callout >}}

###### With PHP

You can also do it from PHP:

```php
header("Access-Control-Allow-Origin: https://www.example.com");
header("Access-Control-Allow-Headers: Authorization");
```

If you want to keep this separate from your application, you can configure the application to execute some code on every request.

In `.user.ini`, add the following line (you need to create `inject_headers.php` first):

```ini
auto_prepend_file=./inject_headers.php
```

Please refer to the [official documentation](https://www.php.net/manual/en/configuration.file.per-user.php) for more information.

You can review the [available directives](https://www.php.net/manual/en/ini.list.php); all the `PHP_INI_USER`, `PHP_INI_PERDIR`, and `PHP_INI_ALL` directives can be set from within `.user.ini`.

##### Memory Limit

When php-fpm spawns a worker it allocates a smaller part of the application's memory to the worker, here is the allocated memory for each flavor:

 | Flavor   | Memory Limit |
 |----------|--------------|
 |Pico      | 64M          |
 |Nano      | 64M          |
 |XS        | 128M         |
 |S         | 256M         |
 |M         | 384M         |
 |L         | 512M         |
 |XL        | 768M         |
 |2XL       | 1024M        |
 |3XL       | 1536M        |
 |4XL+      | 2048M        |

To change this limit you can define `MEMORY_LIMIT` [environment variable]({{< ref "doc/reference/reference-environment-variables.md#php" >}}).

If you define a limit exceeding the application memory it will use the default one.

## Configure Apache

We use Apache 2 as HTTP Server. In order to configure it, you can create a `.htaccess` file and set directives inside this file.

### htaccess

The `.htaccess` file can be created everywhere in you app, depending of the part of the application covered by directives.

However, directives who applies to the entire application must be declared in a `.htaccess` file to the application root.

### htpasswd

You can configure basic authentication using [environment variables]({{< ref "doc/reference/reference-environment-variables.md#php" >}}). You will need to set `CC_HTTP_BASIC_AUTH` variable to your own `login:password` pair. If you need to allow access to multiple users, you can create additional environment `CC_HTTP_BASIC_AUTH_n` (where `n` is a number) variables.

### Define a custom HTTP timeout

You can define the timeout of an HTTP request in Apache using the `HTTP_TIMEOUT` [environment variable]({{< ref "doc/develop/env-variables.md" >}}).

**By default, the HTTP timeout is set to 3 minutes (180 seconds)**.

### Header size

Default Apache header size is `8k`. If you need to increase it, you can set `CC_APACHE_HEADERS_SIZE` environment variable, between `8` and `256`. Effective value depends on deployment region. [Ask for a dedicated load balancer](https://console.clever-cloud.com/ticket-center-choice) for a specific value.

### Force HTTPS traffic

Load balancers handle HTTPS traffic ahead of your application. You can use the `X-Forwarded-Proto` header to know the original protocol (`http` or `https`).

Place the following snippet in a `.htaccess` file to ensure that your visitors only access your application through HTTPS.

```conf
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

### Prevent Apache to redirect HTTPS calls to HTTP when adding a trailing slash

`DirectorySlash` is enabled by default on the PHP scalers, therefore Apache will add a trailing slash to a resource when it detects that it is a directory.

E.g. if foobar is a directory, Apache will automatically redirect `http://example.com/foobar` to `http://example.com/foobar/`.

Unfortunately the module is unable to detect if the request comes from a secure connection or not. As a result it will force an HTTPS call to be redirected to HTTP.

In order to prevent this behavior, you can add the following statements in a `.htaccess` file:

```conf
DirectorySlash Off
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^(.+[^/])$ %{HTTP:X-Forwarded-Proto}://%{HTTP_HOST}/$1/ [R=301,L,QSA]
```

These statements will keep the former protocol of the request when issuing the redirect. Assuming that the header `X-Forwarded-Proto` is always filled (which is the case on our platform).

If you want to force all redirects to HTTPS, you can replace `%{HTTP:X-Forwarded-Proto}` with `https`.

### Change the FastCGI module

You can choose between two FastCGI modules, `fastcgi` and `proxy_fcgi`, using the `CC_CGI_IMPLEMENTATION` environment variable. If you don't set it `proxy_fcgi` is used as default value. We recommend it, as `fastcgi` implementation is not maintained anymore.

If you have issues with downloading content, it could be related to the `fastcgi` module not working correctly in combination with the `deflate` module, as the `Content-Length` header is not updated to the new size of the encoded content. To resolve this issue, use `proxy_fcgi`.

### Environment injection

As mentioned above, Clever Cloud can inject environment variables that are defined in the
dashboard and by add-ons linked to your application.

To access the variables, use the `getenv` function. So, for example, if
your application has a postgresql add-on linked:

```php
$host = getenv("POSTGRESQL_ADDON_HOST");
$database = getenv("POSTGRESQL_ADDON_DB");
$username = getenv("POSTGRESQL_ADDON_USER");
$password = getenv("POSTGRESQL_ADDON_PASSWORD");

$pg = new PDO("postgresql:host={$host};dbname={$database}, $username, $password);
```

{{< callout type="warning" >}}
Environment variables are displayed in the default output of `phpinfo()`. If you want to use `phpinfo()` without exposing environment variables, you have to call it this way: `phpinfo(INFO_GENERAL | INFO_CREDITS | INFO_CONFIGURATION | INFO_MODULES | INFO_LICENSE)`
{{< /callout >}}

## Composer

We support Composer build out of the box. You just need to provide a `composer.json` file in the root of your repository and we will run `composer.phar install --no-ansi --no-progress --no-interaction --no-dev` for you.

You can also set the `CC_COMPOSER_VERSION` to `1` or `2` to select the composer version to use.

{{< callout type="info" >}}
If you encounter any issues, add your own `composer.phar` file in the root of your repository which will override the version we use.
{{< /callout >}}

You can perform your own `composer.phar install` by using the [Post Build hook]({{< ref "doc/develop/build-hooks.md#post-build-cc_post_build_hook" >}}).

Example of a `composer.json` file:

```json{linenos=table}
{
    "require": {
        "laravel/framework": "4.1.*",
        "ruflin/Elastica": "dev-master",
        "shift31/laravel-elasticsearch": "dev-master",
        "natxet/CssMin": "dev-master"
    },
    "repositories": [
        {
            "type": "vcs",
            "url": "https://GitHub.com/timothylhuillier/laravel-elasticsearch.git"
        }
    ],
    "autoload": {
        "classmap": [
            "app/controllers",
            "app/models",
            "app/database/migrations",
            "app/database/seeds"
        ],
        "psr-0": {
            "SomeApp": "app"
        }
    },
    "config": {
        "preferred-install": "dist"
    },
    "minimum-stability": "dev"
}
```

Example of a minimalist PHP application using composer and custom scripts: [php-composer-demo](https://GitHub.com/CleverCloud/php-composer-demo)

## Development Dependencies

Development dependencies will not be automatically installed during the deployment. You can control their installation by using the `CC_PHP_DEV_DEPENDENCIES` environment variable which takes `install` value.

Any other value than `install` will prevent development dependencies from being installed.

### GitHub rate limit

Sometimes, you can encounter the following error when downloading dependencies:

```txt
Failed to download symfony/symfony from dist: Could not authenticate against GitHub.com
```

To prevent this download dependencies's fails that is often caused by rate limit of GitHub API while deploying your apps,
we recommend you to add `oauth` token in your composer configuration file or in separate file named as described in
[composer FAQ (API rate limit and OAuth tokens)](https://getcomposer.org/doc/articles/troubleshooting.md#api-rate-limit-and-oauth-tokens).

You can find more documentation about composer configuration at [getcomposer.com](https://getcomposer.org/doc/04-schema.md).

#### Example

You use Artisan to manage your project and you want to execute *artisan migrate* before running your app.

To do this, we use a post build hook, you have to set a new environment variable on your Clever application as following:

```bash
CC_POST_BUILD_HOOK=php artisan migrate --force
```

**Note:** You must add the *execute* permission to your file (`chmod u+x yourfile`) before pushing it.

## Frameworks and CMS

The following is the list of tested CMS by our team.

It's quite not exhaustive, so it does not mean that other CMS can't work on the Clever Cloud platform.

{{< cards >}}
  {{< card link="../../..../../../guides/tutorial-drupal" title="Drupal" subtitle= "Deploy a Drupal-based website on Clever Cloud" icon="drupal" >}}
  {{< card link="../../..../../../guides/tutorial-laravel" title="Laravel" subtitle= "Deploy a Laravel app on Clever Cloud" icon="laravel" >}}
  {{< card link="../../..../../../guides/tutorial-symfony" title="Symfony" subtitle= "Deploy a Symfony application on Clever Cloud" icon="symfony" >}}
  {{< card link="../../..../../../guides/tutorial-wordpress" title="WordPress" subtitle= "Deploy WordPress on Clever Cloud" icon="wordpress" >}}
  {{< card link="../../..../../../guides/moodle" title="Moodle" subtitle="Full Moodle installation and configuration guide" icon="moodle" >}}

{{< /cards >}}

Others PHP frameworks tested on Clever Cloud:

- Prestashop
- Dokuwiki
- Joomla
- SugarCRM
- Drupal
- Magento
- Status.net
- Symfony
- Thelia
- Laravel
- Sylius

## Available extensions and modules

Clever Cloud PHP with Apache applications enable the following extensions by default:

`amqp`, `bcmath`, `bz2`, `calendar`, `ctype`, `curl`, `dba`, `exif`, `fileinfo`, `filter`, `ftp`, `gd`, `gettext`, `gmp`, `iconv`, `imagick`, `imap`, `intl`, `json`, `ldap`, `libsodium`, `mbstring`, `mcrypt`, `memcached`, `memcache`, `mongodb`, `mysql`, `mysqli`, `opcache`, `pcntl`, `pcre`, `pdo-mysql`, `pdo-odbc`, `pdo-pgsql`, `pdo-sqlite`, `pgsql`, `phar`, `posix`, `pspell`, `readline`, `redis`, `session`, `shmop`, `sockets`, `sodium`, `solr`, `ssh2`, `ssl`, `tidy`, `tokenizer`, `unixodbc`, `xml`, `xmlrpc`, `xsl`, `zip`, `zlib`.

You can also enable the following extensions on demand:

`apcu`, `blackfire`, `elastic_apm_agent`, `event`, `excimer`, `geos`, `gnupg`, `grpc`, `ioncube`, `imap`, `mailparse`, `maxminddb`, `mongo`, `newrelic`, `oauth`, `opentelemetry`, `pcs`, `PDFlib`, `pdo_sqlsrv`, `protobuf`, `pspell`, `rdkafka`, `scoutapm`, `sqlsrv`, `sqreen`, `tideways`, `uopz`, `uploadprogress`, `xdebug`, `xmlrpc`, `yaml`

>[!NOTE]
>Only some extensions support PHP 8.4 for now: `amqp`, `apcu`, `blackfire`, `event`, `gnupg`, `grpc`, `imagick`, `imap`, `mailparse`, `maxminddb`, `memcache`, `memcached`, `mongodb`, `newrelic`, `oauth`, `opentelemetry`, `pdo_sqlsrv`, `protobuf`, `pspell`, `rdkafka`, `redis`, `solr`, `sqlsrv`, `ssh2`, `tideways`, `uploadprogress`, `yaml`, `zip`. We'll add support for more extensions as they are released.

You can check extensions and versions by viewing our `phpinfo()` for:

- [PHP 5.6](https://php56info.cleverapps.io)
- [PHP 7.1](https://php71info.cleverapps.io)
- [PHP 7.2](https://php72info.cleverapps.io)
- [PHP 7.3](https://php73info.cleverapps.io)
- [PHP 7.4](https://php74info.cleverapps.io)
- [PHP 8.0](https://php80info.cleverapps.io)
- [PHP 8.1](https://php81info.cleverapps.io)
- [PHP 8.2](https://php82info.cleverapps.io)
- [PHP 8.3](https://php83info.cleverapps.io)
- [PHP 8.4](https://php84info.cleverapps.io)

If you have a request about extensions, contact [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice).

### Enable specific extensions

Some extensions need to be enabled explicitly. To do so, set the corresponding [environment variable](#setting-up-environment-variables-on-clever-cloud):

- APCu: set `ENABLE_APCU` to `true`.

    APCu is an in-memory key-value store for PHP. Keys are of type string and values can be any PHP variables.

- Elastic APM Agent: set `ENABLE_ELASTIC_APM_AGENT` to `true` (default if `ELASTIC_APM_SERVER_URL` is defined).

    Elastic APM agent is Elastic's APM agent extension for PHP. The PHP agent enables you to trace the execution of operations
    in your application, sending performance metrics and errors to the Elastic APM server.
    **Warning**: This extension is available starting PHP 7.2.

- Event: set `ENABLE_EVENT` to `true`.

    Event is an extension to schedule I/O, time and signal based events.

- Excimer: set `ENABLE_EXCIMER` to `true`.

    Excimer is an extension that provides a low-overhead interrupting timer and sampling profiler.

- GEOS: set `ENABLE_GEOS` to `true`.

    GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology Suite (JTS).

- GnuPG: set `ENABLE_GNUPG` to `true`.

    GnuPG is an extension that provides methods to interact with GNU Privacy Guard (OpenPGP implementation).

- gRPC: set `ENABLE_GRPC` to `true`.

    gRPC is an extension for the high performance, open source, general RPC framework layered over HTTP/2.

- IonCube: set `ENABLE_IONCUBE` to `true`.

    IonCube is a tool to obfuscate PHP code. It's often used by paying Prestashop and WordPress plugins.

- IMAP (only for PHP 8.4+): set `ENABLE_IMAP` to `true`.

    IMAP is an extension to operate with the IMAP protocol, as well as the NNTP, POP3, and local mailbox access methods.

- Mailparse: set `ENABLE_MAILPARSE` to `true`.

    Mailparse is an extension for parsing and working with email messages. It can deal with RFC 822 and RFC 2045 (MIME) compliant messages.

- MaxMind DB: set `ENABLE_MAXMINDDB` to `true`.

    Extension for reading MaxMind DB files. MaxMind DB is a binary file format that stores data indexed by IP address subnets (IPv4 or IPv6).

- Mongo: set `ENABLE_MONGO` to `true`.

    MongoDB is a NoSQL Database. This extension allows to use it from PHP.
    **Warning**: this extension is now superseded by the `mongodb` extension. We provide it for backward compatibility.

- NewRelic: set `ENABLE_NEWRELIC` to `true`.

    Newrelic Agent for PHP. Newrelic is a software analytics tool.

- OAuth: set `ENABLE_OAUTH` to `true`.

    OAuth consumer extension. OAuth is an authorization protocol built on top of HTTP.

- OpenTelemetry: set `ENABLE_OPENTELEMETRY` to `true`.

    OpenTelemetry is an extension to facilitate the generation, export, collection of telemetry data such as traces, metrics, and logs.

- PCS: set `ENABLE_PCS` to `true`.

    PCS provides a fast and easy way to mix C and PHP code in your PHP extension.

- PDFlib: set `ENABLE_PDFlib` to `true`.

    PDFlib is a commercial library for generating PDF files. It provides a PHP extension to create and manipulate PDF documents.

- Protobuf: set `ENABLE_PROTOBUF` to `true`.

    Protobuf is an extension for the language-neutral, platform-neutral extensible mechanism for serializing structured data.

- Pspell: set `ENABLE_PSPELL` to `true`.

    Pspell is an extension to check the spelling of words and offer suggestions.

- Rdkafka: set `ENABLE_RDKAFKA` to `true`.

    PHP-rdkafka is a thin librdkafka binding providing a working PHP 5 / PHP 7 Kafka client.

- Scout APM: set `ENABLE_SCOUTAPM` to `true`.

    The Scout APM extension to provide additional capabilities to application monitoring over just using the base PHP userland library.

- SQL Server: set `ENABLE_SQLSRV` or `ENABLE_PDO_SQLSRV` to `true`.

    These extensions enable drivers that rely on the Microsoft ODBC Driver to handle the low-level communication with SQL Server. The `SQLSRV` extension provides a procedural interface while the `PDO_SQLSRV` extension implements PDO for accessing data in all editions of SQL Server 2012 and later (including Azure SQL DB).

- Sqreen: The Sqreen agent is started automatically after adding the environment variables (`SQREEN_API_APP_NAME` and `SQREEN_API_TOKEN`).

- Tideways: set `ENABLE_TIDEWAYS` to `true`.

    Tideways is an extension that provides profiling and monitoring capabilities for PHP applications.

- Uopz: set `ENABLE_UOPZ` to `true`.

    The uopz extension is focused on providing utilities to aid with unit testing PHP code.

- Uploadprogress: set `ENABLE_UPLOADPROGRESS` to `true`.

    The uploadprogress extension is used to track the progress of a file download.

- XDebug: set `ENABLE_XDEBUG` to `true`.

    XDebug is a debugger and profiler tool for PHP.

- XML RPC: set `ENABLE_XMLRPC` to `true`.

    XML-RPC is an extension for server and client bindings

- YAML: set `ENABLE_YAML` to `true`.

    YAML is an extension providing a YAML-1.1 parser and emitter

You can use `DISABLE_<extension_name>=true` in your [environment variables](/developers/doc/reference/reference-environment-variables/) to disable an extension.

## Configure the session storage

By default, a FS Bucket is created for each PHP applications. It is used to store session files, so that session data is available on each instance.

This FS Bucket is also used to store TMP files by default.
You can change this behaviour by setting the `TMPDIR` environment variable.
You can set it to `/tmp` for example.

### Speed up or disable the session FS Bucket

You can set the following environment variables:

- `CC_PHP_ASYNC_APP_BUCKET=async` to mount the session FS Bucket with the `async` option.
  It speeds up the FS Bucket usage, but it can corrupt files in case of a network outage.
- `CC_PHP_DISABLE_APP_BUCKET=(true|yes|disable)` to entirely prevent the session FS Bucket
  from being mounted.
  Use this if you don't use the default PHP session library.
  It will speed up your application but users might lose their session across instances
  and deployments.

### Use Redis to store PHP Sessions

We provide the possibility to store the PHP sessions in a [Redis database]({{< ref "doc/addons/redis" >}}) to improve reliability.

If your application is under heavy load, redis persistence for sessions can improve latency.

To enable this feature, you need to:

- enable Redis support on the application (create an [environment variable]({{< ref "doc/develop/env-variables.md" >}}) named `ENABLE_REDIS` with the value `true`.)
- create and link a Redis add-on
- create an [environment variable](#setting-up-environment-variables-on-clever-cloud) named `SESSION_TYPE` with the value `redis`.

{{< callout type="warning" >}}
You must have a [Redis]({{< ref "doc/addons/redis" >}}) add-on [linked with your application](#linking-a-database-or-any-other-add-on-to-your-application) to enable PHP session storage in Redis. If no Redis add-on is linked with your application, the deployment will fail.
{{< /callout >}}

## Sending emails

The PHP language has the `mail` function to directly send emails. While we do not provide a SMTP server (needed to send the emails), you can configure one through environment variables.

We provide Mailpace add-on to send emails through PHP `mail()` function. You have to turn TLS on with port 465 (environment variable `CC_MTA_SERVER_USE_TLS=true`) to make Mailpace working.

We also recommend you to use [Mailgun](https://www.mailgun.com/) or [Mailjet](https://www.mailjet.com/) if your project supports it. These services already have everything you need to send emails from your code.

### Configure the SMTP server

Services like [Mailgun](https://www.mailgun.com/) or [Mailjet](https://www.mailjet.com/) provide SMTP servers. If your application has no other way but to use the `mail` function of PHP to send emails, you have to configure a SMTP server. This can be done through environment variables:

- `CC_MTA_SERVER_HOST`: Host of the SMTP server.
- `CC_MTA_SERVER_PORT`: Port of the SMTP server. Defaults to `465` whether TLS is enabled or not.
- `CC_MTA_AUTH_USER`: User to authenticate to the SMTP server.
- `CC_MTA_AUTH_PASSWORD`: Password to authenticate to the SMTP server.
- `CC_MTA_SERVER_USE_TLS`: Enable or disable TLS. Defaults to `true`.
- `CC_MTA_SERVER_STARTTLS`: Enable or disable STARTTLS. Defaults to `false`.
- `CC_MTA_SERVER_AUTH_METHOD`: Enable or disable authentication. Defaults to `on`.

## Configure Monolog

A lot of frameworks (including Symfony) use Monolog to handle logging. The default configuration of Monolog doesn't allow to log errors into the console.

Here is a basic configuration of Monolog to send your application's logs into our logging system and access them into the Console:

```yaml
monolog:
  handlers:
    clever_logs:
      type: error_log
      level: warning
```

You can change the level to whatever level you desire. For Symfony, the configuration file is `app/config/config_prod.yml`.

Laravel doesn't need Monolog to retrieve logs via Clever console or Clever CLI. Here, ensure that you have the following line in `config/app.php`:

```php
return [
    // …
    'log' => env('APP_LOG'),
    // …
];
```

Then, set `APP_LOG=syslog` as Clever application environment variable.

## Using HTTP authentication

Using basic HTTP authentication, PHP usually handles the values of user and password in variables named `$_SERVER['PHP_AUTH_USER']` and `$_SERVER['PHP_AUTH_PW']`.

At Clever Cloud, we have enabled an Apache option to pass directly the Authorization header, even though we are using FastCGI; still, the header is not used by PHP, and the aforementioned variables are empty.

You can do this to fill them using the Authorization header:

```php
list($_SERVER['PHP_AUTH_USER'], $_SERVER['PHP_AUTH_PW']) = explode(':' , base64_decode(substr($_SERVER['Authorization'], 6)));
```

{{< content "new-relic" >}}

{{< content "blackfire" >}}

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via **Git or FTP**.

{{< content "deploy-git" >}}

{{< content "deploy-ftp" >}}

## ProxySQL

{{< content "proxysql" >}}

You can learn more about ProxySQL on the [dedicated documentation page]({{< ref "/guides/proxysql" >}} "ProxySQL")

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}
