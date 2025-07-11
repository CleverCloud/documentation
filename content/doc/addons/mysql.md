---
type: docs
title: MySQL

Description: MySQL is an open source relational database management system (RDBMS).
tags:
- addons
keywords:
- sql
- mysql
- mariadb
- RDBMS
aliases:
- /doc/deploy/addon/mysql/mysql
type: docs
---
## Overview
MySQL is an open source relational database management system (RDBMS). Clever Cloud's add-on uses the [Percona Server](https://www.percona.com/mysql/software/percona-server-for-mysql), a 100% compatible open source implementation, with performances improvements and more features.

## Supported Versions

MySQL is available in regular versions and `early` for 8.4. That means it's the first release (8.4.0) of this long term support (LTS) branch, so you should consider it mostly to make some tests and discover what's new. But we recommend waiting a bit before using a new branch in production.

{{< software_versions_shared_dedicated mysql>}}

{{< content "db-backup" >}}

## Migrating from an old database

Some applications require a populated database to run properly.
If you want to import your **SQL** dump, you can use several methods:

1. [The WebGUI (PhpMyAdmin)](https://pma.services.clever-cloud.com/).
2. Command line tool for MySQL administration
3. Any MySQL client such as [MySQL Workbench](https://www.mysql.fr/products/workbench/)

If you need to import a very large dump, contact [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice).

{{< content "dbMigration" >}}

## Direct access

{{< callout type="warning">}}
Using direct access is a trade-off: if you migrate your add-on, you will need to generate the hostname and port again, so your application will need to update that environment, while using a proxy does not change anything.
{{< /callout>}}

All our dedicated MySQL databases are served via a proxy. To reduce the latency you can bypass this proxy by generating direct hostname and port for the add-on. You can do it by clicking the "Generate direct hostname and port" on the add-on dashboard.

This action will add new environment variables to reach the add-on without any proxy.

## Encryption at rest

Encryption at rest is available on MySQL. You can have more information on the [dedicated page]({{< ref "doc/administrate/encryption-at-rest.md" >}})

## ProxySQL

{{< content "proxysql" >}}

You can learn more about ProxySQL on the [dedicated documentation page]({{< ref "/guides/proxysql" >}})

## Plans

{{< callout type="warning" >}}
As Shared databases (DEV) are shared between multiple applications and delays could appear in case of an high demand. If this delays create problems in your application or are problematic, we recommend you to use a dedicated database (XS plans and above).
{{< /callout >}}

## 🔑 Rights and permissions

Add-ons are managed services, meaning that users have **standard access** to the database (**ALL privileges**). Some operations like databases and users creation, as well as some settings modifications aren't available by default. This ensures optimal performances and security for managed services as configured by Clever Cloud.

Authorized actions:
- Manage tables (create, delete…).
- Manage indexes.

If you think your system might require more advanced administrative access, contact [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice) to explain your use case, and we will work with you to find a solution.

Here is the list of actions that you won't be able to perform:
- Database administration (for example you won't be able to create new databases).
- Users administration (you won't be able to create other users than the one handled with our control plane, i.e. the base owner and read-only users).
- Server configuration update.
- Plugins installation.
- Replica creation.
- Backup frequency or retention control.
- Create Trigger or Function (Only on DEV plan)

Ask Clever Cloud support if you want to perform one of these actions.
