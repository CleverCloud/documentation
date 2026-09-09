---
type: docs
weight: 35
linkTitle: Databases
title: Databases
description: Deploy managed databases on Clever Cloud with automated backups, monitoring and scaling
keywords:
- databases
- managed databases
- sql
- nosql
- key-value
- search
aliases:
- /doc/databases
---

Two models sit side by side. PostgreSQL, MySQL, MongoDB, Redis and Elastic run as managed instances you size, with backups, monitoring and version upgrades handled by the platform. Materia KV and Materia TS are serverless: no instance to choose, no capacity to plan, and your data replicated synchronously across three data centers. Both link to an application the same way, through environment variables.

{{< cards >}}
  {{< card link="/developers/doc/deploy/databases/elastic" title="Elastic Stack" subtitle="Managed search and analytics engine" icon="elastic" >}}
  {{< card link="/developers/doc/deploy/databases/materia-kv" title="Materia KV" subtitle="Serverless distributed key-value database" icon="materia" tag="Beta" >}}
  {{< card link="/developers/doc/deploy/databases/materia-ts" title="Materia TS" subtitle="Serverless distributed time-series database" icon="materia" tag="Private access" >}}
  {{< card link="/developers/doc/deploy/databases/mongodb" title="MongoDB" subtitle="Managed NoSQL document database" icon="mongo" >}}
  {{< card link="/developers/doc/deploy/databases/mysql" title="MySQL" subtitle="Managed relational database" icon="mysql" >}}
  {{< card link="/developers/doc/deploy/databases/postgresql" title="PostgreSQL" subtitle="Managed object-relational database" icon="pg" >}}
  {{< card link="/developers/doc/deploy/databases/redis" title="Redis" subtitle="Managed key-value database" icon="redis" >}}
{{< /cards >}}
