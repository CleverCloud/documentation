---
title: "Metabase 60 and RAM requirements"
description: New Metabase add-ons are deployed on a S Java instance, and existing add-ons will be upgraded to S when they'll move to 60.
date: 2026-05-06
tags:
  - addons
  - metabase
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

Starting with its `x.60` branch, [Metabase requires at least 2 GB of RAM](https://github.com/metabase/metabase/issues/72942) to run. The XS Java instance currently used by default for the Metabase add-on on Clever Cloud only provides 1 GB of RAM, which is no longer enough. To make sure your Metabase instance keeps deploying and running smoothly, we are adapting the default sizing:

- Metabase add-ons created from today onwards use a **S Java instance** instead of XS
- When the update to version 60 will be offered, existing add-ons will **automatically be migrated to a S Java instance** during the upgrade

If you want to keep an XS instance, stay on the `x.59` branch by setting `CC_METABASE_VERSION` to `0.59` (or `1.59` for the Enterprise Edition) on the underlying Java application. Keep in mind that staying on x.59 means you will not receive the new features shipped with x.60 and beyond; security patches and some fixes will still be provided as long as the 0.59 branch is maintained. We recommend moving to a S instance and the latest branch as soon as possible.

- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)
- [Pricing of Java instances on Clever Cloud](https://www.clever-cloud.com/pricing/)
