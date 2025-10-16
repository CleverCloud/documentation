---
title: Operators' service dependencies update
description: Rely on new dashboards to get URL and credentials for Keycloak, Metabase, Matomo and Otoroshi
date: 2025-10-16
tags:
  - addons
  - keycloak
  - matomo
  - metabase
  - otoroshi
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

As new dashboards are available for [Keycloak](/changelog/2025/10-07-keycloak-dashboard/), [Metabase, Matomo and Otoroshi](/changelog/2025/10-15-operators-dashboards/), you can get important information from them. Thus, we don't show URLs and initial credentials anymore in shared dependencies tab on newly created services.

You can also rely on [Clever Tools](/doc/cli/operators/) or [the API](/api/v4#operators) to manage operators and their underlying resources.
