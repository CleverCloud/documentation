---
type: docs
title: ProxySQL

shortdesc: How to configure and use ProxySQL for MySQL add-ons
tags:
- addons
keywords:
- proxysql
- proxy
- sql
- mysql
- connection
- limit
- pool
aliases:
- /doc/deploy/addon/mysql/proxysql
type: docs
---

ProxySQL is a tool available on applications instances to help you manage your connection pool towards your MySQL add-on.

{{< callout type="warning" >}}
ProxySQL is not available on Docker instances. If you want to use ProxySQL, you can add it and configure it in
your Dockerfile.
{{< /callout >}}

## What is ProxySQL

{{< content "proxysql" >}}

## When do I need ProxySQL

You might need ProxySQL if your application can't manage a connection pool. This is usually the case with PHP applications or any other application that do not
have a connection pooling policy in place.

{{< callout type="info" >}}
A connection pool will cache your database connections and keep them open for future requests.
The connections can then be reused if needed or closed if they weren't used after a certain time.
{{< /callout >}}

By using connection pooling from ProxySQL to your MySQL add-on, you make sure that a certain number of connections stay open to your add-on, leading to faster requests.

For example, on a PHP application, each HTTP request will spawn a new Apache worker and your PHP code will be executed. If your application does an SQL request, a new TCP connection will be open to the remote MySQL add-on. Once your SQL request is done, the TCP connection will be closed and a new one will need to be opened on the next SQL query.

Each new connection means a new [TCP handshake](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Connection_establishment) which takes some time.
If you use TLS to secure the connection, then there is an [aditionnal handshake](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_handshake). All of this, multiplied
by the number of connections you make to your add-on can greatly increase your application's response time.

