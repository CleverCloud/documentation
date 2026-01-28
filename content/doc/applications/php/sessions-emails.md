---
type: docs
linkTitle: Sessions and Emails
title: PHP sessions and email configuration
description: Configure PHP session storage with FS Buckets or Redis, and SMTP email sending on Clever Cloud
keywords:
- php sessions
- fs bucket
- redis sessions
- materia kv
- smtp
- email sending
---

## Configure the session storage

By default, an [FS Bucket](/doc/addons/fs-bucket/) is created for each PHP application, so that session data is available on each instance. This FS Bucket is also used to store TMP files by default. You can change this behavior by setting the `TMPDIR` environment variable. You can set it to `/tmp` for example.

> [!NOTE] FS Buckets are not available in HDS regions
> To deploy a PHP application on an HDS region, set [`CC_PHP_DISABLE_APP_BUCKET=true`](#speed-up-or-disable-the-session-fs-bucket). Consider using Redis to manage PHP sessions.

### Speed up or disable the session FS Bucket

You can set the following environment variables:

- `CC_PHP_ASYNC_APP_BUCKET=async` to mount the session FS Bucket with the `async` option.
  It speeds up the FS Bucket usage, but it can corrupt files in case of a network outage.
- `CC_PHP_DISABLE_APP_BUCKET=(true|yes|disable)` to entirely prevent the session FS Bucket
  from being mounted.
  Use this if you don't use the default PHP session library.
  It will speed up your application but users might lose their session across instances
  and deployments.

### Use Materia KV or Redis to store PHP Sessions

Clever Cloud allows you to store PHP sessions easily in a [Materia KV](/doc/addons/materia-kv) or [Redis](/doc/addons/redis) add-on to improve performance/reliability.

To enable this feature, you need to:

- Set `ENABLE_REDIS=true` as [environment variable](/doc/develop/env-variables) in the PHP application
- Set `SESSION_TYPE=redis` as [environment variable](/doc/develop/env-variables) in the PHP application
- Create and link a Materia KV or Redis add-on to the PHP application

## Sending emails

The PHP language has the `mail` function to directly send emails. While no SMTP server is provided (needed to send the emails), you can configure one through environment variables.

Mailpace add-on can send emails through PHP `mail()` function. You have to turn TLS on with port 465 (environment variable `CC_MTA_SERVER_USE_TLS=true`) to make Mailpace working.

[Mailgun](https://www.mailgun.com/) or [Mailjet](https://www.mailjet.com/) are also recommended if your project supports it. These services already have everything you need to send emails from your code.

### Configure the SMTP server

Services like [Mailgun](https://www.mailgun.com/) or [Mailjet](https://www.mailjet.com/) provide SMTP servers. If your application has no other way but to use the `mail` function of PHP to send emails, you have to configure a SMTP server. This can be done through environment variables:

| Name | Description | Default |
|------|-------------|---------|
| `CC_MTA_SERVER_HOST` | Host of the SMTP server | |
| `CC_MTA_SERVER_PORT` | Port of the SMTP server | `465` |
| `CC_MTA_AUTH_USER` | User to authenticate to the SMTP server | |
| `CC_MTA_AUTH_PASSWORD` | Password to authenticate to the SMTP server | |
| `CC_MTA_SERVER_USE_TLS` | Enable or disable TLS | `true` |
| `CC_MTA_SERVER_STARTTLS` | Enable or disable STARTTLS | `false` |
| `CC_MTA_SERVER_AUTH_METHOD` | Enable or disable authentication | `on` |
