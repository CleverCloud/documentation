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

[The release 26.5.6](https://github.com/keycloak/keycloak/releases/tag/26.5.6) of Keycloak is available on Clever Cloud. It addresses eight security vulnerabilities: [CVE-2026-1180](https://github.com/advisories/GHSA-7vw6-5q2f-7w5r), [CVE-2026-1035](https://github.com/advisories/GHSA-m2w5-7xhv-w6fh), [CVE-2025-14777](https://github.com/advisories/GHSA-4cj5-g32w-86fv), [CVE-2025-14082](https://github.com/advisories/GHSA-6q37-7866-h27j), [CVE-2026-3121](https://github.com/keycloak/keycloak/issues/46719), [CVE-2026-3190](https://github.com/keycloak/keycloak/issues/46723), [CVE-2026-3911](https://github.com/advisories/GHSA-xh32-c9wx-phrp) and [CVE-2026-2366](https://github.com/advisories/GHSA-r8jr-wg88-fq5c).

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.5.6` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.5.6
```

- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
