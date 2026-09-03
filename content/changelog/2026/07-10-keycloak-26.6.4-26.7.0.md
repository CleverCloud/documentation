---
title: Keycloak 26.6.4 and 26.7.0 are available (security updates)
description: Keycloak 26.6.4 and 26.7.0 fix twelve vulnerabilities, while 26.7.0 adds SCIM provisioning, multi-cluster improvements and SAML step-up authentication
date: 2026-07-10
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

[Keycloak 26.6.4](https://github.com/keycloak/keycloak/releases/tag/26.6.4) and [Keycloak 26.7.0](https://github.com/keycloak/keycloak/releases/tag/26.7.0) are available on Clever Cloud. Keycloak 26.6.4 addresses eight security vulnerabilities: [CVE-2026-9099](https://nvd.nist.gov/vuln/detail/CVE-2026-9099), [CVE-2026-9083](https://nvd.nist.gov/vuln/detail/CVE-2026-9083), [CVE-2026-9086](https://nvd.nist.gov/vuln/detail/CVE-2026-9086), [CVE-2026-9705](https://nvd.nist.gov/vuln/detail/CVE-2026-9705), [CVE-2026-9795](https://nvd.nist.gov/vuln/detail/CVE-2026-9795), [CVE-2026-9799](https://nvd.nist.gov/vuln/detail/CVE-2026-9799), [CVE-2026-9800](https://nvd.nist.gov/vuln/detail/CVE-2026-9800) and [CVE-2026-11800](https://nvd.nist.gov/vuln/detail/CVE-2026-11800).

Keycloak 26.7.0 fixes four additional vulnerabilities: [CVE-2026-9796](https://nvd.nist.gov/vuln/detail/CVE-2026-9796), [CVE-2026-9689](https://nvd.nist.gov/vuln/detail/CVE-2026-9689), [CVE-2026-9798](https://nvd.nist.gov/vuln/detail/CVE-2026-9798) and [CVE-2026-11986](https://nvd.nist.gov/vuln/detail/CVE-2026-11986). It also promotes the SCIM API to preview, adds a preview of simplified multi-cluster high availability without external caches and supports step-up authentication for SAML clients.

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.7.0` and rebuild it, or use [Clever Tools](/doc/manage/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.7.0
```

- [Learn more about Keycloak on Clever Cloud](/doc/deploy/services/keycloak)
