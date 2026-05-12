---
type: docs
linkTitle: MySQL
title: MySQL
description: Deploy MySQL relational database add-on service on Clever Cloud with automated backups, scaling for enterprise applications
keywords:
- mysql
- relational database
- sql database
- mysql hosting
- percona server
- database management
aliases:
- /doc/mysql
- /doc/add-ons/mysql
- /doc/databases/mysql
- /doc/deploy/addon/mysql
- /doc/deploy/addon/mysql/mysql
- /doc/en/mysql-hosting
---
## Overview
MySQL is an open source relational database management system (RDBMS). Clever Cloud's add-on uses the [Percona Server](https://www.percona.com/mysql/software/percona-server-for-mysql), a 100% compatible open source implementation, with performances improvements and more features.

## Supported Versions

Use the 8.4 long term support (LTS) branch for new add-ons. MySQL 8.0 [reached its end of life on 30 April 2026](https://www.mysql.com/support/eol-notice.html) and [Percona Server 8.0 had its final release in June 2026](https://docs.percona.com/new/2026/06/10/percona-server-for-mysql-8046-37-has-been-released/), so we recommend you migrate your existing 8.0 add-ons to 8.4.

{{< software_versions_shared_dedicated mysql>}}

{{% content "db-backup" %}}

## Migrating from an old database

Some applications require a populated database to run properly.
If you want to import your **SQL** dump, you can use several methods:

1. [The WebGUI (PhpMyAdmin)](https://pma.services.clever-cloud.com/).
2. Command line tool for MySQL administration
3. Any MySQL client such as [MySQL Workbench](https://www.mysql.fr/products/workbench/)

If you need to import a very large dump, contact [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice).

{{% content "db-migration" %}}

## Replication

You can add up to two replicas to an existing MySQL database on Clever Cloud to enhance performance and reliability. Replication is available for MySQL 5.7 and later versions. Read-only replicas use [logical replication based on the binary log](https://dev.mysql.com/doc/refman/8.4/en/binlog-replication-configuration-overview.html) and can be deployed in a different availability zone (AZ) or region on request.

If a primary server isn't available, a replica can be promoted as a standalone server and linked to applications.

> [!NOTE]
> Replica creation and promotion aren't yet available through the API or the Console. To create or configure replicas, or to promote one, contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).

## Direct access

{{< callout type="warning">}}
Using direct access is a trade-off: if you migrate your add-on, you will need to generate the hostname and port again, so your application will need to update that environment, while using a proxy does not change anything.
{{< /callout>}}

All our dedicated MySQL databases are served via a proxy. To reduce the latency you can bypass this proxy by generating direct hostname and port for the add-on. You can do it by clicking the "Generate direct hostname and port" on the add-on dashboard.

This action will add new environment variables to reach the add-on without any proxy.

## Encryption at rest

Encryption at rest is available on MySQL. You can have more information on the [dedicated page](/doc/administrate/encryption-at-rest).

## ProxySQL

{{% content "proxysql" %}}

You can learn more about ProxySQL on the [dedicated documentation page](/guides/proxysql)

## Plans

{{< callout type="warning" >}}
As Shared databases (DEV) are shared between multiple applications and delays could appear in case of an high demand. If this delays create problems in your application or are problematic, we recommend you to use a dedicated database (XS plans and above).
{{< /callout >}}

## 🔑 Rights and permissions

Clever Cloud configures and maintains the MySQL server. You have **standard access** to the database with **ALL privileges**, but some administrative operations and server settings aren't available directly. This ensures optimal performance and security.

Authorized actions:

- Manage tables (create, delete…).
- Manage indexes.

The following actions aren't available directly:

- Database administration (for example you won't be able to create new databases).
- Users administration (you won't be able to create other users than the one handled with our control plane, i.e. the base owner and read-only users).
- Server configuration update.
- Plugins installation.
- Replica creation.
- Backup frequency or retention control.
- Create triggers or functions (DEV plans only).

If your use case requires specific server parameters or one of these restricted operations, contact [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) to discuss feasibility.
