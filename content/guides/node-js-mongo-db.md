---
type: docs
linkTitle: Node.js & MongoDB
title: Deploy a Node.js application with MongoDB
description: Deploy an Express.js application connected to a MongoDB database, with automatic environment variable injection
keywords:
- Node.js
- mongodb
- javascript
- database tutorial
- web application
aliases:
- /doc/deploy/application/javascript/tutorials/node-js-mongo-db
- /doc/nodejs/nodejs-mongodb-sample-app
---

{{< hextra/hero-subtitle >}}
  Deploy an Express.js application backed by a MongoDB database and verify data persistence
{{< /hextra/hero-subtitle >}}

This guide uses a [Clever Cloud example application](https://github.com/CleverCloud/demo-nodejs-mongodb-rest) where you can create and delete values. The application reads its connection string from `MONGODB_ADDON_URI`, which Clever Cloud injects when a MongoDB add-on is linked.

## Prerequisites

- A [Clever Cloud account](https://console.clever-cloud.com)
- [Git](https://git-scm.com/downloads)
- [Clever Tools](/doc/cli), installed and connected to your account

## Clone the example application

Clone the repository and move into its directory:

```bash
git clone https://github.com/CleverCloud/demo-nodejs-mongodb-rest myNodeMongoApp
cd myNodeMongoApp
```

## Create the application and database

Create a Node.js application with the `myNodeApp` alias:

```bash
clever create -t node -a myNodeApp
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

You can display your application’s URL or add a custom domain. A custom domain also requires DNS configuration:

```bash
clever domain
clever domain add your.website.tld
```

Create a MongoDB add-on and link it to the application:

```bash
clever addon create mongodb-addon myMongoDb -p xs_sml -l myNodeApp
```

Linking the add-on injects its [environment variables](/doc/develop/env-variables/#how-are-variables-defined), including `MONGODB_ADDON_URI`, into the application. If you already have a MongoDB add-on, link it instead:

```bash
clever addon link myMongoDb
```

## Deploy the application

The example repository already contains the `start` script and listens on the port provided by Clever Cloud. Deploy it without additional configuration:

```bash
clever deploy
clever open
```

Add and delete a value from the displayed page to verify the database connection. Values are stored in MongoDB and remain available across application restarts and deployments.

## MongoDB compatibility

Clever Cloud provides MongoDB 4.0.3, the last release under the GNU AGPL v3 licence. The example therefore uses Mongoose 6.x, whose bundled MongoDB driver supports this server version. Keep this compatibility constraint in mind when updating the application dependencies.

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/nodejs" title="Node.js applications" subtitle="Configure and deploy Node.js applications" icon="node" >}}
  {{< card link="/developers/doc/addons/mongodb" title="MongoDB add-on" subtitle="Manage MongoDB databases" icon="database" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://mongoosejs.com/docs/compatibility.html" title="Mongoose compatibility" subtitle="Check MongoDB server compatibility" icon="external-link" >}}
{{< /cards >}}
