---
type: docs
linkTitle: Sessions and emails
title: PHP sessions and email configuration
description: Store the sessions of PHP applications on Clever Cloud in an FS Bucket, Materia KV, or Redis, and send emails with mail() through an SMTP server
keywords:
- email sending
- fs bucket
- materia kv
- php sessions
- redis sessions
- smtp
aliases:
- /doc/applications/php/sessions-emails
---

## Configure the session storage

Clever Cloud mounts an [FS Bucket](/doc/deploy/storage/fs-bucket/) on each instance of a [PHP application](/doc/deploy/applications/php/). PHP stores its sessions there: all instances share them, and they last across deployments. It also keeps uploads there until the end of the request, unless your code moves them.

> [!NOTE] Health Data Hosting (HDS) regions
> FS Buckets aren't available in these regions: set [`CC_PHP_DISABLE_APP_BUCKET=true`](#configure-or-disable-the-session-fs-bucket), and store the sessions in [Redis](#use-materia-kv-or-redis-to-store-php-sessions).

### Configure or disable the session FS Bucket

Clever Cloud mounts this FS Bucket in the `async` mode, which speeds up writes, but can lose the latest ones on a network outage. To mount it in the `sync` mode instead, set `CC_PHP_ASYNC_APP_BUCKET` to `false`.

With `CC_PHP_DISABLE_APP_BUCKET=true`, Clever Cloud doesn't mount it: each instance keeps its own sessions and temporary files, which a deployment deletes. Users then lose their session when they reach another instance, unless you store sessions elsewhere.

### Use Materia KV or Redis to store PHP sessions

To store the PHP sessions in a [Materia KV](/doc/deploy/databases/materia-kv/) or [Redis](/doc/deploy/databases/redis/) add-on, link it to your application and set `SESSION_TYPE`:

```bash
clever env set SESSION_TYPE redis
```

Clever Cloud then configures the `redis` session handler of PHP with the credentials of the add-on, over TLS when it supports it. Without a linked add-on, the deployment fails on the missing `REDIS_PASSWORD`. Frameworks such as Laravel or Symfony have their own session settings.

## Send emails

PHP sends the emails of `mail()` through the SMTP server set by the variables below, such as the one of a [MailPace add-on](/doc/deploy/services/mailpace/#send-from-your-application).

### Configure the SMTP server

| Name                        | Description                                       | Default                                 |
| --------------------------- | ------------------------------------------------- | --------------------------------------- |
| `CC_MTA_SERVER_HOST`        | Host of the SMTP server                           |                                         |
| `CC_MTA_SERVER_PORT`        | Port of the SMTP server                           | `465`                                   |
| `CC_MTA_AUTH_USER`          | User to authenticate to the SMTP server           |                                         |
| `CC_MTA_AUTH_PASSWORD`      | Password to authenticate to the SMTP server       |                                         |
| `CC_MTA_SERVER_USE_TLS`     | Enable or disable TLS                             | `true` on port `465`, `false` otherwise |
| `CC_MTA_SERVER_STARTTLS`    | Enable or disable STARTTLS                        | `false`                                 |
| `CC_MTA_SERVER_AUTH_METHOD` | Authentication method, such as `plain`, or `off`  | `on`                                    |

Clever Cloud configures `mail()` only when `CC_MTA_SERVER_HOST`, `CC_MTA_AUTH_USER`, and `CC_MTA_AUTH_PASSWORD` are all set. To use STARTTLS, on port `587` for instance, set both `CC_MTA_SERVER_USE_TLS` and `CC_MTA_SERVER_STARTTLS` to `true`.

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/php" title="PHP with Apache" subtitle="PHP version, settings, memory, variables, caches, and tasks" icon="php" >}}
  {{< card link="/developers/doc/deploy/applications/php/apache" title="Apache" subtitle="Configure the web server with .htaccess, authentication, and timeouts" icon="feather" >}}
  {{< card link="/developers/doc/deploy/applications/php/composer" title="Composer" subtitle="Install dependencies, choose Composer, reach private repositories" icon="php" >}}
  {{< card link="/developers/doc/deploy/applications/php/extensions" title="Extensions" subtitle="Enable or disable PHP extensions" icon="puzzle" >}}
{{< /cards >}}
