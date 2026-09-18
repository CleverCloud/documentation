---
title: Keycloak 26.7.4 (security update)
description: Keycloak 26.7.4 fixes six vulnerabilities, including an authorization bypass in the policy enforcer, and normalizes resource URIs before matching them in Authorization Services
date: 2026-09-17
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

[The release 26.7.4](https://github.com/keycloak/keycloak/releases/tag/26.7.4) of Keycloak is available on Clever Cloud. It's a security update that addresses six vulnerabilities, without any critical one.

[CVE-2026-74909](https://nvd.nist.gov/vuln/detail/CVE-2026-74909), rated 8.1, is an incomplete fix: a percent-encoded semicolon in a request path bypasses the matrix parameters stripping of the policy enforcer and grants access to protected resources. [CVE-2026-79651](https://nvd.nist.gov/vuln/detail/CVE-2026-79651), rated 7.5, lets an unauthenticated attacker exhaust memory through the theme localization endpoints. [CVE-2026-17526](https://nvd.nist.gov/vuln/detail/CVE-2026-17526), rated 7.2, allows a user holding the `impersonation` role to impersonate a realm administrator.

The other fixes address [CVE-2026-18212](https://nvd.nist.gov/vuln/detail/CVE-2026-18212), [CVE-2026-90997](https://nvd.nist.gov/vuln/detail/CVE-2026-90997) and [CVE-2026-19607](https://nvd.nist.gov/vuln/detail/CVE-2026-19607), affecting SAML Redirect binding, replay protection on MySQL and MariaDB, and an account lockout in the first broker login flow.

Authorization Services now normalize resource URIs before matching them. They strip matrix parameters, resolve dot segments, decode `%2F`, and drop the trailing slash, query string and fragment. If your resources rely on these elements to differ, review their URIs before you update. The release also upgrades Quarkus to 3.33.3.2 and fixes performance issues introduced in 26.6.2, an Admin Console error when you select a subgroup and a startup crash with the Oracle OCI driver.

Update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.7.4` and rebuild it, or use [Clever Tools](/doc/manage/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId --format json
clever keycloak version update yourKeycloakNameOrId --target 26.7.4
```

- [Read the Keycloak 26.7.4 release notes](https://www.keycloak.org/2026/09/keycloak-2674-released)
- [Read the Keycloak upgrading guide](https://www.keycloak.org/docs/latest/upgrading/)
- [Learn more about Keycloak on Clever Cloud](/doc/deploy/services/keycloak)
