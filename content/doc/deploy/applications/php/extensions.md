---
type: docs
linkTitle: Extensions
title: PHP extensions
description: Default and on-demand PHP extensions of PHP with Apache applications on Clever Cloud, how to enable or disable them, and the phpinfo of each PHP version
keywords:
- apcu
- grpc
- opentelemetry
- php extensions
- phpinfo
- xdebug
aliases:
- /doc/applications/php/extensions
---

## Available extensions and modules

[PHP applications](/doc/deploy/applications/php/) load these extensions by default with PHP 8.2 and later, besides core ones such as `json`:

`amqp`, `bcmath`, `bz2`, `calendar`, `ctype`, `curl`, `dba`, `dom`, `exif`, `fileinfo`, `filter`, `ftp`, `gd`, `gettext`, `gmp`, `iconv`, `imagick`, `intl`, `ldap`, `mbstring`, `mcrypt`, `memcache`, `memcached`, `mongodb`, `mysqli`, `mysqlnd`, `odbc`, `opcache`, `openssl`, `pcntl`, `pdo`, `pdo_mysql`, `pdo_odbc`, `pdo_pgsql`, `pdo_sqlite`, `pgsql`, `phar`, `posix`, `readline`, `redis`, `session`, `shmop`, `simplexml`, `soap`, `sockets`, `sodium`, `solr`, `sqlite3`, `ssh2`, `sysvmsg`, `sysvsem`, `sysvshm`, `tidy`, `tokenizer`, `xml`, `xmlreader`, `xmlwriter`, `xsl`, `zip`, `zlib`.

Before PHP 8.4, the Internet Message Access Protocol (IMAP) and Pspell extensions load by default too.

Many extensions don't have a release supporting PHP 8.6 yet: with this version, `amqp`, `imagick`, `mcrypt`, `memcache`, `memcached`, `mongodb`, `redis`, `solr`, and `ssh2` aren't available.

To check the extensions of a PHP version, and their own versions, see its `phpinfo()`:

