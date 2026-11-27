---
title: PostgreSQL 19 is available
description: PostgreSQL 19.0 is available for new add-ons and migrations, with REPACK (CONCURRENTLY), INSERT … ON CONFLICT DO SELECT, and WAIT FOR LSN
date: 2026-11-26
tags:
  - addons
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[PostgreSQL 19](https://www.postgresql.org/about/news/postgresql-19-released-3449/) is available on Clever Cloud for new dedicated add-ons and migrations, with the same default extensions as PostgreSQL 18, such as PostGIS 3.7 and `vector`. PostgreSQL 18 remains the default version of new add-ons.

`REPACK (CONCURRENTLY)` rebuilds a table while reads and writes go on, and only locks it briefly to swap its files at the end. `INSERT ... ON CONFLICT DO SELECT` returns the existing rows, and `WAIT FOR LSN` brings read-your-writes consistency on [replicas](/doc/deploy/databases/postgresql/#replication).

Some defaults change: TOAST compression uses `lz4`, and just-in-time compilation is off, so run `SET jit = on` in sessions with large analytical queries. TimescaleDB and RUM remain available up to PostgreSQL 18: a migration to PostgreSQL 19 of a database using them fails.

> [!NOTE] Check the incompatibilities before you migrate
> `standard_conforming_strings` is always on, `json_array()` over a query without rows returns an empty array instead of `NULL`, and `soundex()` or `metaphone()` ignore non-ASCII letters. Read the [migration notes](https://www.postgresql.org/docs/release/19.0/#RELEASE-19-MIGRATION) first.

Create a PostgreSQL 19 add-on from the Console or with Clever Tools, or [migrate](/doc/develop/database-migration/) an existing one:

```bash
clever addon create postgresql-addon myDatabase -p xxs_sml --addon-version 19
```

- [Learn more about PostgreSQL on Clever Cloud](/doc/deploy/databases/postgresql/)
- [PostgreSQL 19 release notes](https://www.postgresql.org/docs/release/19.0/)
