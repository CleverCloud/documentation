---
title: Changes in applications custom metrics retention
date: 2026-01-27
description: Starting February 2nd, custom application metrics retention will be 7 days
tags:
  - metrics
  - platform
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Starting February 2nd, 2026, the retention period for custom application metrics will be 7 days. This change only affects metrics that you expose from your applications through the [statsd protocol or Prometheus endpoints](/doc/metrics/#publish-your-own-metrics).

**System metrics remain unaffected** by this change. All automatically collected metrics, including CPU usage, RAM consumption, disk usage, network activity, and load metrics, will continue to be available with the existing retention period.

* [Learn more about metrics on Clever Cloud](/doc/metrics/)
* [How to publish your own metrics](/doc/metrics/#publish-your-own-metrics)
