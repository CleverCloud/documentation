---
type: docs
linkTitle: Node.js & Bun
title: Node.js & Bun runtime
description: Run JavaScript applications on Clever Cloud with Node.js and npm, or alternative tools (Bun, Deno, pnpm or Yarn)
aliases:
- /doc/applications/javascript
- /doc/applications/javascript/by-framework/nodejs
- /doc/deploy/application/node
- /doc/getting-started/by-language/node
- /doc/deploy/application/javascript/
- /doc/deploy/application/javascript/by-framework/meteor
- /doc/deploy/application/javascript/by-framework/nodejs
- /doc/nodejs/nodejs
- /doc/partials/language-specific-deploy/node
---

## Overview

Clever Cloud allows you to deploy any [Node.js](https://nodejs.org) application. We do support **any stable version of Node.js**. Learn more about [Node.js release schedule](https://nodejs.org/en/about/previous-releases). This page explains how to set up your application to run it on our service.

## Configure your Node.js application

### Mandatory configuration

Be sure that:

* you listen on HTTP port **0.0.0.0:8080**
* you have a `package.json` file
* your `package.json` either has a **scripts.start** or **main** field
* the folder `/node_modules` is mentioned in your `.gitignore` file
* you enable production mode by setting the [environment variable](#setting-up-environment-variables-on-clever-cloud) `NODE_ENV=production`

### About package.json

A valid `package.json` file should look like the following:

```json
{
  "name" : "myApp",
  "version" : "0.1.0",
  "main" : "myApp.js",
}
```

or

```json
{
  "name" : "myApp",
  "version" : "0.1.0",
  "scripts" : {
    "start" : "node myApp.js"
  }
}
```

You can use additional scripts as an alternative to [Clever Cloud hooks](/developers/doc/develop/build-hooks/#hooks-types); see [the npm documentation](https://docs.npmjs.com/cli/using-npm/scripts#npm-install). For example, `scripts.preinstall`, `scripts.install` and `scripts.postinstall` are executed during the build phase if defined. `scripts.prestart` and `scripts.poststart` are executed before and after the `scripts.start` command. Thus, your `package.json` can look like this:

```json
{
  "name" : "myApp",
  "version" : "0.1.0",
  "scripts" : {
    "preinstall": "./download.sh",  // during build phase, before dependencies installation
    "postinstall": "./cleanup.sh",  // during build phase, after dependencies installation
    "prestart": "./prepare.sh",     // during run phase, before the start command
    "start" : "node myApp.js",
  }
}
```

### Custom run command

If you need to run a custom command (or just pass options to the program), you can specify it through the `CC_RUN_COMMAND` [environment variable](#setting-up-environment-variables-on-clever-cloud). For instance, to launch `scripts.start` with a yarn based application, you must have `CC_RUN_COMMAND="yarn start"`.

### Dependencies

If you need some modules you can easily add some with the *dependencies* field in your `package.json`. Here is an example:

```json  {linenos=table}
{
  "name" : { … },
  "engines": { … },
  "dependencies": {
    "express": "5.x",
    "socket.io": "4.8.x",
    "underscore": "1.13.7"
  }
}
```

If your application has private dependencies, you can add a [private SSH key](/developers/doc/reference/common-configuration/#private-ssh-key).

## Supported package managers

We support any package manager compatible with Node.js. The [environment variable](#setting-up-environment-variables-on-clever-cloud) `CC_NODE_BUILD_TOOL` allows you to define which one you want to use. The default value is set to `npm`, but it can be any of these values:

* `bun`: uses [Bun](https://bun.sh) as a package manager and as a runtime
* `npm` or `npm-install`: default, uses [npm install](https://docs.npmjs.com/cli/install)
* `npm-ci`: uses [npm clean-install](https://docs.npmjs.com/cli/ci)
* `yarn`: uses [Yarn Classic (v1)](https://classic.yarnpkg.com/lang/en/)
* `yarn2`: uses [Yarn Berry (v2 or later)](https://yarnpkg.com/)
* `custom`: use another package manager, defined with `CC_CUSTOM_BUILD_TOOL`

You can also deploy using Deno with additional configuration. See the [Lume with Deno guide](/developers/guides/lume-deno/) for example.

>[!NOTE]
> If a `bun.lock` or a `yarn.lock` file exists in your application's main folder, `bun`/`yarn` is used. To overwrite this behavior, either delete the `bun.lock`/`yarn.lock` file or set the `CC_NODE_BUILD_TOOL` environment variable.

### Set Node.js version

If you need a specific version or branch of Node.js, set `CC_NODE_VERSION`. You can use major, minor, patch version, such as `24`, `23.11` or `22.15.1` for example. If this environment variable isn't set, the latest LTS version available on Clever Cloud is used.

{{< runtimes_versions node >}}

>[!NOTE]
For legacy reasons, the system prioritizes to the `engines.node` value in `package.json` over the `CC_NODE_VERSION` environment variable when both are set.

### Bun version

If you use Bun, your application is deployed with the latest available version on Clever Cloud:

{{< runtimes_versions bun >}}

### Yarn 3.x and 4.x support

With recent versions of Yarn, you need to put the global folder within your application to manage restarts from build cache. You can do it by setting `YARN_GLOBAL_FOLDER` to `$APP_HOME/.yarncache/` for example, in the [Console](https://console.clever-cloud.com) or through [Clever Tools](https://github.com/CleverCloud/clever-tools):

```
clever env set YARN_GLOBAL_FOLDER '$APP_HOME/.yarncache/'
```

### Corepack and packageManager support

Since Node.js v14.19.0 and v16.9.0, you can use [Corepack](https://nodejs.org/api/corepack.html) as an experimental feature  to select a package manager—npm, pnpm, or yarn—and specify its version. You can do this with a simple command (e.g.: `corepack use yarn@*`) or the [`packageManager`](https://nodejs.org/api/packages.html#packagemanager) field in `package.json`. Always set `CC_NODE_BUILD_TOOL` when using `pnpm` or `yarn`, and make sure to set `CC_CUSTOM_BUILD_TOOL` when using `pnpm`.

#### Example: Deploy with pnpm

To deploy an  application with pnpm, set the following environment variables:

{{< tabs items="npm, Corepack" >}}
  {{< tab >}}**Install with `npm`**:
  ```bash
  CC_NODE_BUILD_TOOL="custom"
  CC_PRE_BUILD_HOOK="npm install -g pnpm"
  CC_CUSTOM_BUILD_TOOL="pnpm install && pnpm build"
  ```
  {{< /tab >}}

  {{< tab >}}**Enable with Corepack**:
  ```bash
  CC_NODE_BUILD_TOOL="custom"
  CC_PRE_BUILD_HOOK="corepack enable pnpm"
  CC_CUSTOM_BUILD_TOOL="pnpm install && pnpm build"
  ```
  {{< /tab >}}
{{< /tabs >}}

This performs the following steps:

1. `CC_NODE_BUILD_TOOL` indicates that your applications is using a custom build tool
2. `CC_PRE_BUILD_HOOK` installs/enable `pnpm` globally
3. `CC_CUSTOM_BUILD_TOOL` installs the dependencies and builds the app

Depending on your stack, you may also need to add `CC_RUN_COMMAND` to your environment variables, with the appropriate command to run your application. For example, to deploy an [Astro](https://astro.build/) application in a Node.js runtime, use `CC_RUN_COMMAND="pnpm start --port 8080 --host 0.0.0.0"`.

{{< callout type="info" >}}
`CC_RUN_COMMAND` depends on your framework and your stack. The one in this example starts an Astro app, [which takes the port and the host as arguments](https://docs.astro.build/en/reference/cli-reference/#--port-number). To run your app, make sure you are using the correct command by checking the accurate framework documentation.
{{< /callout >}}

#### Development Dependencies

Development dependencies aren't automatically installed during the deployment. You can control their installation setting `CC_NODE_DEV_DEPENDENCIES` environment variable to `install` or `ignore`. This variable overrides the default behavior of `NODE_ENV`.

Here are various scenarios:

* `CC_NODE_DEV_DEPENDENCIES=install`: Development dependencies are installed.
* `CC_NODE_DEV_DEPENDENCIES=ignore`: Development dependencies aren't installed.
* `NODE_ENV=production` and `CC_NODE_DEV_DEPENDENCIES=install`: Development dependencies are installed.
* `NODE_ENV=production` and `CC_NODE_DEV_DEPENDENCIES=ignore`: Development dependencies aren't installed.
* `NODE_ENV=production`: Package manager (npm/yarn) default behavior. Development dependencies aren't installed.
* Neither `NODE_ENV` nor `CC_NODE_DEV_DEPENDENCIES` are defined: Package manager (npm/yarn) default behavior. Development dependencies are installed.

### Use private repositories with CC_NPM_REGISTRY and NPM_TOKEN

Since April 2015, `npm` allows you to have private repositories. If you want to use such a feature, you only need to provide the auth token. Add it to your application through the `NPM_TOKEN` environment variable:

```bash
NPM_TOKEN="00000000-0000-0000-0000-000000000000"
```

Then, the `.npmrc` file is created automatically for your application, with the registry URL and the token.

```txt
//registry.npmjs.org/:_authToken=00000000-0000-0000-0000-000000000000
```

Or you can set `CC_NPM_BASIC_AUTH` to use basic authentication

```bash
CC_NPM_BASIC_AUTH="user:password"
```

To authenticate to another registry (like GitHub), you can use the `CC_NPM_REGISTRY` environment variable to define its host.

```bash
CC_NPM_REGISTRY="npm.pkg.github.com"
NPM_TOKEN="00000000-0000-0000-0000-000000000000"
```

```txt
//npm.pkg.github.com/:_authToken=00000000-0000-0000-0000-000000000000
```

## Deployment video

{{< youtube id="9ww_t0o-GmA" >}}

## Automatic HTTPS redirection

You can use the [X-Forwarded-Proto header]({{< ref "doc/find-help/faq.md#how-to-know-if-a-user-comes-from-a-secure-connection" >}}) to enable it.

If you are using [Express.js](https://expressjs.com/), you can use [express-sslify](https://www.npmjs.com/package/express-sslify) by adding:

```javascript
app.use(enforce.HTTPS({
  trustProtoHeader: true
}));
```

{{< content "new-relic" >}}

## Troubleshooting your application

If you are often experiencing auto restart of your Node.js instance, maybe you have an application crashing that we automatically restart.
To target this behavior, you can gracefully shut down with events handlers on `uncaughtExeption` `unhandledRejection` `sigint` and `sigterm` and log at this moment, so you can fix the problem.

{{< content "env-injection" >}}

To access environment variables from your code, you can use `process.env.MY_VARIABLE`.

{{< content "deploy-git" >}}

{{< content "link-addon" >}}

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}
