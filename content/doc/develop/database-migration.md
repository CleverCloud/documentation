---
type: docs
linkTitle: Migrate/Update Database
title: Migrate/Update Database
description: Migrate a database add-on on Clever Cloud to apply security updates, change its plan, upgrade its version, or move it to another region, while it keeps its data and its ID
keywords:
- database migration
- database upgrade
- postgresql mysql mongodb
- redis elasticsearch
- major version upgrade
- plan change
aliases:
- /doc/manage/database-migration
- /doc/administrate/database-migration
- /doc/database-migration
---

{{< hextra/hero-subtitle style="margin:.3rem 0 2rem 0">}}
  Move a database add-on to a new server, to update it, resize it, or upgrade its version, without losing its data.
{{< /hextra/hero-subtitle >}}

Database add-ons run on immutable virtual machines: Clever Cloud never updates a running server. A migration creates a new server with an updated system and database, copies your data, then switches the add-on to it. The add-on keeps its ID, and its applications get its new settings.

Migrate a database to:

- Apply the security updates of its system and database, with the same plan, version, and region
- Change its plan, such as from a `DEV` plan to a dedicated one, or to a larger size
- Upgrade its version, such as from PostgreSQL 17 to PostgreSQL 18
- Move it to another region

The PostgreSQL, MySQL, MongoDB, Redis, and Elasticsearch add-ons support migrations.

## What changes

On a dedicated plan, the database name, the user, and the password stay the same, and so do the host name and the port. The direct connection settings, such as `POSTGRESQL_ADDON_DIRECT_HOST`, change with the server. If the add-on only offers direct access, its host name and port change too. The version variable changes when you upgrade the version.

From a shared plan, such as `DEV`, the host name, the port, and the database name change, but the user and the password stay the same.

At the end of the migration, Clever Cloud updates the environment variables of the add-on, and redeploys the running applications linked to it, so they connect to the new server. Update any setting that you copied elsewhere instead of reading these variables.

## During the migration

The database is read-only from the start of the migration until its end: your applications can read data, but writes fail. On PostgreSQL, the migration also closes the open connections. At the end, the switch to the new server briefly interrupts all connections. Redis is the exception: it copies the data by replication, and only pauses the clients during the switch.

The duration depends on the size of the database: a small one can migrate in less than a minute, and a large one takes much longer. Plan the migration at a time of low traffic for your applications.

How each add-on copies its data:

| Add-on        | Copy                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------ |
| PostgreSQL    | Dump and restore of the database                                                           |
| MySQL         | Dump and restore of the database, with its routines and events                             |
| MongoDB       | Dump and restore of the database                                                           |
| Redis         | Replication to the new server, then a switch; always to the version Clever Cloud provides  |
| Elasticsearch | Snapshot and restore of the indexes; a migration can't change the major version            |

### Users and extensions

When the target plan is dedicated, the migration creates the read-only users of PostgreSQL, MySQL, and MongoDB again on the new server. For PostgreSQL, it also brings the users managed from the Console, with their privileges.

PostgreSQL extensions come with the dump. Some don't exist anymore in recent versions, and the migration removes them first. The Console lists them before you confirm: if objects of your database depend on one of them, the migration can't remove it and fails.

## Migrate from the Console

{{% steps %}}

### Open the Migrate / Upgrade menu

In the Console, open the add-on, then its **Migrate / Upgrade** menu. Read the warning on the read-only mode and on the connection settings, then click **Migration settings** to choose the target.

### Choose the target

Select the plan, the version, and the region of the database. The Console offers the plans at the same price or higher: to move to a smaller plan, contact [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice). Then, click **Migrate the database**.

### Confirm

The summary lists the target plan and version, the linked applications, and the PostgreSQL extensions to remove. Check that your applications support the new version, then click **Start the migration**.

### Follow the migration

The Console shows each step of the migration, with its status. While the data is copied, **Abort migration** asks to stop the migration, and Clever Cloud tries to roll it back as after a failure, then shows the result.

{{% /steps %}}

## Migrate with the API

Clever Tools has no migration command, but `clever curl` calls the API with your credentials. Get the ID of the target plan from the add-on provider, such as `postgresql-addon`, then start the migration with the plan, the region, and the version. Replace `<orgID>` and `<addonID>` with the IDs of your organisation and of the add-on, shown in the Console:

```bash
clever curl -s https://api.clever-cloud.com/v2/products/addonproviders/postgresql-addon | jq -r '.plans[] | "\(.slug) \(.id)"'

clever curl -s -X POST -H "Content-Type: application/json" \
  -d '{"planId":"plan_xxx","region":"par","version":"18"}' \
  "https://api.clever-cloud.com/v2/organisations/<orgID>/addons/<addonID>/migrations"
```

The answer gives the `migrationId` of the migration. Follow its status and its steps with a `GET` request on `…/migrations/<migrationId>`, until the status is `OK`, or `RECOVERED` or `FAILED` [if it fails](#if-the-migration-fails).

## If the migration fails

When a step fails, Clever Cloud tries to roll the migration back. If it succeeds, the database gets its write permissions back and keeps its data, plan, and version. The Console shows the failed step and its output, with a **Contact support** button.

If the rollback fails too, the migration ends as failed. In both cases, contact [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) with the ID of the add-on and the ID of the migration, so they can check its state and help you to complete it.
