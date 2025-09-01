---
title: Keycloak 26.3.3 now available with enhanced stability and dependency updates
date: 2025-08-25
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
description: Latest Keycloak update brings Infinispan 15.0.19.Final, Quarkus 3.20.2.1, improved cache configuration, and bug fixes.
excludeSearch: true
---

[The release 26.3.3](https://github.com/keycloak/keycloak/releases/26.3.3) of Keycloak is available on Clever Cloud. It brings Infinispan 15.0.19.Final, Quarkus 3.20.2.1, ensures cache configuration has correct number of owners, fixes [CVE-2025-7962](https://nvd.nist.gov/vuln/detail/CVE-2025-7962) and various bug for improved stability.

This release is now used as default for new created add-ons. To update an existing add-on, set `CC_KEYCLOAK_VERSION` of its Java application to `26.3.3` and rebuild it. You can also use [the new Clever Tools commands](/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.3.3
```

- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
