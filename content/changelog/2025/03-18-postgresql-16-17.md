---
title: PostgreSQL 16 and 17 are available
date: 2025-03-18
tags:
  - addons
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: It's time to prepare for PostgreSQL 18!
excludeSearch: true
---

PostgreSQL 16.8 and 17.4 are now available for add-on creation and migration. Some extensions were removed of these releases: `plcoffee`, `plls`, `plv8` starting PostgreSQL 16 and `pgadmin` which is not available starting PostgreSQL 17. They won't be available after a migration. If you used any of them, the process could fail and your database will be kept in its current version.

We also updated PostgreSQL 15 to release 15.12, PostgreSQL 14 to release 14.17, PostgreSQL 13 to release 13.20. Migrate your database to the desired major version to get the latest release.

* [Learn more about PostgreSQL on Clever Cloud](/developers/doc/addons/postgresql/)
* [PostgreSQL release notes](https://www.postgresql.org/docs/release/)
