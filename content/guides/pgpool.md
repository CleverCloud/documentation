---
type: docs
title: Pgpool-II
position: 3
shortdesc: How to configure and use Pgpool-II for PostgreSQL add-ons
tags:
- addons
keywords:
- balancing
- connection
- limit
- load
- pgpool
- pool
- postgres
- proxy
- sql
aliases:
- /doc/deploy/addon/postgresql/pgpool
type: docs
---

Pgpool-II is a tool available on application instances to help manage your connection pool and load balancing of your PostgreSQL add-ons.

{{< callout type="warning" >}}
Pgpool-II is not available on Docker instances. If you want to use Pgpool-II, you can add it and configure it in your Dockerfile.
{{< /callout >}}

## What's Pgpool-II?

{{< content "pgpool" >}}

## Why use Pgpool-II?

**Connection pooling**: Pgpool-II maintains established connections to the PostgreSQL servers, and reuses them whenever a new connection with the same properties (user name, database, protocol version, and other connection parameters if any) comes in. It reduces the connection overhead, and improves the system's overall throughput.

**Load balancing**: If a database is replicated (because running in either replication mode or native replication mode), performing a `SELECT` query on any server will return the same result. Pgpool-II takes advantage of the replication feature in order to reduce the load on each PostgreSQL server. It does that by distributing `SELECT` queries among available servers, improving the system's overall throughput. In an ideal scenario, read performance could improve proportionally to the number of PostgreSQL servers. Load balancing works best in a scenario where a lot of users execute many read-only queries at the same time.

**Automated fail over**: If one of the database servers goes down or becomes unreachable, Pgpool-II will detach it and will continue operations by using the rest of the database servers. Some sophisticated features that help for automated failovers including timeouts and retries.

**Limiting Exceeding Connections**: PostgreSQL puts a limit on the amount of concurrent connections, so that new connections are rejected when this number is reached. Raising this maximum number of connections, however, increases resource consumption and has a negative impact on overall system performance. Pgpool-II also limits the number of concurrent connections, but extra connections will be queued instead of returning an error immediately. Or you can configure it to return an error when the connection limit is exceeded (`4.1` or later).

**In Memory Query Cache**: In memory query cache allows to save a `SELECT` statement with its result. If an identical `SELECT` comes in, Pgpool-II returns the value from cache. Since neither SQL parsing nor access to PostgreSQL are involved, using in memory cache is extremely fast. On the other hand, it might be slower than the normal path in some cases, because it adds some overhead of storing cache data.

