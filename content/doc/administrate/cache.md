---
type: docs
title: Varnish as HTTP Cache
position: 3
shortdesc: Configuring Varnish on Clever Cloud
tags:
- administrate
keywords:
- varnish
- varnish-modules
- caching
- cache
type: docs
---

## Overview

[Varnish](https://www.varnish-cache.org/) is a HTTP proxy-cache, which works as a reverse proxy between your application and the client. Following rules defined by the user, Varnish will cache the data of an application to reduce the load on its server. We use **Varnish 7.7.1 and varnish-modules 0.26.0**.

## Limitations

Varnish is available on **FrankenPHP**, **Go**, **Node.js** and **PHP with Apache** applications. Support for other applications is in discussion.

For more information about it, contact [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice).

## Enable Varnish for your application

To enable it, you just have to create a `varnish.vcl` file in the `/clevercloud` folder.
This file describes how Varnish caches your applications and how it decides to return a cached resource or not.

{{< callout type="warning" >}}
The `vcl 4.1;` and backend section of the `varnish.vcl` configuration file are not necessary as they are already handled by Clever Cloud.
If you have a PHP FTP application or if your `varnish.vcl` file is on an FS Bucket, make sure you redeploy the application for the changes to take effect.
{{< /callout >}}

To learn how to write your `varnish.vcl` file, read:
- [Varnish documentation](https://varnish-cache.org/docs/)
- [Varnish 6 book](https://info.varnish-software.com/resources/varnish-6-by-example-book)

If you already have a configuration for an older version of Varnish, read [the upgrading to 7.0 guide](https://varnish-cache.org/docs/7.0/whats-new/upgrading-7.0.html).

## Listen on the right port

Once varnish is enabled, your application should no longer listen on port **8080**, but on port **8081**. Because it's Varnish that will listen on port **8080**, and it will have in its configuration your application as backend.

## Configure the cache size

You can change the storage size specified in the varnish.params file with the `CC_VARNISH_STORAGE_SIZE` environment variable (the default value is `1G`).

```bash
CC_VARNISH_STORAGE_SIZE=2G
```

## Varnish to cache your application's content

We provide some [examples of Varnish configuration files](https://GitHub.com/CleverCloud/varnish-examples) that you can use for your application.

## Varnish to restrict access to your application

As Varnish acts as a reverse proxy, you can also use it to chose whether requests should be forwarded to your application, based on the Authorization header or the IP address of the client for example.

>[!NOTE] Varnish on Clever Cloud and client IP
>Clever Cloud's applications are behind a load balancer, which means that the `client.ip` variable in Varnish will always be the IP address of the load balancer. To get the real client IP address, you should use the `X-Forwarded-For` or `Forwarded` headers.

### Block IP addresses

```bash {filename="clevercloud/varnish.vcl"}
sub vcl_recv {
    # Local health check
    if (client.ip == "127.0.0.1") {
        return (synth(200, "OK"));
    }

    # We don't rely on client.ip which send the load balancer IP address
    # We check if the IP to block is included in the Forwarded header instead
    # Replace X.X.X.X and Y.Y.Y.Y with the IP addresses you want to block
    if (req.http.Forwarded ~ "X.X.X.X" ||
        req.http.Forwarded ~ "Y.Y.Y.Y" ) {
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

If you need to only authorize some IP addresses, you can't just block if the IP is mentioned in the `Forwarded` header, as a user can add content to it. Instead, block all malformed requests and extract the IP address to check it:

```bash {filename="clevercloud/varnish.vcl"}
    # For other requests, we check the Forwarded header to extract the client IP and refuse access if it's malformed or missing
    if (!req.http.Forwarded) {
        return (synth(403, "Access Denied"));
    }

    # Expected format is proto=https;for=IP:PORT;by=IP
    if (req.http.Forwarded !~ "^proto=https;for=[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]+;by=[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$") {
        return (synth(403, "Access Denied"));
    }

    # We get and check the client IP format
    set req.http.X-Client-IP = regsub(req.http.Forwarded, "^proto=https;for=([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}):[0-9]+;by=.*$", "\1");
    if (req.http.X-Client-IP !~ "^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$") {
        return (synth(403, "Access Denied"));
    }

    if (req.http.X-Client-IP != "X.X.X.X" &&
        req.http.X-Client-IP != "Y.Y.Y.Y" ) {
        return (synth(403, "Blocked"));
    }

    unset req.http.X-Client-IP;
```

To be able to configure multiple IPs to authorize/block, CIDR, exceptions, with an environment variable, use ACL as in the following example:

- [Varnish multiple IP blocking with environment variable](https://github.com/CleverCloud/varnish-examples/blob/main/varnish-ip-blocking/varnish.vcl)

### Basic authentication

To ask for a login/password, you can use [Basic authentication](https://www.rfc-editor.org/rfc/rfc7617.txt) and the `Authorization` header:

```bash {filename="clevercloud/varnish.vcl"}
sub vcl_recv {
    # Local health check
    if (client.ip == "127.0.0.1") {
        return (synth(200, "OK"));
    }

    if (!req.http.Authorization) {
        return (synth(401, "Authentication Required"));
    }

    if (req.http.Authorization !~ "^Basic ") {
        return (synth(401, "Basic Authentication Required"));
    }

    set req.http.X-Auth-Credentials = regsub(req.http.Authorization, "^Basic ", "");

    # Replace CREDENTIALS with your base64 encoded login:password
    # You can generate it with this command: echo -n "username:password" | base64
    if (req.http.X-Auth-Credentials != "CREDENTIALS" &&
        req.http.X-Auth-Credentials != "ANOTHER_CREDENTIALS") {
        return (synth(401, "Valid Basic Authentication Required"));
    }

    # Remove the Authorization header to avoid sending it to the backend
    unset req.http.X-Auth-Credentials;
    unset req.http.Authorization;

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
        set resp.http.WWW-Authenticate = "Basic realm='Restricted Area'";
        synthetic("<html><body><h1>Authentication Required</h1></body></html>");

        return (deliver);
    }
}
```

To avoid writing your credentials in the `varnish.vcl` file, you can use an environment variable to store them:

- [Varnish Basic authentication with environment variable](https://github.com/CleverCloud/varnish-examples/blob/main/varnish-ip-blocking/varnish.vcl)

### Bearer token authentication

To protect access to an API, using a Bearer token is a common practice. You can use Varnish to check the `Authorization` header and validate the Bearer token before forwarding the request to your application:

```bash {filename="clevercloud/varnish.vcl"}
sub vcl_recv {
    # Local health check
    if (client.ip == "127.0.0.1") {
        return (synth(200, "OK"));
    }

    if (!req.http.Authorization) {
        return (synth(401, "Authentication Required"));
    }

    if (req.http.Authorization !~ "^Bearer ") {
        return (synth(401, "Bearer token Required"));
    }

    set req.http.X-Token = regsub(req.http.Authorization, "^Bearer ", "");

    # Replace YOUR_BEARER_TOKEN and ANOTHER_BEARER_TOKEN with your actual tokens
    if (req.http.X-Token != "YOUR_BEARER_TOKEN" &&
        req.http.X-Token != "ANOTHER_BEARER_TOKEN") {
        return (synth(401, "Valid Bearer token Required"));
    }

    # Remove the Authorization header to avoid sending it to the backend
    unset req.http.X-Token;
    unset req.http.Authorization;

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

To avoid writing your credentials in the `varnish.vcl` file, you can use an environment variable to store them:

- [Varnish Bearer token with environment variable](https://github.com/CleverCloud/varnish-examples/blob/main/varnish-ip-blocking/varnish.vcl)

## Varnish to throttle your application's traffic

You can use Varnish to limit the number of requests per second to your application, which is useful to prevent abuse or to protect your application from DDoS attacks. This can be combined with other Varnish rules and features.

```bash {filename="clevercloud/varnish.vcl"}
import vsthrottle;

sub vcl_recv {

    # Local health check
    if (client.ip == "127.0.0.1") {
        return (synth(200, "OK"));
    }

    # For other requests, we check the Forwarded header to extract the client IP and refuse access if it's malformed or missing
    if (!req.http.Forwarded) {
        return (synth(403, "Access Denied"));
    }

    # Expected format is proto=https;for=IP:PORT;by=IP
    if (req.http.Forwarded !~ "^proto=https;for=[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]+;by=[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$") {
        return (synth(403, "Access Denied"));
    }

    # We get and check the client IP format
    set req.http.X-Client-IP = regsub(req.http.Forwarded, "^proto=https;for=([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}):[0-9]+;by=.*$", "\1");
    if (req.http.X-Client-IP !~ "^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$") {
        return (synth(403, "Access Denied"));
    }

    # Limit to 10 requests per 1 minute
    # It's good values for tests, use higher values in production
    if (vsthrottle.is_denied(req.http.X-Client-IP, 10, 1m)) {
        return (synth(429, "Rate limit exceeded"));
    }

    # Use return (hash); to use the cache
    return (pass);
}

sub vcl_synth {
    if (resp.status == 403) {
        set resp.http.Content-Type = "text/plain";
        synthetic("Access Denied");
        return (deliver);
    }

    if (resp.status == 429) {
        set resp.http.Retry-After = "60";
        set resp.http.Content-Type = "text/plain";
        synthetic("Rate limit exceeded. Please try again later.");
        return (deliver);
    }
}

# Send informations about rate limit and remaining requests in response headers
sub vcl_deliver {
    set resp.http.X-RateLimit-Limit = "10";
    set resp.http.X-RateLimit-Remaining = "" + vsthrottle.remaining(req.http.X-Client-IP, 10, 1m);

    unset resp.http.X-Client-IP;
}
```

## Varnish with a monorepo

If you use a monorepo, you may want to use Varnish for only some of the applications inside it.
If you have a `/clevercloud/varnish.vcl` file at the root of your monorepo, all of your applications automatically start using Varnish.

To resolve this issue, you can create a symlink during the deployments.

1. Put your `varnish.vcl` file anywhere but at the root of your monorepo.
2. Create a symlink inside a `CC_PRE_BUILD_HOOK`.

Here is an example :

```bash
CC_PRE_BUILD_HOOK="mkdir $APP_HOME/clevercloud; ln -s $APP_HOME/path/to/your/file/varnish.vcl $APP_HOME/clevercloud/varnish.vcl"
```

Then add the `CC_PRE_BUILD_HOOK` as a variable to the app that needs to use Varnish. If you don't add this variable, the application won't use it.
