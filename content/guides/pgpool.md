---
type: docs
linkTitle: Pgpool-II
title: Configure Pgpool-II for PostgreSQL
description: Enable Pgpool-II and connect applications to Clever Cloud PostgreSQL through a local connection pool
keywords:
- connection pooling
- pgpool
- postgresql
aliases:
- /deploy/addon/postgresql/pgpool
- /doc/deploy/addon/postgresql/pgpool
- /pgpool
---

[Pgpool-II](https://www.pgpool.net/) runs between your application and a linked [PostgreSQL add-on](/doc/addons/postgresql). It provides local connection pooling and can distribute read queries when Clever Cloud has configured PostgreSQL streaming replication for your organisation.

Pgpool-II is available in every runtime except Docker, where processes and services are managed by the container image.

## Enable Pgpool-II

Link a PostgreSQL add-on to the application, then enable Pgpool-II:

```bash
clever env set CC_ENABLE_PGPOOL true
```

The platform starts one Pgpool-II process on each application instance and injects these variables:

- `CC_PGPOOL_SOCKET_PATH` is the local Unix socket directory your application connects to
- `PGHOST`, `PGDATABASE` and `PGUSER` let PostgreSQL clients use Pgpool-II without additional connection arguments

Your application must keep using the linked add-on credentials from `POSTGRESQL_ADDON_USER`, `POSTGRESQL_ADDON_PASSWORD` and `POSTGRESQL_ADDON_DB`. Use port `5432` when a client requires an explicit port, because Pgpool-II listens on the standard PostgreSQL port through its local socket.

## Connect your application

### PHP with PDO

Use the socket directory as the host in a [PDO PostgreSQL DSN](https://www.php.net/manual/en/ref.pdo-pgsql.connection.php):

```php
<?php

$dsn = sprintf(
    'pgsql:host=%s;port=5432;dbname=%s',
    getenv('CC_PGPOOL_SOCKET_PATH'),
    getenv('POSTGRESQL_ADDON_DB')
);

$connection = new PDO(
    $dsn,
    getenv('POSTGRESQL_ADDON_USER'),
    getenv('POSTGRESQL_ADDON_PASSWORD'),
    [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
);
```

### Node.js with node-postgres

Use the socket directory as `host` with [`node-postgres`](https://node-postgres.com/features/connecting):

```javascript
import pg from "pg";

const pool = new pg.Pool({
  host: process.env.CC_PGPOOL_SOCKET_PATH,
  port: 5432,
  user: process.env.POSTGRESQL_ADDON_USER,
  password: process.env.POSTGRESQL_ADDON_PASSWORD,
  database: process.env.POSTGRESQL_ADDON_DB,
});
```

## Size the connection pool

`CC_PGPOOL_NUM_INIT_CHILDREN` controls the number of concurrent client sessions accepted by each Pgpool-II process and defaults to `16`. `CC_PGPOOL_MAX_POOL` controls how many backend connections each child can cache for different user and database pairs and defaults to `1`.

During a rolling deployment, old and new instances can run simultaneously. The maximum number of client sessions can therefore temporarily reach:

```text
2 × maximum running instances × CC_PGPOOL_NUM_INIT_CHILDREN
```

Keep this result below the PostgreSQL plan's connection limit and reserve capacity for administration or other clients. See the [environment variables reference](/doc/reference/reference-environment-variables/#pgpool-ii) for connection lifetime, logging, health check and query cache settings.

## Configure read replicas

Pgpool-II can distribute read queries only after Clever Cloud has configured PostgreSQL streaming replication. Contact [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice) or [Sales](https://www.clever.cloud/en/contact-sales) to discuss this setup.

Once replication is available, define `CC_PGPOOL_FOLLOWERS` as a JSON array containing each follower's direct hostname, direct port and weight:

```json
[
  {
    "hostname": "FOLLOWER_DIRECT_HOST",
    "port": "FOLLOWER_DIRECT_PORT",
    "weight": "1"
  }
]
```

The leader's weight is configured with `CC_PGPOOL_LEADER_WEIGHT`. Higher follower weights direct a larger share of eligible read queries to followers. The Ruby Deployer uses the linked leader's direct address when direct variables are available and otherwise uses its standard add-on address.

## Inspect Pgpool-II

Open an [SSH session](/doc/administrate/ssh-clever-tools/) to an application instance and start `psql`:

```bash
clever ssh
psql
```

Pgpool-II supports administrative SQL commands such as:

```sql
SHOW POOL_NODES;
SHOW POOL_PROCESSES;
SHOW POOL_POOLS;
SHOW POOL_BACKEND_STATS;
```

The local [PCP commands](https://www.pgpool.net/docs/latest/en/html/pcp-commands.html) are preconfigured through `/home/bas/.pcppass`. For example, use the local socket to inspect status or attach and detach a configured follower:

```bash
pcp_pool_status -h /tmp -U pcp -w
pcp_detach_node -h /tmp -U pcp -w -n 1
pcp_attach_node -h /tmp -U pcp -w -n 1
```

Detaching the leader or an unreplicated backend interrupts database access. Only manage nodes that are already part of a supported replication setup.

## Learn more

- [Pgpool-II documentation](https://www.pgpool.net/docs/latest/en/html/) — Configure pooling, load balancing and monitoring
- [PostgreSQL add-ons](/doc/addons/postgresql) — Create, link and administer PostgreSQL databases
- [Environment variables reference](/doc/reference/reference-environment-variables/#pgpool-ii) — Review all Pgpool-II settings available on Clever Cloud
