---
title: Drains legacy stack deprecation
date: 2026-03-19
description: Deprecation of the legacy drains stack in Clever Tools, encouraging migration to the new drain stack for improved reliability and monitoring.
tags:
  - clever-tools
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

For the past few months, Clever Cloud has provided a new drain stack and a `v4` API that is more reliable and provides better monitoring. It's available through Clever Tools since [release `4.4.0`](https://github.com/CleverCloud/clever-tools/releases/tag/4.4.0). If you still use the legacy drains implementation, we encourage you to migrate to the new stack as soon as possible.

The legacy drains will be disabled on June 1st, 2026. In the meantime, we will make some changes to prepare for the migration and help you transition smoothly:
- March 19th, 2026: we added `CC_PREVENT_LEGACY_LOGSCOLLECTION=false` environment variable on applications linked to a legacy active drain
- Starting with the next image release, if not set to `false`, we will consider this environment variable as `true` and only push logs of applications with a drain to the new drain stack
- June 1st, 2026: legacy drains will be disabled and all applications will need to use the new drain stack to receive logs

## How to migrate

To migrate to the new drain stack, just create a new drain with Clever Tools, then remove `CC_PREVENT_LEGACY_LOGSCOLLECTION=false` from your application environment variables and restart it. The new drain should start receiving logs immediately.

If you have any questions or if you need help with the migration, contact [our support team](https://console.clever-cloud.com/ticket-center-choice).

- [Learn more about Clever Tools drain command ](/doc/cli/logs-drains/)
