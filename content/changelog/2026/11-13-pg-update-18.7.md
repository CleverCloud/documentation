---
title: PostgreSQL 18.7, 17.12, 16.16, 15.20, 14.25 are available (security update)
description: Security patches, bug fixes and improvements for PostgreSQL 14 to 18, and the final release of PostgreSQL 14
date: 2026-11-13
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

- PostgreSQL 18.7
- PostgreSQL 17.12
- PostgreSQL 16.16
- PostgreSQL 15.20
- PostgreSQL 14.25

These versions include [over 140 bug fixes and improvements](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/), with security patches for 52 CVEs: [CVE-2026-6460](https://nvd.nist.gov/vuln/detail/CVE-2026-6460), [CVE-2026-6467](https://nvd.nist.gov/vuln/detail/CVE-2026-6467), [CVE-2026-14661](https://nvd.nist.gov/vuln/detail/CVE-2026-14661), [CVE-2026-16237](https://nvd.nist.gov/vuln/detail/CVE-2026-16237), [CVE-2026-16240](https://nvd.nist.gov/vuln/detail/CVE-2026-16240), [CVE-2026-18447](https://nvd.nist.gov/vuln/detail/CVE-2026-18447), [CVE-2026-116303](https://nvd.nist.gov/vuln/detail/CVE-2026-116303), [CVE-2026-116304](https://nvd.nist.gov/vuln/detail/CVE-2026-116304), [CVE-2026-116306](https://nvd.nist.gov/vuln/detail/CVE-2026-116306), [CVE-2026-116307](https://nvd.nist.gov/vuln/detail/CVE-2026-116307), [CVE-2026-116308](https://nvd.nist.gov/vuln/detail/CVE-2026-116308), [CVE-2026-116309](https://nvd.nist.gov/vuln/detail/CVE-2026-116309), [CVE-2026-116310](https://nvd.nist.gov/vuln/detail/CVE-2026-116310), [CVE-2026-116311](https://nvd.nist.gov/vuln/detail/CVE-2026-116311), [CVE-2026-116312](https://nvd.nist.gov/vuln/detail/CVE-2026-116312), [CVE-2026-116313](https://nvd.nist.gov/vuln/detail/CVE-2026-116313), [CVE-2026-116314](https://nvd.nist.gov/vuln/detail/CVE-2026-116314), [CVE-2026-116315](https://nvd.nist.gov/vuln/detail/CVE-2026-116315), [CVE-2026-116316](https://nvd.nist.gov/vuln/detail/CVE-2026-116316), [CVE-2026-116317](https://nvd.nist.gov/vuln/detail/CVE-2026-116317), [CVE-2026-116318](https://nvd.nist.gov/vuln/detail/CVE-2026-116318), [CVE-2026-116319](https://nvd.nist.gov/vuln/detail/CVE-2026-116319), [CVE-2026-116320](https://nvd.nist.gov/vuln/detail/CVE-2026-116320), [CVE-2026-116321](https://nvd.nist.gov/vuln/detail/CVE-2026-116321), [CVE-2026-116322](https://nvd.nist.gov/vuln/detail/CVE-2026-116322), [CVE-2026-116323](https://nvd.nist.gov/vuln/detail/CVE-2026-116323), [CVE-2026-116325](https://nvd.nist.gov/vuln/detail/CVE-2026-116325), [CVE-2026-116326](https://nvd.nist.gov/vuln/detail/CVE-2026-116326), [CVE-2026-116327](https://nvd.nist.gov/vuln/detail/CVE-2026-116327), [CVE-2026-116328](https://nvd.nist.gov/vuln/detail/CVE-2026-116328), [CVE-2026-116329](https://nvd.nist.gov/vuln/detail/CVE-2026-116329), [CVE-2026-116330](https://nvd.nist.gov/vuln/detail/CVE-2026-116330), [CVE-2026-116331](https://nvd.nist.gov/vuln/detail/CVE-2026-116331), [CVE-2026-116332](https://nvd.nist.gov/vuln/detail/CVE-2026-116332), [CVE-2026-116333](https://nvd.nist.gov/vuln/detail/CVE-2026-116333), [CVE-2026-116335](https://nvd.nist.gov/vuln/detail/CVE-2026-116335), [CVE-2026-116336](https://nvd.nist.gov/vuln/detail/CVE-2026-116336), [CVE-2026-120139](https://nvd.nist.gov/vuln/detail/CVE-2026-120139), [CVE-2026-120141](https://nvd.nist.gov/vuln/detail/CVE-2026-120141), [CVE-2026-120142](https://nvd.nist.gov/vuln/detail/CVE-2026-120142), [CVE-2026-120143](https://nvd.nist.gov/vuln/detail/CVE-2026-120143), [CVE-2026-120144](https://nvd.nist.gov/vuln/detail/CVE-2026-120144), [CVE-2026-120145](https://nvd.nist.gov/vuln/detail/CVE-2026-120145), [CVE-2026-120146](https://nvd.nist.gov/vuln/detail/CVE-2026-120146), [CVE-2026-120147](https://nvd.nist.gov/vuln/detail/CVE-2026-120147), [CVE-2026-120148](https://nvd.nist.gov/vuln/detail/CVE-2026-120148), [CVE-2026-120149](https://nvd.nist.gov/vuln/detail/CVE-2026-120149), [CVE-2026-120150](https://nvd.nist.gov/vuln/detail/CVE-2026-120150), [CVE-2026-120151](https://nvd.nist.gov/vuln/detail/CVE-2026-120151), [CVE-2026-120152](https://nvd.nist.gov/vuln/detail/CVE-2026-120152), [CVE-2026-120153](https://nvd.nist.gov/vuln/detail/CVE-2026-120153) and [CVE-2026-120154](https://nvd.nist.gov/vuln/detail/CVE-2026-120154).

A migration recreates the indexes of your database on the updated server, so the index fixes described in the [Updating section](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/) of the release announcement apply without further action. On PostgreSQL 18, a migration fails and rolls back if a partitioned table has a `NOT NULL NO INHERIT` constraint. Find these constraints with the query of the [Updating section](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/) and repair them before you migrate.

PostgreSQL 14.25 is the final release of PostgreSQL 14, which [reached its end of life](https://www.postgresql.org/support/versioning/) on 12 November 2026. It no longer receives security fixes: [migrate your databases](/doc/develop/database-migration/) to a newer version.

- [Learn more about PostgreSQL on Clever Cloud](/doc/deploy/databases/postgresql/)
- [PostgreSQL versioning policy](https://www.postgresql.org/support/versioning/)
