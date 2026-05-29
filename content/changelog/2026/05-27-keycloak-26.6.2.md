---
title: Keycloak 26.6.2 (security update)
description: Keycloak 26.6.2 ships on Clever Cloud with the 26.6.1 fixes and addresses seventeen CVEs
date: 2026-05-27
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

[The release 26.6.2](https://github.com/keycloak/keycloak/releases/tag/26.6.2) of Keycloak is available on Clever Cloud. It brings some enhancements, but mainly security fixes. It also includes those from [26.6.1](https://github.com/keycloak/keycloak/releases/tag/26.6.1).

Together these releases address seventeen security vulnerabilities: [CVE-2026-4366](https://nvd.nist.gov/vuln/detail/CVE-2026-4366), [CVE-2026-4633](https://nvd.nist.gov/vuln/detail/CVE-2026-4633), [CVE-2026-33870](https://nvd.nist.gov/vuln/detail/CVE-2026-33870), [CVE-2026-33871](https://nvd.nist.gov/vuln/detail/CVE-2026-33871), [CVE-2026-4628](https://nvd.nist.gov/vuln/detail/CVE-2026-4628), [CVE-2026-4630](https://nvd.nist.gov/vuln/detail/CVE-2026-4630), [CVE-2026-5588](https://nvd.nist.gov/vuln/detail/CVE-2026-5588), [CVE-2026-6856](https://nvd.nist.gov/vuln/detail/CVE-2026-6856), [CVE-2026-7307](https://nvd.nist.gov/vuln/detail/CVE-2026-7307), [CVE-2026-7504](https://nvd.nist.gov/vuln/detail/CVE-2026-7504), [CVE-2026-7507](https://nvd.nist.gov/vuln/detail/CVE-2026-7507), [CVE-2026-7571](https://nvd.nist.gov/vuln/detail/CVE-2026-7571), [CVE-2026-37978](https://nvd.nist.gov/vuln/detail/CVE-2026-37978), [CVE-2026-37979](https://nvd.nist.gov/vuln/detail/CVE-2026-37979), [CVE-2026-37980](https://nvd.nist.gov/vuln/detail/CVE-2026-37980), [CVE-2026-37981](https://nvd.nist.gov/vuln/detail/CVE-2026-37981) and [CVE-2026-37982](https://nvd.nist.gov/vuln/detail/CVE-2026-37982).

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.6.2` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.6.2
```

- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
