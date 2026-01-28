---
type: docs
linkTitle: Extensions
title: PHP extensions
description: Available and on-demand PHP extensions on Clever Cloud, with activation instructions and phpinfo links
keywords:
- php extensions
- apcu
- xdebug
- opcache
- grpc
- opentelemetry
---

## Available extensions and modules

Clever Cloud PHP with Apache applications enables the following extensions by default:

`amqp`, `bcmath`, `bz2`, `calendar`, `ctype`, `curl`, `dba`, `exif`, `fileinfo`, `filter`, `ftp`, `gd`, `gettext`, `gmp`, `iconv`, `imagick`, `imap`, `intl`, `json`, `ldap`, `libsodium`, `mbstring`, `mcrypt`, `memcached`, `memcache`, `mongodb`, `mysql`, `mysqli`, `opcache`, `pcntl`, `pcre`, `pdo-mysql`, `pdo-odbc`, `pdo-pgsql`, `pdo-sqlite`, `pgsql`, `phar`, `posix`, `pspell`, `readline`, `redis`, `session`, `shmop`, `sockets`, `sodium`, `solr`, `ssh2`, `ssl`, `tidy`, `tokenizer`, `unixodbc`, `xml`, `xmlrpc`, `xsl`, `zip`, `zlib`.

You can also enable the following extensions on demand:

`apcu`, `blackfire`, `elastic_apm_agent`, `event`, `excimer`, `geos`, `gnupg`, `grpc`, `ioncube`, `imap`, `mailparse`, `maxminddb`, `mongo`, `newrelic`, `oauth`, `opentelemetry`, `pcs`, `PDFlib`, `pdo_sqlsrv`, `protobuf`, `pspell`, `rdkafka`, `scoutapm`, `sqlsrv`, `sqreen`, `tideways`, `uopz`, `uploadprogress`, `xdebug`, `xmlrpc`, `yaml`

> [!NOTE]
> Only some extensions support PHP 8.5 for now: `amqp`, `apcu`, `blackfire`, `event`, `excimer`, `gnupg`, `grpc`, `imagick`, `imap`, `mailparse`, `maxminddb`, `memcached`, `oauth`, `opentelemetry`, `pdo_sqlsrv`, `protobuf`, `pspell`, `rdkafka`, `redis`, `sqlsrv`, `ssh2`, `tideways`, `uploadprogress`, `yaml`, `zip`. More extensions will be added as they are released.

You can check extensions and versions by viewing the `phpinfo()` for:

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

If you have a request about extensions, contact [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice).

## Enable specific extensions

Some extensions need to be enabled explicitly. To do so, set the corresponding environment variable:

- APCu: set `ENABLE_APCU` to `true`.

    APCu is an in-memory key-value store for PHP. Keys are of type string and values can be any PHP variables.

- Elastic APM Agent: set `ENABLE_ELASTIC_APM_AGENT` to `true` (default if `ELASTIC_APM_SERVER_URL` is defined).

    Elastic APM agent is Elastic's APM agent extension for PHP. The PHP agent enables you to trace the execution of operations
    in your application, sending performance metrics and errors to the Elastic APM server.
    **Warning**: This extension is available starting PHP 7.2.

- Event: set `ENABLE_EVENT` to `true`.

    Event is an extension to schedule I/O, time and signal based events.

- Excimer: set `ENABLE_EXCIMER` to `true`.

    Excimer is an extension that provides a low-overhead interrupting timer and sampling profiler.

- GEOS: set `ENABLE_GEOS` to `true`.

    GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology Suite (JTS).

- GnuPG: set `ENABLE_GNUPG` to `true`.

    GnuPG is an extension that provides methods to interact with GNU Privacy Guard (OpenPGP implementation).

- gRPC: set `ENABLE_GRPC` to `true`.

    gRPC is an extension for the high performance, open source, general RPC framework layered over HTTP/2.