- [PHP 5.6](https://php56info.cleverapps.io)
- [PHP 7.1](https://php71info.cleverapps.io)
- [PHP 7.2](https://php72info.cleverapps.io)
- [PHP 7.3](https://php73info.cleverapps.io)
- [PHP 7.4](https://php74info.cleverapps.io)
- [PHP 8.0](https://php80info.cleverapps.io)
- [PHP 8.1](https://php81info.cleverapps.io)
- [PHP 8.2](https://php82info.cleverapps.io)
- [PHP 8.3](https://php83info.cleverapps.io)
- [PHP 8.4](https://php84info.cleverapps.io)
- [PHP 8.5](https://php85info.cleverapps.io)
- [PHP 8.6](https://php86info.cleverapps.io)

## Enable specific extensions

Other extensions load only when you set their variable to `true`, such as the agents of application performance monitoring (APM) tools:

```bash
clever env set ENABLE_APCU true
```

Each extension of this table loads with its own variable, after a restart of your application:

| Extension                                                                                           | Variable                             | Use                                                |
| --------------------------------------------------------------------------------------------------- | ------------------------------------ | -------------------------------------------------- |
| [APCu](https://www.php.net/manual/en/book.apcu.php)                                                 | `ENABLE_APCU`                        | In-memory cache of PHP values                      |
| [Blackfire](/doc/observability/blackfire/)                                                          | `ENABLE_BLACKFIRE`                   | Profiling and performance monitoring               |
| [Couchbase](https://docs.couchbase.com/php-sdk/current/hello-world/overview.html)                   | `ENABLE_COUCHBASE`                   | Couchbase client, up to PHP 8.2                    |
| [Elastic APM](https://www.elastic.co/docs/reference/apm/agents/php)                                 | `ENABLE_ELASTIC_APM_AGENT`           | Traces and errors sent to Elastic APM              |
| [Event](https://www.php.net/manual/en/book.event.php)                                               | `ENABLE_EVENT`                       | Scheduling of I/O, time, and signal events         |
| [Excimer](https://www.mediawiki.org/wiki/Excimer)                                                   | `ENABLE_EXCIMER`                     | Sampling profiler and timers                       |
| [GnuPG](https://www.php.net/manual/en/book.gnupg.php)                                               | `ENABLE_GNUPG`                       | OpenPGP encryption and signatures                  |
| [gRPC](https://grpc.io/docs/languages/php/)                                                         | `ENABLE_GRPC`                        | gRPC client                                        |
| [IMAP](https://www.php.net/manual/en/book.imap.php)                                                 | `ENABLE_IMAP`                        | Mailbox client, on demand starting with PHP 8.4    |
| [Mailparse](https://www.php.net/manual/en/book.mailparse.php)                                       | `ENABLE_MAILPARSE`                   | Parsing of email messages                          |
| [MaxMind DB](https://pecl.php.net/package/maxminddb)                                                | `ENABLE_MAXMINDDB`                   | Reader of MaxMind DB files, such as GeoIP          |
| [OAuth](https://www.php.net/manual/en/book.oauth.php)                                               | `ENABLE_OAUTH`                       | OAuth 1.0 consumer and provider                    |
| [OpenTelemetry](https://opentelemetry.io/docs/zero-code/php/)                                       | `ENABLE_OPENTELEMETRY`               | Automatic instrumentation for OpenTelemetry        |
| [PDFlib](https://www.pdflib.com/products/pdflib-family/)                                            | `ENABLE_PDFLIB`                      | Generation of PDF files, with a commercial license |
| [Protobuf](https://protobuf.dev/reference/php/php-generated/)                                       | `ENABLE_PROTOBUF`                    | Faster Protocol Buffers                            |
| [Pspell](https://www.php.net/manual/en/book.pspell.php)                                             | `ENABLE_PSPELL`                      | Spell checking, on demand starting with PHP 8.4    |
| [rdkafka](https://pecl.php.net/package/rdkafka)                                                     | `ENABLE_RDKAFKA`                     | Kafka client                                       |
| [Scout APM](https://scoutapm.com/docs/php)                                                          | `ENABLE_SCOUTAPM`                    | Monitoring agent, up to PHP 8.3                    |
| [SQL Server](https://learn.microsoft.com/en-us/sql/connect/php/microsoft-php-driver-for-sql-server) | `ENABLE_SQLSRV`, `ENABLE_PDO_SQLSRV` | SQL Server drivers, starting with PHP 8.4          |
| [uopz](https://www.php.net/manual/en/book.uopz.php)                                                 | `ENABLE_UOPZ`                        | Test utilities, up to PHP 8.3                      |
| [Uploadprogress](https://pecl.php.net/package/uploadprogress)                                       | `ENABLE_UPLOADPROGRESS`              | Progress of file uploads                           |
| [Xdebug](https://xdebug.org)                                                                        | `ENABLE_XDEBUG`                      | Debugger and profiler                              |
| [YAML](https://www.php.net/manual/en/book.yaml.php)                                                 | `ENABLE_YAML`                        | YAML parser and emitter                            |

Setting `ELASTIC_APM_SERVER_URLS`, or `ELASTIC_APM_SERVER_URL`, enables the Elastic APM agent too, unless `ENABLE_ELASTIC_APM_AGENT` is `false`. [New Relic](/doc/observability/new-relic/) loads with `NEW_RELIC_LICENSE_KEY`, and Tideways with `CC_TIDEWAYS_API_KEY` and `CC_TIDEWAYS_SERVICE`.

With PHP 8.6, only these extensions of the table are available: Blackfire, Mailparse, MaxMind DB, OAuth, OpenTelemetry, and SQL Server.

For another extension, [contact the support team](https://console.clever-cloud.com/ticket-center-choice).

## Disable extensions

To disable an extension loaded by default, set `DISABLE_<EXTENSION>` to `true`, such as `DISABLE_IMAGICK`. It works for `amqp`, `imagick`, `mcrypt`, `memcache`, `memcached`, `mongodb`, `opcache`, `redis`, `solr`, and `ssh2`: PHP includes the others.

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/php" title="PHP with Apache" subtitle="PHP version, settings, memory, variables, caches, and tasks" icon="php" >}}
  {{< card link="/developers/doc/deploy/applications/php/apache" title="Apache" subtitle="Configure the web server with .htaccess, authentication, and timeouts" icon="feather" >}}
  {{< card link="/developers/doc/deploy/applications/php/composer" title="Composer" subtitle="Install dependencies, choose Composer, reach private repositories" icon="php" >}}
  {{< card link="/developers/doc/deploy/applications/php/sessions-emails" title="Sessions and emails" subtitle="Store sessions on an FS Bucket or Materia KV, send emails" icon="mail" >}}
{{< /cards >}}
