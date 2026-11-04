---
title: Add-on logs move to the new logs interface, in beta
description: The logs page of Elasticsearch, Jenkins, MongoDB, MySQL, PostgreSQL, and Redis® add-ons uses the new logs interface of the Console, built on the logs API v4
date: 2025-09-12
tags:
  - console
  - logs
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

As [announced](/changelog/2025/02-20-logs-interface-old-decomission/) when we decommissioned the old logs stack of applications, add-ons move to the new one too. In the [Clever Cloud Console](https://console.clever-cloud.com), their logs page now uses the same interface as application and [access logs](/changelog/2025/09-11-access-logs-console/), built on the logs API v4.

It applies to [Elasticsearch](/doc/deploy/databases/elastic/), [Jenkins](/doc/deploy/services/jenkins/), [MongoDB](/doc/deploy/databases/mongodb/), [MySQL](/doc/deploy/databases/mysql/), [PostgreSQL](/doc/deploy/databases/postgresql/), and [Redis®](/doc/deploy/databases/redis/) add-ons, except for plans that don't provide logs, such as DEV. You get the features you already use for applications: live view, custom time range, and selection and copy of log lines. The text filter can also match an exact string or a regular expression.

This interface is in beta.

- [Learn more about logs on Clever Cloud](/doc/develop/observability/logs/)
- [Share your feedback on the new logs interface](https://github.com/CleverCloud/Community/discussions/categories/new-logs-interface)
