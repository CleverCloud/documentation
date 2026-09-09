---
title: Matomo 5.13 is available with redesigned sparklines
description: Read key metrics on redesigned sparkline cards, confirm your password before granting the admin role and let pending invitees recover their access
date: 2026-09-08
tags:
  - addons
  - matomo
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Our [Matomo](https://matomo.org/) add-on has been updated to version `5.13.0` which is now used by default. This release redesigns sparkline summary cards to make key metrics easier to scan: each metric now appears in its own card, with a clear title and a larger value. The layout adapts to the available space, including in dashboard widgets, and comparisons across dates, segments or both are easier to read.

User management also gets stricter: granting the admin role now requires a password confirmation, and pending invitees can recover access to their account. Evolution graphs show a metric forecast for incomplete periods, and table display settings persist per report across reloads.

This version hardens the Page Overlay API, adds an opt-in SSRF-safe fetch for user-configured URLs, caps e-commerce money values to handle extreme amounts and fixes archive aggregation across multiple sites for the same period. As usual, it ships its batch of bug fixes, mostly for sparklines and Dark Mode.

You can deploy this release from our [Console](https://console.clever-cloud.com) or [Clever Tools](/doc/manage/cli/). Existing customers' add-ons are already up-to-date.

- [Learn more about Matomo 5.13](https://matomo.org/changelog/matomo-5-13-0/)
- [Learn more about Matomo on Clever Cloud](/doc/deploy/services/matomo/)
