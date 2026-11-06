---
type: docs
weight: 90
linkTitle: Manage
title: Manage
description: Link services on Clever Cloud, migrate database add-ons, and move resources between regions
keywords:
- manage
- migration
- service dependencies
- operations
aliases:
- /doc/admin
- /doc/administrate
- /doc/manage/administrate
---

Day-to-day operations run from [Clever Tools](/doc/tools/cli/), the Console or the API: scaling, backups, logs, drains and notifications. Database migration, service dependencies and zone migration are a different matter, since each changes a service already carrying traffic and follows a procedure worth reading before you start.

{{< cards >}}
  {{< card link="/developers/doc/manage/database-migration" title="Migrate/Update Database" subtitle="Rebuild a database add-on on an up-to-date virtual machine" icon="circle-stack" >}}
  {{< card link="/developers/doc/manage/service-dependencies" title="Service Dependencies" subtitle="Link applications and add-ons to propagate their credentials" icon="plug" >}}
  {{< card link="/developers/doc/manage/zone-migration" title="Zone Migration" subtitle="Move your applications and add-ons to another region" icon="map-pin" >}}
{{< /cards >}}
