---
type: docs
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
aliases:
- /doc/deploy/addon/redis
type: docs
---

Redis is an open source, in-memory data structure store, used as database, cache and message broker.

## Version

The version currently installed by the add-on are the following :

{{< software_versions_shared_dedicated redis>}}

{{< content "db-backup" >}}

A backup is a `tar.gz` archive containing both the `.rdb` and `.aof` files. You can extract this archive and run `redis-server` in the extracted folder to access data.

{{< content "dbMigration" >}}

## Leader / follower topology

By default, all redis add-ons are configured as leaders. You can set up a redis add-on as a follower from the add-on panel (in the "Add-on information" tab). You need to set the leader
information (host, port, password) to start the replication. The add-on panel will display the sync process status so that you know when the synchronisation is done.

While a redis database is configured as a follower, it's read-only.

## Redis-cli usage

You can use Redis URI to connect to your databases with -u option. However, the generated URI in the information tab (`REDIS_URL`) of you add-on is not a legal syntax to use `redis-cli`.

This is the correct syntax for `redis-cli` URI : *redis ://password@host:port[/database]*

{{< content "kv-explorer" >}}

## Default retention policy

By default, the eviction policy is `noeviction`. If you plan to use Redis as a LRU cache,
please contact the support to change its policy.

## 🔑 Rights and permissions

Add-ons are managed services, meaning that users have **controlled access** to the server. They are granted access to all proposed operations except changing the server configuration. Based on the plan, they are granted access to a fix amount of databases. This ensures optimal performances and security for managed services as configured by Clever Cloud.

Authorized actions:
- Access to one or more databases depending on your plan.
- Access to all Redis operations except *CONFIG* and *CLUSTER*.
- Set up replica via clever cloud console.

If you think your system might require more advanced administrative access, [contact Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) to explain your use case, and we will work with you to find a solution.

Here is the list of actions that you won't be able to perform:
- Server configuration update.
- Modules installation.
- Backup frequency or retention control.

Ask Clever Cloud support if you want to perform one of these actions.
