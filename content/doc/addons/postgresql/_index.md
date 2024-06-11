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
## Overview

PostgreSQL is an object-relational database management system (ORDBMS) with an emphasis on extensibility and on standards-compliance.

### Supported versions

{{< software_versions_shared_dedicated pg>}}


{{% content/db-backup %}}

## Migrating from an old database

Some applications require a non-empty database to run properly. If you want to import your **SQL** dump, you can use several methods:
1. [WebGUI (Adminer)](https://dbms-adminer.clever-cloud.com/)
2. Command line tool for PostgreSQL administration like `psql`
3. Any PostgreSQL client such as [pgAdmin](https://www.pgadmin.org/)

## Direct access

A proxy serves all dedicated PostgreSQL databases. In some cases, this can add some latency between applications and their database. If this is an issue, you can generate a direct hostname and port for the add-on to bypass the proxy, using the "Generate direct hostname and port" button in the add-on dashboard.

Generating direct access adds new variables to the add-on's environment, allowing connections without going through the proxy.

{{< callout type="info" >}} 
Direct access doesn't persist after migrating a database. Manually re-generate direct host name and port after a migration to allow applications linked through direct access to connect to the database. 

Such a limitation doesn't exist when using proxy access.
{{< /callout >}}

## Encryption at rest

Encryption at rest is available on PostgreSQL. You can find more information on the [dedicated page]({{< ref "doc/administrate/encryption-at-rest.md" >}})

## Note on shared databases

If you try to list the databases on the shared cluster, you will see the names of the databases of all other users of the cluster. This is normal behaviour. Rest assured, permissions are set properly, meaning no one but your user can read or write data to your database.

This referencing does not exist for dedicated databases.

## Pgpool-II

{{% content/pgpool %}}

You can learn more about Pgpool-II on the [dedicated documentation page]({{< ref "/guides/pgpool" >}})

## Default extensions

PostgreSQL databases managed by Clever Cloud comes with these extensions:

Extension               | Description
----------------------- | -----------
 adminpack              | Administrative functions for PostgreSQL
 autoinc                | Functions for autoincrementing fields
 btree_gin              | Support for indexing common datatypes in GIN
 btree_gist             | Support for indexing common datatypes in GiST
 citext                 | Data type for case-insensitive character strings
 cube                   | Data type for multidimensional cubes
 dblink                 | Connect to other PostgreSQL databases from within a database
 dict_int               | Text search dictionary template for integers
 dict_xsyn              | Text search dictionary template for extended synonym processing
 earthdistance          | Calculate great-circle distances on the surface of the Earth
 file_fdw               | Foreign-data wrapper for flat file access
 fuzzystrmatch          | Determine similarities and distance between strings
 hstore                 | Data type for storing sets of (key, value) pairs
 hypopg                 | Hypothetical indexes for PostgreSQL
 insert_username        | Functions for tracking who changed a table
 intagg                 | Integer aggregator and enumerator (obsolete)
 intarray               | Functions, operators, and index support for 1-D arrays of integers
 isn                    | Data types for international product numbering standards
 lo                     | Large Object maintenance
 ltree                  | Data type for hierarchical tree-like structures
 moddatetime            | Functions for tracking last modification time
 pageinspect            | Inspect the contents of database pages at a low level
 pg_buffercache         | Examine the shared buffer cache
 pg_freespacemap        | Examine the free space map (FSM)
 pg_stat_statements     | Track planning and execution statistics of all SQL statements executed
 pg_trgm                | Text similarity measurement and index searching based on trigrams
 pgcrypto               | Cryptographic functions
 pgrowlocks             | Show row-level locking information
 pgstattuple            | Show tuple-level statistics
 plcoffee               | PL/CoffeeScript (v8) trusted procedural language
 plls                   | PL/LiveScript (v8) trusted procedural language
 plpgsql                | PL/pgSQL procedural language
 plv8                   | PL/JavaScript (v8) trusted procedural language
 postgis                | PostGIS geometry and geography spatial types and functions
 postgis_raster         | PostGIS raster types and functions
 postgis_tiger_geocoder | PostGIS tiger geocoder and reverse geocoder
 postgis_topology       | PostGIS topology spatial types and functions
 postgres_fdw           | Foreign-data wrapper for remote PostgreSQL servers
 refint                 | Functions for implementing referential integrity (obsolete)
 seg                    | Data type for representing line segments or floating-point intervals
 sslinfo                | Information about SSL certificates
 tablefunc              | Functions that manipulate whole tables, including crosstab
 tcn                    | Triggered change notifications
 unaccent               | Text search dictionary that removes accents
 uuid-ossp              | Generate universally unique identifiers (UUIDs)
 xml2                   | XPath querying and XSLT

## On-demand extensions

In the [Console's Ticket Center](https://console.clever-cloud.com/ticket-center-choice), you can ask our support team to add any of these extensions for you:

Extension   | Description
----------- | -----------
pg_cron     | Job scheduler for PostgreSQL
pgtap       | Unit testing for PostgreSQL
pgvector    | Vector data type and ivfflat and hnsw access methods
timescaledb | Enables scalable inserts and complex queries for time-series data (Community Edition)

{{< callout type="warning" >}}
On-demand extensions aren't available for DEV plans.
{{< /callout >}}

## Automatic vacuuming

[Autovacuum](https://www.postgresql.org/docs/current/routine-vacuuming.html) is automatically enabled on PostgreSQL add-ons.  
The autovacuum will proceed when a given percentage of rows of a table will be updated/inserted/deleted.  
Usually this threshold is set to 20%.

## `pg_activity`

If you want to use [pg_activity](https://github.com/dalibo/pg_activity) on a PostgreSQL add-on, but you encounter the following error `Exception: Must be run with database superuser privileges.`, you need to add the `--rds` flag when you start it.

{{% content/managed-services %}}