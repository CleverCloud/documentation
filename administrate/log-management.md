---
title: Logs management
position: 3
shortdesc: How to manage addons and applications log drains
tags:
 - administrate
keywords:
- logs
- log
- logging
- log drains
- drain
- drains
---

Log management is currently only available through our API and [clever-tools]({{< ref "/getting-started/cli.html" >}}).

## Get continuous logs from your application

You can see logs with the command down below.

```bash
clever logs
```

You can also add a flag `--before` or `--after` followed by a date (ISO8601 format).

```bash
# Here is an example
clever logs --before 2016-08-11T14:54:33.971Z
```

### Access logs

It contains all incoming requests to your application. Here is an example:

```txt
255.255.255.255 - - [06/Feb/2020:07:59:22 +0100] "GET /aget/to/your/beautiful/website -" 200 1453
```

They are available in different formats, the most common is CLF which stands for Common Log Format.

You can see access logs with the following command:

```bash
clever accesslogs
```

As with the `logs` command, you can specify `--before` and `--after` flags as well as the `--follow`  to display access logs continuously.

## Exporting logs to an external tools

You can use the logs drains to send your application's logs to an external server with the following command.

```bash
clever drain create [--alias <alias>] <DRAIN-TYPE> <DRAIN-URL> [--username <username>] [--password <password>]
```

Where `DRAIN-TYPE` is one of:

- `TCPSyslog`: for TCP syslog endpoint;
- `UDPSyslog`: for UDP syslog endpoint;
- `HTTP`: for TCP syslog endpoint (note that this endpoint has optional username/password parameters as HTTP Basic Authentication);
- `ElasticSearch`: for ElasticSearch endpoint (note that this endpoint requires username/password parameters as HTTP Basic Authentication);
- `DatadogHTTP`: for Datadog endpoint (note that this endpoint needs your Datadog API Key).

You can list the currently activated drains with this command.

```bash
clever drain [--alias <alias>]
```

And remove them if needed

```bash
clever drain remove [--alias <alias>] <DRAIN-ID>
```

If the status of your drain is shown as `DISABLED` without you disabling it, it may be because we  have not been able to send your logs to your drain endpoint or because the requests timed out after 25 seconds.

### ElasticSearch

ElasticSearch drains use the Elastic bulk API. To match this endpoint, specify `/_bulk` at the end of your ElasticSearch endpoint.

Each day, we will create an index `logstash-<yyyy-MM-dd>` and push logs to it.

### Datadog

Datadog has two zones, EU and COM. An account on one zone is not available on the other, make sure to target the good EU or COM intake endpoint.

To create a [Datadog](https://docs.datadoghq.com/fr/api/latest/logs/#send-logs) drain, you just need to use:

```bash
clever drain create DatadogHTTP "https://http-intake.logs.datadoghq.com/v1/input/<API_KEY>?ddsource=clevercloud&service=<SERVICE>&hostname=<HOST>"
```

## Logs extended storage

Each organisations or personal space has a `Logs extended storage` Cellar addon.
This addon will be used to store your applications/addons logs when the hot retention is reached when the feature will be available.

The most aged logs will be pushed to `Logs extended storage` as cold storage.
The retention for cold storage will be user defined via a new log management interface.
