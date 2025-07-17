---
title: MySQL update, with a new option
date: 2025-02-05
tags:
  - addons
  - update
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Use skip-log-bin from Clever Tools
excludeSearch: true
---

We updated MySQL images for releases 8.4 (8.4.2-2) and 8.0 (8.0.39-30). A new option is available at database creation from Clever Tools: [skip-log-bin](https://dev.mysql.com/doc/refman/8.4/en/replication-options-binary-log.html#option_mysqld_log-bin). To use it, add `--option skip-log-bin` flag with the `clever create addon mysql-addon` command.

* [Learn more about MySQL 8.4](https://www.percona.com/blog/mysql-8-4-first-peek/)
* [Learn more about MySQL on Clever Cloud](/developers/doc/addons/mysql/)
