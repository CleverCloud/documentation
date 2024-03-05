---
type: docs
title: MySQL

Description: MySQL is an open-source relational database management system (RDBMS).
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
MySQL is an open-source relational database management system (RDBMS).

### Supported versions

{{< software_versions_shared_dedicated mysql>}}

{{% content/db-backup %}}

## Migrating from an old database

Some applications require a populated database to run properly.
If you want to import your **SQL** dump, you can use several methods:

1. [Our WebGUI (PHP My Admin)](https://dbms-pma.clever-cloud.com/).
2. Command line tool for MySQL administration.
3. Any MySQL client such as [MySQL Workbench](https://www.mysql.fr/products/workbench/).

If you need to import a very large dump, please send an email to <support@clever-cloud.com>.

## Direct access

{{< callout type="warning">}}
Using direct access is a trade-off: if you migrate your addon, you will need to generate the hostname and port again, so your application will need to update that environment, while using a proxy does not change anything.
{{< /callout>}}

All our dedicated MySQL databases are served via a proxy. To reduce the latency you can bypass this proxy by generating direct hostname and port for the addon. You can do it by clicking the "Generate direct hostname and port" on the addon dashboard.

This action will add new environment variables to reach the addon without any proxy.

## Encryption at rest

Encryption at rest is available on MySQL. You can have more information on the [dedicated page]({{< ref "doc/administrate/encryption-at-rest.md" >}})

## ProxySQL

{{% content/proxysql %}}

You can learn more about ProxySQL on the [dedicated documentation page]({{< ref "/guides/proxysql" >}})

## Plans

{{< callout type="warning" >}}
As Shared databases (DEV) are shared between multiple applications and delays could appear in case of an high demand. If this delays create problems in your application or are problematcs, we recommend you to use a dedicated database (XS plans and above).
{{< /callout >}}
