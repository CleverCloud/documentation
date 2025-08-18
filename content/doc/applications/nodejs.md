---
type: docs
linkTitle: Node.js & Bun
title: Node.js & Bun runtime
description: Deploy JavaScript applications on Clever Cloud with Node.js runtime and npm, or alternative tools like Bun, Deno, pnpm or Yarn
keywords:
- nodejs app hosting
- nodejs cloud
- javascript
- bun app hosting
- bun cloud
- deno app hosting
- deno cloud
- npm
- pnpm
- typescript
- yarn
aliases:
- /applications/javascript/nodejs
- /deploy/application/javascript/by-framework/nodejs
- /doc/applications/javascript
- /doc/applications/javascript/by-framework/nodejs
- /doc/applications/javascript/nodejs
- /doc/deploy/application/node
- /doc/getting-started/by-language/node
- /doc/deploy/application/javascript
- /doc/deploy/application/javascript/by-framework/meteor
- /doc/deploy/application/javascript/by-framework/nodejs
- /doc/deploy/application/javascript/nodejs
- /doc/nodejs
- /doc/nodejs/nodejs
- /doc/nodejs-hosting
- /doc/partials/language-specific-deploy/node
- /getting-started/by-language/node
---

## Overview

Clever Cloud allows you to deploy any JavaScript and TypeScript application. We do support **any stable version of Node.js**. Learn more about [Node.js release schedule](https://nodejs.org/en/about/previous-releases). This page explains how to set up your application to run it on our service.

## Create your Node.js & Bun application

To create a new Node.js & Bun application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type node
```
* [Learn more about Clever Tools](/doc/cli/)
* [Learn more about Clever Cloud application deployment](/doc/quickstart/#create-an-application-step-by-step)

## Configure your Node.js & Bun application

### Mandatory needs

Be sure that:

* You listen on HTTP port **0.0.0.0:8080**
* You have a `package.json` file
* Your `package.json` either has a **scripts.start** or a **main** field
* The folder `/node_modules` is mentioned in your `.gitignore` file
* You enable production mode by setting the [environment variable](#setting-up-environment-variables-on-clever-cloud) `NODE_ENV=production`

### Build phase

During the build phase, Clever Cloud will install your application dependencies with the selected package manager.

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

You can use additional scripts as an alternative to [Clever Cloud hooks](/doc/develop/build-hooks/#hooks-types); see [the npm documentation](https://docs.npmjs.com/cli/using-npm/scripts#npm-install). For example, `scripts.preinstall`, `scripts.install` and `scripts.postinstall` are executed during the build phase if defined. `scripts.prestart` and `scripts.poststart` are executed before and after the `scripts.start` command. Thus, your `package.json` can look like this:

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

If your application has private dependencies, you can add a [private SSH key](/doc/reference/common-configuration/#private-ssh-key).

- [Use private repositories](#use-private-repositories)
- [Manage Development Dependencies](#development-dependencies)

## Supported package managers

Clever Cloud supports any package manager compatible with Node.js ecosystem. The [environment variable](#setting-up-environment-variables-on-clever-cloud) `CC_NODE_BUILD_TOOL` allows you to define which one you want to use to install dependencies during the build phase:

* `bun`: uses [Bun](https://bun.sh) as a package manager and as a runtime
* `npm` or `npm-install`: default, uses [npm install](https://docs.npmjs.com/cli/install)
* `npm-ci`: uses [npm clean-install](https://docs.npmjs.com/cli/ci)
* `pnpm`: uses [pnpm](https://pnpm.io)
* `yarn-berry`: uses [Yarn](https://yarnpkg.com/)
* `custom`: use another package manager, defined with `CC_CUSTOM_BUILD_TOOL`

> [!NOTE] Yarn 1.x and 2.x deprecation
> `yarn` and `yarn2` are still valid values but the Yarn team no longer maintains 1.x and 2.x branches. Use `yarn-berry` instead.

### What about Deno?

Deno is not natively supported on Clever Cloud, but you can get it [using Mise](/doc/reference/reference-environment-variables#install-tools-with-mise-package-manager), by setting a `mise.toml` file with the following content:

```toml {filename="mise.toml"}
[tools]
deno = "latest"
```

Then it will be installed during deployment. You can replace `latest` with a specific version.

* [Lume with Deno guide](/guides/lume-deno/)

### Automatic detection

If a lock file exists in your application's main folder, the corresponding package manager is set:

- If a `bun.lock` file exists, `bun` is used for build/run
- If a `pnpm-lock.yaml` file exists, `pnpm` is used for build/run
- If a `yarn.lock` file exists, and a 3.x/4.x version is declared in `package.json`, `yarn-berry` is used for build/run

To overwrite this behavior, either delete the lock file or set the `CC_NODE_BUILD_TOOL` environment variable.

## Version management

### Set Node.js version

If you need a specific version or branch of Node.js, set `CC_NODE_VERSION`. You can use major, minor, patch version, such as `24`, `23.11` or `22.15.1` for example. If this environment variable isn't set, the latest LTS version available on Clever Cloud is used.

{{< runtimes_versions node >}}

> [!NOTE]
> For legacy reasons, the system prioritizes to the `engines.node` value in `package.json` over the `CC_NODE_VERSION` environment variable when both are set.

### Bun version

If you use Bun, your application is deployed with the latest available version on Clever Cloud:

{{< runtimes_versions bun >}}

### pnpm and Yarn versions

To load a specific version, set the `packageManager` field in your `package.json` file. For example, to use `pnpm@10.14.0`:

```json
{
  "packageManager": "pnpm@10.14.0"
}
```

This is the default way to manage version for pnpm and Yarn when a new project is initialized. It will define the version used for dependency installation during the build phase and in run command. Yarn `1.22.22` remains the default system version included for legacy reasons.

* If `CC_NODE_BUILD_TOOL` is set to `yarn-berry`, the latest 4.x packaged version of Yarn becomes the system default
* If you use Yarn 1.x or Yarn 2.x, a deprecation warning is displayed during deployment as they're not maintained anymore

> [!TIP]
> If you set `CC_NODE_BUILD_TOOL` to `yarn-berry` in any Clever Cloud runtime, Yarn 4.x becomes the default system version.

## Development Dependencies

Development dependencies aren't automatically installed during the deployment. You can control their installation setting `CC_NODE_DEV_DEPENDENCIES` environment variable to `install` or `ignore`. This variable overrides the default behavior of `NODE_ENV`.

Here are various scenarios:

* `CC_NODE_DEV_DEPENDENCIES=install`: Development dependencies are installed.
* `CC_NODE_DEV_DEPENDENCIES=ignore`: Development dependencies aren't installed.
* `NODE_ENV=production` and `CC_NODE_DEV_DEPENDENCIES=install`: Development dependencies are installed.
* `NODE_ENV=production` and `CC_NODE_DEV_DEPENDENCIES=ignore`: Development dependencies aren't installed.
* `NODE_ENV=production`: Package manager (npm/yarn) default behavior. Development dependencies aren't installed.
* Neither `NODE_ENV` nor `CC_NODE_DEV_DEPENDENCIES` are defined: Package manager (npm/yarn) default behavior. Development dependencies are installed.

## Use private repositories

### With NPM_TOKEN

Since April 2015, `npm` allows you to have private repositories. If you want to use such a feature, you only need to provide the auth token. Add it to your application through the `NPM_TOKEN` environment variable:

```bash
NPM_TOKEN="00000000-0000-0000-0000-000000000000"
```

Then, the `.npmrc` file is created automatically for your application, with the registry URL and the token.

```txt
//registry.npmjs.org/:_authToken=00000000-0000-0000-0000-000000000000
```

### With CC_NPM_BASIC_AUTH

Or you can set `CC_NPM_BASIC_AUTH` to use basic authentication

```bash
CC_NPM_BASIC_AUTH="user:password"
```

### Define the host

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

You can use the [X-Forwarded-Proto header](/doc/find-help/faq#how-to-know-if-a-user-comes-from-a-secure-connection) to enable it.

If you are using [Express.js](https://expressjs.com/), you can use [express-sslify](https://www.npmjs.com/package/express-sslify) by adding:

```javascript
app.use(enforce.HTTPS({
  trustProtoHeader: true
}));
```

{{% content "new-relic" %}}

## Troubleshooting your application

If you are often experiencing auto restart of your Node.js instance, maybe you have an application crashing that we automatically restart.
To target this behavior, you can gracefully shut down with events handlers on `uncaughtExeption` `unhandledRejection` `sigint` and `sigterm` and log at this moment, so you can fix the problem.

{{% content "env-injection" %}}

To access environment variables from your code, you can use `process.env.MY_VARIABLE`.

{{% content "deploy-git" %}}

{{% content "link-addon" %}}

{{% content "more-config" %}}

{{% content "url_healthcheck" %}}
