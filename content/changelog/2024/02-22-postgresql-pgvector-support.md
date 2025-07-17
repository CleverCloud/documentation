---
title: "PostgreSQL: ask for pgvector support"
date: 2024-02-22
tags:
  - addons
  - postgresql
authors:
  - name: Lucas Draescher
    link: https://github.com/draescherl
    image: https://github.com/draescherl.png?size=40
  - name: Aurélien Hébert
    link: https://github.com/aurrelhebert
    image: https://github.com/aurrelhebert.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Your wishes are our commands
aliases:
- /changelog/2024-02-22-postgresql-pgvector-support
excludeSearch: true
---

PostgreSQL databases managed by Clever Cloud come with [lots of extensions enabled by default](/developers/doc/addons/postgresql/#default-extensions). There are also [some you can ask for](/developers/doc/addons/postgresql/#on-demand-extensions), and we'll set them up, like `pg_cron`, `pgtap` or `timescaledb`.

We recently noticed an increased interest from our clients in supporting the `pgvector` extension, needed for specific (AI) workloads. To answer these needs, we've packaged it and are now able to provide it on-demand.

If you need `pgvector`, open a ticket to our support team through [the Console Ticket Center](https://console.clever-cloud.com/ticket-center-choice). If you need any other extension, feel free to ask, we will try our best to respond to your use-case.

- Learn more about `pgvector` [on GitHub](https://github.com/pgvector/pgvector) {{< icon "github" >}}