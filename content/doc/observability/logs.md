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

Applications and add-ons emit logs, made of what they write to their output. Applications also have access logs, which record the HTTP requests, the TCP redirections, and the SSH connections reaching them, with their origin.

Logs are kept for 7 days: [contact the sales team](https://www.clever.cloud/contact/) or the [Support](https://console.clever-cloud.com/ticket-center-choice) to keep them longer. To stop Clever Cloud from collecting the logs of an application, set `CC_PREVENT_LOGSCOLLECTION` to `true`.

- [Forward your logs and access logs to an external tool with drains](/doc/observability/drains/)

## Console

In the [Console](https://console.clever-cloud.com), the **Logs** menu of an application or an add-on shows its logs, and the **Access Logs** menu of an application its access logs. Both follow live logs by default, or show past logs over the time window you pick. You can select log lines and copy them with the keyboard or the mouse. Log availability for add-ons depends on the add-on and its plan.

By default, the text filter keeps the lines containing every word you type, whatever their case. You can switch it to an exact, case-sensitive string, or to a regular expression. The filter lives in the URL of the page, in the `filter` and `filterMode` parameters. It survives a page reload, and you can share a link to a filtered view.

To see a filtered line in context, select it and click `Inspect`. The interface clears the filter, pauses the stream, and centers the view on this line among the logs around it. `Clear logs` empties the view, to focus on the lines that come next. When the connection to the logs stream drops, the interface shows its reconnection attempts.

The settings panel lets you choose a color theme, wrap lines, and strip ANSI escape codes. You can also choose the date and time format, UTC or local time, and whether to show the instance names.

![New logs interface](/images/new-logs.webp)

- [Share your feedback on the logs interface](https://github.com/CleverCloud/Community/discussions/categories/new-logs-interface)

## Clever Tools

[Clever Tools](/doc/tools/cli/) shows the logs and the access logs of your applications. Without `--until`, they follow the new lines. To follow the logs of an application:

```bash
clever logs --since 1h
```

To read its access logs of the last 15 minutes:

```bash
clever accesslogs --since 15m --until now
```

The output of your [CRON jobs](/doc/manage/cron/) appears in these logs too, between the `CMD` and `CMDEND` lines the cron daemon writes when a job starts and ends. `CMDEND` doesn't hold the exit code of the command: make your job write a message when it fails.

- [Learn more about logs and access logs in Clever Tools](/doc/tools/cli/logs-drains/)

## API

The [Clever Cloud API](/api/swagger/#/Logs) streams the logs and the access logs of your applications and add-ons as Server-Sent Events. It also exports them: for an organisation, it builds an archive of the logs and access logs of the resources you choose over a time window. Once the export is ready, you can download the archive for 7 days.
