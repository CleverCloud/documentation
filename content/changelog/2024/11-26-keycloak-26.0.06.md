---
title: "Keycloak 26.0.6 is available (security update)"
date: 2024-11-26
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
aliases:
- /changelog/2024-11-26-keycloak-26.0.06
excludeSearch: true
---

The release `26.0.6` of Keycloak is available on Clever Cloud. [It fixes](https://github.com/keycloak/keycloak/releases/26.0.6) some bugs, but also security issues: [CVE-2024-10451](https://nvd.nist.gov/vuln/detail/CVE-2024-10451), [CVE-2024-10270](https://nvd.nist.gov/vuln/detail/CVE-2024-10270), [CVE-2024-10492](https://nvd.nist.gov/vuln/detail/CVE-2024-10492), [CVE-2024-9666](https://nvd.nist.gov/vuln/detail/CVE-2024-9666) and [CVE-2024-10039](https://nvd.nist.gov/vuln/detail/CVE-2024-10039).

To update, just set `CC_KEYCLOAK_VERSION` of the add-on's Java application to `26.0.6` and rebuild it.

- [Learn more about Keycloak on Clever Cloud](/developers/doc/addons/keycloak)
