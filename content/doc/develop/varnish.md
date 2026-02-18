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
- /doc/administrate/cache
- /doc/tools/varnish
---

## Overview

[Varnish](https://www.varnish-cache.org/) is an HTTP proxy-cache that sits as a reverse proxy between your application and the client. It caches responses according to rules you define, reducing load on your application. Clever Cloud provides **Varnish {{< runtime_version varnish >}} and varnish-modules {{< runtime_version varnish-modules >}}**.

> [!NOTE] Supported runtimes
> Varnish is available on all runtimes that support [Request Flow](/doc/develop/request-flow/).

## Enable Varnish for your application

Create a `varnish.vcl` file in the `clevercloud/` folder at the root of your application. You can also set the `CC_VARNISH_FILE` environment variable to a custom path within your application root, written as an absolute path starting at `/` (for example `CC_VARNISH_FILE=/config/varnish.vcl`). If the file does not exist, deployment fails.

This file describes how Varnish caches your application's responses and when it returns a cached resource. To learn how to write your `varnish.vcl` file, refer to the [Varnish documentation](https://varnish-cache.org/docs/8.0/index.html).

The `vcl 4.1;` declaration and backend section are not necessary as they are already handled by Clever Cloud. If your `varnish.vcl` file is stored on an FS Bucket, redeploy the application for changes to take effect.

## Listen on the right port

Varnish is managed through [Request Flow](/doc/develop/request-flow/). Once Varnish is enabled, your application must listen on port **9000** instead of **8080**. Request Flow places Varnish (and any other configured middleware) between the public port (`8080`) and your application. In runtimes where Clever Cloud manages the port configuration (FrankenPHP, Java, PHP, Static), this is handled transparently.

## Configure the cache size

Set the `CC_VARNISH_STORAGE_SIZE` environment variable to configure the Varnish cache size (default: `1G`).

```bash
CC_VARNISH_STORAGE_SIZE=2G
```

## Varnish migration

If you have a configuration for an older version of Varnish, read:

- [Upgrading to Varnish 7.0](https://varnish-cache.org/docs/7.0/whats-new/upgrading-7.0.html) guide
- [Upgrading to Varnish 8.0](https://varnish-cache.org/docs/8.0/whats-new/upgrading-8.0.html) guide

## Example files

Clever Cloud provides [example Varnish configuration files](https://github.com/CleverCloud/varnish-examples). Download the one that fits your needs, rename it to `varnish.vcl` and place it in the `clevercloud/` folder at the root of your application.

## Varnish with a monorepo

If you use a monorepo, you may want to use Varnish for only some of its applications. Use `CC_VARNISH_FILE` to point to a specific configuration file. A `clevercloud/varnish.vcl` file at the root of your monorepo activates Varnish for all applications. To limit Varnish to specific applications, place the file elsewhere and create a symlink during deployment only for the applications that need it:

```bash
CC_PRE_BUILD_HOOK="mkdir $APP_HOME/clevercloud; ln -s $APP_HOME/path/to/your/file/varnish.vcl $APP_HOME/clevercloud/varnish.vcl"
```

Applications without this hook or without `CC_VARNISH_FILE` set will not use Varnish.
