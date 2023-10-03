---
type: docs
title: Database migration and security updates
shortdesc: How to migrate your database
keywords:
- database
- dbaas
- migration
tags:
- administrate
type: docs
---

## Migrating any database and updating its security

{{< callout type="warning" >}}
    We do not support the migration of read only users except for PostgreSQL addons. If you have any, you will have to create new ones at the end of the migration.
{{< /callout >}}

You can migrate any database easily in Clever Cloud to upgrade the size of the addon and improve its security by updating underlaying softwares.

Indeed, our databases add-ons are deployed on immutable Virtual Machines. No updates are made on those VMs.
To improve security, you need to perform a "migration", which will boot a new VM with up-to-date system and database.
Unless you want to upgrade your database to a new major version or to give it more resources, you just have to perform a migration on the same zone, same plan and same major version.

These updates are not related to your addon (PostgreSQL, MySQL...) major version. Only patches or minor versions of the addon software along with system upgrades (security patches and new kernel features) are performed. For example, you can keep *PostgreSQL 11* if you want to.

## Migration (updating) step-by-step

Under any database add-on menu, go to the **Migrate/Upgrade** section.

You will see the disclaimer of the database migration assistant. It informs you that *your databse will be read-only during the migration process* and that the *hostname and database name will be automatically changed*. 

{{<image "/images/database-migration-01.png" "Migrate/Upgrade section">}} 

Regarding this, we strongly recommend that you make sure every linked application uses the database add-on environment variables so those values will be automatically updated in your application.

Once you are ready, you can click on **Migration Settings**.

A menu will open, where you will see your current database informations.

{{<image "/images/database-migration-02.png" "Migration settings">}} 

Under you will see that you can select your new batabse size and pricing plan. Billing section in Summary will be edited accordingly.

Under **Targeted version** you can choose the desired database version.

Please note that downgrading database is currently not supported, you can however ask our support team to do it at support@clever-cloud.com.

Once you are happy with the changes you made, you can select **Migrate the Database**. You will be prompted to confirm the migration. 

{{<image "/images/database-migration-03.png" "Confirmation prompt screen">}} 

As soon as you do so, the database will be set in read-only mode and the migration process will start.

{{<image "/images/database-migration-04.png" "Migration in progress">}} 

If the process succeeds, you will get a success screen. Every linked applications will automatically restart to use the new configuration. Please make sure to update configuration that do not use environment variable if you have some.

{{<image "/images/database-migration-05.png" "Migration successful">}} 

In case the database migration fails, you will be informed at wich point it did and a button to contact our support team will appear. Reach out to them at support@clever-cloud.com with you add-on ID (available in the **Addon Dashboard** section) and they will help you finish the process.
