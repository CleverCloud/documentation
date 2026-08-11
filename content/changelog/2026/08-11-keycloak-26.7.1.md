---
title: Keycloak 26.7.1 (security update)
description: Keycloak 26.7.1 brings the 26.7 features to Clever Cloud and fixes twelve vulnerabilities affecting OIDC, SAML, LDAP and fine-grained permissions
date: 2026-08-11
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

[The release 26.7.1](https://github.com/keycloak/keycloak/releases/tag/26.7.1) of Keycloak is available on Clever Cloud. It includes the new capabilities introduced in [Keycloak 26.7.0](https://github.com/keycloak/keycloak/releases/tag/26.7.0), such as the SCIM API promoted to preview, simplified multi-cluster high availability without external caches, step-up authentication for SAML clients and the experimental Admin API v2 for declarative client management.

This security update addresses twelve vulnerabilities: [CVE-2026-9793](https://nvd.nist.gov/vuln/detail/CVE-2026-9793), [CVE-2026-4629](https://nvd.nist.gov/vuln/detail/CVE-2026-4629), [CVE-2026-14209](https://nvd.nist.gov/vuln/detail/CVE-2026-14209), [CVE-2026-14614](https://nvd.nist.gov/vuln/detail/CVE-2026-14614), [CVE-2026-14615](https://nvd.nist.gov/vuln/detail/CVE-2026-14615), [CVE-2026-15573](https://nvd.nist.gov/vuln/detail/CVE-2026-15573), [CVE-2026-15572](https://nvd.nist.gov/vuln/detail/CVE-2026-15572), [CVE-2026-16100](https://nvd.nist.gov/vuln/detail/CVE-2026-16100), [CVE-2026-16442](https://nvd.nist.gov/vuln/detail/CVE-2026-16442), [CVE-2026-16443](https://nvd.nist.gov/vuln/detail/CVE-2026-16443), [CVE-2026-16071](https://nvd.nist.gov/vuln/detail/CVE-2026-16071) and [CVE-2026-16102](https://nvd.nist.gov/vuln/detail/CVE-2026-16102).

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.7.1` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.7.1
```

- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
