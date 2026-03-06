---
title: Keycloak 26.5.5 (security update)
description: Keycloak 26.5.5 fixes four CVEs related to SAML broker authentication bypass and encrypted assertion injection
date: 2026-03-06
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

[The release 26.5.5](https://github.com/keycloak/keycloak/releases/tag/26.5.5) of Keycloak is available on Clever Cloud. It addresses four security vulnerabilities: [CVE-2026-3047](https://nvd.nist.gov/vuln/detail/CVE-2026-3047), [CVE-2026-3009](https://nvd.nist.gov/vuln/detail/CVE-2026-3009), [CVE-2026-2603](https://github.com/keycloak/keycloak/issues/46911) and [CVE-2026-2092](https://github.com/keycloak/keycloak/issues/46912).

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.5.5` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.5.5
```

- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
