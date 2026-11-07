---
type: docs
linkTitle: Meteor.js
title: Meteor.js application runtime
description: Build and deploy Meteor.js applications on Clever Cloud, with the Meteor version of your project, Node.js, and a MongoDB database
keywords:
- meteor
- meteor.js
- javascript framework
- full-stack framework
- mongodb
- node.js
- real-time applications
aliases:
- /deploy/application/javascript/by-framework/meteor
- /doc/applications/javascript/by-framework/meteor
- /doc/applications/javascript/meteor
- /doc/applications/meteor
- /doc/nodejs/meteor
---

## Overview

[Meteor](https://www.meteor.com) is a full-stack JavaScript framework that runs on Node.js and stores its data in MongoDB. Clever Cloud installs the Meteor version of your project, builds a server bundle with `meteor build`, and starts it with Node.js.

## Create your Meteor.js application

To create a new Meteor.js application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type meteor
```

Use the `meteor` type: a [Node.js application](/doc/deploy/applications/nodejs/) doesn't build Meteor projects, it only logs a warning when it finds a `.meteor` folder. To move such an application to the Meteor runtime, deploy your code to a new Meteor.js application.

- [Learn more about Clever Tools](/doc/tools/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

## Configure your Meteor.js application

### Mandatory needs

A Meteor.js application needs:

- The `.meteor` folder and `package.json` file, at the root of the project or of the folder set in `APP_FOLDER`
- The Node.js version of your Meteor release, set in [`engines.node`](#nodejs-version)
- A MongoDB database, set in `MONGO_URL`
- The URL of your application, set in `ROOT_URL`

`meteor create` creates these files. In the `.meteor` folder, the `release` file sets the Meteor version that Clever Cloud installs. `package.json` lists the npm packages, the libraries, of your project.

Meteor listens on [the port in `PORT`](/doc/manage/#listen-on-the-right-port), on every interface: you have nothing to set.

### Connect a MongoDB database

On your computer, `meteor run` starts its own MongoDB database. In production, Meteor reads the URL of its database in `MONGO_URL`.

Create a [MongoDB add-on](/doc/deploy/databases/mongodb/), link it to your application, and show the variables it provides:

```bash
clever addon create mongodb-addon my-meteor-db --plan xs_sml
clever service link-addon my-meteor-db
clever env
```

Copy the value of `MONGODB_ADDON_URI` into `MONGO_URL`, the add-on doesn't set it:

```bash
clever env set MONGO_URL "mongodb://user:password@host:port/database"
```

Then set `ROOT_URL` to the URL of your application, which Meteor uses to build absolute URLs. `clever domain` lists its domain names:

```bash
clever domain
clever env set ROOT_URL https://my-meteor-app.cleverapps.io
```

### Build phase

On a new build, Clever Cloud installs the Meteor version set in `.meteor/release`, then the dependencies of your project. It then builds the bundle, the production version of your application, in the `.build` folder, and installs its dependencies:

```bash
npm install --no-progress
meteor build .build --architecture os.linux.x86_64 --server-only --directory
cd .build/bundle/programs/server && npm install --no-progress
```

Clever Cloud uses npm by default. To use another package manager, such as pnpm or Yarn, see the [Node.js page](/doc/deploy/applications/nodejs/).

Building a Meteor application needs a lot of memory. If the build stops with `Killed`, as it does for a new Meteor 3 project on an `XS` instance, enable a [dedicated build instance](/doc/manage/#dedicated-build-instance), of size `M` or larger:

```bash
clever scale --build-flavor M
```

### Node.js version

Each Meteor release runs on a given Node.js version. To find it, run in your project:

```bash
meteor node -v
```

Add its major version to your `package.json` file, in an `engines` section, here when `meteor node -v` shows a `20.x` version:

```json {filename="package.json"}
{
  "engines": {
    "node": "^20"
  }
}
```

Clever Cloud uses the Node.js version of the image if it matches, otherwise it installs the most recent one that matches, as on the [Node.js runtime](/doc/deploy/applications/nodejs/#set-nodejs-version). Without `engines.node`, it uses `CC_NODE_VERSION`, or the version of the image, which may not suit your Meteor release.

### Meteor settings

If your application reads its settings with [`Meteor.settings`](https://docs.meteor.com/api/meteor.html#Meteor-settings), from a `settings.json` file, set its content in `METEOR_SETTINGS`:

```bash
clever env set METEOR_SETTINGS "$(cat settings.json)"
```

Meteor sends the `public` part of these settings to the browser: keep your secrets out of it.

### Start command

Clever Cloud starts the bundle with `node .build/bundle/main.js`. It ignores the `start` script of `package.json`, which usually runs `meteor run`, a development server. If `NODE_OPTIONS` doesn't set `--max-old-space-size`, Clever Cloud adds it, so that the JavaScript heap of Node.js can use three quarters of the memory of the instance.

To pass arguments to your application, set `CC_RUN_COMMAND`. It runs from the root of the repository:

```bash
clever env set CC_RUN_COMMAND "node .build/bundle/main.js --my-option"
```

With `APP_FOLDER`, start the path of the bundle with this folder.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps Meteor and the npm cache between commits, to avoid downloading them again.

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/databases/mongodb" title="MongoDB" subtitle="Create and manage the database of your application" icon="simple:mongodb" >}}
  {{< card link="/developers/doc/deploy/applications/nodejs" title="Node.js" subtitle="Package managers, Node.js versions, and build options" icon="simple:nodedotjs" >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
