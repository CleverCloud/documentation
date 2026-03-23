---
title: Keycloak 26.5.6 (security update)
description: Keycloak 26.5.6 fixes eight CVEs including SSRF, IDOR, privilege escalation and information disclosure vulnerabilities
date: 2026-03-23
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

[The release 26.5.6](https://github.com/keycloak/keycloak/releases/tag/26.5.6) of Keycloak is available on Clever Cloud. It addresses eight security vulnerabilities: [CVE-2026-1180](https://nvd.nist.gov/vuln/detail/CVE-2026-1180), [CVE-2026-1035](https://nvd.nist.gov/vuln/detail/CVE-2026-1035), [CVE-2025-14777](https://nvd.nist.gov/vuln/detail/CVE-2025-14777), [CVE-2025-14082](https://nvd.nist.gov/vuln/detail/CVE-2025-14082), [CVE-2026-3121](https://nvd.nist.gov/vuln/detail/CVE-2026-3121), [CVE-2026-3190](https://nvd.nist.gov/vuln/detail/CVE-2026-3190), [CVE-2026-3911](https://nvd.nist.gov/vuln/detail/CVE-2026-3911) and [CVE-2026-2366](https://nvd.nist.gov/vuln/detail/CVE-2026-2366).

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.5.6` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.5.6
```

- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
