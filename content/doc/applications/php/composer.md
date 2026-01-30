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

Composer build is supported out of the box. You just need to provide a `composer.json` file in the root of your repository and `composer.phar install --no-ansi --no-progress --no-interaction --no-dev` is run automatically during the build phase.

You can also set the `CC_COMPOSER_VERSION` to `1` or `2` to select the composer version to use.

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

Development dependencies are not automatically installed during the deployment. You can control their installation by using the `CC_PHP_DEV_DEPENDENCIES` environment variable which takes `install` value.

Any other value than `install` will prevent development dependencies from being installed.

## GitHub rate limit

Sometimes, you can encounter the following error when downloading dependencies:

```txt
Failed to download symfony/symfony from dist: Could not authenticate against GitHub.com
```

To prevent this download dependencies's fails that is often caused by rate limit of GitHub API while deploying your apps,
we recommend you to add `oauth` token in your composer configuration file or in separate file named as described in
[composer FAQ (API rate limit and OAuth tokens)](https://getcomposer.org/doc/articles/troubleshooting.md#api-rate-limit-and-oauth-tokens).

You can find more documentation about composer configuration at [getcomposer.com](https://getcomposer.org/doc/04-schema.md).

## Post-build hook example

You use Artisan to manage your project and you want to execute *artisan migrate* before running your app.

To do this, use a post build hook by setting the following environment variable on your Clever application:

```bash
CC_POST_BUILD_HOOK=php artisan migrate --force
```

> [!NOTE]
> You must add the *execute* permission to your file (`chmod u+x yourfile`) before pushing it.
