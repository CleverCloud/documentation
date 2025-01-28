---
title: Better new Logs
date: 2024-06-21
tags:
  - console
  - logs
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Pierre De Soyres
    link: https://github.com/pdesoyres-cc
    image: https://github.com/pdesoyres-cc.png?size=40
description: Lots of new features included!
aliases:
- /changelog/2024-06-21-better-new-logs
excludeSearch: true
---

We recently introduced a new Logs interface for applications in [the Console](https://console.clever-cloud.com), available on-demand in public beta. Since, we listened customers feedbacks and improved this feature. An updated version is now available, with two modes in the text filter field:

- Exact match (case-sensitive)
- Regular expression

You can select one or the other using the buttons to the right of the text field. This is only a first step, as we'll later introduce a new stack with indexed logs to better handle such filters and provide new features.

![New logs interface](/images/changelog/new-logs-update.webp)

Some of you also asked for a change of the default behavior of this Logs interface. Until now, users were redirected to `Live` view during a deployment, otherwise to the `7 days` view, containing all available deployments/instances, with logs of the last deployment shown. We today introduce a new mechanism and now remember the last choice of a user, per application.

Depending on your feedback, we'll improve this further in the coming weeks. Here again, this is a first step as the indexed logs will open up a wide range of possibilities in this area.

* Share your comments and ideas on our [GitHub Community](https://github.com/CleverCloud/Community/discussions/categories/new-logs-interface)

