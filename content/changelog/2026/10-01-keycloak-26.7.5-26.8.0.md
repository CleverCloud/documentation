---
title: Keycloak 26.7.5 and 26.8.0 are available (security updates)
description: Keycloak 26.7.5 and 26.8.0 fix critical vulnerabilities in dependencies and are now the only recommended versions, while 26.8.0 adds digital wallet credentials, SCIM provisioning and stateless multi-cluster deployments
date: 2026-10-01
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

[Keycloak 26.7.5](https://github.com/keycloak/keycloak/releases/tag/26.7.5) and [Keycloak 26.8.0](https://github.com/keycloak/keycloak/releases/tag/26.8.0) are available on Clever Cloud. Both releases fix security vulnerabilities, some of them critical. Earlier versions are affected by known security flaws, so 26.7.5 and 26.8.0 are now the only versions Clever Cloud recommends. Update your Keycloak add-ons to one of them as soon as possible.

## Keycloak 26.7.5

Keycloak 26.7.5 updates several dependencies to fix security vulnerabilities, including critical ones. [CVE-2026-84939](https://nvd.nist.gov/vuln/detail/CVE-2026-84939), rated 9.1, is a path traversal in the template loading of FreeMarker. The release also closes vulnerabilities in Bouncy Castle ([CVE-2026-8763](https://nvd.nist.gov/vuln/detail/CVE-2026-8763)) and Netty ([CVE-2026-75595](https://nvd.nist.gov/vuln/detail/CVE-2026-75595)). It also brings Quarkus 3.33.4 and fixes high severity issues in Bouncy Castle FIPS and the OWASP Java HTML Sanitizer: [CVE-2026-8798](https://nvd.nist.gov/vuln/detail/CVE-2026-8798), [CVE-2026-13505](https://nvd.nist.gov/vuln/detail/CVE-2026-13505) and [CVE-2025-66021](https://nvd.nist.gov/vuln/detail/CVE-2025-66021).

The other fixes address medium and low severity issues in Keycloak itself, mostly in client policies, token introspection, token exchange and the Device Authorization Grant: [CVE-2026-18203](https://nvd.nist.gov/vuln/detail/CVE-2026-18203), [CVE-2026-18207](https://nvd.nist.gov/vuln/detail/CVE-2026-18207), [CVE-2026-18208](https://nvd.nist.gov/vuln/detail/CVE-2026-18208), [CVE-2026-88770](https://nvd.nist.gov/vuln/detail/CVE-2026-88770), [CVE-2026-89298](https://nvd.nist.gov/vuln/detail/CVE-2026-89298), [CVE-2026-16103](https://nvd.nist.gov/vuln/detail/CVE-2026-16103), [CVE-2026-18211](https://nvd.nist.gov/vuln/detail/CVE-2026-18211), [CVE-2026-93999](https://nvd.nist.gov/vuln/detail/CVE-2026-93999), [CVE-2026-18206](https://nvd.nist.gov/vuln/detail/CVE-2026-18206) and [CVE-2026-18217](https://nvd.nist.gov/vuln/detail/CVE-2026-18217).

Two changes may require an action before you update. The `client-updater-source-groups` client policy condition now matches the full path of a group instead of its name: a value without a leading slash targets a top-level group, so write subgroups as `/topGroup/subGroup`. If you develop a custom organisation provider, implement `OrganizationProvider#getByAlias`, now abstract. The release also fixes bugs affecting rolling restarts of clustered nodes, persistent sessions with debug logs enabled, and the resolution of organisations during authentication.

## Keycloak 26.8.0

Keycloak 26.8.0 includes all the security fixes of 26.7.5, along with [CVE-2026-12388](https://nvd.nist.gov/vuln/detail/CVE-2026-12388), [CVE-2026-59889](https://nvd.nist.gov/vuln/detail/CVE-2026-59889), [CVE-2026-59903](https://nvd.nist.gov/vuln/detail/CVE-2026-59903), [CVE-2026-19608](https://nvd.nist.gov/vuln/detail/CVE-2026-19608), [CVE-2026-54515](https://nvd.nist.gov/vuln/detail/CVE-2026-54515), [CVE-2026-14781](https://nvd.nist.gov/vuln/detail/CVE-2026-14781) and [CVE-2026-4633](https://nvd.nist.gov/vuln/detail/CVE-2026-4633). It moves to Quarkus 3.40 and brings new features:

- Digital wallet credentials, issued with OID4VCI in preview and verified with OID4VP as an experimental feature
- Multi-cluster deployments without an external cache, through the `stateless` feature, now supported
- SCIM API and client secret rotation, now supported and enabled by default
- Token exchange delegation in preview, for AI agents and automation acting on behalf of a user
- Identity providers shared across several organisations and redesigned identity provider buttons on the login page

Review the [upgrading guide](https://www.keycloak.org/docs/latest/upgrading/) before you update, as this version changes some default behaviors. Identity provider mappers no longer grant admin roles unless you enable `allowAdminRoleMapping`, and retrieving client secrets now requires the `manage-clients` role or equivalent client management permissions. Keycloak now ignores the `initiating_idp` logout parameter by default and no longer adds disabled clients to the `aud` and `resource_access` claims of tokens. The user session idle timeout now caps the lifetime of refresh tokens, and custom login themes may need changes to support the new identity provider buttons. On PostgreSQL, Keycloak creates the indexes skipped during schema migration in the background, after startup.

This release also deprecates several features, including the `multi-site` feature, replaced by `stateless`, in-memory login failures and the "Full scope allowed" client setting. The Keycloak Realm Operator reaches its end of life.

## How to update

Update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.8.0` or `26.7.5` and rebuild it, or use [Clever Tools](/doc/manage/cli/operators/). Each `version update` command rebuilds the add-on, so run only one of them. Check the current version, then update to 26.8.0:

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId --format json
clever keycloak version update yourKeycloakNameOrId --target 26.8.0
```

To stay on the 26.7 branch, update to 26.7.5 instead:

```bash
clever keycloak version update yourKeycloakNameOrId --target 26.7.5
```

- [Read the Keycloak 26.7.5 release notes](https://www.keycloak.org/2026/09/keycloak-2675-released)
- [Read the Keycloak 26.8.0 release notes](https://www.keycloak.org/2026/10/keycloak-2680-released)
- [Learn more about Keycloak on Clever Cloud](/doc/deploy/services/keycloak)
