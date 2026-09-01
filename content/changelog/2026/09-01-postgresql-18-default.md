---
title: PostgreSQL 18 becomes the default version on 15 September
description: New PostgreSQL add-ons created without an explicit version will run PostgreSQL 18
date: 2026-09-01
tags:
  - addons
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[PostgreSQL 18 is available on Clever Cloud](/changelog/2025/10-08-postgresql-18/) since October 2025, and [PostgreSQL 17 has been the default](/changelog/2025/03-27-postgresql-default/) for new add-ons since March 2025. **Starting 15 September 2026**, a new PostgreSQL add-on created without an explicit version runs PostgreSQL 18.

This affects add-ons creation only. Existing databases keep the version they run today and are never upgraded without your action. When you're ready, use Clever Cloud's automatic migration process to move them to PostgreSQL 18.

You can still create an add-on on any other supported version, from the Console or with Clever Tools:

```bash
clever addon create postgresql-addon myDatabase -p xxs_sml --addon-version 17
```

PostgreSQL 18 uses the same default extensions as PostgreSQL 17. It brings asynchronous I/O with `io_uring`, [virtual generated columns](https://www.postgresql.org/docs/18/sql-createtable.html#SQL-CREATETABLE-PARMS-GENERATED-STORED), UUIDv7 generation, improved text processing and multiple authentication and security features.

Keep in mind that PostgreSQL 14 reaches its end of life on 12 November 2026. Plan a migration to a newer version before that date to keep receiving security updates.

- [Learn more about PostgreSQL on Clever Cloud](/doc/addons/postgresql/)
- [PostgreSQL versioning policy](https://www.postgresql.org/support/versioning/)
