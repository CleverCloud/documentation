---
type: docs
linkTitle: Logs & Access Logs
title: Logs & Access Logs
description: Read the logs of your applications and add-ons, and the access logs of your applications, on Clever Cloud from the Console, Clever Tools or the API
keywords:
- logs
- access logs
- http requests
- application logs
- debugging
- monitoring
- troubleshooting
aliases:
- /doc/observability/access-logs
- /doc/develop/observability/access-logs
- /doc/administrate/access-logs/
- /doc/develop/observability/accesslogs
- /doc/find-help/access-logs/
- /doc/develop/observability/logs
- /clever-cloud-apis/add-ons-log-collector
- /doc/administrate/log-management
- /doc/administrate/log-management/#get-continuous-logs-from-your-application
- /doc/administrate/logs
- /doc/clever-cloud-apis/add-ons-log-collector
- /doc/observability/log-management
---

The [Console](https://console.clever-cloud.com) shows the logs of your applications and add-ons, and the [access logs](#application-access-logs) of your applications, in the same interface. It follows live logs by default, or shows past logs over the time window you pick. You can select log lines and copy them with the keyboard or the mouse. Log availability for add-ons depends on the add-on and its plan.

By default, the text filter keeps the lines containing every word you type, whatever their case. You can switch it to an exact, case-sensitive string, or to a regular expression. The filter lives in the URL of the page, in the `filter` and `filterMode` parameters. It survives a page reload, and you can share a link to a filtered view.

To see a filtered line in context, select it and click `Inspect`. The interface clears the filter, pauses the stream, and centers the view on this line among the logs around it. `Clear logs` empties the view, to focus on the lines that come next. When the connection to the logs stream drops, the interface shows its reconnection attempts.

The settings panel lets you choose a color theme, wrap lines, and strip ANSI escape codes. You can also choose the date and time format, UTC or local time, and whether to show the instance names.

![New logs interface](/images/new-logs.webp)

- [Share your feedback on the logs interface](https://github.com/CleverCloud/Community/discussions/categories/new-logs-interface)

{{< callout type="info">}}
Logs are retained for 7 days, sometimes more for specific customers/needs.
{{< /callout >}}

## Application Logs

Log management is also available through [Clever Tools](https://github.com/CleverCloud/clever-tools) and the [Clever Cloud API](/api/swagger/#/Logs). They're collected and sent through the Vector service enabled in every application deployed on Clever Cloud. To disable it, set the `CC_PREVENT_LOGSCOLLECTION` environment variable to `true`.

You can see logs with the command down below:

```bash
clever logs
```

You can add `--since` or `--until`, followed by a duration, a number of seconds, a date (ISO8601 format) or `now`.

```bash
clever logs --since 2h
clever logs --until 2024-04-15T13:37:42Z
```

Without `--until`, `clever logs` keeps following new lines after printing the past ones, even with `--since`. Set `--until` to stop at a given end time and get the prompt back, as a script or an AI agent needs, and add `--since` to choose where to start. Use `--until now` to read up to the current time. The `json` output format requires `--until`:

```bash
clever logs --since 15m --until now
clever logs --since 15m --until now --format json
```

Clever Tools disables colors when its output isn't a terminal, for example when you pipe it to another command. Add `--color true` to keep them, for example in a pager:

```bash
clever logs --since 15m --until now --color true | less -R
```

Log messages can contain ANSI codes, which set colors, move the cursor or clear a line. In the `human` format, Clever Tools removes them when colors are disabled, with `--no-color`, a non-empty `NO_COLOR` or an output that isn't a terminal. The `json` and `json-stream` formats keep messages as your application wrote them, unless you add `--strip-ansi`, which removes these codes in any format:

```bash
clever logs --since 1h --until now --format json --strip-ansi > logs.json
```

You can also get your add-on's logs by using `--addon` flag, the value is the add-on ID starting by `addon_`, or its real ID:

```bash
clever logs --addon postgresql_xxxxxxxx
```

{{< callout type="warning" >}}
   With add-ons, only the last 1000 lines of logs are got by `clever logs`.
{{< /callout >}}

The output of your [CRON jobs](/doc/manage/cron/) appears in these logs too, between the `CMD` and `CMDEND` lines the cron daemon writes when a job starts and ends. `CMDEND` doesn't hold the exit code of the command: make your job write a message when it fails.

## Application Access Logs

Access logs list the HTTP requests reaching your application. They also record the TCP redirections and SSH connections to its instances.

You can see access logs with the following command:

```bash
clever accesslogs
```

As with the `logs` command, you can specify `--since` and `--until`. Without `--until`, the command keeps following new requests, even with `--since`. Set `--until` to stop at a given end time and get the prompt back, and add `--since` to choose where to start. Use `--until now` to read up to the current time:

```bash
clever accesslogs --since 15m --until now
```

To change the output, specify the `--format` (`-F`) flag with one of these values:

- `human` (default): a human-readable, colored table. The second column shows the transport of each line, `HTTP`, `TCP` or `SSH`. Status, method and path columns only appear for HTTP requests.

  ```txt
  2026-06-24T08:05:43.880Z   HTTP   255.255.255.255   FR/Nantes   200   GET       /
  ```

- `clf`: [Common Log Format](https://en.wikipedia.org/wiki/Common_Log_Format), which only outputs HTTP access logs

  ```txt
  255.255.255.255 - - [24/Jun/2026:08:05:43 +0000] "GET /" 200 562
  ```

  The HTTP protocol version isn't part of the access log payload, so the request line is limited to `method path` (no `HTTP/x.y` token).

- `json`: a JSON array of log objects (requires a bounding flag such as `--until`)
- `json-stream`: a stream of JSON log objects

  Both JSON formats share the same object shape:

  ```json
  {
    "id": "01F91AEG8Z9RJKYB7JY7H56FNB",
    "date": "2026-06-24T08:05:43.880Z",
    "applicationId": "app_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "instanceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "region": "par",
    "zone": "par",
    "requestId": "01F91AEG8Z9RJKYB7JY7H56FNB",
    "bytesIn": 658,
    "bytesOut": 562,
    "source": {
      "ip": "255.255.255.255",
      "port": 58477,
      "city": "Nantes",
      "countryCode": "FR",
      "geoLocation": { "latitude": 50.624, "longitude": 3.0511 }
    },
    "destination": {
      "ip": "46.252.181.17",
      "port": 14001,
      "city": "Chaponost",
      "countryCode": "FR",
      "geoLocation": { "latitude": 45.7059, "longitude": 4.7444 }
    },
    "http": {
      "request": {
        "method": "GET",
        "path": "/",
        "host": "www.clever-cloud.com",
        "scheme": "https"
      },
      "response": {
        "statusCode": 200,
        "serviceTime": null,
        "time": 31
      }
    },
    "tls": null
  }
  ```

  TCP redirections and SSH connections use the same shape, without the `http` section.

- [Forward your logs and access logs to an external tool with drains](/doc/observability/drains/)
