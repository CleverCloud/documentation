---
type: docs
title: Node.js
shortdesc: Node.js is a platform built on Chrome's JavaScript runtime for building fast, scalable network applications.
tags:
- deploy
keywords:
- nodejs
str_replace_dict:
  "@application-type@": "Node"
type: docs
aliases:
- /doc/applications/javascript/by-framework/nodejs
- /doc/nodejs/nodejs
---

## Overview

Clever Cloud allows you to deploy any [Node.js](https://nodejs.org) application. We do support **any stable version of Node.js**. Their release schedule is available [here](https://nodejs.org/en/about/previous-releases). This page explains how to set up your application to run it on our service.

{{% content/create-application %}}

{{% content/set-env-vars %}}

## Configure your Node.js application

### Mandatory configuration

Be sure that:

* you listen on HTTP port **0.0.0.0:8080**
* you have a `package.json` file
* your `package.json` either has a **scripts.start** or **main** field
* the folder `/node_modules` is mentioned in your `.gitignore` file
* you enable production mode by setting the [environment variable](#setting-up-environment-variables-on-clever-cloud) `NODE_ENV=production`

### Set Node.js version

You can use the `engines.node` field in `package.json` to define the wanted version, if not provided we will use the latest LTS version.

### About package.json

The `package.json` file should look like the following:

```json
{
  "name" : "myapp",
  "version" : "0.1.0",
  "main" : "myapp.js",
  "scripts" : {
    "start" : "node myapp.js"
  },
  "engines" : {
    "node" : "^20"
  }
}
```

The following table describes each of the fields formerly mentioned:

| Usage        | Field         | Description                                |
|--------------|---------------|--------------------------------------------|
| **At least one** | `scripts.start` | This field provides a command line to run. If defined, `npm start` will be launched. Otherwise, we will use the `main` field. See below to know how and when to use the `scripts.start` field.                   |
| **At least one** | `main`          | This field allows you to specify the file you want to run. It should be the relative path of the file starting at the project's root. It's used to launch your application if `scripts.start` is not defined. |
| Optional     | `engines.node`  | Sets the Node.js version you app runs with. Any `A.B.x` or `^A.B.C` or `~A.B` version will lead to run the application with the latest `A.B` local version. If this field is missing, we use the latest LTS available. If you want to ensure that your app will always run, please put something of the form `^A.B.C` and avoid setting only `>=A.B.C`.            |

### Dependencies

If you need some modules you can easily add some with the *dependencies* field in your `package.json`. Here is an example:

```json  {linenos=table}
{
  "name" : { ... },
  "engines": { ... },
  "dependencies": {
    "express": "4.x",
    "socket.io": "4.7.x",
    "underscore": "1.13.6"
  }
}
```

If your application has private dependencies, you can add a [Private SSH Key]({{< ref "doc/reference/common-configuration.md#private-ssh-key" >}}).

#### Development Dependencies

Development dependencies will not be automatically installed during the deployment. You can control their installation setting `CC_NODE_DEV_DEPENDENCIES` environment variable to `install` or `ignore`. This variable overrides the default behavior of `NODE_ENV`.

Here are various scenarios:

* `CC_NODE_DEV_DEPENDENCIES=install`: Development dependencies will be installed.
* `CC_NODE_DEV_DEPENDENCIES=ignore`: Development dependencies will not be installed.
* `NODE_ENV=production, CC_NODE_DEV_DEPENDENCIES=install`: Development dependencies will be installed.
* `NODE_ENV=production, CC_NODE_DEV_DEPENDENCIES=ignore`: Development dependencies will not be installed.
* `NODE_ENV=production`: Package manager (NPM / Yarn) default behavior. Development dependencies will not be installed.
* Neither `NODE_ENV` nor `CC_NODE_DEV_DEPENDENCIES` are defined: Package manager (NPM / Yarn) default behavior. Development dependencies will be installed.

### Supported package managers

We support any package manager compatible with Node.js. The [environment variable](#setting-up-environment-variables-on-clever-cloud) `CC_NODE_BUILD_TOOL` allows you to define which one you want to use. The default value is set to `npm`, but it can be any of these values:

* `npm-install`: uses [npm install](https://docs.npmjs.com/cli/install)
* `npm-ci`: uses [npm clean-install](https://docs.npmjs.com/cli/ci)
* `npm`: Defaults to `npm-install`
* `yarn`: uses [yarn@1](https://classic.yarnpkg.com/lang/en/)
* `yarn2`: uses [yarn@2 or later versions](https://yarnpkg.com/)
* `custom`: use another package manager (bun, pnpm, etc.) with `CC_CUSTOM_BUILD_TOOL`

If a `yarn.lock` file exists in your application's main folder, `yarn` will be set as package manager. To overwrite this behavior, either delete the `yarn.lock` file or set the `CC_NODE_BUILD_TOOL` environment variable.

#### Yarn 3.x and 4.x support

With recent versions of Yarn, you need to put the global folder within your application to manage restarts from build cache. You can do it by setting `YARN_GLOBAL_FOLDER` to `$APP_HOME/.yarncache/` for example, in the [Console](https://console.clever-cloud.com) or through [Clever Tools](https://github.com/CleverCloud/clever-tools):

```
clever env set YARN_GLOBAL_FOLDER '$APP_HOME/.yarncache/'
```

#### Corepack and packageManager support

Since Node.js v14.19.0 and v16.9.0, you can use [Corepack](https://nodejs.org/api/corepack.html) as an experimental feature to set a package manager from `npm`, `pnpm` or `yarn`, and its version. It can be achieved through a simple command (e.g.: `corepack use yarn@*`) or the [`packageManager`](https://nodejs.org/api/packages.html#packagemanager) field in `package.json`. If you use `pnpm` or `yarn`, you should always set `CC_NODE_BUILD_TOOL` and `CC_CUSTOM_BUILD_TOOL` for `pnpm`.

### Custom build phase

The build phase installs the dependencies and executes the `scripts.install` you might have defined in your `package.json`. It's meant to build the whole application including dependencies and / or assets (if there are any).

All the build part should be written into the `scripts.install` field of the `package.json` file. You can also add a custom bash script and execute it with: `"scripts.install": "./build.sh"`. For more information, see [the npm documentation](https://docs.npmjs.com/misc/scripts)

### Custom run phase

The run phase is executed from `scripts.start` if defined. It's only meant to start your application and should not
contain any build task.

### Custom run command

If you need to run a custom command (or just pass options to the program), you can specify it through the `CC_RUN_COMMAND` [environment variable](#setting-up-environment-variables-on-clever-cloud). For instance, to launch `scripts.start` with a yarn based application, you must have `CC_RUN_COMMAND="yarn start"`.

### Alternative runtimes

There are multiples JavaScript server runtimes out there. On Clever Cloud, you can deploy your applications with the one of your choice. You'll find guides for [Bun](https://www.clever-cloud.com/fr/blog/fonctionnalites/2023/09/19/bun-comment-heberger-vos-applications-sur-clever-cloud/) or [Deno](/guides/lume-deno/) for example.

### Use private repositories with CC_NPM_REGISTRY and NPM_TOKEN

Since April 2015, `npm` allows you to have private repositories. If you want to use such a feature, you only need to provide the auth token. Add it to your application through the `NPM_TOKEN` environment variable:

```bash
NPM_TOKEN="00000000-0000-0000-0000-000000000000"
```

Then, the `.npmrc` file will be created automatically for your application, with the registry URL and the token.

```txt
//registry.npmjs.org/:_authToken=00000000-0000-0000-0000-000000000000
```

To authenticate to another registry (like GitHub), you can use the `CC_NPM_REGISTRY` environment variable to define its host.

```bash
CC_NPM_REGISTRY="npm.pkg.github.com"
NPM_TOKEN="00000000-0000-0000-0000-000000000000"
```

```txt
//npm.pkg.github.com/:_authToken=00000000-0000-0000-0000-000000000000
```

{{% content/new-relic %}}

{{% content/env-injection %}}

To access environment variables from your code, you can use `process.env.MY_VARIABLE`.

{{% content/deploy-git %}}

## Automatic HTTPS redirection

You can use the [X-Forwarded-Proto header]({{< ref "doc/find-help/faq.md#how-to-know-if-a-user-comes-from-a-secure-connection" >}}) to enable it.

If you are using [Express.js](https://expressjs.com/), you can use [express-sslify](https://www.npmjs.com/package/express-sslify) by adding:

```javascript
app.use(enforce.HTTPS({
  trustProtoHeader: true
}));
```

## Troubleshooting your application

If you are often experiencing auto restart of your Node.js instance, maybe you have an application crashing that we automatically restart.
To target this behavior, you can gracefully shut down with events handlers on `uncaughtExeption` `unhandledRejection` `sigint` and `sigterm` and log at this moment, so you can fix the problem.

{{% content/link-addon %}}

{{% content/more-config %}}

{{% content/env-injection %}}

{{% content/url_healthcheck %}}

## Deployment video

{{< youtube id="dxhSjHnrrhA" >}}
