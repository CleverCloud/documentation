---
title: "Keycloak critical security update, 26.7.2 is available"
description: Keycloak 26.7.2 fixes CVE-2026-18963, a critical unauthenticated account takeover vulnerability in the password reset flow
date: 2026-08-24
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

[Keycloak 26.7.2](https://github.com/keycloak/keycloak/releases/tag/26.7.2) is available on Clever Cloud. It fixes [CVE-2026-18963](https://access.redhat.com/security/cve/CVE-2026-18963), a critical vulnerability with a CVSS score of 9.1. An unauthenticated attacker can bypass the email verification step of the password reset flow, set new credentials for any user and take control of their account without user interaction.

## Update or temporarily disable password resets

Update every Keycloak add-on to version 26.7.2 as soon as possible. You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.7.2` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId --target 26.7.2
```

If you can't update immediately, temporarily disable password resets in every realm. In the Keycloak Admin Console, select a realm, open **Realm settings**, then **Login**, switch **Forgot password** to **Off** and repeat for every realm. This prevents legitimate users from requesting a password reset; re-enable the feature only after the instance runs version 26.7.2.

If you suspect that an account was compromised before the update, reset its credentials, revoke its active sessions and review its recent activity, roles and permissions for unexpected changes.

## Other security fixes

Keycloak 26.7.2 addresses seven other vulnerabilities: [CVE-2026-45292](https://nvd.nist.gov/vuln/detail/CVE-2026-45292), [CVE-2026-14613](https://nvd.nist.gov/vuln/detail/CVE-2026-14613), [CVE-2026-59888](https://nvd.nist.gov/vuln/detail/CVE-2026-59888), [CVE-2026-59889](https://nvd.nist.gov/vuln/detail/CVE-2026-59889), [CVE-2026-15945](https://nvd.nist.gov/vuln/detail/CVE-2026-15945), [CVE-2026-17048](https://nvd.nist.gov/vuln/detail/CVE-2026-17048) and [CVE-2026-15571](https://nvd.nist.gov/vuln/detail/CVE-2026-15571). They cover account takeover risks in account linking flows, permission bypasses and information disclosure in fine-grained admin permissions, exposure of rotated client secrets, unbounded memory allocation in OpenTelemetry baggage processing and vulnerabilities in Jackson Databind. The release also prevents `show-config` from displaying the Vault keystore password in clear text and fixes bugs affecting SCIM, OIDC, WebAuthn, stateless clusters and the Admin UI.

- [Read the CVE-2026-18963 advisory](https://access.redhat.com/security/cve/CVE-2026-18963)
- [Read the Keycloak 26.7.2 release notes](https://www.keycloak.org/2026/08/keycloak-2672-released)
- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
