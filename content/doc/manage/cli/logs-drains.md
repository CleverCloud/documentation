---
type: docs
linkTitle: Logs Drains
title: Logs Drains
description: Manage log drains using Clever Tools CLI for centralized logging, monitoring, and troubleshooting capabilities
keywords:
- logs
- drains
- monitoring
- cli
- troubleshooting
- centralized
- pulsar
aliases:
- /doc/cli/logs-drains
- /doc/logs-drains
---

You can use Clever Tools to control logs drains, through following commands. Each can target a specific application, adding `--app APP_ID_OR_NAME` or a local alias (`--alias`, `-a`):

```console
clever drain
clever drain -F json
clever drain create DRAIN_TYPE DRAIN_URL
clever drain get DRAIN_ID
clever drain get DRAIN_ID --format json
clever drain check DRAIN_ID
clever drain remove DRAIN_ID
clever drain enable DRAIN_ID
clever drain disable DRAIN_ID
```

All drain subcommands except `clever drain list` also accept `--addon ADDON_ID_OR_REAL_ID` to target an add-on instead of an application. The `--addon` option is mutually exclusive with `--app` and `--alias`.

```console
clever drain --addon postgresql_xxxxxxxx
clever drain create raw-http https://logs.example.com --addon postgresql_xxxxxxxx
clever drain get DRAIN_ID --addon postgresql_xxxxxxxx
clever drain remove DRAIN_ID --addon postgresql_xxxxxxxx
```

