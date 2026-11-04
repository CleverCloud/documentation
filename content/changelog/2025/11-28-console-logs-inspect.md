---
title: Inspect a filtered log line in context from the Console
description: An Inspect button in the logs interface of the Console shows a filtered line among the logs around it, for application, access, and add-on logs
date: 2025-11-28
tags:
  - console
  - logs
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

When you look for an issue in your logs, the text filter of the [Clever Cloud Console](https://console.clever-cloud.com) helps you find the relevant line. But you often need to see what happened right before or after it. The logs interface now gets an `Inspect` button for this.

While a filter is active, select a log line, then click `Inspect`. The interface clears the filter, pauses the stream, and centers the view on this line among the logs around it. It works for application logs, [access logs](/changelog/2025/09-11-access-logs-console/), and the [add-on logs](/changelog/2025/09-12-console-addon-logs-beta/) in beta.

- [Learn more about logs on Clever Cloud](/doc/develop/observability/logs/)
