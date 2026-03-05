---
title: Keycloak 26.5.3 (security update)
description: Keycloak 26.5.3 fixes four CVEs including disabled user token grants, forged invitation tokens, and UMA policy endpoint vulnerabilities
date: 2026-02-10
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

[The release 26.5.3](https://github.com/keycloak/keycloak/releases/tag/26.5.3) of Keycloak is available on Clever Cloud. It fixes bugs, reduces memory consumption during startup and addresses four security vulnerabilities: [CVE-2026-1609](https://github.com/keycloak/keycloak/issues/46144), [CVE-2026-1529](https://nvd.nist.gov/vuln/detail/CVE-2026-1529), [CVE-2026-1486](https://nvd.nist.gov/vuln/detail/CVE-2026-1486) and [CVE-2025-14778](https://nvd.nist.gov/vuln/detail/CVE-2025-14778).

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.5.3` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.5.3
```

- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
