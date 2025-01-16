---
title: New Gravelines HDS region
date: 2024-02-12
tags:
  - addons
  - applications
  - platform
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: HDS servers, the duplicate way
aliases:
- /changelog/2024-02-12-new-grahds-region
excludeSearch: true
---

For some time now, you can deploy your applications and add-ons through Clever Cloud, to Health Data Hosting (HDS) certified servers provided by OVHcloud in Roubaix. We also provide an object storage service (Cellar) from cluster composed of such servers in Roubaix and Gravelines (separated by ~100 km), available as the `fr-north-hds` region.

Some customers asked us to make the Gravelines HDS region available independently for applications and add-ons, we listened to them. You can now deploy to it from [`clever-tools`](https://github.com/CleverCloud/clever-tools) or [the Console](https://console.clever-cloud.com) as `grahds`.

Please note that Clever Cloud’s services and infrastructures obtained the ISO 9001 certification last year, we’re waiting for the definitive approval of ISO 27001. HDS certification is the next step and our current priority