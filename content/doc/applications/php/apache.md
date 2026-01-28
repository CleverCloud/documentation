---
type: docs
linkTitle: Apache
title: Apache web server configuration
description: Configure Apache 2 for PHP applications on Clever Cloud with htaccess, authentication, HTTPS redirection, and FastCGI settings
keywords:
- apache
- htaccess
- htpasswd
- fastcgi
- https redirect
---

## Configure Apache

Apache 2 is used as HTTP Server for PHP applications on Clever Cloud. You can configure it with `.htaccess` files and environment variables.

### htaccess

The `.htaccess` file can be created anywhere in your app, depending on the part of the application that the directives cover.

However, directives that apply to the entire application must be declared in a `.htaccess` file at the application root.

### Basic authentication

You can configure basic authentication using [environment variables](/doc/reference/reference-environment-variables#php). You will need to set `CC_HTTP_BASIC_AUTH` variable to your own `login:password` pair. If you need to allow access to multiple users, you can create additional environment `CC_HTTP_BASIC_AUTH_n` (where `n` is a number) variables.

### HTTP timeout

You can define the timeout of an HTTP request in Apache using the `HTTP_TIMEOUT` [environment variable](/doc/develop/env-variables).

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

You can choose between two FastCGI modules, `fastcgi` and `proxy_fcgi`, using the `CC_CGI_IMPLEMENTATION` environment variable. If you don't set it `proxy_fcgi` is used as default value. `proxy_fcgi` is recommended, as `fastcgi` implementation is not maintained anymore.

If you have issues with downloading content, it could be related to the `fastcgi` module not working correctly in combination with the `deflate` module, as the `Content-Length` header is not updated to the new size of the encoded content. To resolve this issue, use `proxy_fcgi`.

## Environment injection

Clever Cloud injects environment variables defined in the Console and by linked add-ons. To access them from PHP, use the `getenv` function. For example, if your application has a PostgreSQL add-on linked:

```php
$host = getenv("POSTGRESQL_ADDON_HOST");
$database = getenv("POSTGRESQL_ADDON_DB");
$username = getenv("POSTGRESQL_ADDON_USER");
$password = getenv("POSTGRESQL_ADDON_PASSWORD");

$pg = new PDO("pgsql:host={$host};dbname={$database}", $username, $password);
```

> [!WARNING]
> Environment variables are displayed in the default output of `phpinfo()`. To use `phpinfo()` without exposing environment variables, call it this way: `phpinfo(INFO_GENERAL | INFO_CREDITS | INFO_CONFIGURATION | INFO_MODULES | INFO_LICENSE)`

## Header injection

### With .htaccess

To inject headers on HTTP responses, add this configuration to `.htaccess` file:

```sh
Header Set Access-Control-Allow-Origin "https://www.example.com"
Header Set Access-Control-Allow-Headers "Authorization"
```

> [!NOTE]
> You can use a `.htaccess` file to create or update headers, but you can't delete them.

### With PHP

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

- [Learn more about .user.ini directives](https://www.php.net/manual/en/configuration.file.per-user.php)

## Using HTTP authentication

Using basic HTTP authentication, PHP usually handles the values of user and password in variables named `$_SERVER['PHP_AUTH_USER']` and `$_SERVER['PHP_AUTH_PW']`.

At Clever Cloud, an Apache option is enabled to pass directly the Authorization header, even though FastCGI is used; still, the header is not used by PHP, and the aforementioned variables are empty.

You can do this to fill them using the Authorization header:

```php
list($_SERVER['PHP_AUTH_USER'], $_SERVER['PHP_AUTH_PW']) = explode(':' , base64_decode(substr($_SERVER['Authorization'], 6)));
```
