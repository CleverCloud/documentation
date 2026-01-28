---
type: docs
linkTitle: Composer
title: Composer and dependencies
description: Manage PHP dependencies with Composer on Clever Cloud, including version selection, development dependencies, and private repositories
keywords:
- composer
- php dependencies
- github rate limit
- dev dependencies
---

## Composer

Composer build is supported out of the box. If a `composer.json` file is detected at the root of your project, dependencies are installed during the build phase with `--no-interaction --no-progress --no-scripts --no-dev` flags. To override the base flags (`--no-interaction --no-progress --no-scripts`), set the `CC_PHP_COMPOSER_FLAGS` environment variable.

To install development dependencies, set `CC_PHP_DEV_DEPENDENCIES` to `install`. This removes the `--no-dev` flag independently of `CC_PHP_COMPOSER_FLAGS`.

Set `CC_COMPOSER_VERSION` to select the Composer version: `1`, `2` (default) or `lts` (maps to `2.2`).

> [!TIP] Use a local Composer version
> If you put a `composer.phar` file at the root of your project, it will be used to install dependencies.

You can perform your own `composer.phar install` by using the [Post Build hook](/doc/develop/build-hooks#post-build-cc_post_build_hook).

Example of a `composer.json` file:

```json
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
            "url": "https://github.com/timothylhuillier/laravel-elasticsearch.git"
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

- [Example: minimalist PHP application using Composer and custom scripts](https://github.com/CleverCloud/php-composer-demo)

## Development Dependencies

Development dependencies are not automatically installed during the deployment. Set `CC_PHP_DEV_DEPENDENCIES` to `install` to include them. Set it to `skip` or leave it unset to exclude them.

## GitHub rate limit

Sometimes, you can encounter the following error when downloading dependencies:

```txt
Failed to download symfony/symfony from dist: Could not authenticate against GitHub.com
```

To avoid failed dependency downloads caused by GitHub API rate limits during deployment,
configure an OAuth token in your Composer configuration file or in a separate file as described in the
[Composer FAQ (API rate limit and OAuth tokens)](https://getcomposer.org/doc/articles/troubleshooting.md#api-rate-limit-and-oauth-tokens).

You can find more documentation about Composer configuration in the [Composer schema reference](https://getcomposer.org/doc/04-schema.md).

## Post-build hook example

You use Artisan to manage your project and you want to execute *artisan migrate* before running your app.

To do this, use a post build hook by setting the following environment variable on your Clever application:

```bash
CC_POST_BUILD_HOOK=php artisan migrate --force
```

> [!NOTE]
> You must add the *execute* permission to your file (`chmod u+x yourfile`) before pushing it.
