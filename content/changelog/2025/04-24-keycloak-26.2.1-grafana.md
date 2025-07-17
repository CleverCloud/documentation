---
title: "Keycloak 26.2.1 is available with new features and a Grafana dashboard"
date: 2025-04-24
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
description: Thanks to Clever Cloud's native Grafana experience
excludeSearch: true
---

The release `26.2.1` of Keycloak is available on Clever Cloud. [This new branch fixes](https://github.com/keycloak/keycloak/releases?q=26.2&expanded=true) some bugs, supports Standard Token Exchange according to [Token exchange specification](https://datatracker.ietf.org/doc/html/rfc8693), brings ECS (Elastic Common Schema) JSON format [for logs](https://www.keycloak.org/server/logging), fine-grained admin permissions, etc. To update, just set `CC_KEYCLOAK_VERSION` of the add-on's Java application to `26.2.1` and rebuild it.

## Grafana dashboard

Each Clever Cloud account organisation [comes with a pre-configured Grafana service](/developers/doc/metrics/#publish-your-own-metrics). With recent Keycloak enhancements on metrics and observability, we've worked on a Grafana dashboard ready to import:
- Go to the `Metrics in Grafana` section of your organisation or personal space in [Console](https://console.clever-cloud.com/)
- Open Grafana, click on the `+` icon in the upper right corner and select `Import` dashboard
- Import this [JSON file](https://cc-keycloak.cellar-c2.services.clever-cloud.com/keycloak-grafana-dashboard.json)

Then you'll have a `Keycloak dashboard` in your Grafana folders. Just select your Keycloak add-on in the `runtime section`, you'll automatically get instance's information, metrics, cache and performance data, etc.

## New features and settings

Starting with this release, Keycloak add-ons on Clever Cloud come with `admin-cli` client disabled by default. If you need it for provisioning through a `direct access grant`, you must enable it first.

You can now set up a new client with the `admin` role for `master` realm during build using `CC_KEYCLOAK_BOOTSTRAP_ADMIN_CLIENT_ID` and `CC_KEYCLOAK_BOOTSTRAP_ADMIN_CLIENT_SECRET` environment variables. Once created, delete them from your application. Bootstrap client [should be temporary](https://www.keycloak.org/server/bootstrap-admin-recovery) and is mostly necessary for provisioning.

- [Learn more about Keycloak on Clever Cloud](/developers/doc/addons/keycloak)
