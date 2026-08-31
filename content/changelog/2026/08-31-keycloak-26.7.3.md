---
title: Keycloak 26.7.3 (security update)
description: Keycloak 26.7.3 fixes twenty vulnerabilities affecting token exchange, OIDC and fine-grained admin permissions, and corrects performance regressions introduced in 26.7.1
date: 2026-08-31
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

[The release 26.7.3](https://github.com/keycloak/keycloak/releases/tag/26.7.3) of Keycloak is available on Clever Cloud. It's a security update that addresses twenty vulnerabilities, without any critical one, unlike [26.7.2](/changelog/2026/08-24-keycloak-26.7.2/) published last week.

Two issues stand out. [CVE-2026-18215](https://nvd.nist.gov/vuln/detail/CVE-2026-18215) and [CVE-2026-18214](https://nvd.nist.gov/vuln/detail/CVE-2026-18214), both rated 8.1, let external token exchanges bypass the configured Microsoft tenant and Google hosted domain. [CVE-2026-18571](https://nvd.nist.gov/vuln/detail/CVE-2026-18571), rated 7.2, allows a delegated administrator to assign groups they don't manage when creating a user.

[CVE-2026-35563](https://nvd.nist.gov/vuln/detail/CVE-2026-35563) carries the highest score of the release, 8.5, but it doesn't affect running instances. The vulnerable Apache Directory client is a test dependency, used by the embedded LDAP server of the Keycloak test suite. The upgrade to ApacheDS 2.0.0.AM27 that closes it leaves the LDAP user federation code untouched.

The other fixes address medium and low severity issues, mostly in fine-grained admin permissions (FGAP v2) and OIDC edge cases: [CVE-2026-16093](https://nvd.nist.gov/vuln/detail/CVE-2026-16093), [CVE-2026-16072](https://nvd.nist.gov/vuln/detail/CVE-2026-16072), [CVE-2026-16089](https://nvd.nist.gov/vuln/detail/CVE-2026-16089), [CVE-2026-16104](https://nvd.nist.gov/vuln/detail/CVE-2026-16104), [CVE-2026-16105](https://nvd.nist.gov/vuln/detail/CVE-2026-16105), [CVE-2026-16106](https://nvd.nist.gov/vuln/detail/CVE-2026-16106), [CVE-2026-16108](https://nvd.nist.gov/vuln/detail/CVE-2026-16108), [CVE-2026-17059](https://nvd.nist.gov/vuln/detail/CVE-2026-17059), [CVE-2026-18201](https://nvd.nist.gov/vuln/detail/CVE-2026-18201), [CVE-2026-18209](https://nvd.nist.gov/vuln/detail/CVE-2026-18209), [CVE-2026-18218](https://nvd.nist.gov/vuln/detail/CVE-2026-18218), [CVE-2026-18570](https://nvd.nist.gov/vuln/detail/CVE-2026-18570), [CVE-2026-18572](https://nvd.nist.gov/vuln/detail/CVE-2026-18572), [CVE-2026-18573](https://nvd.nist.gov/vuln/detail/CVE-2026-18573), [CVE-2026-79652](https://nvd.nist.gov/vuln/detail/CVE-2026-79652) and [CVE-2026-19729](https://github.com/keycloak/keycloak/issues/51745), an incomplete fix for a path traversal reported in 26.6.4.

The release also corrects performance issues of the 26.7 branch. Admin API requests no longer resolve every role across all realms, their cost stops growing super-linearly with the number of realms, and an upgrade no longer causes sustained high CPU usage on every node. It fixes an Admin UI regression introduced in 26.7.2, a `NullPointerException` on composite roles referencing a deleted role and offline client session errors.

Update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.7.3` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId --target 26.7.3
```

- [Read the Keycloak 26.7.3 release notes](https://www.keycloak.org/2026/08/keycloak-2673-released)
- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
