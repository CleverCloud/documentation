---
title: Deploy a Symfony application
shortdesc: This article shows you how to deploy a Symfony application on Clever Cloud.
tags:
- php
- symfony
---

# Deploy a Symfony application

Symfony applications almost work out of the box on Clever Cloud, you just have a few adjustments to make.

## Create an application

You can find in [this article](/doc/clever-cloud-overview/add-application/#create-an-application) the process to create an application.
We strongly recommend to use git deployment for Symfony applications. This tutorial assumes a git deployment.

### Configure `DocumentRoot`

Create a `php.json` file in a `clevercloud` directory at the root of your application.

```json
{
  "deploy": {
    "webroot": "/public"
  }
}
```

### Configure your application secret

`APP_SECRET` environement variable is required to generate CSRF tokens. By default for [symfony/framework-bundle](https://github.com/symfony/framework-bundle) generates one when it's installed via [Symfony Flex](https://github.com/symfony/flex). If you do not use Flex, make sure to change your APP_SECRET. The default value is `ThisTokenIsNotSoSecretChangeIt`, change it.

### Configure the Symfony environment

If you already have a `.env` file in your application, please don't commit it: credentials are not meant to be committed alongside your applications. Clever Cloud allows you to inject environment in your app, so you can dynamically like databases and have separate environments with the same code base.

From the console, you can edit the application's environment variables. Click on "expert mode", you'll be able to directly paste the contents of the .env file.

From the CLI, it's even simpler: `clever env import < .env`.


### Configure monolog to use syslog

Make sure that Symfony send error level logs to syslog, then you will be able to read them in clever-cloud log console.

Here is an exemple of monolog configuration that stores all log messages during a request but only writes them only if one of the messages reaches error level, and in all cases passes all error level message to syslog:

```
monolog:
    handlers:
        handlers:
            filter_for_errors:
                type: fingers_crossed
                action_level: error
                handler: file_handler

            file_handler:
                type: stream
                path: "%kernel.logs_dir%/%kernel.environment%.log"

            syslog_handler:
                type: syslog
                level: error
```


### Configure your database

From the console, edit the application's environment variables. Find DATABASE_URL variable, or create it. And set it to `$MYSQL_ADDON_URI`, that you can find lower in the list, under "Add-on : your-application" title. Here, you can find all environment variables about your add-on, espacially about your database.

#### Optional: run tasks after build step

If you want to have database migrations automatically run during each deployment, or frontend assets which must be built, you can write all these commands in `clevercloud/post_build.sh` like this one:

```
# Database migrations
./bin/console doctrine:migrations:migrate

# Frontend build
yarn run build
```

Thens, add this to the application's environment variables:

```
CC_POST_BUILD_HOOK=./post_build.sh
```
