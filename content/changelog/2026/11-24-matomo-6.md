---
title: Matomo 6 is available, and our Matomo add-on is out of beta
description: Choose between Matomo 6.0.0 and 5.14.3, keep your plugins across restarts, and lower the cost of add-ons that no longer need Redis
date: 2026-11-24
tags:
  - addons
  - matomo
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
excludeSearch: true
---

Our [Matomo](https://matomo.org/) add-on is out of beta, and Matomo `6.0.0` is now available on Clever Cloud. Matomo `5.14.3` stays the default version, and you choose the version of a new add-on in the [Console](https://console.clever-cloud.com), or with the `--addon-version` option of [Clever Tools](/doc/tools/cli/):

```bash
clever addon create addon-matomo myMatomo --addon-version 6.0.0
```

## What's new in Matomo 6

Matomo 6 measures the Average Time on Page for each page view rather than for each visit, without recalculating older data. Tracking Spam Prevention is now part of Matomo and enabled by default: it filters headless browsers, including AI tools. Each API token can get its own access level, such as read-only. Scheduled reports show percentage columns, such as **Visits (%)**.

The interface gets a new site selector, standardized dropdowns and search fields, and a rebuilt Transitions report. Matomo 6 removes the search engine optimization (SEO) plugin and its `SEO.getRank` API method. Its database migration adds a column to the table of visits, which can take several minutes on a large database. Matomo 5 now only receives security and critical bug fixes.

Some third-party plugins of the Marketplace may not support Matomo 6 on its release day: check yours before you update. Matomo `5.14.3`, the latest release of Matomo 5, brings general fixes, such as scheduled reports sent on the local day of each website.

## Plugins that persist

The plugins you activate in Matomo now persist across restarts and deployments. At each start, the add-on activates them again, and downloads those missing from the Marketplace, in the version recorded in your database. Paid plugins use your license key, and a restart never updates a plugin: you keep updating them from the Marketplace, whenever you choose.

## Redis only when instances share data

Until now, each Matomo add-on came with a Redis add-on. It held the cache of Matomo and the queue of tracking requests. On a single instance, Redis wasn't useful: Matomo keeps its cache in files as well, and every add-on now queues its tracking requests in MySQL. New add-ons run on a PHP application and a MySQL add-on only, without a Redis add-on to pay for, which lowers their cost.

Matomo [recommends a shared cache such as Redis](https://matomo.org/faq/how-to/faq_20511/) when several servers run it: clearing the cache on one server then clears it on all. That's how we now use Redis: only for a multi-instance mode, in which instances share data, available later.

## Other improvements

The add-on now installs the official release of Matomo, and checks its signature at each build, so you run exactly what Matomo publishes. If your tracking requests go through a proxy of your own, Matomo can now locate your visitors rather than your proxy. Set `MATOMO_GENERAL_PROXY_IP_READ_LAST_IN_LIST=0` on the PHP application and restart it, with the [safeguards our documentation details](/doc/deploy/services/matomo/#visitors-behind-a-proxy).

## What changes when you move to Matomo 6

When you move an existing add-on to Matomo 6, Clever Cloud updates it for you:

- Deletes its Redis add-on, if its PHP application runs on a single instance
- Prepares the files of Matomo once per build, so the application restarts faster
- Rebuilds the application with the signed release of Matomo 6, and the plugins we add
- Migrates the database schema and your Marketplace plugins when Matomo starts

Your websites, data, users, and settings stay in MySQL. Soon, a click in the Console or a Clever Tools command will do all of this.

## How to update

Until then, one call to the Clever Cloud API does it, with `clever curl` and the `matomo_` ID that `clever matomo get` shows:

```bash
clever curl https://api.clever-cloud.com/v4/addon-providers/addon-matomo/addons/matomo_xxx/version/check

clever curl -X POST -H "Content-Type: application/json" -d '{"targetVersion":"6.0.0"}' \
  https://api.clever-cloud.com/v4/addon-providers/addon-matomo/addons/matomo_xxx/version/update
```

Set `targetVersion` to `latest` to follow the next releases of Matomo at each rebuild. Matomo doesn't run a version older than its database, so check the daily [backups of your MySQL add-on](/doc/deploy/databases/mysql/#database-daily-backup-and-retention) in the Console before you update.

- [Learn more about Matomo 6](https://matomo.org/blog/2026/11/matomo-6-new-version-numbers-trust-faster/)
- [Learn more about Matomo 6.0.0](https://matomo.org/changelog/matomo-6-0-0/)
- [Learn more about Matomo 5.14.3](https://matomo.org/changelog/matomo-5-14-3/)
- [Learn more about Matomo on Clever Cloud](/doc/deploy/services/matomo/)
