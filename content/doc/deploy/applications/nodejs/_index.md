---
type: docs
linkTitle: Node.js & Bun
title: Node.js application runtime
description: Build and deploy Node.js applications on Clever Cloud with npm, pnpm, or Yarn, from JavaScript or TypeScript, with the Node.js version of your choice
keywords:
- bun
- express
- javascript
- nodejs app hosting
- nodejs cloud
- npm
- package.json
- pnpm
- typescript
- yarn
aliases:
- /applications/javascript/nodejs
- /deploy/application/javascript/by-framework/nodejs
- /doc/applications/javascript
- /doc/applications/javascript/by-framework/nodejs
- /doc/applications/javascript/nodejs
- /doc/applications/nodejs
- /doc/applications/nodejs/custom-run-command
- /doc/deploy/application/javascript
- /doc/deploy/application/javascript/by-framework/meteor
- /doc/deploy/application/javascript/by-framework/nodejs
- /doc/deploy/application/javascript/nodejs
- /doc/deploy/application/node
- /doc/deploy/application/nodejs
- /doc/deploy/application/nodejs/nodejs
- /doc/getting-started/by-language/node
- /doc/nodejs
- /doc/nodejs-hosting
- /doc/nodejs/nodejs
- /doc/partials/language-specific-deploy/node
- /nodejs/nodejs/
- /getting-started/by-language/node
---

## Overview

