---
title: Matomo 5.14 is available with aggregated real-time counters
description: Follow real-time visits and actions with the Visits Log disabled, display goal conversions in more charts and forecast unique visitors
date: 2026-10-07
tags:
  - addons
  - matomo
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Our [Matomo](https://matomo.org/) add-on has been updated to version `5.14.1` which is now used by default. Matomo 5.14 lets you follow real-time activity even when compliance requirements lead you to disable the Visits Log: aggregated real-time counters show the number of visits and actions without displaying any individual visit detail. Enable them for all sites from **Administration** > **System** > **General settings** > **Live**, or for specific sites from their settings.

Reports also get richer: bar, pie and evolution charts can show the conversions of a selected goal, forecasts now cover unique visitors and other distinct counts, and AI Chatbot reports display the percentage of the report total. Pie charts render as perfect circles, login and invitation pages get a refreshed layout with a "What's New" panel, and the Marketplace page loads faster. Matomo Tag Manager fixes an error when creating tags by publishing a default container version.

This release includes the fixes of Matomo `5.14.1`, which solves a race condition in nonce validation, redesigns the Marketplace with a dedicated page for each plugin, and refreshes its lists in the background instead of hourly. As usual, it ships its batch of bug fixes, mostly for sparkline cards and Dark Mode.

You can deploy this release from our [Console](https://console.clever-cloud.com) or [Clever Tools](/doc/manage/cli/). Existing customers' add-ons are already up-to-date.

- [Learn more about Matomo 5.14](https://matomo.org/changelog/matomo-5-14-0/)
- [Learn more about Matomo 5.14.1](https://matomo.org/changelog/matomo-5-14-1/)
- [Learn more about Matomo on Clever Cloud](/doc/deploy/services/matomo/)
