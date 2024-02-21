---
type: docs
title: PostgreSQL
position: 7
shortdesc: PostgreSQL is an open-source relational database management system (RDBMS).
tags:
- addons
keywords:
- sql
- postgresql
- pg
- pgsql
- mariadb

aliases: 
- /doc/deploy/addon/postgresql/postgresql

type: docs
---

PostgreSQL is an object-relational database management system (ORDBMS) with an emphasis on extensibility and on standards-compliance.

## Versions

Versions currently available for order are as follows:
- On our shared (DEV) cluster: PostgreSQL version 15
- On dedicated plans: PostgreSQL versions 10, 11, 12, 13, 14 and 15

{{< readfile file="db-backup.md" >}}

## Migrating from an old database

Some applications require a non-empty database to run properly. If you want to import your **SQL** dump, you can use several methods:
1. [Our WebGUI (Adminer)](https://dbms-adminer.clever-cloud.com/)
2. Command line tool for PostgreSQL administration like `psql`
3. Any PostgreSQL client such as [pgAdmin](https://www.pgadmin.org/)

## Direct access

All our dedicated PostgreSQL databases are served through a proxy. In some cases, this can add some latency between applications and their database. If this is an issue, the proxy can be bypassed by generating a direct host-name and port for the add-on. You can do so by clicking the "Generate direct hostname and port" button in the add-on dashboard.

Doing this will add new variables to the add-on's environment, allowing connections without going through the proxy.

{{< callout type="info" >}} 
Bear in mind that there is a trade-off with direct access. After migrating an add-on, you will need to re-generate the host name and port. This means applications linked through direct access will not be able to connect until you manually regenerate them. 

Such a limitation doesn't exist when using proxy access.
{{< /callout >}}

## Note on shared databases

Encryption at rest is available on PostgreSQL. You can find more information on the [dedicated page]({{< ref "doc/administrate/encryption-at-rest.md" >}})

This referencing does not exist for dedicated databases.

## Pgpool-II

{{< readfile file="pgpool.md" >}}

You can learn more about Pgpool-II on the [dedicated documentation page]({{< ref "/guides/pgpool" >}})

## Default extensions

Every PostgreSQL database managed by Clever Cloud comes with the following default extensions:
`adminpack`,
`autoinc`,
`btree_gin`,
`btree_gist`,
`citext`,
`cube`,
`dblink`,
`dict_int`,
`dict_xsyn`,
`earthdistance`,
`file_fdw`,
`fuzzystrmatch`,
`hstore`,
`insert_username`,
`intagg`,
`intarray`,
`isn`,
`lo`,
`ltree`,
`moddatetime`,
`pageinspect`,
`pg_buffercache`,
`pgcrypto`,
`pg_freespacemap`,
`pgrowlocks`,
`pg_stat_statements`,
`pgstattuple`,
`pg_trgm`,
`plcoffee`,
`plls`,
`plv8`,
`postgis`,
`postgis_tiger_geocoder`,
`postgis_topology`
`postgres_fdw`,
`refint`,
`seg`,
`sslinfo`,
`tablefunc`,
`tcn`,
`timetravel`,
`unaccent`,
`"uuid-ossp"`,
`xml2`

## Automatic vacuuming

[Autovacuum](https://www.postgresql.org/docs/current/routine-vacuuming.html) is automatically enabled on PostgreSQL add-ons.  
The autovacuum will proceed when a given percentage of rows of a table will be updated/inserted/deleted.  
Usually this threshold is set to 20%.

## `pg_activity`

If you want to use [pg_activity](https://github.com/dalibo/pg_activity) on a PostgreSQL add-on, but you encounter the following error `Exception: Must be run with database superuser privileges.`, you need to add the `--rds` flag when you start it.
