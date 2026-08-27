---
type: docs
linkTitle: Symfony
title: Deploy a Symfony application
description: Deploy a Symfony PHP application on Clever Cloud with Composer, a managed PostgreSQL database, migrations, assets, and production configuration
keywords:
- symfony
- php
- doctrine
- postgresql
- composer
aliases:
- /doc/applications/php/symfony
- /doc/deploy/application/php/tutorials/tutorial-symfony
- /doc/php/tutorial-symfony
- /php/tutorial-symfony
- /tutorial-symfony
---

{{< hextra/hero-subtitle >}}
  Deploy a Symfony application on Clever Cloud with a managed PostgreSQL database.
{{< /hextra/hero-subtitle >}}

[Symfony](https://symfony.com/) applications run on Clever Cloud's [PHP runtime](/developers/doc/applications/php/), which installs Composer dependencies and serves the application's public directory through Apache.

## Prepare the application

This guide assumes that your Symfony application uses Symfony Flex, works locally, and contains `composer.json` and `composer.lock`. Commit the lock file so that Clever Cloud installs the dependency versions you tested.

Apache must be able to route requests that do not match a public file to Symfony's front controller. If `public/.htaccess` is absent, install the official Apache recipe locally and commit the generated files:

```bash
composer require symfony/apache-pack
```

If the application uses Doctrine with PostgreSQL, map the linked add-on URI and its version in the production configuration:

```yaml {filename="config/packages/doctrine.yaml"}
doctrine:
  dbal:
    url: '%env(resolve:POSTGRESQL_ADDON_URI)%'
    server_version: '%env(POSTGRESQL_ADDON_VERSION)%.0.0'
```

The explicit server version lets Doctrine select the correct PostgreSQL platform. A linked PostgreSQL add-on exposes a major version such as `17`; the suffix produces the complete version format expected by current Doctrine DBAL releases.

## Create and configure the application

Install [Clever Tools](/developers/doc/cli/), log in, initialize Git if needed, then create a PHP application with an alias:

```bash
npm i -g clever-tools
clever login

git init
clever create -t php -a mySymfonyApp
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link a resource.

You can display your application's URL or add a custom domain. A custom domain also requires [DNS configuration](/developers/doc/administrate/domain-names/):

```bash
clever domain
clever domain add your.website.tld
```

Create a PostgreSQL add-on and link it to the application:

```bash
clever addon create postgresql-addon mySymfonyDatabase -p dev --link mySymfonyApp
```

You can also create and link these resources from the [Clever Cloud Console](https://console.clever-cloud.com/).

Set the public directory, PHP version, production environment, and application secret. The Composer flags replace the runtime's default `--no-scripts` flag so Symfony Flex can execute the application's trusted auto-scripts:

```bash
clever env set CC_WEBROOT /public
clever env set CC_PHP_VERSION 8.4
clever env set APP_ENV prod
clever env set APP_SECRET "$(openssl rand -hex 32)"
clever env set -- CC_PHP_COMPOSER_FLAGS "--no-interaction --no-progress --optimize-autoloader"
```

Generate a different `APP_SECRET` for each application environment and do not change it after the application starts using signed data.

### Trust Clever Cloud proxies

To use the original client address and request scheme, configure Symfony with the reverse proxy addresses injected by Clever Cloud:

```yaml {filename="config/packages/framework.yaml"}
framework:
  trusted_proxies: '%env(CC_REVERSE_PROXY_IPS)%'
```

See Symfony's [reverse proxy documentation](https://symfony.com/doc/current/deployment/proxies.html) before changing the trusted headers or adding other proxies.

## Run migrations and build assets

Run database migrations during the build phase so an incompatible instance is not promoted. Put deployment operations in an executable script:

```bash {filename="clevercloud/post_build.sh"}
#!/bin/bash
set -euo pipefail

php bin/console doctrine:migrations:migrate --no-interaction --allow-no-migration
```

Add asset commands required by your application before the migration command. For example, an application using AssetMapper may need `php bin/console asset-map:compile`. Follow the deployment instructions for the asset packages installed in your project.

```bash
chmod +x clevercloud/post_build.sh
clever env set CC_POST_BUILD_HOOK "./clevercloud/post_build.sh"
```

Review destructive migrations and use an application-specific deployment strategy when a schema change is not backward-compatible. Avoid `doctrine:schema:update --force` in production: it can attempt to alter objects managed by PostgreSQL extensions in addition to application tables.

Current Monolog recipes write production errors to standard error, which Clever Cloud collects automatically. If the application uses a custom Monolog configuration, keep its production handlers directed to `php://stderr`.

## Deploy Symfony

Commit the application and deploy it:

```bash
git add .
git commit -m "Deploy Symfony"

clever deploy
clever open
```

Follow deployments and inspect application logs with:

```bash
clever activity --follow
clever logs
```

## Learn more

{{< cards >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://symfony.com/doc/current/deployment.html" title="Symfony deployment" subtitle="Prepare and optimize a Symfony application for production" icon="symfony" >}}
  {{< card link="/developers/doc/applications/php/" title="PHP applications" subtitle="Configure and deploy PHP applications" icon="php" >}}
  {{< card link="/developers/doc/addons/postgresql/" title="PostgreSQL" subtitle="Create and operate a managed PostgreSQL database" icon="circle-stack" >}}
  {{< card link="/developers/doc/develop/build-hooks/" title="Deployment hooks" subtitle="Run commands during build and deployment phases" icon="rocket-launch" >}}
{{< /cards >}}
