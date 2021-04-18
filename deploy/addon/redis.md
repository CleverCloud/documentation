---
title: Redis
position: 8
shortdesc: Redis is an open source, in-memory data structure store, used as database, cache and message broker.
tags:
- addons
keywords:
- key
- value
- key value
- key-value
- in-memory
---

Redis is an open source, in-memory data structure store, used as database, cache and message broker.

## Redis version

The version currently installed by the add-on is : Redis 6.0.10

## Redis administration with Redsmin

Each Redis add-on provides a [Redsmin](https://www.redsmin.com) dashboard, which allows
you to query and monitor your redis database activity.

{{< readfile "/content/partials/db-backup.md" >}}

A backup is a `tar.gz` archive containing both the `.rdb` and `.aof` files. You can extract this archive and run `redis-server` in the extracted folder to access data.

## Leader / follower topology

By default, all redis add-ons are configured as leaders. You can set up a redis add-on as a follower from the add-on panel (in the "Add-on information" tab). You need to set the leader
information (host, port, password) to start the replication. The add-on panel will display the sync process status so that you know when the synchronisation is done.

While a redis database is configured as a follower, it's read-only.

## Default retention policy

By default, the eviction policy is `noeviction`. If you plan to use Redis as a LRU cache,
please contact the support to change its policy.
