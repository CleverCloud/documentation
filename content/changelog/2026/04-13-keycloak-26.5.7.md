---
title: Keycloak 26.5.7 (security update)
description: Keycloak 26.5.7 fixes seven CVEs including access control, path traversal, privilege escalation and denial of service vulnerabilities
date: 2026-04-13
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

[The release 26.5.7](https://github.com/keycloak/keycloak/releases/tag/26.5.7) of Keycloak is available on Clever Cloud. It addresses seven security vulnerabilities: [CVE-2025-14083](https://nvd.nist.gov/vuln/detail/CVE-2025-14083), [CVE-2026-1002](https://nvd.nist.gov/vuln/detail/CVE-2026-1002), [CVE-2026-3429](https://nvd.nist.gov/vuln/detail/CVE-2026-3429), [CVE-2026-4634](https://nvd.nist.gov/vuln/detail/CVE-2026-4634), [CVE-2026-4636](https://nvd.nist.gov/vuln/detail/CVE-2026-4636), [CVE-2026-3872](https://nvd.nist.gov/vuln/detail/CVE-2026-3872) and [CVE-2026-4282](https://nvd.nist.gov/vuln/detail/CVE-2026-4282).

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.5.7` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.5.7
```

- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
