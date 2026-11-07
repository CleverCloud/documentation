---
type: docs
linkTitle: Logs Drains
title: Log Drains
description: Forward the logs and access logs of your applications and add-ons to Better Stack, Datadog, Elasticsearch, New Relic, OVHcloud, Sekoia.io, Splunk, or any HTTP or syslog endpoint
keywords:
- log drains
- access logs
- syslog
- elasticsearch
- better stack
- datadog
- newrelic
- ovhcloud
- sekoia
- splunk
- export
aliases:
- /doc/develop/observability/drains
- /doc/administrate/log-drains
- /doc/administrate/drains/
---

A drain forwards the [logs](/doc/observability/logs/) of an application or an add-on to the tool of your choice: a log management service, a SIEM, or your own endpoint. For an application, it can forward its access logs instead. Clever Cloud keeps logs for 7 days, your tool keeps them according to its retention settings.

Drains work with applications and with PostgreSQL, MySQL, MongoDB, Redis®, and Elasticsearch add-ons, through [Clever Tools](/doc/tools/cli/logs-drains/#drains) or the [API](#manage-drains-through-the-api):

```bash
clever drain create raw-http https://logs.example.com/ingest
clever drain create raw-http https://logs.example.com/ingest --kind ACCESSLOG
clever drain create datadog "$DATADOG_INTAKE_URL" --addon postgresql_xxxxxxxx
```

## Destinations

Each drain sends its logs to one recipient. Pick the drain type that matches it:

| Drain type      | Recipient                                                              | Format                         |
|-----------------|------------------------------------------------------------------------|--------------------------------|
| `betterstack`   | [Better Stack](/doc/tools/cli/logs-drains/#better-stack-logs-drains)   | JSON over HTTPS                |
| `datadog`       | [Datadog](/doc/tools/cli/logs-drains/#datadog-logs-drains)             | JSON over HTTPS                |
| `elasticsearch` | [Elasticsearch](/doc/tools/cli/logs-drains/#elasticsearch-logs-drains) | Bulk API, one index per day    |
| `newrelic`      | [New Relic](/doc/tools/cli/logs-drains/#new-relic-logs-drains)         | Log API over HTTPS             |
| `ovh-tcp`       | [OVHcloud Logs Data Platform](#ovhcloud-logs-data-platform)            | Syslog RFC 5424 over TCP       |
| `raw-http`      | [Any HTTP endpoint](/doc/tools/cli/logs-drains/#raw-http-logs-drains)  | JSON array in a `POST` request |
| `sekoia`        | [Sekoia.io](/doc/tools/cli/logs-drains/#sekoiaio-logs-drains)          | JSON over HTTPS                |
| `splunk`        | [Splunk](/doc/tools/cli/logs-drains/#splunk-logs-drains)               | HTTP Event Collector events    |
| `syslog-tcp`    | [Any syslog server](/doc/tools/cli/logs-drains/#syslog-logs-drains)    | Syslog RFC 5424 over TCP       |
| `syslog-udp`    | [Any syslog server](/doc/tools/cli/logs-drains/#syslog-logs-drains)    | Syslog RFC 5424 over UDP       |

A raw HTTP drain sends a JSON array, one object per log entry. For logs, it holds fields such as `id`, `date`, `message`, and `instanceId`. For access logs, it describes the request or the connection. TCP syslog recipients accept a `tcp://` URL, or `tcps://` for TLS.

## How drains deliver logs

A new drain forwards the logs that arrive after its creation, not the past ones. An HTTP drain sends them in batches, and retries a batch the recipient doesn't accept: logs can then arrive twice or out of order, and the `id` of JSON payloads lets you spot duplicates. A `syslog-udp` drain gets no acknowledgment, so it can't detect lost logs.

When a recipient keeps refusing logs, for instance with an invalid token or a wrong URL, or stays unreachable after the retries, Clever Cloud disables the drain. Fix the recipient, check it, then enable the drain again: it resumes where it stopped, if its backlog is still available.

```bash
clever drain check DRAIN_ID
clever drain enable DRAIN_ID
```

`clever drain get DRAIN_ID` shows the status of a drain, its backlog, its retries, and its last error. To skip the logs a drain hasn't sent yet and resume from the latest ones, reset its cursor through the [API](#manage-drains-through-the-api).

## Elasticsearch index lifecycle

The daily indexes of a drain can fill the storage of your Elasticsearch instance. Its [Index Lifecycle Management](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html) applies policies, for instance to delete indexes after a given age. With the Elasticsearch add-on of Clever Cloud, create them from Kibana, or through API requests.

Here is an example that will create a policy to delete indexes older than 30 days:

```bash
curl -X PUT "https://username:password@xxx-elasticsearch.services.clever-cloud.com/_ilm/policy/logs_drain?pretty" -H 'Content-Type: application/json' -d'
{
  "policy": {
    "phases": {
      "delete": {
        "min_age": "30d",
        "actions": {
          "delete": {}
        }
      }
    }
  }
}
'
```

An index template example to apply the policy to the indexes of a drain created with `--index-prefix logstash`. Replace `logstash-*` with the pattern of your own prefix:

```bash
curl -X PUT "https://username:password@xxx-elasticsearch.services.clever-cloud.com/_index_template/logs_drain?pretty" -H 'Content-Type: application/json' -d'
{
  "index_patterns": ["logstash-*"],
  "template": {
    "settings": {
      "index.lifecycle.name": "logs_drain"
    }
  }
}
'
```

- [Learn more about lifecycle policies in the Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/set-up-lifecycle-policy.html)

## OVHcloud Logs Data Platform

To export logs from an application or an add-on to [OVHcloud Logs Data Platform](https://help.ovhcloud.com/csm/en-ie-logs-data-platform-quick-start?id=kb_article_view&sysparm_article=KB0055819), use the following setup:

- A **TCP** drain log with `clever drain create ovh-tcp`
- Your Logs Data Platform **host** with **port** `514`, or a `tcps://` URL for TLS
- The **write token** for your stream (provided on your Logs Data Platform console)

On your terminal, use the following command:

{{< tabs >}}

  {{< tab name="Application" >}}**Exporting logs from an application**:

  ```shell
  clever drain create ovh-tcp "tcp://$LDP_HOST:514" --app APP_ID_OR_NAME --sd-params "X-OVH-TOKEN=\"$LDP_WRITE_TOKEN\""
  ```

  Set `LDP_HOST` to your Logs Data Platform host and `LDP_WRITE_TOKEN` to the write token of your stream, then replace `APP_ID_OR_NAME` with your application ID or name.

  {{< /tab >}}

  {{< tab name="Add-on" >}}**Exporting logs from an add-on**:

  ```shell
  clever drain create ovh-tcp "tcp://$LDP_HOST:514" --addon ADDON_ID --sd-params "X-OVH-TOKEN=\"$LDP_WRITE_TOKEN\""
  ```

  Set `LDP_HOST` to your Logs Data Platform host and `LDP_WRITE_TOKEN` to the write token of your stream, then replace `ADDON_ID` with your add-on ID or real ID.

  {{< /tab >}}

{{< /tabs >}}

## Manage drains through the API

Clever Tools relies on the `/v4/drains` endpoints of the [Clever Cloud API](/api/), which you can call directly from your own tools. Drains belong to a resource: an application ID, or the real ID of an add-on such as `postgresql_xxxxxxxx`. To create one, send a `POST` request to `/v4/drains/organisations/{ownerId}/resources/{resourceId}/drains`:

```json
{
  "kind": "LOG",
  "recipient": {
    "type": "RAW_HTTP",
    "url": "https://logs.example.com/ingest",
    "username": "drain-user",
    "password": "drain-password"
  }
}
```

Set `kind` to `LOG` for application logs or `ACCESSLOG` for access logs. The `recipient.type` value sets which fields the recipient accepts, besides `type` and `url`:

| `type`          | Required      | Optional                                                      |
| :-------------- | :------------ | :------------------------------------------------------------ |
| `BETTERSTACK`   | `sourceToken` | —                                                             |
| `DATADOG`       | —             | —                                                             |
| `ELASTICSEARCH` | `index`       | `username`, `password`, `tlsVerification`                     |
| `NEWRELIC`      | `apiKey`      | —                                                             |
| `OVH_TCP`       | —             | `token`, `rfc5424StructuredDataParameters`, `tlsVerification` |
| `RAW_HTTP`      | —             | `username`, `password`                                        |
| `SEKOIA`        | `intakeKey`   | `tlsVerification`                                             |
| `SPLUNK`        | `token`       | `index`, `sourcetype`, `tlsVerification`                      |
| `SYSLOG_TCP`    | —             | `rfc5424StructuredDataParameters`, `tlsVerification`          |
| `SYSLOG_UDP`    | —             | `rfc5424StructuredDataParameters`                             |

`tlsVerification` is either `DEFAULT`, which verifies the certificate against the default trust store, or `TRUSTFUL`, which skips certificate and hostname verification. `OVH_TCP` and `SYSLOG_TCP` recipients use TLS with a `tcps://` URL: a `tcp://` URL stays unencrypted, and refuses `TRUSTFUL`. `rfc5424StructuredDataParameters` holds RFC 5424 structured data, such as `X-OVH-TOKEN="…"`.

The API probes the recipient before it saves the drain: an unreachable recipient fails the creation with a `412` status. Add `?skipCheck=true` to the request to create the drain without this probe.

The other endpoints act on existing drains, under the same `/v4/drains/organisations/{ownerId}` prefix:

| Method   | Path                                                    | Action                                            |
| :------- | :------------------------------------------------------ | :------------------------------------------------ |
| `DELETE` | `/resources/{resourceId}/drains/{drainId}`              | Remove a drain                                    |
| `GET`    | `/drains`                                               | List the drains of every resource of the owner    |
| `GET`    | `/resources/{resourceId}/drains`                        | List the drains of a resource                     |
| `GET`    | `/resources/{resourceId}/drains/{drainId}`              | Get a drain                                       |
| `GET`    | `/resources/{resourceId}/drains/{drainId}/test-command` | Get a shell command to test the recipient         |
| `PATCH`  | `/resources/{resourceId}/drains/{drainId}/reset-cursor` | Restart log forwarding from the latest position   |
| `POST`   | `/resources/{resourceId}/drains/{drainId}/check`        | Probe the recipient and return diagnostic results |
| `PUT`    | `/resources/{resourceId}/drains/{drainId}/disable`      | Disable a drain                                   |
| `PUT`    | `/resources/{resourceId}/drains/{drainId}/enable`       | Enable a drain                                    |

Both list endpoints accept the optional `status`, `executionStatus` and `executionStatusNotIn` query parameters to filter the results. The check result uses a `200` status even when the probe fails: read its `ok` field, then its `code` and `message` fields to diagnose a failure. A `SYSLOG_UDP` recipient sends no acknowledgment, so its check returns `ok` with the `skipped` code.

## Community software

Some tools on GitHub receive the logs of a raw HTTP drain, such as [http-logs-drain](https://github.com/sebartyr/http-logs-drain), which you can host on Clever Cloud as an application with an add-on. Clever Cloud doesn't support community software: report its issues on its repository, not to the Support.
