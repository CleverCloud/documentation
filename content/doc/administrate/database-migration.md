---
type: docs
title: Database migration
description: How to migrate your database to improve performance or security
keywords:
- database
- dbaas
- migration
tags:
- administrate
type: docs
---

{{< hextra/hero-subtitle style="margin:.3rem 0 2rem 0">}}
  Clever Cloud features a simple, elegant way of migrating your databases to change the size of the instance, or improving its security by updating the middleware on it.
{{< /hextra/hero-subtitle >}}

## Migrating any database and updating its security

Our databases add-ons are deployed on immutable Virtual Machines. No updates are made on those VMs.
To improve security, you need to perform a "migration", which will boot a new VM with up-to-date system and database.
Unless you want to upgrade your database to a new major version or to give it more resources, you just have to perform a migration on the same zone, same plan and same major version.

These updates are not related to your add-on (PostgreSQL, MySQL…) major version. Only patches or minor versions of the add-on software along with system upgrades (security patches and new kernel features) are performed. For example, you can keep *PostgreSQL 11* if you want to.

{{< callout type="warning" >}}
We **do not** support the migration of read only users except for PostgreSQL add-ons. If you have any, you will have to create new ones at the end of the migration.
{{< /callout >}}

## Migration (updating) step-by-step

{{% steps %}}

### Go to your database menu

### Go to the *Migrate/Upgrade* section

You will see the disclaimer of the database migration assistant. It informs you that *your databse will be read-only during the migration process* and that the *hostname and database name will be automatically changed*.

Regarding this, we strongly recommend that you make sure every linked application uses the database add-on environment variables so those values will be automatically updated in your application.

### Click on *Migration Settings*

A menu will open, where you will see your current database informations.

Under you will see that you can select your new batabse size and pricing plan. Billing section in Summary will be edited accordingly.

Under **Targeted version** you can choose the desired database version.

Downgrading database is currently not supported, you can however ask [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice).

### Select *Migrate the Database*

You will be prompted to confirm the migration.

As soon as you do so, the database will be set in read-only mode and the migration process will start.

{{% /steps %}}

If the process succeeds, you will get a success screen. Every linked applications will automatically restart to use the new configuration. Please make sure to update configuration that do not use environment variable if you have some.

In case the database migration fails, you will be informed at which point it did and a button to contact our support team will appear. Reach out to [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice) with you add-on ID (available in the **Addon Dashboard** section) and they will help you finish the process.
