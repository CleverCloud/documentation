---
title: Database migration
shortdesc: How to migrate your database
keywords:
- database
- dbaas
- migration
tags:
- administrate
---

## Migrating any database

You can now migrate any database easily in Clever Cloud

Under any database add-on menu, go to the **Migrate/Upgrade** section.
You will see the disclaimer of the database migration assistant. It informs you that *your databse will be read-only during the migration process* and that the *hostname and database name will be automatically changed*. 
Regading this, we strongly recommend that you make sure every linked application uses the database add-on environment variables so those values will be automatically updated in your application.

Once you are ready, you can click on **Migration Settings**.

A menu will open, where you will see your current database informations.
Under you will see that you can select your new batabse size and pricing plan. Billing section in Summary will be edited accordingly.
Under **Targeted version** you can choose the desired database version.

Please note that downgrading database is currently not supported, you can however ask our support team to do it at support@clever-cloud.com.

Once you are happy with the changes you made, you can select **Migrate the Database**. You will be prompted to confirm the migration. As soon as you do so, the database will be set in read-only mode and the migration process will start.

If the process succeeds, you will get a success screen. Every linked applications will automatically restart to use the new configuration. Please make sure to update configuration that do not use environment variable if you have some.
In case the database migration fails, you will be informed at wich point it did and a button to contact our support team will appear. Reach out to them at support@clever-cloud.com with you add-on ID (available in the **Addon Dashboard** section) and they will help you finish the process.
