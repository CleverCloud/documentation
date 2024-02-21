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
excludeSearch: true
---

PostgreSQL databases managed by Clever Cloud come with [lots of extensions activated by default](/doc/addons/postgresql/#default-extensions). There are also [some you can ask for](/doc/addons/postgresql/#on-demand-extensions), and we'll set them up, like `pg_cron`, `pgtap` or `timescaledb`.

Recently, some customers also asked us a `pgvector` support, needed for specific (AI) workloads. So we started to work on it and integrated this extension to our workflow. We are now able to provide it on-demand.

So if you need `pgvector`, just raise a ticket to our support team through [the Console Ticket Center](https://console.clever-cloud.com/ticket-center-choice). And if there is any other extension you need, feel free to ask, we will check how easy it is for us to provide it.

- Learn more about `pgvector` [on GitHub](https://github.com/pgvector/pgvector) {{< icon "github" >}}