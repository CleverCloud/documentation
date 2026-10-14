---
title: PostgreSQL DEV plan moves to PostgreSQL 18
description: New PostgreSQL add-ons created on the free DEV plan run PostgreSQL 18.6
date: 2026-10-14
tags:
  - addons
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The shared clusters behind the free DEV plan of PostgreSQL now run PostgreSQL 18, the [default version](/changelog/2026/09-01-postgresql-18-default/) of dedicated add-ons since 15 September. A new DEV add-on runs PostgreSQL 18.6, so you can test your application against the same major version you use in production:

```bash
clever addon create postgresql-addon myDevDatabase -p dev --region par
```

The DEV plan remains for testing purposes only: it comes without backups, extensions or SLA. For production workloads, use a dedicated plan.

- [Learn more about PostgreSQL on Clever Cloud](/doc/deploy/databases/postgresql/)