[Node.js](https://nodejs.org) is a JavaScript runtime, which also runs TypeScript. Clever Cloud installs the dependencies of your project with npm, pnpm, or Yarn, then starts it from its `package.json` file. It works with frameworks such as [Express](https://expressjs.com), [Hono](https://hono.dev), or [NestJS](https://nestjs.com).

[Bun](https://bun.com) is another JavaScript runtime, compatible with Node.js, and a package manager. When it finds a `bun.lock` file, Clever Cloud installs and starts your project with Bun, as the [Bun page](/doc/deploy/applications/nodejs/bun/) explains. For Meteor, see the [Meteor.js page](/doc/deploy/applications/meteor/).

## Create your Node.js application

To create a new Node.js application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type node
```

The [getting started guide](/doc/getting-started/) describes each step of the creation of an application.

## Configure your Node.js application

### Mandatory needs

A Node.js application needs:

- A `package.json` file, at the root of the project or of the folder set in `CC_APP_FOLDER`
- A start script or a `main` field in this file, to [start your application](#start-command)
- A web server listening on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port)

The `package.json` file describes your project: its dependencies, its scripts, and the Node.js version it needs. The lock file of your package manager, such as `package-lock.json` for npm, sets the exact version of each dependency. Commit it, and add `node_modules/` to your `.gitignore` file: Clever Cloud installs these dependencies itself, during the build.

For instance, a minimal [Express](https://expressjs.com) application:

```json {filename="package.json"}
{
  "name": "hello",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^5.3.0"
  }
}
```

```js {filename="server.js"}
import express from 'express';

const app = express();

app.get('/', (req, res) => {
  res.send('Hello from Node.js on Clever Cloud');
});

app.listen(process.env.PORT ?? 8080, '0.0.0.0');
```

To try it locally, run `npm install`, then `npm start`: it listens on port 8080. A [Clever Task](#nodejs-applications-as-clever-tasks) doesn't need a web server.

### About package.json

Clever Cloud reads these fields of your `package.json` file:

- `dependencies` and `devDependencies`: the packages to install, as [development dependencies](#development-dependencies) explains
- `engines.node`: the [Node.js version](#set-nodejs-version), when `CC_NODE_VERSION` isn't set
- `main`: the file that `node` starts, when there's no start script
- `packageManager`: the version of [pnpm or Yarn](#pnpm-and-yarn)
- `scripts.start`: the command that starts your application

Without a start script or a `main` field, the deployment logs `Error: No main or start script`, then fails when the [health check](/doc/manage/healthcheck/) times out.

npm also runs the [lifecycle scripts](https://docs.npmjs.com/cli/using-npm/scripts) of your project, such as `postinstall` after the installation, and `prestart` before `npm start`.

### Build phase

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/), then installs the dependencies with the package manager of the first lock file it finds:

1. `yarn.lock`: [Yarn](#pnpm-and-yarn), with `yarn install`
2. `pnpm-lock.yaml`: [pnpm](#pnpm-and-yarn), with `pnpm install --prod`
3. `bun.lock`: [Bun](/doc/deploy/applications/nodejs/bun/), with `bun install --omit dev`

Without any of them, Clever Cloud runs `npm install`.

Clever Cloud doesn't run your `build` script. To build your application, such as to compile TypeScript, run it in the post-build hook:

```bash
clever env set CC_POST_BUILD_HOOK "npm run build"
```

A hook runs from the root of your repository: with `CC_APP_FOLDER`, start it with `cd` to this folder.

Build tools, such as `tsc` or Vite, are often development dependencies, which pnpm and Bun skip, as well as npm and Yarn 1 with `NODE_ENV=production`. To build your application, [install them](#development-dependencies).

### Package managers

To choose the package manager or the command that installs the dependencies, set `CC_NODE_BUILD_TOOL`:

- `bun`: [Bun](/doc/deploy/applications/nodejs/bun/), which also starts your application
- `custom`: the command set in `CC_CUSTOM_BUILD_TOOL`
- `npm` or `npm-install`: `npm install`, the default
- `npm-ci`: `npm ci`, which installs the versions of `package-lock.json`
- `pnpm`: `pnpm install --prod`, which also starts your application
- `yarn-berry`: `yarn install`, which also starts your application

This setting takes precedence over the lock files. A custom command can chain the installation and the build:

```bash
clever env set CC_NODE_BUILD_TOOL custom
clever env set CC_CUSTOM_BUILD_TOOL "npm ci --include=dev && npm run build"
```

The `yarn` and `yarn2` values select Yarn 1 and Yarn 2, which their developers no longer maintain: the deployment logs a warning.

### pnpm and Yarn

Clever Cloud installs pnpm, and Yarn 3 or 4, with [Corepack](https://github.com/nodejs/corepack), which sets their version from the `packageManager` field:

```json {filename="package.json"}
{
  "packageManager": "pnpm@12.21.0"
}
```

With a `yarn.lock` file, Clever Cloud uses Yarn 1, unless this field sets Yarn 3 or 4, such as `yarn@4.19.0`, whose Plug'n'Play mode works.

### TypeScript

Starting with version 22.18, Node.js runs TypeScript files, after removing their types. Start a file of your project with `node`, without a build:

```json {filename="package.json"}
{
  "scripts": {
    "start": "node src/server.ts"
  }
}
```

This mode only supports the [TypeScript syntax it can erase](https://nodejs.org/api/typescript.html), such as types. For an `enum` or a `namespace`, compile your project with [TypeScript](https://www.typescriptlang.org): run `tsc` in the [post-build hook](#build-phase), then start the file it writes, such as `node dist/server.js`.

The `paths` aliases of `tsconfig.json` need a bundler. [Bun](/doc/deploy/applications/nodejs/bun/) runs TypeScript without these limits, and without a build. [Mise](/doc/manage/mise/) also lets you install [Deno](https://deno.com), another TypeScript runtime. Use it to run an application on the [Linux runtime](/doc/deploy/applications/linux/) or to build a static site, as in the [Lume guide](/guides/static-sites/lume/).

### Node.js version {#set-nodejs-version}

Each image includes a Node.js version installed with `nvm`: the latest long-term support (LTS) release when Clever Cloud built the image. Your application uses it when it doesn't request another version.

{{< runtimes_versions node >}}

To request a version, set `CC_NODE_VERSION`, as Clever Cloud ignores and deletes `.nvmrc` files. It accepts a version or a [semantic versioning range](https://github.com/npm/node-semver#ranges), such as `26`, `24.22`, `24.22.2`, or `>=24`. A partial version is a range: `26` matches any 26.x release, `24.22` any 24.22.x release.

During the build phase, Clever Cloud resolves the requested version in this order:

1. If the version included in the image matches the request, your application uses it
2. Otherwise, Clever Cloud installs with `nvm` the latest Node.js release that matches the request
3. If no release matches, the deployment fails

For example, with Node.js 26.13.1 in the image, `26` and `>=24` both resolve to 26.13.1, while `24` installs the latest 24.x release. An open range such as `>=24` doesn't select the latest release: it keeps the included version as long as this version matches.

Image updates can move the included version to a new patch release or LTS branch: set a major version, such as `26`, to stay on one.

Without `CC_NODE_VERSION`, Clever Cloud reads the `engines.node` field of your `package.json`, with the same rules. Prefer the variable: it makes the version you deploy explicit, while `engines.node` describes the versions your package supports.

### Start command

Clever Cloud starts your application from the folder of your project, with the first of these commands that applies:

1. `CC_RUN_COMMAND`, when you set it
2. `npm start`, which runs the start script of your `package.json` file
3. `node` and the file of the `main` field, such as `node server.js`

With pnpm, or Yarn 3 or 4, Clever Cloud runs the start script or the `main` file through them, such as `pnpm start` or `yarn node server.js`.

### Memory

Clever Cloud sets the heap size of Node.js to three quarters of the memory available to your application, such as 644 MB on `XS`. It adds this `--max-old-space-size` option to the `NODE_OPTIONS` you set, unless your value already holds one.

To set your own value, put `--` before it, so that Clever Tools doesn't read it as an option:

```bash
clever env set NODE_OPTIONS -- "--max-old-space-size=512"
```

### Development dependencies

Clever Cloud doesn't set `NODE_ENV`. Set it to `production`, which most frameworks, such as Express, expect in production. With this value, npm and Yarn 1 skip the `devDependencies` of your project, while pnpm always skips them. Yarn 3 and 4 install them.

To install them, such as for a build tool, set `CC_NODE_DEV_DEPENDENCIES=install`. Clever Cloud then adds the matching option to the command: `--production=false` for npm and Yarn 1, `--include=dev` for `npm ci`, and `--no-prod` for pnpm.

### Private registries

To install private packages, set your access token in `NPM_TOKEN`: Clever Cloud writes it to `~/.npmrc`, for the host in `CC_NPM_REGISTRY`. Set it to `github` for GitHub Packages, or to the host of another registry, instead of `registry.npmjs.org`.

```bash
clever env set CC_NPM_REGISTRY github
clever env set NPM_TOKEN "<your-token>"
```

npm then still installs the other packages from `registry.npmjs.org`. GitHub Packages only hosts scoped packages: map your scope to it in a `.npmrc` file of your project, as for any scope of another registry:

```ini {filename=".npmrc"}
@my-organisation:registry=https://npm.pkg.github.com
```

Instead of a token, `CC_NPM_BASIC_AUTH` sets a user and a password, such as `user:password`, for the registry host. Clever Cloud then makes it the default registry of npm. Use either `NPM_TOKEN` or `CC_NPM_BASIC_AUTH`: the deployment fails with both.

For dependencies on private Git repositories, add a [private SSH key](/doc/manage/#private-ssh-key) to your application.

### Client address and protocol

The requests that reach your application come from the [load balancers](/doc/network/load-balancers/), which set the address of the client in their headers. To read it with Express, trust the addresses that `CC_REVERSE_PROXY_IPS` lists, and `127.0.0.1` for [Request Flow](/doc/manage/request-flow/):

```js {filename="server.js"}
const proxies = (process.env.CC_REVERSE_PROXY_IPS ?? '').split(',').filter(Boolean);
app.set('trust proxy', ['loopback', ...proxies]);
```

`req.ip` then holds the address of the client. Don't rely on `req.protocol` and `req.hostname`: a client can set them with its own headers.

With [Force HTTPS](/doc/manage/#force-https), enabled by default, every request came over HTTPS. Without it, [get the protocol](/doc/network/load-balancers/#get-the-protocol) from the `Forwarded` header.

### Environment variables

Your application reads its [environment variables](/doc/manage/environment-variables/) with `process.env.MY_VARIABLE`, such as the credentials of linked add-ons. They exist during the build too, for your hooks and the scripts of your `package.json` file.

### Monitoring

To monitor your application with the agent of a service, such as [New Relic](/doc/observability/new-relic/), add it to the dependencies of your project.

To send traces to an [OpenTelemetry](https://opentelemetry.io/docs/zero-code/js/) collector, add its packages, then load them in your start script. Don't load them in `NODE_OPTIONS`: this variable also applies to the build, which then fails before their installation:

```json {filename="package.json"}
{
  "scripts": {
    "start": "node --require @opentelemetry/auto-instrumentations-node/register server.js"
  }
}
```

```bash
npm install @opentelemetry/api @opentelemetry/auto-instrumentations-node
clever env set OTEL_SERVICE_NAME my-application
clever env set OTEL_EXPORTER_OTLP_ENDPOINT https://collector.example.com
```

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps the packages that your package manager downloads between commits: `~/.npm` for npm, `~/.cache/pnpm` for pnpm, and `~/.cache/yarn` for Yarn 1. The build cache already holds the packages of Yarn 3 and 4.

## Node.js applications as Clever Tasks

A Node.js application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration. Clever Cloud installs its dependencies, then runs `CC_RUN_COMMAND` from the folder of your project, instead of starting a web server. The task stops when this command ends.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks):

```bash
clever create --type node --task "node migrate.js"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/nodejs/bun" title="Bun" subtitle="Install the dependencies and start your application with Bun" icon="simple:bun" >}}
{{< /cards >}}
