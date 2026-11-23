---
type: docs
linkTitle: Apache
title: Apache web server configuration
description: Configure Apache for PHP applications on Clever Cloud with .htaccess files, HTTP authentication, headers, redirections, timeouts, and the FastCGI module
keywords:
- apache
- basic authentication
- fastcgi
- htaccess
- https redirect
aliases:
- /doc/applications/php/apache
- /doc/deploy/php/apache
- /doc/languages/php/apache
- /doc/php/apache
- /doc/runtimes/php/apache
---

## Overview

[Apache](https://httpd.apache.org) 2.4 serves the webroot of your [PHP application](/doc/deploy/applications/php/), and passes the PHP files to PHP-FPM. Configure it with `.htaccess` files and environment variables, for headers, redirections, authentication, or timeouts, as the sections below explain.

## Configure Apache with .htaccess

Apache reads the `.htaccess` files of the webroot and of its folders: put the directives of the whole application at the root of the webroot. They can rewrite URLs, set headers, or control access, as the [Apache documentation](https://httpd.apache.org/docs/2.4/howto/htaccess.html) explains:

```apache {filename="public/.htaccess"}
Header set Access-Control-Allow-Origin "https://www.example.com"

RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^ index.php [L]
```

To remove a header that PHP sends, use `Header always unset` in `.htaccess`. To set headers from PHP instead, call `header()`, or prepend a script to every request with `auto_prepend_file` in a `.user.ini` file, which then runs before your code.

### Redirections of folders

Apache adds a trailing slash to the URL of a folder. As the load balancers reach it over HTTP, it redirects an HTTPS request to HTTP: `https://example.com/docs` gets a redirection to `http://example.com/docs/`. Add the trailing slash yourself instead, over HTTPS:

```apache {filename="public/.htaccess"}
DirectorySlash Off
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^(.+[^/])$ https://%{HTTP_HOST}/$1/ [R=301,L,QSA]
```

[Force HTTPS](/doc/manage/#force-https), enabled by default, already redirects HTTP requests to HTTPS: you don't need a rule for it. To read the protocol of the client, see the headers that the [load balancers](/doc/network/load-balancers/#get-the-protocol) add to each request they forward.

## Basic authentication

To ask for a login and a password before any request, set them in `CC_HTTP_BASIC_AUTH`, as `login:password`. Add other users with `CC_HTTP_BASIC_AUTH_1`, `CC_HTTP_BASIC_AUTH_2`, and so on, in the same format:

```bash
clever env set CC_HTTP_BASIC_AUTH "alice:a-long-password"
```

Requests without these credentials get a `401` answer. With them, or with an HTTP authentication of your own, PHP receives the credentials in `$_SERVER['PHP_AUTH_USER']` and `$_SERVER['PHP_AUTH_PW']`, and the header in `$_SERVER['HTTP_AUTHORIZATION']`.

## Requests and timeouts

Apache waits 180 seconds for the answer of PHP, then returns a `504` error. Lower this delay, in seconds, with `HTTP_TIMEOUT`: the [load balancers](/doc/find-help/troubleshooting/#network) end any request after 180 seconds, whatever its value.

```bash
clever env set HTTP_TIMEOUT 60
```

PHP also stops a script after 30 seconds of execution, its default `max_execution_time`, which doesn't count waits such as database queries. Raise it in a `.user.ini` file, such as `max_execution_time=120`.

Apache refuses a request header longer than 8 KB with a `400` error. Raise this limit with `CC_APACHE_HEADERS_SIZE`, in KB, between `8` and `256`. The load balancers of some regions have a lower limit: [ask for a dedicated load balancer](https://console.clever-cloud.com/ticket-center-choice) to go beyond it.

## Change the FastCGI module

Apache passes the requests to PHP-FPM with the `proxy_fcgi` module. `CC_CGI_IMPLEMENTATION=fastcgi` selects the former `fastcgi` module instead, which isn't maintained anymore. With it, PHP receives the `Authorization` header only in `$_SERVER['Authorization']`, and the `deflate` module can send a `Content-Length` header that doesn't match the compressed content.

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/php" title="PHP with Apache" subtitle="PHP version, settings, memory, variables, caches, and tasks" icon="php" >}}
  {{< card link="/developers/doc/deploy/applications/php/composer" title="Composer" subtitle="Install dependencies, choose Composer, reach private repositories" icon="php" >}}
  {{< card link="/developers/doc/deploy/applications/php/extensions" title="Extensions" subtitle="Enable or disable PHP extensions" icon="puzzle" >}}
  {{< card link="/developers/doc/deploy/applications/php/sessions-emails" title="Sessions and emails" subtitle="Store sessions on an FS Bucket or Materia KV, send emails" icon="mail" >}}
{{< /cards >}}
