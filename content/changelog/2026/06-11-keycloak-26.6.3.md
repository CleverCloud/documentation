---
title: Keycloak 26.6.3 (security update)
description: Keycloak 26.6.3 ships on Clever Cloud with enhancements and addresses sixteen CVEs
date: 2026-06-11
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

[The release 26.6.3](https://github.com/keycloak/keycloak/releases/tag/26.6.3) of Keycloak is available on Clever Cloud. It brings some enhancements and bug fixes, but mainly security fixes.

This release addresses sixteen security vulnerabilities: [CVE-2026-0707](https://nvd.nist.gov/vuln/detail/CVE-2026-0707), [CVE-2026-4800](https://nvd.nist.gov/vuln/detail/CVE-2026-4800), [CVE-2026-4874](https://nvd.nist.gov/vuln/detail/CVE-2026-4874), [CVE-2026-7500](https://nvd.nist.gov/vuln/detail/CVE-2026-7500), [CVE-2026-8830](https://nvd.nist.gov/vuln/detail/CVE-2026-8830), [CVE-2026-8922](https://nvd.nist.gov/vuln/detail/CVE-2026-8922), [CVE-2026-9087](https://nvd.nist.gov/vuln/detail/CVE-2026-9087), [CVE-2026-9088](https://nvd.nist.gov/vuln/detail/CVE-2026-9088), [CVE-2026-9704](https://nvd.nist.gov/vuln/detail/CVE-2026-9704), [CVE-2026-9791](https://nvd.nist.gov/vuln/detail/CVE-2026-9791), [CVE-2026-9792](https://nvd.nist.gov/vuln/detail/CVE-2026-9792), [CVE-2026-9794](https://nvd.nist.gov/vuln/detail/CVE-2026-9794), [CVE-2026-9801](https://nvd.nist.gov/vuln/detail/CVE-2026-9801), [CVE-2026-9802](https://nvd.nist.gov/vuln/detail/CVE-2026-9802), [CVE-2026-37977](https://nvd.nist.gov/vuln/detail/CVE-2026-37977) and [CVE-2026-42581](https://nvd.nist.gov/vuln/detail/CVE-2026-42581).

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.6.3` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.6.3
```

- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