One of the goals of ProxySQL is to keep the connections open to your MySQL add-on. Your application can then connect to the local proxy
using a [Unix Domain Socket](https://en.wikipedia.org/wiki/Unix_domain_socket) for each SQL request it has to do.
Unix Domain Sockets are faster than TCP sockets because there are no handshakes and the connection is made locally on the same machine.

When ProxySQL receives a new SQL query, it will open a new connection to the remote MySQL add-on if no connection is currently available. But if one is available, it will be reused and the query should take less time. The connection will then be kept for further use.

## How to configure ProxySQL

In order to configure ProxySQL, the first thing to do is to link your MySQL add-on. To do that, you can go to the `Service Dependencies` page of your application
and select your MySQL add-on.

Once linked, you can enable the ProxySQL feature by defining the following environment variable: `CC_ENABLE_MYSQL_PROXYSQL=true`.
If you ever need to stop using ProxySQL, you can remove this variable or set it to `false`.

You can customize some other parameters:

- `CC_MYSQL_PROXYSQL_MAX_CONNECTIONS`: Integer. This is the maximum connections ProxySQL will open to your add-on. See the [Scalability](#scalability) part
below for more explanations on how to customize this variable. Defaults to `10`.
- `CC_MYSQL_PROXYSQL_USE_TLS`: Boolean (`true` or `false`). This controls whether ProxySQL should open a secure connection using `TLS` to your add-on. Defaults to `true`.

To connect to ProxySQL, a special environment variable will be injected to your environment variables: `CC_MYSQL_PROXYSQL_SOCKET_PATH`. This variable contains the
path to the Unix Domain Socket you have to connect. See [Usages](#usages) below for some example on how to use it.

### Scalability

When the scalability of your application is enabled, you may need to tweak the `CC_MYSQL_PROXYSQL_MAX_CONNECTIONS` value. This is what we are going to see here.

Auto scalability will add or remove instances following your needs. This means that you may have multiple instances running at the same time for a certain period of time.
If your application restarts, you will have `your current instance number * 2`  instances running in parallel while the deployment finishes and the old instances are stopped.
A new deployment **starts** new instances with the old ones alongside them.

This means that have up to `maximum scalability * 2` instances can run at the same time. And if all of your instances open the maximum connections they are allowed to,
it means there will be up to `maximum scalability * 2 * CC_MYSQL_PROXYSQL_MAX_CONNECTIONS` connections at the same time. We will call this result `MaxCon`.

Each MySQL add-on has a connection limit which varies following the plan you are using. You must be sure that `MaxCon` doesn't exceed your plan's max connections. If it does, you might have issues connecting to the remote MySQL add-on. You have to adjust `CC_MYSQL_PROXYSQL_MAX_CONNECTIONS` to a number that makes sense for your scalability parameters.

#### Example

Let's say that I'm hosting a simple PHP application on `1 XS` instance, with a scalability that can go up to `4 M` instances. And I'm using the MySQL `S Small Space` plan
which has a connection limit of `125`.

Now my application receives a lot of traffic and scales up to `4 M` instances. But at the same time, I also need to deploy a hot fix. This means that `4 new M` instances will be started, alongside the already existing `4 M` instances. I need to make sure that `MaxCon` doesn't go above `125`.

Here is the summary:

- 8 instances: 4 currently running, 4 currently deploying my hot fix
- 125 max connections: the maximum number of connections of my MySQL add-on's plan
- 5 other connections: I want to be able to use PHPMyAdmin or any CLI tool at the same time, in case I need it

`CC_MYSQL_PROXYSQL_MAX_CONNECTIONS = ( (125 - 5) / 8 ) = 15`. If I set `CC_MYSQL_PROXYSQL_MAX_CONNECTIONS` to `15`, each instance should have enough connections to query the database without errors. And it also let you some spare connections (`5`) available if anything goes wrong and you need to connect to your database using a CLI tool or PHPMyAdmin.

## Usages

### PHP using PDO

Using [PDO](https://www.php.net/manual/en/ref.pdo-mysql.connection.php), you have to use the `unix_socket` option in your DSN:

```php
<?php
// Get the database name from the environment
$db = getenv("MYSQL_ADDON_DB");
// Get the database user from the environment
$user = getenv("MYSQL_ADDON_USER");
// Get the database password from the environment
$pass = getenv("MYSQL_ADDON_PASSWORD");
// This variable is injected during the deployment
$socket = getenv("CC_MYSQL_PROXYSQL_SOCKET_PATH");
$dsn = "mysql:unix_socket=$socket;dbname=$db";
try {
     $pdo = new PDO($dsn, $user, $pass);
} catch (PDOException $e) {
     throw new PDOException($e->getMessage(), (int)$e->getCode());
}
```

### Wordpress

For Wordpress, you can change the `DB_HOST` variable in your `wp-config.php`:

```php
// To connect using a socket, the syntax is: `localhost:/path/to/socket`
define( 'DB_HOST', "localhost:" . getenv("CC_MYSQL_PROXYSQL_SOCKET_PATH") );
```

### Symfony

For symfony, you will need to edit its [configuration](https://symfony.com/doc/current/configuration.html#configuration-environments).

A working example would be:

```yaml
dbal:
  unix_socket: '%env(CC_MYSQL_PROXYSQL_SOCKET_PATH)%'
  url: 'mysql://%env(MYSQL_ADDON_USER)%:%env(MYSQL_ADDON_PASSWORD)%@localhost/%env(MYSQL_ADDON_DB)%?serverVersion=%env(MYSQL_ADDON_VERSION)%'
```

### Node.js

On Node.js, using the `mysql` npm package, you have to set the `socketPath` property:

```javascript
const mysql      = require('mysql');
const connection = mysql.createConnection({
  // Get ProxySQL unix domain socket path from the environment
  socketPath : process.env["CC_MYSQL_PROXYSQL_SOCKET_PATH"],
  // Get the database user from the environment
  user       : process.env["MYSQL_ADDON_USER"],
  // Get the database password from the environment
  password   : process.env["MYSQL_ADDON_PASSWORD"],
  // Get the database name from the environment
  database   : process.env["MYSQL_ADDON_DB"]
});
connection.connect(function(err) {
  if (err) {
    console.error('error connecting: ' + err.stack);
    return;
  }

  console.log('connected as id ' + connection.threadId);
});
```

## Metrics

ProxySQL exposes some metrics using Prometheus. Some of those metrics are ingested in our metrics system. You can then explore them
in the [Web Console]({{< ref "doc/metrics#display-metrics" >}}).

Here is the list of currently tracked metrics, those may evolve over time:

- `prometheus.proxysql_access_denied_max_connections_total`
- `prometheus.proxysql_access_denied_max_user_connections_total`
- `prometheus.proxysql_access_denied_wrong_password_total`
- `prometheus.proxysql_client_connections_connected`
- `prometheus.proxysql_client_connections_hostgroup_locked`
- `prometheus.proxysql_client_connections_non_idle`
- `prometheus.proxysql_client_connections_total`
- `prometheus.proxysql_connpool_conns`
- `prometheus.proxysql_connpool_conns_latency_us`
- `prometheus.proxysql_connpool_conns_queries_total`
- `prometheus.proxysql_connpool_conns_status`
- `prometheus.proxysql_connpool_conns_total`
- `prometheus.proxysql_connpool_data_bytes_total`
- `prometheus.proxysql_connpool_get_conn_failure_total`
- `prometheus.proxysql_connpool_get_conn_success_immediate_total`
- `prometheus.proxysql_connpool_get_conn_success_latency_awareness_total`
- `prometheus.proxysql_connpool_get_conn_success_total`
- `prometheus.proxysql_connpool_memory_bytes`
- `prometheus.proxysql_mysql_error_total`
- `prometheus.proxysql_server_connections_connected`

Those metrics might help you follow how effective your connection pool is or have more insights into your client's requests.

Keep in mind that each instance will have those metrics because each instance has its own ProxySQL service.
