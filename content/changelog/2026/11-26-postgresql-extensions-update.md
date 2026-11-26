---
title: PostgreSQL extensions update, with PostGIS 3.7 and TimescaleDB 2.32.1
description: New PostgreSQL add-ons get PostGIS 3.7.0 and TimescaleDB 2.32.1, and the platform prepares the availability of PostgreSQL 19
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

New PostgreSQL add-ons and migrations now get updated extensions, on the same PostgreSQL versions: 18.7, 17.12, 16.16, 15.20, and 14.25. This update also prepares the availability of PostgreSQL 19 on Clever Cloud.

- **PostGIS:** Update to [3.7.0](https://postgis.net/2026/10/PostGIS-3.7.0/), with `postgis_tiger_geocoder` 2025.2
- **TimescaleDB:** Update to [2.32.1](https://github.com/timescale/timescaledb/releases/tag/2.32.1)
- **`pg_partman`:** Update to [5.5.1](https://github.com/pgpartman/pg_partman/releases/tag/v5.5.1)

PostgreSQL 14 and 15 keep PostGIS 3.6.4, and get TimescaleDB 2.19.3 and [2.28.5](https://github.com/timescale/timescaledb/releases/tag/2.28.5) respectively.

PostGIS 3.7 moves the `postgis_tiger_geocoder` and `address_standardizer` extensions to their own projects, still available on Clever Cloud. Topology building functions now read a tolerance of `0` as an exact zero, and `-1` as the topology precision. PostGIS 3.7 also removes the `ST_MemCollect` aggregate: check the [breaking changes](https://git.osgeo.org/gitea/postgis/postgis/raw/tag/3.7.0/NEWS) before you migrate a database.

Existing databases get PostGIS 3.7 with a [migration](/doc/develop/database-migration/). TimescaleDB and `pg_partman` are [on-demand extensions](/doc/deploy/databases/postgresql/#on-demand-extensions): to update them in an existing database, ask [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) in the Console's Ticket Center.

- [Learn more about PostgreSQL on Clever Cloud](/doc/deploy/databases/postgresql/)