- IonCube: set `ENABLE_IONCUBE` to `true`.

    IonCube is a tool to obfuscate PHP code. It's often used by paying Prestashop and WordPress plugins.

- IMAP (only for PHP 8.4+): set `ENABLE_IMAP` to `true`.

    IMAP is an extension to operate with the IMAP protocol, as well as the NNTP, POP3, and local mailbox access methods.

- Mailparse: set `ENABLE_MAILPARSE` to `true`.

    Mailparse is an extension for parsing and working with email messages. It can deal with RFC 822 and RFC 2045 (MIME) compliant messages.

- MaxMind DB: set `ENABLE_MAXMINDDB` to `true`.

    Extension for reading MaxMind DB files. MaxMind DB is a binary file format that stores data indexed by IP address subnets (IPv4 or IPv6).

- Mongo: set `ENABLE_MONGO` to `true`.

    MongoDB is a NoSQL Database. This extension allows to use it from PHP.
    **Warning**: this extension is now superseded by the `mongodb` extension. It is provided for backward compatibility.

- NewRelic: set `ENABLE_NEWRELIC` to `true`.

    Newrelic Agent for PHP. Newrelic is a software analytics tool.

- OAuth: set `ENABLE_OAUTH` to `true`.

    OAuth consumer extension. OAuth is an authorization protocol built on top of HTTP.

- OpenTelemetry: set `ENABLE_OPENTELEMETRY` to `true`.

    OpenTelemetry is an extension to facilitate the generation, export, collection of telemetry data such as traces, metrics, and logs.

- PCS: set `ENABLE_PCS` to `true`.

    PCS provides a fast and easy way to mix C and PHP code in your PHP extension.

- PDFlib: set `ENABLE_PDFlib` to `true`.

    PDFlib is a commercial library for generating PDF files. It provides a PHP extension to create and manipulate PDF documents.

- Protobuf: set `ENABLE_PROTOBUF` to `true`.

    Protobuf is an extension for the language-neutral, platform-neutral extensible mechanism for serializing structured data.

- Pspell: set `ENABLE_PSPELL` to `true`.

    Pspell is an extension to check the spelling of words and offer suggestions.

- Rdkafka: set `ENABLE_RDKAFKA` to `true`.

    PHP-rdkafka is a thin librdkafka binding providing a working PHP 5 / PHP 7 Kafka client.

- Scout APM: set `ENABLE_SCOUTAPM` to `true`.

    The Scout APM extension to provide additional capabilities to application monitoring over just using the base PHP userland library.

- SQL Server: set `ENABLE_SQLSRV` or `ENABLE_PDO_SQLSRV` to `true`.

    These extensions enable drivers that rely on the Microsoft ODBC Driver to handle the low-level communication with SQL Server. The `SQLSRV` extension provides a procedural interface while the `PDO_SQLSRV` extension implements PDO for accessing data in all editions of SQL Server 2012 and later (including Azure SQL DB).

- Sqreen: The Sqreen agent is started automatically after adding the environment variables (`SQREEN_API_APP_NAME` and `SQREEN_API_TOKEN`).

- Tideways: set `ENABLE_TIDEWAYS` to `true`.

    Tideways is an extension that provides profiling and monitoring capabilities for PHP applications.

- Uopz: set `ENABLE_UOPZ` to `true`.

    The uopz extension is focused on providing utilities to aid with unit testing PHP code.

- Uploadprogress: set `ENABLE_UPLOADPROGRESS` to `true`.

    The uploadprogress extension is used to track the progress of a file download.

- XDebug: set `ENABLE_XDEBUG` to `true`.

    XDebug is a debugger and profiler tool for PHP.

- XML RPC: set `ENABLE_XMLRPC` to `true`.

    XML-RPC is an extension for server and client bindings

- YAML: set `ENABLE_YAML` to `true`.

    YAML is an extension providing a YAML-1.1 parser and emitter

## Disable extensions

You can use `DISABLE_<extension_name>=true` in your [environment variables](/doc/reference/reference-environment-variables/) to disable an extension.
