---
type: docs
linkTitle: Varnish as HTTP Cache
title: Varnish as HTTP Cache
description: Configure Varnish HTTP accelerator on Clever Cloud for performance optimization, content delivery, and traffic management
keywords:
- varnish cache
- http accelerator
- performance optimization
- content delivery
- reverse proxy
- caching strategy
aliases:
- /administrate/cache
- /doc/tools/varnish
---

## Overview

[Varnish](https://www.varnish-cache.org/) is a HTTP proxy-cache, which works as a reverse proxy between your application
and the client. Following rules defined by the user, Varnish will cache the data of an application to reduce the load on its server. We use **Varnish 7.7.1 and varnish-modules 0.26.0**.


> [!NOTE] Supported runtimes
> Varnish is available on **FrankenPHP**, **Go**, **Linux**, **Node.js**, **PHP with Apache**, **Static**, and **V (Vlang)** applications

## Enable Varnish for your application

To enable it, create a `varnish.vcl` file in the `/clevercloud` folder. You can also define `CC_VARNISH_FILE=/path/to/varnish.vcl` environment variable relative to your application root. This file describes how Varnish caches your applications and how it decides to return a cached resource or not. To know how to write your `varnish.vcl` file, have a look at the [Varnish 6 book](https://info.varnish-software.com/resources/varnish-6-by-example-book).

The `vcl 4.1;` and backend section of the `varnish.vcl` configuration file are not necessary as they are already handled by Clever Cloud.
If you have a PHP FTP application or if your `varnish.vcl` file is on an FS Bucket, make sure you redeploy the application for the changes to take effect.

## Varnish to restrict access to your application

### Block IP addresses

```bash {filename="clevercloud/varnish.vcl"}
sub vcl_recv {
    # Local health check
    if (client.ip == "127.0.0.1" && !req.http.X-Forwarded-For) {
        return (synth(200, "OK"));
    }

    # We don't rely on client.ip which send the load balancer IP address
    # We check if the IP to block is included in the Forwarded header instead
    if (req.http.Forwarded ~ "X.X.X.X") {
        return (synth(403, "Blocked"));
    }

    # Use return (hash); to use the cache
    return (pass);
}

sub vcl_synth {
    if (resp.status == 403) {
        set resp.http.Content-Type = "text/plain";
        synthetic("Access denied");
        return (deliver);
    }
}
```

Replace `X.X.X.X` with the IP address you want to block.

If you want to block multiple IP addresses, you can use a regular expression like this:

```bash
if (req.http.Forwarded ~ "^(X.X.X.X|Y.Y.Y.Y|Z.Z.Z.Z)$") {
    return (synth(403, "Blocked"));
}
```

To be able to configure with an environment variable multiple IPs to block, CIDR, exceptions, etc. use the following example:

- [Varnish IP blocking with environment variable](https://github.com/CleverCloud/varnish-examples/blob/main/varnish-ip-blocking/varnish.vcl)

### Ask for a login/password (Basic authentication)

```bash {filename="clevercloud/varnish.vcl"}
sub vcl_recv {
    # Local health check
    if (client.ip == "127.0.0.1" && !req.http.X-Forwarded-For) {
        return (synth(200, "OK"));
    }

    if (!req.http.Authorization) {
        return (synth(401, "Authentication Required"));
    }

    if (req.http.Authorization !~ "^Basic ") {
        return (synth(401, "Basic Authentication Required"));
    }

    set req.http.X-Auth-Credentials = regsub(req.http.Authorization, "^Basic ", "");

    if (req.http.X-Auth-Credentials != "CREDENTIALS") {
        return (synth(401, "Valid Basic Authentication Required"));
    }
}

sub vcl_synth {
    if (resp.status == 200) {
        set resp.http.Content-Type = "text/plain";
        synthetic("OK");
        return (deliver);
    }

    if (resp.status == 401) {
        set resp.http.Content-Type = "text/html; charset=utf-8";
        set resp.http.WWW-Authenticate = "Basic realm='Restricted Area'";
        synthetic("<html><body><h1>Authentication Required</h1></body></html>");

        return (deliver);
    }

    # Use return (hash); to use the cache
    return (pass);
}
```

The `CREDENTIALS` string should be replaced with the base64 encoded value of `username:password`. You can use the following command to generate it on UNIX-based systems:

```bash
echo -n "username:password" | base64
```

### Bearer token authentication

```bash {filename="clevercloud/varnish.vcl"}
import env;

sub vcl_recv {
    # Local health check
    if (client.ip == "127.0.0.1" && !req.http.X-Forwarded-For) {
        return (synth(200, "OK"));
    }

    if (!req.http.Authorization) {
        return (synth(401, "Authentication Required"));
    }

    if (req.http.Authorization !~ "^Bearer ") {
        return (synth(401, "Bearer token Required"));
    }

    set req.http.X-Token = regsub(req.http.Authorization, "^Bearer ", "");

    if (req.http.X-Token != env.get("CC_VARNISH_BEARER_TOKEN")) {
        return (synth(401, "Valid Bearer token Required"));
    }

    # Use return (hash); to use the cache
    return (pass);
}

sub vcl_synth {
    if (resp.status == 200) {
        set resp.http.Content-Type = "text/plain";
        synthetic("OK");
        return (deliver);
    }

    if (resp.status == 401) {
        set resp.http.Content-Type = "text/html; charset=utf-8";
        synthetic("<html><body><h1>Authentication Required</h1></body></html>");

        return (deliver);
    }
}
```

## Listen on the right port

Once varnish is enabled, your application should no longer listen on port **8080**, but on port **8081**. Because it's Varnish that will listen on port **8080**, and it will have in its configuration your application as backend.

## Configure the cache size

Change the storage size specified in the varnish.params file with the `CC_VARNISH_STORAGE_SIZE` environment variable (the default value is `1G`).

```bash
CC_VARNISH_STORAGE_SIZE=2G
```

## Varnish 7 migration

If you have a configuration for an older version of varnish, read [Upgrading to Varnish 7.0](https://varnish-cache.org/docs/7.0/whats-new/upgrading-7.0.html) guide.

## Example files

We provide some [examples of Varnish configuration files](https://github.com/CleverCloud/varnish-examples) that you can
use for your application. Create a `/clevercloud` folder at the root of your application if it does not exist,
rename the file to `varnish.vcl` and move it in the `/clevercloud` folder.

## Varnish with a monorepo

If you use a monorepo, you may want to use Varnish for only some of its applications. Use a dedicated `CC_VARNISH_FILE` for that.

If you have a `/clevercloud/varnish.vcl` file at the root of your monorepo, all of your applications automatically start using it with Varnish. To resolve this create a symlink during the deployments:

1. Put your `varnish.vcl` file anywhere but at the root of your monorepo.
2. Create a symlink inside a `CC_PRE_BUILD_HOOK` to the app that needs to use Varnish, such as:

```bash
CC_PRE_BUILD_HOOK="mkdir $APP_HOME/clevercloud; ln -s $APP_HOME/path/to/your/file/varnish.vcl $APP_HOME/clevercloud/varnish.vcl"
```

If you don't add this variable, the application won't use Varnish.
