---
type: docs
linkTitle: Matomo
title: Matomo
description: Deploy Matomo on Clever Cloud, an open source web analytics platform that keeps your data under your control, with sign-in through your Clever Cloud account
keywords:
- matomo
- web analytics
- privacy analytics
- gdpr compliant
- google analytics alternative
- website tracking
- open source analytics
aliases:
- /addons/matomo
- /doc/addons/matomo
- /doc/deploy/addon/matomo
- /doc/matomo
- /doc/services/matomo
---

[Matomo](https://matomo.org) is an open source web analytics platform, and an alternative to Google Analytics that gives you full ownership of your data. Its privacy controls, which anonymize or delete data, help you to [comply with the GDPR](https://matomo.org/gdpr-analytics).

Matomo on Clever Cloud runs the official release of Matomo on the services of the platform, in the version you choose. You sign in with your Clever Cloud account, and the plugins you activate persist across restarts.

## Create a Matomo add-on

### From the Console

1. [Create a new add-on](https://console.clever-cloud.com/users/me/addons/new) by clicking **Create** in the sidebar, then **Add-on**
2. Select the Matomo add-on, then its version
3. Skip the link to an application, Matomo doesn't need it
4. Enter a name for the add-on, and select its region

### With Clever Tools

Install [Clever Tools](/doc/tools/cli/install/), then create the add-on. Add `--addon-version` to choose the [version of Matomo](#versions-and-updates), `--org` to create it in an organisation, and `--region` to choose its region, `par` by default. Without `--addon-version`, the add-on uses the default version:

```bash
clever addon create addon-matomo myMatomo
clever addon create addon-matomo myMatomo --addon-version 6.0.0
```

The command shows the URL of Matomo:

```text
Add-on created successfully!
ID: addon_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Real ID: matomo_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Name: myMatomo

Your Matomo is starting:
 - Access it: https://xxxxxxxxxxxxxxxxxxxx-matomo.services.clever-cloud.com
 - Manage it: https://console.clever-cloud.com/goto/addon_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

Learn more about Matomo on Clever Cloud: https://www.clever.cloud/developers/doc/addons/matomo/
```

To serve Matomo on your own domain instead of a `services.clever-cloud.com` one, set it at creation with the `access-domain` option:

```bash
clever addon create addon-matomo myMatomo --option access-domain=matomo.example.com
```

Point it to Clever Cloud: in the `par` region, use a CNAME record to `domain.par.clever-cloud.com.`, as [Domain names](/doc/manage/domain-names/) details per region.

## Underlying resources

A Matomo add-on runs on resources of your organisation, which you see and manage [in the Console](https://console.clever-cloud.com/):

- A [PHP](/doc/deploy/applications/php/) application that runs Matomo, of size `XS` with a single instance at creation
- A [MySQL](/doc/deploy/databases/mysql/) add-on of size `XXS Big Space`, which stores the visits, the reports, and the queue of tracking requests

You can change these sizes afterwards, as for any application or add-on. A website with a lot of traffic, or long reports, may need a larger PHP application, or a larger MySQL add-on to keep its history.

Older Matomo add-ons also have a [Redis](/doc/deploy/databases/redis/) add-on of size `S` for their cache. When you move such an add-on to Matomo 6, Clever Cloud deletes it if its PHP application runs on a single instance. Matomo then keeps its cache in files.

## Access Matomo

Open Matomo from the dashboard of the add-on in the Console, or with its URL. Sign in with the **Clever Cloud** button: Matomo uses your Clever Cloud account, so you don't manage another password.

{{% include "shared/single-sign-on" %}}

Then, add your websites and their tracking code, and invite the members of your team. If you're new to Matomo, start with [its guides](https://matomo.org/guides/).

With Clever Tools, the operators commands show the information of the add-on, open it, and restart or rebuild its application:

```bash
clever features enable operators
clever matomo get myMatomo

clever matomo open webui myMatomo
clever matomo open logs myMatomo

clever matomo restart myMatomo
clever matomo rebuild myMatomo
```

## Configuration by Clever Cloud

Clever Cloud downloads the official release of Matomo at each build, and checks that Matomo signed it, so the files are exactly those Matomo publishes. Then, it configures Matomo when it starts, so it works without any setup:

- A cache in files, or in the Redis add-on of older Matomo add-ons
- Sign-in with your Clever Cloud account, through the `LoginOIDC` plugin
- Migrations of the database schema at each start, which follow the version of Matomo
- Report archiving every hour by a scheduled task, instead of when someone opens a report
- Geolocation of visitors with the free DB-IP City Lite database, downloaded at each build
- The `QueuedTracking` plugin, which queues the tracking requests in MySQL and processes them in batches of 25

To change the batch size, edit **Number of requests that are processed in one batch** in **Administration** > **System** > **General settings**.

### Visitors behind a proxy

Matomo reads the IP of a visitor in the `X-Forwarded-For` header, which ends with the IP that reached the Clever Cloud load balancers. By default, Matomo uses this last IP, which a client can't forge. When your tracking requests go through your own proxy, all visitors get its IP.

In this case, set `MATOMO_GENERAL_PROXY_IP_READ_LAST_IN_LIST` to `0` on the PHP application of the add-on, then restart it: Matomo reads the first IP of the header instead. A client can forge this first IP, unless your proxy replaces the header with the IP it receives the request from.

## Plugins

Matomo on Clever Cloud comes with the core plugins of Matomo, and you can add plugins from [the Matomo marketplace](https://plugins.matomo.org/). Clever Cloud keeps the plugins you activate. At each start, it activates them again, and downloads the missing ones in the version recorded in the database. Paid plugins use the license key you entered in Matomo, so you don't enter it again.

A restart never updates a plugin: update it from the Marketplace, and the next starts use its new version. If the Marketplace has no such version for a new major version of Matomo, Clever Cloud installs the latest compatible one, which Matomo migrates. A plugin that Clever Cloud can't restore doesn't stop Matomo: it starts without it, and the logs of the application name it.

Some changes don't persist, or need an action from you:

- A core plugin that you deactivate is active again after a restart
- A plugin that depends on another Marketplace plugin may need a second restart
- A deactivated Marketplace plugin needs a new install before you activate it again

Some plugins need more resources, such as [GoogleAnalyticsImporter](https://matomo.org/guide/installation-maintenance/import-google-analytics/), which imports your Google Analytics history into Matomo. Before you run them, increase the size of the PHP application and of the MySQL add-on, which you can reduce once the import ends. If you enabled autoscaling on the PHP application, disable it during the import: a new instance would stop it.

## Delete old data

Matomo keeps all its data by default, so the MySQL add-on grows with your traffic until it's full. To delete old data on a regular basis, open **Administration** > **Privacy** > **Anonymize data**, then enable **Regularly delete old raw data**, **Delete old aggregated report data**, or both, and set the age of the data to delete. Then, choose how often Matomo deletes it in **Schedule old data deletion**.

## Versions and updates

The `CC_MATOMO_VERSION` environment variable of the PHP application sets the version of Matomo. It holds `latest`, the latest release that Clever Cloud offers, which each rebuild follows, or a release such as `6.0.0`. To list the versions you can choose, and the default one, run:

```bash
clever addon providers show addon-matomo
```

`clever matomo get myMatomo` shows the version of the add-on with the version of PHP, as does the dashboard of the add-on in the Console. The Console and the `clever matomo` commands don't change the version of an existing add-on. Use the Clever Cloud API with `clever curl` instead, and the ID of the add-on that `clever matomo get` shows, which starts with `matomo_`.

Check the version of the add-on and the versions on offer, then move the add-on to another version:

```bash
clever curl https://api.clever-cloud.com/v4/addon-providers/addon-matomo/addons/matomo_xxx/version/check

clever curl -X POST -H "Content-Type: application/json" -d '{"targetVersion":"6.0.0"}' \
  https://api.clever-cloud.com/v4/addon-providers/addon-matomo/addons/matomo_xxx/version/update
```

```json
{"available":["5.14.3","6.0.0","latest"],"installed":"5.14.3","latest":"6.0.0","needUpdate":true}
```

The update sets `CC_MATOMO_VERSION`, then rebuilds the application without the build cache. The new instance migrates the database schema when it starts, which takes from a few seconds to several minutes on a large database. During the migration, the previous instance may answer with errors. Before you move to a new major version, check the [backups of the MySQL add-on](/doc/deploy/databases/mysql/#database-daily-backup-and-retention), and that your plugins support it.

Matomo doesn't run a version older than its database. A move to an older version fails at the build, and the running instance stays. Move the add-on back to the version it runs. If you change `CC_MATOMO_VERSION` yourself, run `clever matomo rebuild`: a restart keeps the previous build.