The various features are available in the [official Pgpool documentation](https://www.pgpool.net/docs/latest/en/html/index.html).

{{< callout type="info" >}}
PostreSQL add-ons only support the **Streaming** mode, which is the most used and recommended mode for Pgpool-II. If you need other modes or features that aren't supported on Clever Cloud, contact [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice).
{{< /callout >}}

## How to configure Pgpool-II

### Generate direct variables for PG

Go to the "Add-on dashboard" tab of your PostgreSQL add-ons and click on the "Generate direct hostname and port" button.

### Enable Pgpool-II

In order to configure Pgpool-II, the first thing to do is to link your PostgreSQL add-on. To do that, you can go to the `Service Dependencies` page of your application
and select your PostgreSQL add-on.

Once linked, you can enable the Pgpool-II feature by defining the following environment variable: `CC_ENABLE_PGPOOL=true`.
If you ever need to stop using Pgpool-II, you can remove this variable or set it to `false`.

Your application will use a Unix Domain Socket to connect to Pgpool-II. Unix domain sockets are faster than TCP sockets because there is no handshake and the connection is made locally on the same machine. A special environment variable will be injected to your environment variables: `CC_PGPOOL_SOCKET_PATH`. This variable contains the path to the Unix Domain Socket you have to connect to. See [Usage](#usage) below for some examples on how to use it.

The available Pgpool-II variables and their descriptions are available on our [environment variables reference page](../../doc/reference/reference-environment-variables/).

### Concurrent session and pool size

You can use the `CC_PGPOOL_NUM_INIT_CHILDREN` and `CC_PGPOOL_MAX_POOL` environment variables to set the number of **concurrent sessions** and the number of **connection pool caches per connection**.

Let's take an example where you have 3 PostgreSQL servers, and the `CC_PGPOOL_NUM_INIT_CHILDREN` variable configured with a value of **32**.

On startup, Pgpool-II will start **32** processes, one process per connection. The `CC_PGPOOL_MAX_POOL` variable is used to configure the number of cached connections per connection (process). This option is mostly used when you have different credentials for the same PostgreSQL server (database, user…). But in the case of **Streaming** mode on Clever Cloud, you have access to only one database, and the credentials are the same on all add-ons with binary replication. You should not need to change the default value of this variable (**1** by default).

An example of the `SHOW POOL_POOLS;` command with `CC_PGPOOL_NUM_INIT_CHILDREN=32` and `CC_PGPOOL_MAX_POOL=1`:

```shell
psql -U u1mgltc2ezvkylo2cjno -d bjzfhkl5qcdhdqatyqjk

bjzfhkl5qc**********=> show pool_pools;
 pool_pid |     start_time      | pool_id | backend_id |       database       |       username       |     create_time     | pool_backendpid |
----------+---------------------+---------+------------+----------------------+----------------------+---------------------+-----------------+
 3526     | 2021-06-02 15:22:12 | 0       | 0          | bjzfhkl5qcdhdqatyqjk | u1mgltc2ezvkylo2cjno | 2021-06-02 15:22:35 | 1520665         |
 3526     | 2021-06-02 15:22:12 | 0       | 1          | bjzfhkl5qcdhdqatyqjk | u1mgltc2ezvkylo2cjno | 2021-06-02 15:22:35 | 1665071         |
 3526     | 2021-06-02 15:22:12 | 0       | 2          | bjzfhkl5qcdhdqatyqjk | u1mgltc2ezvkylo2cjno | 2021-06-02 15:22:35 | 531483          |
 3527     | 2021-06-02 15:22:12 | 0       | 0          |                      |                      |                     | 0               |
 3527     | 2021-06-02 15:22:12 | 0       | 1          |                      |                      |                     | 0               |
 3527     | 2021-06-02 15:22:12 | 0       | 2          |                      |                      |                     | 0               |
 3528     | 2021-06-02 15:22:12 | 0       | 0          |                      |                      |                     | 0               |
 3528     | 2021-06-02 15:22:12 | 0       | 1          |                      |                      |                     | 0               |
 3528     | 2021-06-02 15:22:12 | 0       | 2          |                      |                      |                     | 0               |
 ...      | ...                 | .       | .          |                      |                      |                     | .               |
```

We can see the 32 available processes (**3526**, **3527**, **3528...**), and active connections for process **3526**, with an open connection for each PostgreSQL server (**1520665**, **1665071** and **531483**).

If a process remains inactive for more than **300** seconds, it will be deleted and a new process will take its place. This value can be configured with the `CC_PGPOOL_CHILD_LIFE_TIME` variable. This is a measure to prevent memory leaks and other unexpected errors in Pgpool-II children.

Cached connections for each process do not have a default expiration time, but you can set one if needed with the `CC_PGPOOL_CONNECTION_LIFE_TIME` variable.

It's also possible to specify the lifetime of a Pgpool-II child process (`CC_PGPOOL_CHILD_MAX_CONNECTIONS`) and the time in seconds to disconnect a client if it remains inactive since the last request (`CC_PGPOOL_CLIENT_IDLE_LIMIT`).

### Replication and load balancing

Use Pgpool-II to distribute the load and separate **WRITE** and **READ** queries between your PostgreSQL servers.

When using the **Streaming** mode, it's not Pgpool-II that manages the replication of your databases. Clever Cloud engineers must manually set up the replication on the PostgreSQL side, otherwise known as **binary**, **Hot Standby** or **Streaming** replication. To schedule this procedure, you can contact [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice) or make a request via our [sales form](https://www.clever-cloud.com/en/contact-sales).

Once replication is in place, you can use the `CC_PGPOOL_FOLLOWERS` environment variable to add the followers to your Pgpool-II configuration. This variable is in **JSON** format, and must contain the **host**, **port** and **weight** of each follower.

{{< callout type="info" >}}
For the `HOST` and `PORT`, you must use the values of the `POSTGRESQL_ADDON_DIRECT_HOST` and `POSTGRESQL_ADDON_DIRECT_PORT` variables.
{{< /callout >}}

An example of the `CC_PGPOOL_FOLLOWERS` variable with two followers:

```json{linenos=table}
[
  {
    "hostname": "<HOST>",
    "port": "<PORT>",
    "weight": "1"
  },
  {
    "hostname": "<HOST>",
    "port": "<PORT>",
    "weight": "1"
  }
]
```

The weight is used to specify the load balance ratio of the backends, you can also configure the weight of the leader with the `CC_PGPOOL_LEADER_WEIGHT` variable.

{{< callout type="info" >}}
You can set a higher value for followers to avoid overloading the leader with `SELECT` queries that could be made on followers.
{{< /callout >}}

Many other **load balancing** options are configurable with environment variables. You can refer to our [environment variables reference page](../../doc/reference/reference-environment-variables/) and the [official Pgpool-II documentation](https://www.pgpool.net/docs/latest/en/html/runtime-config-load-balancing.html) for more information.

### Health check

Pgpool-II periodically connects to the configured PostgreSQL backends to detect any error on the servers or networks. If an error is detected, Pgpool-II performs failover or degeneration depending on the configurations.

The health check is not activated by default, but you can activate it with the `CC_PGPOOL_HEALTH_CHECK_PERIOD` variable.

Many other health check options are configurable with environment variables, such as:

- `CC_PGPOOL_HEALTH_CHECK_TIMEOUT`: Specifies the timeout in seconds to give up connecting to the backend PostgreSQL if the TCP connect does not succeed within this time.
- `CC_PGPOOL_HEALTH_CHECK_MAX_RETRIES`: Specifies the maximum number of retries before giving up and initiating failover when health check fails.
- `CC_PGPOOL_HEALTH_CHECK_RETRY_DELAY`: Specifies the amount of time (in seconds) to sleep before retrying after a failed health check retries.
- `CC_PGPOOL_CONNECT_TIMEOUT`: Specifies the amount of time in milliseconds before giving up connecting to backend using `connect()` system call.

You can consult the [official Pgpool-II documentation](https://www.pgpool.net/docs/latest/en/html/runtime-config-health-check.html) to get more information about the **health check**.

### In memory cache

In memory cache saves the pair of `SELECT` statement and its result. If the same `SELECT` comes in, Pgpool-II returns the value from cache. This feature can be activated with the `CC_PGPOOL_MEMORY_CACHE_ENABLED=on` variable.

Many other in memory cache options are configurable with environment variables, such as:

- `CC_PGPOOL_MEMQCACHE_TOTAL_SIZE`: Specifies the shared memory cache size in bytes.
- `CC_PGPOOL_MEMQCACHE_MAX_NUM_CACHE`: Specifies the number of cache entries. This is used to define the size of cache management space.
- `CC_PGPOOL_MEMQCACHE_CACHE_BLOCK_SIZE`: Specifies the cache block size.
- `CC_PGPOOL_MEMQCACHE_EXPIRE`: Specifies the life time of query cache in seconds.
- `CC_PGPOOL_MEMQCACHE_AUTO_CACHE_INVALIDATION`: Automatically deletes the cache related to the updated tables.
- `CC_PGPOOL_MEMQCACHE_MAXCACHE`: Specifies the maximum size in bytes of the `SELECT` query result to be cached.
- `CC_PGPOOL_CACHE_SAFE_MEMQCACHE_TABLE_LIST`: Specifies a comma-separated list of table names whose `SELECT` results should be cached by Pgpool-II.
- `CC_PGPOOL_CACHE_UNSAFE_MEMQCACHE_TABLE_LIST`: Specifies a comma-separated list of table names whose `SELECT` results should NOT be cached by Pgpool-II.

You can consult the [official Pgpool-II documentation](https://www.pgpool.net/docs/latest/en/html/runtime-in-memory-query-cache.html#GUC-MEMQCACHE-AUTO-CACHE-INVALIDATION) to get more information about the **in memory cache**.

### Scalability

When the scalability of your application is enabled, you may need to tweak the `CC_PGPOOL_NUM_INIT_CHILDREN` value. This is what we are going to see here.

Auto scalability will add or remove instances following your needs. This means that you may have multiple instances running at the same time for a certain period of time.
If your application restarts, you will have `your current instance number * 2`  instances running in parallel while the deployment finishes and the old instances are stopped.
A new deployment **starts** new instances alongside the old ones.

This means that have up to `maximum scalability * 2` instances can run at the same time. And if all of your instances open the maximum connections they are allowed to,
it means there will be up to `maximum scalability * 2 * CC_PGPOOL_NUM_INIT_CHILDREN` connections at the same time. We will call this result `MaxCon`.

{{< callout type="warning" >}}
Each PostgreSQL add-on has a connection limit which varies following the plan you are using. You must be sure that `MaxCon` doesn't exceed your plan's max connections. If it does, you might have issues connecting to the remote PostgreSQL add-on. You have to adjust `CC_PGPOOL_NUM_INIT_CHILDREN` to a number that makes sense for your scalability parameters.
{{< /callout >}}

#### Example

Let's say that I'm hosting a simple PHP application on `1 XS` instance, with a scalability that can go up to `4 M` instances. And I'm using the PostgreSQL `S Small Space` plan
which has a connection limit of `125`.

Now my application receives a lot of traffic and scales up to `4 M` instances. But at the same time, I also need to deploy a hot fix. This means that `4 new M` instances will be started, alongside the already existing `4 M` instances. I need to make sure that `MaxCon` doesn't go above `125`.

Here is the summary:

- 8 instances: 4 currently running, 4 currently deploying my hot fix
- 125 max connections: the maximum number of connections of my PostgreSQL add-on's plan
- 5 other connections: I want to be able to use PG Studio or any CLI tool at the same time, in case I need it

`CC_PGPOOL_NUM_INIT_CHILDREN = ( (125 - 5) / 8 ) = 15`. If I set `CC_PGPOOL_NUM_INIT_CHILDREN` to `15`, each instance should have enough connections to query the database without errors. And it also leaves me some spare connections (`5`) available if anything goes wrong and I need to connect to my database using a CLI tool or PG Studio.

## Tips / debug

### Connecting to Pgpool-II

Connect via [ssh](../../doc/administrate/ssh-clever-tools/) to your application and use the [psql](https://docs.postgresql.fr/10/app-psql.html) command.

```bash
ssh -t ssh@sshgateway-clevercloud-customers.services.clever-cloud.com <app_id>
```

Then, launch the `psql` command with :

```bash
psql
```

### Showing configured nodes

You can use the [`SHOW POOL_NODES;`](https://www.pgpool.net/docs/latest/en/html/sql-show-pool-nodes.html) command.

```shell
bjzfhkl5qc**********=> SHOW POOL_NODES;
 node_id |                         hostname                          | port | status | lb_weight |  role   | select_cnt | load_balance_node |
---------+-----------------------------------------------------------+------+--------+-----------+---------+------------+-------------------+
 0       | bjzfhkl5qc**********-postgresql.services.clever-cloud.com | 57** | up     | 0.333333  | primary | 0          | false             |
 1       | b3diajq7iy**********-postgresql.services.clever-cloud.com | 57** | up     | 0.333333  | standby | 2          | false             |
 2       | bmtwtemn40**********-postgresql.services.clever-cloud.com | 57** | up     | 0.333333  | standby | 1          | true              |
```

### Watching Pgpool-II processes

You can use the [`SHOW POOL_PROCESSES;`](https://www.pgpool.net/docs/latest/en/html/sql-show-pool-processes.html) command to see processes waiting for connections and processing a connection.

```shell
bjzfhkl5qc**********=> SHOW POOL_PROCESSES;
 pool_pid |     start_time      |       database       |       username       |     create_time     | pool_counter
----------+---------------------+----------------------+----------------------+---------------------+--------------
 21554    | 2021-06-03 11:28:36 | bjzfhkl5qc********** | u5dh6v2ymn********** | 2021-06-03 11:28:48 | 1
 11409    | 2021-06-02 19:54:53 |                      |                      |                     |
 11410    | 2021-06-02 19:54:53 |                      |                      |                     |
 21566    | 2021-06-03 11:29:20 |                      |                      |                     |
```

### Listing managed pools

You can use the [`SHOW POOL_POOLS;`](https://www.pgpool.net/docs/latest/en/html/sql-show-pool-pools.html) command to see the list of pools managed by Pgpool-II.

```shell
bjzfhkl5qc**********=> SHOW POOL_POOLS;
 pool_pid |     start_time      | pool_id | backend_id |       database       |       username       |     create_time     | pool_backendpid |
----------+---------------------+---------+------------+----------------------+----------------------+---------------------+-----------------+
 21554    | 2021-06-03 11:28:36 | 0       | 0          | bjzfhkl5qc********** | u5dh6v2ymn********** | 2021-06-03 11:28:48 | 1549123         |
 21554    | 2021-06-03 11:28:36 | 0       | 1          | bjzfhkl5qc********** | u5dh6v2ymn********** | 2021-06-03 11:28:48 | 1695967         |
 21554    | 2021-06-03 11:28:36 | 0       | 2          | bjzfhkl5qc********** | u5dh6v2ymn********** | 2021-06-03 11:28:48 | 562378          |
 11409    | 2021-06-02 19:54:53 | 0       | 0          |                      |                      |                     | 0               |
 11409    | 2021-06-02 19:54:53 | 0       | 1          |                      |                      |                     | 0               |
 11409    | 2021-06-02 19:54:53 | 0       | 2          |                      |                      |                     | 0               |
 11410    | 2021-06-02 19:54:53 | 0       | 0          |                      |                      |                     | 0               |
 11410    | 2021-06-02 19:54:53 | 0       | 1          |                      |                      |                     | 0               |
 11410    | 2021-06-02 19:54:53 | 0       | 2          |                      |                      |                     | 0               |
 21566    | 2021-06-03 11:29:20 | 0       | 0          |                      |                      |                     | 0               |
 21566    | 2021-06-03 11:29:20 | 0       | 1          |                      |                      |                     | 0               |
 21566    | 2021-06-03 11:29:20 | 0       | 2          |                      |                      |                     | 0               |
```

### Statistics of SQL commands

You can use the [`SHOW POOL_BACKEND_STATS;`](https://www.pgpool.net/docs/latest/en/html/sql-show-pool-backend-stats.html) command to see the statistics of SQL commands.

```shell
bjzfhkl5qc**********=> SHOW POOL_BACKEND_STATS;
 node_id |                         hostname                          | port | status |  role   | select_cnt | insert_cnt | update_cnt | delete_cnt |
---------+-----------------------------------------------------------+------+--------+---------+------------+------------+------------+------------+
 0       | bjzfhkl5qc**********-postgresql.services.clever-cloud.com | 57** | up     | primary | 0          | 0          | 0          | 1          |
 1       | b3diajq7iy**********-postgresql.services.clever-cloud.com | 57** | up     | standby | 2          | 0          | 0          | 0          |
 2       | bmtwtemn40**********-postgresql.services.clever-cloud.com | 57** | up     | standby | 1          | 0          | 0          | 0          |
```

### Using the PCP command

The [PCP tool](https://www.pgpool.net/docs/latest/en/html/pcp-commands.html) is pre-configured and available on your application.

```bash
pcp_pool_status -h /tmp -U pcp -w
```

### Managing nodes

Attach or detach a given node to Pgpool-II;

```bash
pcp_pool_status -h /tmp -U pcp -w -n 0
pcp_pool_status -h /tmp -U pcp -w -n 0
```

### Statistical data

Display the statistical data of the health check on the given node ID

```bash
pcp_pool_status -h /tmp -U pcp -w -n 0 -v
Node Id                       : 0
Host Name                     : bjzfhkl5qc**********-postgresql.services.clever-cloud.com
Port                          : 57**
Status                        : up
Role                          : primary
Last Status Change            : 2021-06-02 19:54:53
Total Count                   : 0
Success Count                 : 0
Fail Count                    : 0
Skip Count                    : 0
Retry Count                   : 0
Average Retry Count           : 0.000000
Max Retry Count               : 0
Max Health Check Duration     : 0
Minimum Health Check Duration : 0
Average Health Check Duration : 0.000000
Last Health Check             :
Last Successful Health Check  :
Last Skip Health Check        :
Last Failed Health Check      :
```

You can find all PCP commands in the [official Pgpool-II documentation](https://www.pgpool.net/docs/latest/en/html/pcp-commands.html).

## Usage

{{< callout type="info" >}}
Please note that to connect to Pgpool-II, the default port **5432** must be used. So if you already have a different port set in your code, you have to change it or simply remove the port from the connection information.
{{< /callout >}}

### PHP using PDO

Using [PDO](https://www.php.net/manual/fr/ref.pdo-pgsql.connection.php), you have to use the `unix_socket` option in your DSN:

```php{linenos=table}
<?php
// This variable is injected during deployment
$host = getenv("CC_PGPOOL_SOCKET_PATH");
// Get the database name from the environment
$database = getenv("POSTGRESQL_ADDON_DB");
// Get the database user from the environment
$user = getenv("POSTGRESQL_ADDON_USER");
// Get the database password from the environment
$password = getenv("POSTGRESQL_ADDON_PASSWORD");

$dsn = "pgsql:host=$host;dbname=$database;user=$user;password=$password";

try {
    $conn = new PDO($dsn);
    if($conn){
  echo "Successfully connected to $dbname!";
     }
} catch (PDOException $e){
     echo $e->getMessage();
}
?>
```

### WordPress

For WordPress, you can change the `DB_HOST` variable in your `wp-config.php`:

```php{linenos=table}
// To connect using a socket, the syntax is: `localhost:/path/to/socket`
define( 'DB_HOST', "localhost:" . getenv("CC_PGPOOL_SOCKET_PATH") );
```

### Node.js

On Node.js, using the `pg` npm package:

```javascript{linenos=table}
const { Client } = require('pg');
client = new Client({
    // This variable is injected during the deployment
    host: process.env["CC_PGPOOL_SOCKET_PATH"],
    // Get the database name from the environment
    database: process.env["POSTGRESQL_ADDON_DB"],
    // Get the database user from the environment
    user: process.env["POSTGRESQL_ADDON_USER"],
    // Get the database password from the environment
    password: process.env["POSTGRESQL_ADDON_PASSWORD"],
});

client.connect();
```
