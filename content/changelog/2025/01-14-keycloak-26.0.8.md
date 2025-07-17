---
title: "Keycloak 26.0.8 is available (security update)"
date: 2025-01-14
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
description: Thanks to Clever Cloud, it's easy to upgrade
excludeSearch: true
---

The release `26.0.8` of Keycloak is available on Clever Cloud. [It fixes](https://github.com/keycloak/keycloak/releases/26.0.8) some bugs, but also security issues: [CVE-2024-11734](https://nvd.nist.gov/vuln/detail/CVE-2024-11734) and [CVE-2024-11736](https://nvd.nist.gov/vuln/detail/CVE-2024-11736). To update, just set `CC_KEYCLOAK_VERSION` of the add-on's Java application to `26.0.8` and rebuild it.

- [Learn more about Keycloak on Clever Cloud](/developers/doc/addons/keycloak)
