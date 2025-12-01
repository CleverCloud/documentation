---
title: Keycloak 26.4.6 is available (security release)
description: Keycloak 26.4.6 security release with CVE-2025-13467 fix and LDAP referral filtering is now available on Clever Cloud
date: 2025-11-26
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
excludeSearch: true
---

[The release 26.4.6](https://github.com/keycloak/keycloak/releases/26.4.6) of Keycloak is available on Clever Cloud. It brings multiple enhancements and a security fix for [CVE-2025-13467](https://nvd.nist.gov/vuln/detail/CVE-2025-13467). It adds filtering of LDAP referrals by default to align with best practices for LDAP configurations.

You can update through add-on’s dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.4.6` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.4.6
```

- [Learn more about Keycloak 26.4.6](https://www.keycloak.org/2025/11/keycloak-2646-released)
- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
