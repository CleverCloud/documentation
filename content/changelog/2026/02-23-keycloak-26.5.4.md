---
title: Keycloak 26.5.4 (security update)
description: Keycloak 26.5.4 fixes five CVEs including SAML vulnerabilities, authorization header bypass, and environment information disclosure
date: 2026-02-23
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

[The release 26.5.4](https://github.com/keycloak/keycloak/releases/tag/26.5.4) of Keycloak is available on Clever Cloud. It fixes bugs, improves performance and addresses five security vulnerabilities: [CVE-2026-1190](https://nvd.nist.gov/vuln/detail/CVE-2026-1190), [CVE-2026-0707](https://nvd.nist.gov/vuln/detail/CVE-2026-0707), [CVE-2025-5416](https://nvd.nist.gov/vuln/detail/CVE-2025-5416), [CVE-2026-2575](https://github.com/keycloak/keycloak/issues/46372) and [CVE-2026-2733](https://nvd.nist.gov/vuln/detail/CVE-2026-2733).

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.5.4` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.5.4
```

- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
