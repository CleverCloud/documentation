---
title: Logs API v2 endpoints decommission
date: 2026-04-23
description: Decommission of the legacy Logs API v2 endpoints on May 23rd, 2026. Migrate to the v4 API to ensure uninterrupted access to your application logs.
tags:
  - api
authors:
  - name: miton18
    link: https://github.com/miton18
    image: https://github.com/miton18.png?size=40
excludeSearch: true
---

Clever Cloud is decommissioning the legacy Logs API v2 endpoints on **May 23rd, 2026**. The v4 API has been available for some time and provides a more reliable and consistent interface to access your application logs. If you still rely on v2 endpoints to fetch logs, migrate to the v4 API as soon as possible.

- **May 23rd, 2026**: v2 logs endpoints will be permanently disabled. Any integration still using v2 will stop receiving logs.

## How to migrate

The v4 Logs API exposes the same capabilities with an improved interface. Update your HTTP calls to target the v4 endpoints documented in the [Logs section of the v4 API reference](/api/v4#logs). Authentication and query parameters follow the same conventions as the rest of the v4 API.

Once updated, your integration will fetch logs immediately without any service interruption.

If you have any questions or need help with the migration, contact [our support team](https://console.clever-cloud.com/ticket-center-choice).

- [Logs API v4 reference](/api/v4#logs)
