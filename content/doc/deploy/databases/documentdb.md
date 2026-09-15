---
type: docs
weight: 5
linkTitle: DocumentDB
title: DocumentDB, a MongoDB-compatible API on PostgreSQL
description: Enable the DocumentDB option on a PostgreSQL add-on to get a MongoDB-compatible endpoint, with the compatibility level, connection examples, clustering and backup details
keywords:
- documentdb
- mongodb compatible
- mongodb alternative
- document database
- nosql
- postgresql extension
- bson
---
## Overview

[DocumentDB](https://documentdb.io) is an open source document database built on PostgreSQL, published under the MIT licence and hosted by the Linux Foundation. A PostgreSQL extension adds a native BSON type and the operations a document store needs, while a gateway speaks the MongoDB wire protocol. Your MongoDB drivers, `mongosh` and existing code connect to the gateway, and PostgreSQL stores and queries the documents.

On Clever Cloud, DocumentDB is an option of the [PostgreSQL add-on](/doc/deploy/databases/postgresql). A single add-on then exposes two endpoints on the same data: the usual PostgreSQL endpoint and a MongoDB-compatible one. Collections live inside your PostgreSQL database, so the daily backups, monitoring, metrics and migration tooling of the add-on apply to them.

DocumentDB is the successor of the `ferretdb` option: FerretDB 2 already relied on the DocumentDB extension, and the native DocumentDB gateway replaces it with a wider compatibility. To move a FerretDB add-on to DocumentDB, migrate it to a new version from the Console or with Clever Tools.

## Create an add-on with DocumentDB

The option is available on dedicated PostgreSQL plans, from PostgreSQL 17. Choose it when you create the add-on: it can't be added to an existing database. The Console doesn't offer the option yet, so create the add-on with [Clever Tools](/doc/manage/cli) and pass `--option documentdb=true`:

```bash
clever addon create postgresql-addon myDocumentDB --plan xxs_sml --addon-version 18 --option documentdb=true
```

Add `--link myApp` to link the add-on to an application, and `--org` to target an organisation. The MongoDB-compatible endpoint takes a few seconds to appear once the add-on is created. Check it with `clever addon env` and the add-on ID displayed at creation:

```bash
clever addon env addon_2a4f8c1e-6b3d-4e7a-9f05-1c8d2e6b7a90
```

## Environment variables

Alongside the `POSTGRESQL_ADDON_*` variables, the add-on exposes these variables to the applications it's linked to:

| Variable                    | Description                                                                      |
| --------------------------- | -------------------------------------------------------------------------------- |
| `DOCUMENTDB_ADDON_HOST`     | Hostname of the MongoDB-compatible endpoint                                      |
| `DOCUMENTDB_ADDON_HOSTNAME` | Same hostname, available as soon as the add-on is created                        |
| `DOCUMENTDB_ADDON_PORT`     | Port of the MongoDB-compatible endpoint                                          |
| `DOCUMENTDB_ADDON_URI`      | Connection string, in the form `mongodb://user:password@host:port/database`      |

The Console displays these variables in the add-on information page, next to the PostgreSQL ones. The user, password and database are the ones of the PostgreSQL add-on: `POSTGRESQL_ADDON_USER`, `POSTGRESQL_ADDON_PASSWORD` and `POSTGRESQL_ADDON_DB`. Authentication uses `SCRAM-SHA-256`. If you [generate a direct access](/doc/deploy/databases/postgresql#direct-access) for the add-on, `DOCUMENTDB_ADDON_DIRECT_HOST`, `DOCUMENTDB_ADDON_DIRECT_PORT` and `DOCUMENTDB_ADDON_DIRECT_URI` appear too.

## Connect to the endpoint

> [!WARNING] TLS is mandatory
> The endpoint only accepts TLS connections and presents a certificate issued by Clever Cloud for the add-on hostname, which isn't part of the public certificate authorities. Enable TLS and skip certificate validation in your client, with the `tls=true&tlsAllowInvalidCertificates=true` connection string parameters or their driver equivalent.

{{< tabs >}}
  {{< tab name="mongosh" icon="mongo" >}}
  Connect with [mongosh](https://www.mongodb.com/docs/mongodb-shell/) and insert a first document:

  ```bash
  mongosh "$DOCUMENTDB_ADDON_URI" --tls --tlsAllowInvalidCertificates
  ```

  ```javascript
  db.cities.insertOne({ name: 'Nantes', population: 320000 })
  db.cities.find({ population: { $gt: 100000 } })
  ```

  {{< /tab >}}

  {{< tab name="Node.js" icon="node" >}}
  Install the official driver with `npm install mongodb`, then connect with the TLS options:

  ```javascript
  import { MongoClient } from 'mongodb';

  const client = new MongoClient(process.env.DOCUMENTDB_ADDON_URI, {
    tls: true,
    tlsAllowInvalidCertificates: true,
  });
  await client.connect();

  const cities = client.db().collection('cities');
  await cities.insertOne({ name: 'Nantes', population: 320000 });
  console.log(await cities.find({ population: { $gt: 100000 } }).toArray());
  await client.close();
  ```

  {{< /tab >}}

  {{< tab name="Python" icon="python" >}}
  Install [PyMongo](https://pymongo.readthedocs.io) with `pip install pymongo`, then connect with the TLS options:

  ```python
  import os
  from pymongo import MongoClient

  client = MongoClient(os.environ["DOCUMENTDB_ADDON_URI"], tls=True, tlsAllowInvalidCertificates=True)
  cities = client.get_default_database().cities
  cities.insert_one({"name": "Nantes", "population": 320000})
  print(list(cities.find({"population": {"$gt": 100000}})))
  ```

  {{< /tab >}}
{{< /tabs >}}

The [Node.js and DocumentDB guide](/guides/node-js-documentdb) deploys a complete application backed by this endpoint.

## MongoDB compatibility

The gateway announces itself as MongoDB 7.0 and implements wire protocol version 21. Drivers and tools released for MongoDB 5.0 and later connect to it: Clever Cloud validated `mongosh` 2.x, the Node.js driver 7.x and PyMongo 4.x. `db.version()` and `buildInfo` return `7.0.0`, and the `hello` command reports the DocumentDB engine version.

Compatibility covers the operations most applications rely on. Clever Cloud verified the following on the add-on:

- CRUD commands: `insert`, `find`, `update`, `delete`, `findAndModify`, `count`, `distinct` and bulk writes
- Aggregation pipelines, including `$group`, `$lookup`, `$facet`, `$unionWith`, `$merge` and `$out`
- Indexes: single field, compound, unique, partial, wildcard, TTL, text and `2dsphere`
- Multi-document transactions, with commit and rollback
- Several databases and collections per add-on, `renameCollection`, JSON schema validation
- GridFS
- Vector search through the `cosmosSearch` index type and the `$search` stage, for AI workloads

The following features aren't available:

- Change streams (`$changeStream`, `watch()`)
- Capped collections
- Collation on `find`
- User and role management: the add-on comes with one user, the PostgreSQL owner, which holds the `readWriteAnyDatabase` and `clusterAdmin` roles
- Server administration commands such as `serverStatus` or `replSetGetStatus`

The [DocumentDB reference](https://documentdb.io/docs/reference/) lists every supported command, operator and aggregation stage. Some behaviours also differ from MongoDB, for example the text of error messages. Test your application against the add-on before switching production traffic to it.

## Clustering and high availability

A DocumentDB endpoint runs on a single dedicated PostgreSQL server. The gateway presents itself to drivers as a standalone, writable node: there is no replica set to join, no election, and no sharding across servers. Don't set `replicaSet` in your connection string, and don't rely on the `shardCollection` family of commands, which the gateway lists but which has no effect on a single node.

Resilience comes from the PostgreSQL add-on itself. Data is written to a durable PostgreSQL database with daily backups and, on request, [point in time recovery](/doc/deploy/databases/postgresql#point-in-time-recovery). To scale, migrate the add-on to a bigger plan from the Console: the endpoint hostname, port and connection string stay the same after the migration.

Read replicas aren't available for the MongoDB-compatible endpoint. [PostgreSQL replicas](/doc/deploy/databases/postgresql#replication) only serve the SQL endpoint, and the gateway offers no read preference or secondary routing to drivers. If your workload needs read scaling or a failover target on the MongoDB side, contact [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) to discuss your needs.

## Query your documents from SQL

Documents are stored as BSON in your PostgreSQL database, in tables managed by the extension. Connect with `psql` to `POSTGRESQL_ADDON_URI` and read a collection with the `documentdb_api.collection()` function, converting documents to JSON on the way:

```sql
SELECT documentdb_core.bson_to_json_string(document) AS document
FROM documentdb_api.collection('your_database_name', 'cities');
```

The `documentdb_api_catalog.collections` table lists the collections of the database. Use this SQL access to inspect data, run analytics with PostgreSQL tools or join documents with relational tables. Keep writes on the MongoDB-compatible endpoint, so the gateway maintains indexes and catalog consistency.

## Backups and restore

Clever Cloud's daily backups of the add-on include your collections, their indexes, and the extension catalog. To take your own logical backup, run `pg_dump` with the add-on credentials and exclude the `cron` schema, which the extension owns and which a non-superuser dump can't read:

```bash
pg_dump -Fc --exclude-schema=cron "$POSTGRESQL_ADDON_URI" -f documentdb.dump
```

To restore a dump, create a fresh PostgreSQL add-on with the DocumentDB option and don't connect any MongoDB client to it before the restore ends. Run `pg_restore --no-owner` against the new `POSTGRESQL_ADDON_URI`, ignoring the errors about `CREATE EXTENSION` and grants to the previous user. The extension stores the name of each MongoDB database as data, and the default database takes the name of the PostgreSQL one, so update it to the new name once:

```sql
UPDATE documentdb_api_catalog.collections
SET database_name = 'new_postgresql_database_name'
WHERE database_name = 'old_postgresql_database_name';
```

Restoring into a PostgreSQL add-on created without the option isn't supported.

## Learn more

{{< cards >}}
  {{< card link="/developers/guides/node-js-documentdb" title="Node.js and DocumentDB guide" subtitle="Deploy a sticky notes application on the endpoint" icon="node" >}}
  {{< card link="/developers/doc/deploy/databases/postgresql" title="PostgreSQL add-on" subtitle="Plans, backups, replication and extensions" icon="database" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://documentdb.io/docs/" title="DocumentDB documentation" subtitle="Reference of supported commands and operators" icon="external-link" >}}
{{< /cards >}}
