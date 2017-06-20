---
title: Redis add-on
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

# Redis

Redis is an open source, in-memory data structure store, used as database, cache and message broker.

## Redis administration with Redsmin

Each Redis addon provides a [Redsmin](https://www.redsmin.com) dasboard, which allows
you to query and monitor your redis database activity.

## Backups

Redis databases are backed up once a day. You can download backups from the addon panel
(in the "backups" tab). A backup is a `tar.gz` archive containing both the `.rdb` and `.aof` files. You can extract this archive and run `redis-server` in the extracted folder
to access data.

## Leader / follower topology

By default, all redis addons are configured as leaders. You can set up a redis addon as a follower from the addon panel (in the "Addon information" tab). You need to set the leader
information (host, port, password) to start the replication. The addon panel will display the sync process status so that you know when the synchronisation is done.

While a redis database is configured as a follower, it's read-only.

## Default retention policy

By default, the eviction policy is `noeviction`. If you plan to use Redis as a LRU cache,
please contact the support to change its policy.