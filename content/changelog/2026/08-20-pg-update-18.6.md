---
title: PostgreSQL 18.6, 17.11, 16.15, 15.19, 14.24 are available (security update)
description: Security patches, bug fixes and improvements for PostgreSQL 14 to 18
date: 2026-08-20
tags:
  - addons
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

New PostgreSQL versions are available for new add-ons and migration:

- PostgreSQL 18.6
- PostgreSQL 17.11
- PostgreSQL 16.15
- PostgreSQL 15.19
- PostgreSQL 14.24

These versions include [over 110 bug fixes and improvements](https://www.postgresql.org/about/news/postgresql-186-1711-1615-1519-1424-and-19-beta-3-released-3365/), with security patches for 28 CVEs: [CVE-2026-6464](https://nvd.nist.gov/vuln/detail/CVE-2026-6464), [CVE-2026-6469](https://nvd.nist.gov/vuln/detail/CVE-2026-6469), [CVE-2026-6470](https://nvd.nist.gov/vuln/detail/CVE-2026-6470), [CVE-2026-6471](https://nvd.nist.gov/vuln/detail/CVE-2026-6471), [CVE-2026-14662](https://nvd.nist.gov/vuln/detail/CVE-2026-14662), [CVE-2026-14663](https://nvd.nist.gov/vuln/detail/CVE-2026-14663), [CVE-2026-14664](https://nvd.nist.gov/vuln/detail/CVE-2026-14664), [CVE-2026-14666](https://nvd.nist.gov/vuln/detail/CVE-2026-14666), [CVE-2026-14668](https://nvd.nist.gov/vuln/detail/CVE-2026-14668), [CVE-2026-14669](https://nvd.nist.gov/vuln/detail/CVE-2026-14669), [CVE-2026-14670](https://nvd.nist.gov/vuln/detail/CVE-2026-14670), [CVE-2026-14671](https://nvd.nist.gov/vuln/detail/CVE-2026-14671), [CVE-2026-14672](https://nvd.nist.gov/vuln/detail/CVE-2026-14672), [CVE-2026-14673](https://nvd.nist.gov/vuln/detail/CVE-2026-14673), [CVE-2026-14676](https://nvd.nist.gov/vuln/detail/CVE-2026-14676), [CVE-2026-14677](https://nvd.nist.gov/vuln/detail/CVE-2026-14677), [CVE-2026-14678](https://nvd.nist.gov/vuln/detail/CVE-2026-14678), [CVE-2026-14679](https://nvd.nist.gov/vuln/detail/CVE-2026-14679), [CVE-2026-14680](https://nvd.nist.gov/vuln/detail/CVE-2026-14680), [CVE-2026-14681](https://nvd.nist.gov/vuln/detail/CVE-2026-14681), [CVE-2026-15741](https://nvd.nist.gov/vuln/detail/CVE-2026-15741), [CVE-2026-15742](https://nvd.nist.gov/vuln/detail/CVE-2026-15742), [CVE-2026-16238](https://nvd.nist.gov/vuln/detail/CVE-2026-16238), [CVE-2026-16239](https://nvd.nist.gov/vuln/detail/CVE-2026-16239), [CVE-2026-16241](https://nvd.nist.gov/vuln/detail/CVE-2026-16241), [CVE-2026-18024](https://nvd.nist.gov/vuln/detail/CVE-2026-18024), [CVE-2026-18408](https://nvd.nist.gov/vuln/detail/CVE-2026-18408) and [CVE-2026-19385](https://nvd.nist.gov/vuln/detail/CVE-2026-19385).

If your database uses GIN indexes, `btree_gist` indexes on `float4`, `float8`, `bit` or `bit varying` columns, or B-tree indexes on `ltree` values, follow the steps of the [Updating section](https://www.postgresql.org/about/news/postgresql-186-1711-1615-1519-1424-and-19-beta-3-released-3365/) after migrating to fix affected statistics and indexes.

PostgreSQL 14 reaches its end of life on 12 November 2026. Plan a migration to a newer version before that date to keep receiving security updates.

- [Learn more about PostgreSQL on Clever Cloud](/doc/deploy/databases/postgresql/)
