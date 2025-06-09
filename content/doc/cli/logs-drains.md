---
type: docs
title: Logs, Drains
description: Use Clever Tools to get logs, access logs and manage logs drains
---

## logs

When you deploy an application on Clever Cloud, we collect its logs, hosted in our internal Pulsar stack, all included.

To listen the stream, use:

```
clever logs
```

You can also get logs from a specific timeline, deployment or add-on through options:

```
[--before, --until] BEFORE          Fetch logs before this date/time (ISO8601 date, positive number in seconds or duration, e.g.: 1h)
[--after, --since] AFTER            Fetch logs after this date/time (ISO8601 date, positive number in seconds or duration, e.g.: 1h)
[--search] SEARCH                   Fetch logs matching this pattern
[--deployment-id] DEPLOYMENT_ID     Fetch logs for a given deployment
[--addon] ADDON_ID                  Add-on ID
[--format, -F] FORMAT               Output format (human, json, json-stream) (default: human)
```

## access logs

When you deploy an application on Clever Cloud, we collect its access logs, hosted in our internal Pulsar stack, all included.

To listen the stream, use:

```
clever accesslogs
```

> [!TIP]
>  This now uses our v4 API, it's available as Alpha feature for now.

You can also get access logs from a specific timeline or add-on through options, in multiple formats:

```
[--before, --until] BEFORE     Fetch logs before this date/time (ISO8601 date, positive number in seconds or duration, e.g.: 1h)
[--after, --since] AFTER       Fetch logs after this date/time (ISO8601 date, positive number in seconds or duration, e.g.: 1h)
[--format, -F] FORMAT          Output format (human, json, json-stream) (default: human)
```

You can for example get access logs in JSON stream format for the last hour with:

```
clever accesslogs --format json-stream --since 1h
clever accesslogs -F json-stream | jq '.source.ip'
```

or JSON if you add a date/time end limit:

```
clever accesslogs --app APP_NAME --since 2025-04-21T13:37:42 --until 1d -F json | jq '[.[] | {date, countryCode: .source.countryCode, ip: .source.ip, port: .source.port}]'
clever accesslogs --app APP_NAME --since 2025-04-21T13:37:42 --until 1d -F json | jq '.[] | [.date, .source.countryCode, .source.ip, .source.port] | @sh'
```

> [!TIP]
> `jq` offers multiple table formatting options, like `@csv`, `@tsv`, `@json`, `@html`, `@uri`, `@base64`, etc.

## drain

You can use Clever Tools to control logs drains, through following commands. Each can target a specific add-on with `--addon ADDON_ID ` or application, adding `--app APP_ID_OR_NAME` or a local alias (`--alias`, `-a`):

```
clever drain
clever drain --format json
clever drain create <DRAIN-TYPE> <DRAIN-URL>
clever drain remove <DRAIN-ID>
clever drain enable <DRAIN-ID>
clever drain disable <DRAIN-ID>
```

Where `DRAIN-TYPE` is one of:

- `DatadogHTTP`: for Datadog endpoint (note that this endpoint needs your Datadog API Key)
- `ElasticSearch`: for ElasticSearch endpoint (note that this endpoint requires username/password parameters as HTTP Basic Authentication)
- `HTTP`: for TCP syslog endpoint (note that this endpoint has optional username/password parameters as HTTP Basic Authentication)
- `NewRelicHTTP`: for NewRelic endpoint (note that this endpoint needs your NewRelic API Key)
- `TCPSyslog`: for TCP syslog endpoint
- `UDPSyslog`: for UDP syslog endpoint

Drain creation supports the following options:

```
[--username, -u] USERNAME             (HTTP drains) basic auth username
[--password, -p] PASSWORD             (HTTP drains) basic auth password
[--api-key, -k] API_KEY               (NewRelic drains) API key
[--index-prefix, -i] INDEX_PREFIX     (ElasticSearch drains) Index prefix (default: logstash-<YYYY-MM-DD>)
[--sd-params, -s] SD_PARAMS           (TCP and UDP drains) sd-params string (e.g.: `X-OVH-TOKEN=\"REDACTED\"`)
```

### ElasticSearch logs drains

ElasticSearch drains use the Elastic bulk API. To match this endpoint, specify `/_bulk` at the end of your ElasticSearch endpoint.

### Datadog logs drains

Datadog has two zones, EU and COM. An account on one zone is not available on the other, make sure to target the good EU or COM intake endpoint. To create a [Datadog](https://docs.datadoghq.com/api/?lang=python#send-logs-over-http) drain, you just need to use one of the following command depending on your zone:

```
# EU
clever drain create DatadogHTTP "https://http-intake.logs.datadoghq.eu/v1/input/<API_KEY>?ddsource=clevercloud&service=<SERVICE>&host=<HOST>"
# US
clever drain create DatadogHTTP "https://http-intake.logs.datadoghq.com/v1/input/<API_KEY>?ddsource=clevercloud&service=<SERVICE>&host=<HOST>"
```

The `host` query parameter is not mandatory: in the Datadog pipeline configuration, you can map `@source_host` which is the host provided by Clever Cloud in logs as `host` property.

### NewRelic logs drains

NewRelic has two zones, EU and US. An account on one zone is not available on the other, make sure to target the good EU or US intake endpoint. To create a [NewRelic](https://docs.newrelic.com/docs/logs/log-api/introduction-log-api/) drain, you just need to use:

```
clever drain create NewRelicHTTP "https://log-api.eu.newrelic.com/log/v1" --api-key <API_KEY>
```
