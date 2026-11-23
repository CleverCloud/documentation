---
type: docs
linkTitle: Composer
title: Composer and dependencies
description: Install the dependencies of PHP applications with Composer on Clever Cloud, choose its version, add development dependencies, and reach private repositories
keywords:
- composer
- composer.lock
- dev dependencies
- github rate limit
- php dependencies
aliases:
- /doc/applications/php/composer
---

## Overview

When your repository holds a `composer.json` file at its root, Clever Cloud installs the dependencies of your [PHP application](/doc/deploy/applications/php/) with [Composer](https://getcomposer.org). During the build, after the pre-build [hook](/doc/manage/build-hooks/), it runs this command without interaction:

```bash
composer install --no-dev
```

Commit your `composer.lock` file, so that Composer installs the versions it lists, instead of resolving them again at each build.

### Composer scripts

The [scripts](https://getcomposer.org/doc/articles/scripts.md) of your `composer.json` run during the install, such as `post-autoload-dump`, or `post-install-cmd` with a `composer.lock` file. Laravel uses them to run `artisan package:discover`, for instance. A failed script fails the build, and the deployment.

To run a command after Composer installs the dependencies, such as the migrations of a Laravel application, set it in a post-build [hook](/doc/manage/build-hooks/):

```bash
clever env set CC_POST_BUILD_HOOK "php artisan migrate --force"
```

## Development dependencies

Clever Cloud skips the `require-dev` dependencies of your `composer.json`. To install them, set `CC_PHP_DEV_DEPENDENCIES` to `install`:

```bash
clever env set CC_PHP_DEV_DEPENDENCIES install
```

## Composer version

Clever Cloud uses the Composer 2 release of its images. For PHP 7.1 and older, set `CC_COMPOSER_VERSION` to `lts`, for Composer 2.2:

```bash
clever env set CC_COMPOSER_VERSION lts
```

To use your own version, put its `composer.phar` file at the root of your repository: Clever Cloud runs it instead.

> [!NOTE] Composer 1 needs a lock file
> Packagist doesn't serve Composer 1 anymore: `CC_COMPOSER_VERSION=1` only works with a `composer.lock` file, and PHP 8.4 or earlier.

{{% include "shared/private-composer-repositories" %}}

## GitHub rate limit

Composer downloads many packages from GitHub, which can limit the anonymous requests and fail the build with `Could not authenticate against GitHub.com`. Add a [GitHub token](https://getcomposer.org/doc/articles/authentication-for-private-packages.md) to `COMPOSER_AUTH`, without any permission for public packages:

```json
{
  "github-oauth": {
    "github.com": "GITHUB_TOKEN"
  }
}
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/php" title="PHP with Apache" subtitle="PHP version, settings, memory, variables, caches, and tasks" icon="php" >}}
  {{< card link="/developers/doc/deploy/applications/php/apache" title="Apache" subtitle="Configure the web server with .htaccess, authentication, and timeouts" icon="feather" >}}
  {{< card link="/developers/doc/deploy/applications/php/extensions" title="Extensions" subtitle="Enable or disable PHP extensions" icon="puzzle" >}}
  {{< card link="/developers/doc/deploy/applications/php/sessions-emails" title="Sessions and emails" subtitle="Store sessions on an FS Bucket or Materia KV, send emails" icon="mail" >}}
{{< /cards >}}
