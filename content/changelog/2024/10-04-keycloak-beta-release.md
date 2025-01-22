---
title: "Keycloak updated to 25.0.6, now in public beta"
date: 2024-10-04
tags:
  - addons
  - keycloak
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Release 26 is coming
aliases:
- /changelog/2024-10-04-keycloak-beta-release
excludeSearch: true
---

Clever Cloud's Keycloak add-on, developed with Please Open-it, is now available in public beta. We enhanced user experience, performances and features since [the alpha stage](../07-17-keycloak-public-release/). We revised the default configuration of underlying resources. We now use a `S flavored` Java application with more memory and a XXS Small Space PostgreSQL database which is enough for low-volume needs. Of course, you can change it according to your needs at any time.

The default Keycloak version is now 25.0.6. If you want to upgrade, change the `CC_KEYCLOAK_VERSION` environment variable to `25.0.6` and restart the Java application. You can also add the new `CC_METRICS_PROMETHEUS_PATH=/metrics` and `CC_METRICS_PROMETHEUS_PORT=9000`to access metrics [from Grafana](/developers/doc/metrics/#publish-your-own-metrics).

We plan to upgrade to [26.x](https://github.com/keycloak/keycloak/releases/tag/26.0.0) in the next few weeks after checking its stability and validating it for our platform.

- [Learn more about Keycloak on Clever Cloud](/developers/doc/addons/keycloak/)
