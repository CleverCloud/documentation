---
title: Intro to add-ons
position: 2
shortdesc: Add-ons allows you to extend your apps with databases, search engines, monitoring etc.
tags:
- dashboard-setup
- addons
---

Applications often requires one or more services in addition to the runtime itself. For example, you may need databases
for storing data, cache engine for performances, long time log storage, etc...

These services are called add-ons. There is a great number of them, based on many technologies, and developed by many
companies, or communities. It could be a database, a cache system or a search engine.

Most of the add-ons catalog is provided by Clever Cloud, but vendors are also allowed to provide services external to Clever Cloud ([See how to integrate your SaaS with Clever Cloud](/doc/clever-cloud-apis/add-ons-api/))

## Clever Cloud's add-ons

Some add-ons are developed and maintained by Clever Cloud, exclusively.

* Cellar S3
* File System Buckets
* MongoDB
* MySQL
* PostgreSQL
* Redis +
* Socks
* Kafka$
* RabbitMQ
* Riak KV

## Adding an add-on

To add an addon, please refer to the [dedicated section](/doc/addons/clever-cloud-addons/).

## Billing

There is two kinds of billing:

* Per-month billing: Add-ons with fixed resources (storage, CPU and RAM)
* Per-usage billing: Add-ons based on consumption, like [FS-Buckets](/doc/addons/fs_buckets/) and [Cellar](/doc/addons/cellar/)

**Note:** Per usage billing will be taken on runtime credits each day, while per-month add-ons will create a new line in the monthly invoice.
