---
title: New Console dashboards for Elastic Stack, Jenkins, Materia KV, and Pulsar
description: Elastic Stack, Jenkins, Materia KV, and Pulsar add-ons get the new Console dashboard, with their state, information, and access details in one place, and Configuration provider gets its new header
date: 2026-01-16
tags:
  - console
  - addons
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

After [Keycloak](/changelog/2025/10-07-keycloak-dashboard/), then [Matomo, Metabase, and Otoroshi](/changelog/2025/10-15-operators-dashboards/), more add-ons get the new dashboard of the [Clever Cloud Console](https://console.clever-cloud.com). [Elastic Stack](/doc/deploy/databases/elastic/), [Jenkins](/doc/deploy/services/jenkins/), [Materia KV](/doc/deploy/databases/materia-kv/), and [Pulsar](/doc/deploy/pulsar/) add-ons now look and behave the same way.

The header shows the state of the add-on and links that depend on the product. Elastic Stack and Jenkins get a link to their logs. Elastic Stack also opens Kibana and Application Performance Monitoring (APM) when enabled. Jenkins opens its web interface, and Materia KV the KV Explorer. The information block gathers what applies to the add-on, such as version, specifications, encryption at rest, and creation date. It also links to the documentation and, for Elastic Stack, to Grafana.

Elastic Stack, Materia KV, and Pulsar also get an access block. It lists what you need to connect to the add-on, such as host, port, user, password, token, or URL. Each value is one click away from your clipboard. Tabs split them by usage when needed: Elastic, Kibana, and APM for Elastic Stack, or API and CLI for Pulsar.

[Configuration provider](/doc/deploy/services/config-provider/) add-ons get the new header too, above the form managing their environment variables.

- [Learn more about add-ons on Clever Cloud](/doc/deploy/addons/)
