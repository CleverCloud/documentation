---
title: Keycloak 26.8.2 is available (security update)
description: Keycloak 26.8.2 brings the fixes of 26.8.1 and 26.8.2 to Clever Cloud, closing more than fifty vulnerabilities in authentication, identity brokering, SAML, token exchange, and admin permissions
date: 2026-11-10
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

[Keycloak 26.8.2](https://github.com/keycloak/keycloak/releases/tag/26.8.2) is available on Clever Cloud. It includes the fixes of [Keycloak 26.8.1](https://github.com/keycloak/keycloak/releases/tag/26.8.1). Both are security releases. Together, they close more than fifty vulnerabilities, several of them allowing an account takeover or an unauthenticated denial of service. Update your Keycloak add-ons to this version as soon as possible, from the Console or with Clever Tools.

## Keycloak 26.8.1

Keycloak 26.8.1 closes eighteen vulnerabilities in Keycloak itself, and updates Jackson Databind ([CVE-2026-91777](https://nvd.nist.gov/vuln/detail/CVE-2026-91777)) and simple-git. Several of them affect authentication and identity brokering. They include a bypass of the two-factor authentication setup, a linking to the wrong account, and a reuse of pushed authorization requests. Another allows Key Distribution Center (KDC) spoofing with Kerberos: [CVE-2026-15943](https://nvd.nist.gov/vuln/detail/CVE-2026-15943), [CVE-2026-18569](https://nvd.nist.gov/vuln/detail/CVE-2026-18569), [CVE-2026-82968](https://nvd.nist.gov/vuln/detail/CVE-2026-82968), [CVE-2026-94218](https://nvd.nist.gov/vuln/detail/CVE-2026-94218), [CVE-2026-96446](https://nvd.nist.gov/vuln/detail/CVE-2026-96446), [CVE-2026-96445](https://nvd.nist.gov/vuln/detail/CVE-2026-96445), and [CVE-2026-95503](https://nvd.nist.gov/vuln/detail/CVE-2026-95503).

Others let delegated administrators escalate their permissions, bypass a denied reset-password permission, or read resources across realms. They affect fine-grained admin permissions, the Admin REST API, and the authorization services: [CVE-2026-94001](https://nvd.nist.gov/vuln/detail/CVE-2026-94001), [CVE-2026-94000](https://nvd.nist.gov/vuln/detail/CVE-2026-94000), [CVE-2026-94215](https://nvd.nist.gov/vuln/detail/CVE-2026-94215), [CVE-2026-94213](https://nvd.nist.gov/vuln/detail/CVE-2026-94213), [CVE-2026-94217](https://nvd.nist.gov/vuln/detail/CVE-2026-94217), [CVE-2026-97177](https://nvd.nist.gov/vuln/detail/CVE-2026-97177), and [CVE-2026-97311](https://nvd.nist.gov/vuln/detail/CVE-2026-97311).

The release also prevents standard token exchange from bypassing the mutual TLS (mTLS) certificate binding, and a path traversal through certificate revocation list (CRL) distribution points. It stops an unbounded creation of metric series on the broker login endpoint, and a plaintext downgrade of SMTP connections with `starttls`: [CVE-2026-97846](https://nvd.nist.gov/vuln/detail/CVE-2026-97846), [CVE-2026-103884](https://nvd.nist.gov/vuln/detail/CVE-2026-103884), [CVE-2026-101333](https://nvd.nist.gov/vuln/detail/CVE-2026-101333), and [CVE-2026-107121](https://nvd.nist.gov/vuln/detail/CVE-2026-107121).

On the bug side, offline client sessions created through token exchange are no longer orphaned, and token introspection returns the `act` claim of delegation tokens. The Trust Email option works again with the userinfo endpoint. Signing out of one session in the Admin Console no longer logs out another session of the same user. Clustered deployments get fixes for JGroups certificate reloads and unreachable nodes.

## Keycloak 26.8.2

Keycloak 26.8.2 closes thirty-three more vulnerabilities and moves to Quarkus 3.40.1.1. Eight of them affect the Security Assertion Markup Language (SAML) support. They include unauthenticated denials of service, and a signature bypass of the redirect binding that allows a broker login as any user. Keycloak also accepted assertions from the wrong issuer, without proof of key possession, or despite a `ProxyRestriction` condition: [CVE-2026-107123](https://nvd.nist.gov/vuln/detail/CVE-2026-107123), [CVE-2026-107602](https://nvd.nist.gov/vuln/detail/CVE-2026-107602), [CVE-2026-110931](https://nvd.nist.gov/vuln/detail/CVE-2026-110931), [CVE-2026-93998](https://nvd.nist.gov/vuln/detail/CVE-2026-93998), [CVE-2026-82965](https://nvd.nist.gov/vuln/detail/CVE-2026-82965), [CVE-2026-92855](https://nvd.nist.gov/vuln/detail/CVE-2026-92855), [CVE-2026-92856](https://nvd.nist.gov/vuln/detail/CVE-2026-92856), and [CVE-2026-117691](https://nvd.nist.gov/vuln/detail/CVE-2026-117691).

Ten others affect OpenID Connect flows and dynamic client registration. They allow session takeovers through Client-Initiated Backchannel Authentication (CIBA) or an injected `id_token_hint` at logout. Protocol mappers could forge the `sub`, `aud`, or `realm_access` claims, and token exchange could issue tokens with an unlimited lifetime: [CVE-2026-105305](https://nvd.nist.gov/vuln/detail/CVE-2026-105305), [CVE-2026-107623](https://nvd.nist.gov/vuln/detail/CVE-2026-107623), [CVE-2026-107124](https://nvd.nist.gov/vuln/detail/CVE-2026-107124), [CVE-2026-97367](https://nvd.nist.gov/vuln/detail/CVE-2026-97367), [CVE-2026-97174](https://nvd.nist.gov/vuln/detail/CVE-2026-97174), [CVE-2026-96547](https://nvd.nist.gov/vuln/detail/CVE-2026-96547), [CVE-2026-96460](https://nvd.nist.gov/vuln/detail/CVE-2026-96460), [CVE-2026-97848](https://nvd.nist.gov/vuln/detail/CVE-2026-97848), [CVE-2026-92857](https://nvd.nist.gov/vuln/detail/CVE-2026-92857), and [CVE-2026-96447](https://nvd.nist.gov/vuln/detail/CVE-2026-96447).

Authentication and organisations are also affected, with account takeovers through an authentication race or the automatic linking of an unverified identity provider email. Others involve a stale authentication note in identity-first login, and a stored cross-site scripting (XSS) on the login page: [CVE-2026-92358](https://nvd.nist.gov/vuln/detail/CVE-2026-92358), [CVE-2026-107889](https://nvd.nist.gov/vuln/detail/CVE-2026-107889), [CVE-2026-112201](https://nvd.nist.gov/vuln/detail/CVE-2026-112201), [CVE-2026-112208](https://nvd.nist.gov/vuln/detail/CVE-2026-112208), [CVE-2026-103112](https://nvd.nist.gov/vuln/detail/CVE-2026-103112), and [CVE-2026-97175](https://nvd.nist.gov/vuln/detail/CVE-2026-97175).

The release also fixes permission bypasses in the Admin API, fine-grained admin permissions, and user-managed access, including a realm takeover by a client manager. It makes `kcadm` reject self-signed certificates absent from its custom truststore: [CVE-2026-114232](https://nvd.nist.gov/vuln/detail/CVE-2026-114232), [CVE-2026-97847](https://nvd.nist.gov/vuln/detail/CVE-2026-97847), [CVE-2026-96457](https://nvd.nist.gov/vuln/detail/CVE-2026-96457), [CVE-2026-109081](https://nvd.nist.gov/vuln/detail/CVE-2026-109081), [CVE-2026-96448](https://nvd.nist.gov/vuln/detail/CVE-2026-96448), [CVE-2026-19688](https://nvd.nist.gov/vuln/detail/CVE-2026-19688), and [CVE-2026-96453](https://nvd.nist.gov/vuln/detail/CVE-2026-96453).

Two others concern the distribution of Keycloak. They are an out-of-bounds write in the bundled Brotli decoder, and an unauthenticated disk exhaustion through the gzip cache of themes: [CVE-2026-111497](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) and [CVE-2026-110932](https://nvd.nist.gov/vuln/detail/CVE-2026-110932).

Some of these fixes change behaviors your integrations may rely on. The Admin REST API now checks the audience of tokens. Assign the `kc-admin-api` client scope to your own clients and service accounts, or it answers `401` to their tokens. Access and ID tokens issued by the standard token exchange no longer outlive the subject token. Identity providers no longer link accounts on an unverified email without **Trust Email**.

The SAML broker now rejects assertions without a bearer subject confirmation, such as holder-of-key ones, and those with a `ProxyRestriction` condition. Dynamic client registration no longer accepts protocol mappers until a realm administrator allows their types. With StartTLS enabled, sending emails fails if the SMTP server doesn't support it. Review the [migration guide](https://www.keycloak.org/docs/latest/upgrading/#migration-changes) before you update.

Among the bug fixes, reaching the maximum number of concurrent sessions no longer counts as a login failure for brute force protection. A PEM bundle with several certificates is fully imported in FIPS mode, and theme resources no longer return `404` on a cold cache. Realm imports with a separate users file work again, and the periodic synchronization of user storage providers follows the configured period again.

## How to update

Update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.8.2` and rebuild it, or use [Clever Tools](/doc/tools/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId --format json
clever keycloak version update yourKeycloakNameOrId --target 26.8.2
```

- [Read the Keycloak 26.8.1 release notes](https://www.keycloak.org/2026/10/keycloak-2681-released)
- [Read the Keycloak 26.8.2 release notes](https://www.keycloak.org/2026/11/keycloak-2682-released)
- [Learn more about Keycloak on Clever Cloud](/doc/deploy/services/keycloak)
