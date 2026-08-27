---
type: docs
linkTitle: ProxySQL
title: Configure ProxySQL for MySQL
description: Enable the local ProxySQL service and connect applications to a Clever Cloud MySQL add-on through its Unix socket
keywords:
- connection pooling
- mysql
- proxysql
aliases:
- /deploy/addon/mysql/proxysql
- /doc/deploy/addon/mysql/proxysql
- /proxysql
---

[ProxySQL](https://proxysql.com/) runs between your application and a linked [MySQL add-on](/doc/addons/mysql). It keeps backend connections available for reuse while your application connects locally through a [Unix domain socket](https://en.wikipedia.org/wiki/Unix_domain_socket). This is useful for applications that do not already maintain an efficient connection pool.

ProxySQL is available in every runtime except Docker, where processes and services are managed by the container image.

## Enable ProxySQL

Link a MySQL add-on to the application, then enable ProxySQL:

```bash
clever env set CC_ENABLE_MYSQL_PROXYSQL true
```

The platform starts one ProxySQL process on each application instance and injects `CC_MYSQL_PROXYSQL_SOCKET_PATH` with the local socket path. Your application must keep using the linked add-on credentials from `MYSQL_ADDON_USER`, `MYSQL_ADDON_PASSWORD` and `MYSQL_ADDON_DB`, but use this socket instead of `MYSQL_ADDON_HOST` and `MYSQL_ADDON_PORT`.

TLS is enabled between ProxySQL and MySQL by default. You can configure the maximum number of backend connections per application instance with `CC_MYSQL_PROXYSQL_MAX_CONNECTIONS`, which defaults to `10`. See the [environment variables reference](/doc/reference/reference-environment-variables/#proxysql) for all available options.

## Connect your application

### PHP with PDO

Pass the socket through the `unix_socket` parameter of the [PDO MySQL DSN](https://www.php.net/manual/en/ref.pdo-mysql.connection.php):

```php
<?php

$dsn = sprintf(
    'mysql:unix_socket=%s;dbname=%s;charset=utf8mb4',
    getenv('CC_MYSQL_PROXYSQL_SOCKET_PATH'),
    getenv('MYSQL_ADDON_DB')
);

$connection = new PDO(
    $dsn,
    getenv('MYSQL_ADDON_USER'),
    getenv('MYSQL_ADDON_PASSWORD'),
    [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
);
```

### Node.js with mysql2

Set `socketPath` when creating a connection or pool with [`mysql2`](https://sidorares.github.io/node-mysql2/docs):

```javascript
import mysql from "mysql2/promise";

const pool = mysql.createPool({
  socketPath: process.env.CC_MYSQL_PROXYSQL_SOCKET_PATH,
  user: process.env.MYSQL_ADDON_USER,
  password: process.env.MYSQL_ADDON_PASSWORD,
  database: process.env.MYSQL_ADDON_DB,
});
```

### WordPress

Use the socket in `wp-config.php`:

```php
define('DB_HOST', 'localhost:' . getenv('CC_MYSQL_PROXYSQL_SOCKET_PATH'));
```

## Size the connection pool

Each running instance owns its ProxySQL process. During a rolling deployment, old and new instances can run simultaneously, so the maximum number of backend connections can temporarily reach:

```text
2 × maximum running instances × CC_MYSQL_PROXYSQL_MAX_CONNECTIONS
```

Keep this result below the MySQL plan's connection limit and reserve capacity for administration or other clients. For example, an application scaling to four instances with `CC_MYSQL_PROXYSQL_MAX_CONNECTIONS=15` can temporarily open up to 120 backend connections during a deployment.

## Monitor ProxySQL

ProxySQL exports connection, query and error metrics for each application instance. Use the [Metrics overview](/doc/metrics) to inspect them in the Console and create alerts for your application.

## Learn more

- [ProxySQL documentation](https://proxysql.com/documentation/) — Configure and operate ProxySQL
- [MySQL add-ons](/doc/addons/mysql) — Create, link and administer MySQL databases
- [Environment variables reference](/doc/reference/reference-environment-variables/#proxysql) — Review all ProxySQL settings available on Clever Cloud
