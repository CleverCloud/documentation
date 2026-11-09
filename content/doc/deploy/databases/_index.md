---
type: docs
linkTitle: Databases
title: Databases
description: Create managed or serverless databases on Clever Cloud, link them to your applications, and delete them
keywords:
- databases
- managed databases
- sql
- nosql
- key-value
- search
aliases:
- /doc/addons/add-an-addon
- /doc/addons/couchbase/
- /doc/databases
- /doc/databases-and-services/couchbase
- /doc/getting-started/dbaas
---

Clever Cloud runs your databases as add-ons, next to your applications. Each one gives the applications you link to it its credentials in environment variables, so that your code holds no password.

PostgreSQL, MySQL, MongoDB, Redis, and Elastic Stack run on instances you size, with backups and monitoring, and you choose when to [migrate](/doc/develop/database-migration/) one to a new version, plan, or region. Materia databases are serverless, and replicate each write across three data centers.

## Relational databases

Store structured data with SQL, transactions, and joins.

{{< cards cols="2" >}}
  {{< card link="/developers/doc/deploy/databases/postgresql" title="PostgreSQL" subtitle="Managed object-relational database" icon="simple:postgresql" >}}
  {{< card link="/developers/doc/deploy/databases/mysql" title="MySQL" subtitle="Managed relational database" icon="mysql" >}}
{{< /cards >}}

## Key-value stores and caches

Keep sessions, caches, and counters: in memory with Redis, or in Materia KV, a serverless store compatible with Redis.

{{< cards cols="2" >}}
  {{< card link="/developers/doc/deploy/databases/redis" title="Redis" subtitle="Managed key-value database" icon="redis" >}}
  {{< card link="/developers/doc/deploy/databases/materia-kv" title="Materia KV" subtitle="Serverless distributed key-value database" icon="materia" tag="Beta" >}}
{{< /cards >}}

## Documents, search, and time series

Store JSON documents, index text for search and logs, or record metrics over time.

{{< cards >}}
  {{< card link="/developers/doc/deploy/databases/mongodb" title="MongoDB" subtitle="Managed NoSQL document database" icon="simple:mongodb" >}}
  {{< card link="/developers/doc/deploy/databases/elastic" title="Elastic Stack" subtitle="Managed search and analytics engine" icon="elastic" >}}
  {{< card link="/developers/doc/deploy/databases/materia-ts" title="Materia TS" subtitle="Serverless distributed time-series database" icon="materia" tag="Private access" >}}
{{< /cards >}}

## Create a database

In the [Console](https://console.clever-cloud.com/), select **Create** at the top of the sidebar, then **Add-on**, and pick a database. Choose its plan, its region, its name, and the applications to link it to. With [Clever Tools](/doc/tools/cli/addons/), create the add-on and link it to an application in one command:

```bash
clever addon create postgresql-addon my-database --plan dev --link my-app
```

Linking a database gives the application its credentials in [environment variables](/doc/manage/environment-variables/), such as `POSTGRESQL_ADDON_URI`: restart the application to read them. To link an existing database, use the **Service dependencies** menu of the application, as [Service dependencies](/doc/manage/service-dependencies/#link-a-service) explains.

Free plans, such as `dev`, are for tests, not for production: they run on shared resources, with variable performance, and may not run the same version as dedicated plans. [Consumption](/doc/account-billing/consumption/) explains how Clever Cloud bills the other plans.

## Delete a database

Select **Delete the add-on** in the danger zone of the **Dashboard** of the add-on, or **Remove add-on** in its **Information** menu. With Clever Tools:

```bash
clever addon delete my-database
```
