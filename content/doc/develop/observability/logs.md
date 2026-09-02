---
type: docs
weight: 50
linkTitle: Logs
title: Logs
description: Access and filter your application logs on Clever Cloud from the Console, Clever Tools or the API
keywords:
- logs
- application logs
- debugging
- monitoring
- troubleshooting
aliases:
- /clever-cloud-apis/add-ons-log-collector
- /doc/administrate/log-management
- /doc/administrate/log-management/#get-continuous-logs-from-your-application
- /doc/administrate/logs
- /doc/clever-cloud-apis/add-ons-log-collector
- /doc/observability/log-management
- /doc/observability/logs
---

Clever Cloud new logs stack is based on Vector and Apache Pulsar. This Web Component allow you to check for live or past logs. You can target a specific time window, select logs lines and copy them in clipboard through keyboard and/or mouse. It's not available for add-ons yet.

There are two text filter modes: exact match (case-sensitive) and regular expression. Settings panel offers lots of parameters such as dark/light themes, line wrapping, ANSI codes escaping, etc. You can also choose the date/time format, UTC or local, to show the instances name or not.

![New logs interface](/images/new-logs.webp)

This interface is constantly improving, used for logs and access logs, send us your feedback through our GitHub Community:

- [Give your feedback about new Logs interface](https://github.com/CleverCloud/Community/discussions/categories/new-logs-interface)

{{< callout type="info">}}
Logs are retained for 7 days, sometimes more for specific customers/needs.
{{< /callout >}}

## Get continuous logs from your application

Log management is also available through [Clever Tools](https://github.com/CleverCloud/clever-tools) and our [APIv4](/api/v4/#logs). They're collected and sent through the Vector service enabled in every application deployed on Clever Cloud. To disable it, set the `CC_PREVENT_LOGSCOLLECTION` environment variable to `true`. You can see logs with the command down below.

```bash
clever logs
```

You can add `--since`, followed by a duration or a date (ISO8601 format). The `--until` flag should be followed by a date (ISO8601 format).

```bash
clever logs --since 2h
clever logs --until 2024-04-15T13:37:42Z
```

You can also get your add-on's logs by using `--addon` flag, the value must be the add-on ID starting by `addon_`.

```bash
clever logs --addon <addon_xxx>
```

{{< callout type="warning" >}}
   With add-ons, only the last 1000 lines of logs are got by `clever logs`.
{{< /callout >}}

See [Access Logs](/doc/develop/observability/access-logs) for incoming HTTP requests, and [Drains](/doc/develop/observability/drains) to forward everything to an external tool.
