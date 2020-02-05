---
title: Deploy a Symfony application
shortdesc: This article shows you how to deploy a Symfony application on Clever Cloud.
tags:
- php
- symfony
---

> This tutorial assumes that your application is based on Symfony 4 and Symfony Flex.

Symfony applications almost work out of the box on Clever Cloud, you just have a few adjustments to make.

## Create an application

You can find in [this article](/doc/clever-cloud-overview/add-application/#create-an-application) the process to create an application.
We strongly recommend to use git deployment for Symfony applications. This tutorial assumes a git deployment.

### Configure `DocumentRoot`

Add a new environment variable called `CC_WEBROOT` and set `/public` as its value. 

```
clever env set CC_WEBROOT /public
```

### Configure your application secret

`APP_SECRET` environement variable is required to generate CSRF tokens. By default for [symfony/framework-bundle](https://github.com/symfony/framework-bundle) generates one when it's installed via [Symfony Flex](https://github.com/symfony/flex). If you do not use Flex, make sure to change your APP_SECRET. The default value is `ThisTokenIsNotSoSecretChangeIt`, change it.

### Configure the Symfony environment

If you already have a `.env` file in your application and Symfony < 3.4, please don't commit it: credentials are not meant to be committed alongside your applications. Clever Cloud allows you to inject environment in your app, so you can dynamically like databases and have separate environments with the same code base.

From the console, you can edit the application's environment variables. Click on "expert mode", you'll be able to directly paste the contents of the .env file.

From the CLI, it's even simpler: `clever env import < .env`.

You will also need to set the environment variable `APP_ENV` to one of:

 - dev
 - test
 - prod


### Configure monolog to use error_log

For your application logs to be collected and available in the console and CLI,
you need to configure monolog to use its `error_log` output.

That does not mean that it will only output error level logs, you can set it to
use any level, here is an exemple with the info level (and above):

```
monolog:
    handlers:
        filter_for_errors:
            type: fingers_crossed
            action_level: error
            handler: error_log_handler
            excluded_404s:
                 # regex: exclude all 404 errors from the logs
                 - ^/

        error_log_handler:
            type: error_log
            level: info
```


### Configure your database

From the console, edit the application's environment variables. Find DATABASE_URL variable, or create it. And set it to the value of `$MYSQL_ADDON_URI`, that you can find lower in the list, under "Add-on : your-application" title. Here, you can find all environment variables about your add-on, espacially about your database.

#### Optional: run tasks after build step

If you want to have database migrations automatically run during each deployment, or frontend assets which must be built, you can write all these commands in `clevercloud/post_build.sh` like this one:

```
# Database migrations
./bin/console doctrine:migrations:migrate

# Frontend build
yarn run build
```

Make sure this file is executable:

```
chmod +x clevercloud/post_build.sh
```
Then, add this to the application's environment variables:

```
CC_POST_BUILD_HOOK=./clevercloud/post_build.sh
```

### Configure Symfony to work behind Clever Cloud reverse proxies

You can use the CC_REVERSE_PROXY_IPS [environment variable](https://www.clever-cloud.com/doc/get-help/reference-environment-variables/) that contains a list of trusted IP addresses, separated by commas.

```
if ($trustedProxies = $request->server->get('CC_REVERSE_PROXY_IPS')) {
    // trust *all* requests
    Request::setTrustedProxies(array_merge(['127.0.0.1'], explode(',', $trustedProxies)),

    // trust *all* "X-Forwarded-*" headers
    Request::HEADER_X_FORWARDED_ALL);
}
```

For more information on configuring symfony behind a reverse proxy, you can read the [official documentation](https://symfony.com/doc/current/deployment/proxies.html).
