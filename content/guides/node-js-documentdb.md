---
type: docs
linkTitle: Node.js & DocumentDB
title: Deploy a Node.js application with DocumentDB on PostgreSQL
description: Deploy an Express application that stores documents through the MongoDB driver in a PostgreSQL add-on with the DocumentDB option, with a private sandbox per visitor
keywords:
- Node.js
- documentdb
- mongodb compatible
- postgresql
- javascript
- database tutorial
---

{{< hextra/hero-subtitle >}}
  Deploy a sticky notes board that writes documents with the MongoDB driver into a PostgreSQL add-on
{{< /hextra/hero-subtitle >}}

This guide uses the [Clever Cloud DocumentDB demo](https://github.com/CleverCloud/demo-documentdb), a sticky notes board built with Express and the official `mongodb` driver. Each visitor gets a private sandbox identified by a cookie, adds coloured notes, and can reset the sandbox with one button. The application reads its connection string from `DOCUMENTDB_ADDON_URI`, which Clever Cloud injects when a PostgreSQL add-on created with the [DocumentDB option](/doc/deploy/databases/documentdb) is linked.

## Prerequisites

- A [Clever Cloud account](https://console.clever-cloud.com)
- [Git](https://git-scm.com/downloads)
- [Clever Tools](/doc/manage/cli), installed and connected to your account

## Clone the example application

Clone the repository and move into its directory:

```bash
git clone https://github.com/CleverCloud/demo-documentdb
cd demo-documentdb
```

The application has no build step. `server.js` connects to the endpoint, creates a TTL index that removes notes after 24 hours, and exposes a small JSON API. The `public` directory holds the board.

## Create the application and database

Create a Node.js application:

```bash
clever create -t node demo-documentdb
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` when you create the application.

You can display your application's URL or add a custom domain. A custom domain also requires DNS configuration:

```bash
clever domain
clever domain add your.website.tld
```

Create a PostgreSQL add-on with the DocumentDB option and link it to the application. The option requires a dedicated plan and PostgreSQL 17 or later:

```bash
clever addon create postgresql-addon demo-documentdb --plan xxs_sml --addon-version 18 --option documentdb=true --link demo-documentdb
```

Linking the add-on injects its [environment variables](/doc/develop/common-configuration/environment-variables/#how-are-variables-defined) into the application, including `DOCUMENTDB_ADDON_URI`. If you already have an add-on with the option, link it instead:

```bash
clever service link-addon demo-documentdb
```

## Deploy the application

The repository already contains the `start` script and listens on the port provided by Clever Cloud. Deploy it without additional configuration:

```bash
clever deploy
clever open
```

Add a few notes, delete one, and press **Reset my sandbox**. Notes are documents of the `notes` collection, stored in your PostgreSQL database, and survive application restarts and deployments. Open the page in another browser to get a separate sandbox with its own notes.

The MongoDB-compatible endpoint appears in the add-on environment a few seconds after its creation. If the first deployment fails because `DOCUMENTDB_ADDON_URI` isn't set yet, restart the application with `clever restart`.

## How the application uses DocumentDB

The server connects once at startup with the TLS options the endpoint requires, then creates the indexes it needs:

```javascript
const client = new MongoClient(process.env.DOCUMENTDB_ADDON_URI, { tls: true, tlsAllowInvalidCertificates: true });
await client.connect();
const notes = client.db().collection('notes');
await notes.createIndex({ createdAt: 1 }, { expireAfterSeconds: 24 * 60 * 60 });
```

Every document carries the sandbox id of its author, so each API route filters on it. The reset button calls `deleteMany({ sandbox })`, and the counters displayed on the board come from an aggregation pipeline:

```javascript
await notes.aggregate([
  { $match: { sandbox: req.sandbox } },
  { $group: { _id: '$color', count: { $sum: 1 } } },
  { $sort: { _id: 1 } },
]).toArray();
```

To look at the same documents from SQL, connect with `psql` to `POSTGRESQL_ADDON_URI` and query the collection, as described in the [DocumentDB documentation](/doc/deploy/databases/documentdb#query-your-documents-from-sql).

## Run the application locally

Load the environment variables of the linked application in your shell, then start the server:

```bash
eval "$(clever env -F shell)"
npm install
npm start
```

The board is available on `http://localhost:8080` and uses the same add-on as the deployed application.

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/deploy/databases/documentdb" title="DocumentDB option" subtitle="Compatibility, connection and backups" icon="database" >}}
  {{< card link="/developers/doc/deploy/applications/nodejs" title="Node.js applications" subtitle="Configure and deploy Node.js applications" icon="node" >}}
  {{< card link="/developers/doc/deploy/databases/postgresql" title="PostgreSQL add-on" subtitle="Plans, backups and extensions" icon="database" >}}
{{< /cards >}}