The `clever drain` command lists all drains for the target application or add-on in a table, with their ID, kind, type, status and target URL. The `STATUS` column combines the status of the drain and the status of its execution. Add `--type DRAIN_TYPE` to only list the drains of a given [type](#drain-types), for example `clever drain --type datadog`. The `clever drain get` command displays detailed metrics for a single drain, including message output rate, throughput (with dynamic units), backlog size, retry attempts, and last error. These metrics help you monitor drain health and troubleshoot delivery issues.

Once a drain exists, `clever drain check DRAIN_ID` verifies that its recipient is reachable and accepts deliveries. Add `--format json` to get the result in a machine-readable format.

## List the drains of all your resources

`clever drain list` lists the drains of every application and add-on of the organisations you belong to, grouped by organisation, with a `RESOURCE` column naming the application or add-on of each drain. Use `--org` (`-o`, `--owner`) to target a single organisation, and `--type` to only list the drains of a given type:

```bash
clever drain list
clever drain list --org my-organisation --type datadog
clever drain list --format json
```

The JSON output is a flat list of drains, each one carrying the `ownerId` and `ownerName` of its organisation. If Clever Tools can't list the drains of an organisation, it prints a warning and lists the others. If it can't list the drains of any targeted organisation, the command fails with an error.

## Drain types

There is one `clever drain create` subcommand per drain type. Each one only accepts the options its drain type supports, and checks the required ones before any API call:

| Drain type      | Required option            | Type-specific optional options                     |
|-----------------|----------------------------|----------------------------------------------------|
| `betterstack`   | `--source-token`, `-t`     | None                                               |
| `datadog`       | None                       | None                                               |
| `elasticsearch` | `--index-prefix`, `-i`     | `--password`, `-p`, `--username`, `-u`             |
| `newrelic`      | `--api-key`, `-k`          | None                                               |
| `ovh-tcp`       | None                       | `--sd-params`, `-s`                                |
| `raw-http`      | None                       | `--password`, `-p`, `--username`, `-u`             |
| `sekoia`        | `--intake-key`             | `--tls-verification`                               |
| `splunk`        | `--hec-token`              | `--index`, `--sourcetype`, `--tls-verification`    |
| `syslog-tcp`    | None                       | `--sd-params`, `-s`                                |
| `syslog-udp`    | None                       | `--sd-params`, `-s`                                |

Run `clever drain create DRAIN_TYPE --help` to list the options of a drain type, or read the [CLI reference](/doc/cli-reference/#drain-create).

## Access logs drains

A drain forwards the output of your application or add-on by default. For an application, all drain types also accept `--kind ACCESSLOG` to forward its [access logs](/doc/develop/observability/access-logs/) instead. Create one drain of each kind to forward both. `clever drain` and `clever drain get` show the kind of each drain:

```console
clever drain create raw-http https://logs.example.com/clever-cloud --kind ACCESSLOG
```

## Better Stack logs drains

To create a [Better Stack](https://betterstack.com/docs/logs/http-rest-api/) drain, use the ingesting host of your source, along with its source token:

```bash
clever drain create betterstack "https://$BETTERSTACK_INGESTING_HOST" --source-token "$BETTERSTACK_SOURCE_TOKEN"
```

## Datadog logs drains

[Datadog](https://docs.datadoghq.com/api/?lang=python#send-logs-over-http) accounts belong to a [Datadog site](https://docs.datadoghq.com/getting_started/site/). An account on one site isn't available on the others, so make sure you target the intake endpoint of your site. These examples target EU1 and US1:

```bash
# EU
clever drain create datadog "https://http-intake.logs.datadoghq.eu/v1/input/$DATADOG_API_KEY?ddsource=clevercloud&service=myapp"
# US
clever drain create datadog "https://http-intake.logs.datadoghq.com/v1/input/$DATADOG_API_KEY?ddsource=clevercloud&service=myapp"
```

You can add a `host` query parameter to the URL, but it's not mandatory: in the Datadog pipeline configuration, you can map `@source_host`, the host provided by Clever Cloud in logs, as the `host` property.

## Elasticsearch logs drains

Elasticsearch drains use the Elastic bulk API, so the drain URL must end with `/_bulk`. The `--index-prefix` option is required: logs go to a daily index named `INDEX_PREFIX-YYYY-MM-DD`. For example, with the credentials of a Clever Cloud Elasticsearch add-on:

```bash
clever drain create elasticsearch "https://$ES_ADDON_HOST/_bulk" --index-prefix logstash --username "$ES_ADDON_USER" --password "$ES_ADDON_PASSWORD"
```

The `--username` and `--password` options are optional, use them when your cluster requires basic authentication.

## New Relic logs drains

[New Relic](https://docs.newrelic.com/docs/logs/log-api/introduction-log-api/) has two zones, EU and US. An account on one zone isn't available on the other, so make sure you target the right intake endpoint (`log-api.eu.newrelic.com` or `log-api.newrelic.com`):

```bash
clever drain create newrelic https://log-api.eu.newrelic.com/log/v1 --api-key "$NEW_RELIC_API_KEY"
```

## OVH TCP logs drains

OVH TCP drains are syslog drains sent over TCP to an [OVHcloud Logs Data Platform](/doc/develop/observability/drains/#ovhcloud-logs-data-platform) endpoint. Pass the write token of your stream as an RFC5424 structured data parameter:

```bash
clever drain create ovh-tcp "tcp://$LDP_HOST:514" --sd-params "X-OVH-TOKEN=\"$LDP_WRITE_TOKEN\""
```

## Raw HTTP logs drains

Raw HTTP drains send log batches as JSON `POST` requests to any HTTP endpoint. Basic authentication is optional:

```bash
clever drain create raw-http https://logs.example.com/clever-cloud
clever drain create raw-http https://logs.example.com/clever-cloud --username "$DRAIN_USERNAME" --password "$DRAIN_PASSWORD"
```

## Sekoia.io logs drains

[Sekoia.io](https://docs.sekoia.com/integration/ingestion_methods/https/overview/) drains post logs to the `/jsons` endpoint of an HTTPS intake, which reads each log as an event. The intake host depends on the region of your Sekoia.io workspace, FRA1 being the default:

```bash
clever drain create sekoia https://intake.sekoia.io/jsons --intake-key "$SEKOIA_INTAKE_KEY"
```

On other regions, use `https://intake.REGION.sekoia.io/api/v1/intake-http/jsons`. The drain sends the intake key in a header, so don't add it to the URL as `?intake_key=`: the API refuses such a URL, as it refuses a URL that doesn't use `https` or doesn't end with `/jsons`. For a self-hosted intake behind a private certificate authority, add `--tls-verification trustful`, which skips certificate and hostname verification.

Sekoia.io has no built-in intake format for Clever Cloud logs: create the intake with a custom format that parses the fields of the forwarded logs.

## Splunk logs drains

Splunk drains send events to the [HTTP Event Collector](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector) (HEC). The drain URL is the full collector endpoint, and the token is the one bound to your HEC input:

```bash
clever drain create splunk https://splunk.example.com:8088/services/collector/event --hec-token "$SPLUNK_HEC_TOKEN"
```

The `--index` and `--sourcetype` options are optional. When you don't set them, the values configured on the HEC token apply. When you set them, they override these values for every forwarded event.

A self-hosted Splunk instance ships a self-signed certificate on port `8088` by default. If you didn't replace it, add `--tls-verification trustful` so the drain doesn't fail on certificate verification. Without it, the drain fully verifies the certificate:

```bash
clever drain create splunk https://splunk.example.com:8088/services/collector/event --hec-token "$SPLUNK_HEC_TOKEN" --tls-verification trustful
```

## Syslog logs drains

Syslog drains forward logs in the RFC5424 format, over a TCP connection with `syslog-tcp`, or over UDP with `syslog-udp`, which means without any delivery guarantee. Use `--sd-params` when your collector expects structured data parameters, such as an authentication token:

```bash
clever drain create syslog-tcp tcp://logs.example.com:514
clever drain create syslog-tcp tcp://logs.example.com:514 --sd-params "token=\"$SYSLOG_TOKEN\""
clever drain create syslog-udp udp://logs.example.com:514
```
