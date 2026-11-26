---
title: Elasticsearch 8.19.25 and 9.5.6 are available
description: New Elasticsearch releases for the 8 and 9 branches, with security fixes, ES|QL views, PromQL, and batched query execution
date: 2026-11-26
tags:
  - addons
  - elastic
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

We updated Elasticsearch Platinum to releases [8.19.25](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/release-notes-8.19.25.html) and [9.5.6](https://www.elastic.co/docs/release-notes/elasticsearch#elasticsearch-9.5.6-release-notes). They're available for add-on creation, along with [7.17.29](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/release-notes-7.17.29.html), the latest release of the 7 branch. Both include [security fixes](https://discuss.elastic.co/c/announcements/security-announcements/31) and update several bundled libraries.

Between 9.2 and 9.5, Elasticsearch gains native support for OpenTelemetry exponential histograms, `bfloat16` dense vectors, ES|QL views, and native PromQL support. Elasticsearch 9.5 also runs the query phase in batches, and hardens the `_reindex` API.

> [!NOTE] Check your time series indices before you upgrade
> Starting with Elasticsearch 9.4, time series indices no longer keep sequence numbers, and reject documents too far in the future starting with 9.5. Read the [breaking changes](https://www.elastic.co/docs/release-notes/elasticsearch/breaking-changes) before you migrate an add-on.

To update an add-on, [migrate it](/doc/develop/database-migration/) within its major version. To change its major version, contact [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).

- [Learn more about Elasticsearch on Clever Cloud](/doc/deploy/databases/elastic/)
