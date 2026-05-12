---
title: Keycloak 26.6 with per-realm IP filtering
description: Keycloak 26.6 is available on Clever Cloud and adds IP filtering to restrict admin, public and SCIM endpoints per realm
date: 2026-05-12
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

[The release 26.6.1](https://github.com/keycloak/keycloak/releases/tag/26.6.1) of Keycloak is available on Clever Cloud, bringing bug fixes on top of the new features introduced in [Keycloak 26.6.0](https://github.com/keycloak/keycloak/releases/tag/26.6.0). This version graduates several features from preview and adds new ones:

- Step-up authentication for SAML (preview)
- Zero-downtime patch releases supported, with rolling updates for minor versions
- New Groups scope for user membership changes and Vault SPI lookup for client secrets
- JWT Authorization Grant, Federated client authentication and Workflows promoted to supported
- Identity Brokering APIs V2 (preview), the successor to legacy Token Exchange V1 for retrieving external IdP tokens
- OAuth Client ID Metadata Document (experimental), enabling Keycloak as an authorization server for the Model Context Protocol
- New `KCRAW_` environment variable prefix to preserve literal values, dedicated HTTP access log file, configurable log file rotation, graceful HTTP shutdown

## Organization groups

[Organization groups](https://www.keycloak.org/2026/04/org-groups) give each organization its own isolated, nestable group hierarchy. Two organizations can now have a `/Engineering/Backend` group each without sharing members, attributes or identifiers, which removes the need to namespace groups across the realm.

Identity providers can assign users to organization groups automatically through two new mappers: Hardcoded Group, which adds every brokered user to a specific group, and Advanced Claim to Group, which routes users based on the value of an external IdP claim. Group memberships appear in the `organization` claim of OIDC tokens and as attributes in SAML assertions, so applications can authorize on them without an extra round-trip. Full automation is available through the new endpoints under `/admin/realms/<realm>/organizations/{orgId}/groups`.

## SCIM Realm API (experimental)

This release also introduces the [SCIM Realm API](https://www.keycloak.org/2026/04/scim-as-experimental-feature) (System for Cross-domain Identity Management) as an experimental feature, disabled by default. It exposes POST, GET, PATCH, PUT and DELETE operations for users and groups, the core user, enterprise user and group schemas, and SCIM filtering and pagination on search endpoints. Bulk operations, password management, sorting and custom schemas and attributes are not supported yet. Two security fixes ship in this release, addressing an [IDOR on the SCIM PUT endpoint](https://github.com/keycloak/keycloak/issues/46658) and an [authorization bypass on user group management](https://github.com/keycloak/keycloak/issues/47536).

To expose `/realms/<realm>/scim/*` endpoints, add `scim-api` to the `KC_FEATURES` environment variable of the Java application and rebuild it. `KC_FEATURES` is a build-time setting, so a simple restart is not enough. Once the rebuild completes, enable SCIM on each target realm from the Keycloak admin console (Realm Settings, *SCIM API Enabled* toggle) where the SCIM base URL is also displayed.

## Per-realm IP filtering

On top of upstream features, this version of the Keycloak add-on deployed on Clever Cloud extends its IP filtering capabilities. In addition to the existing in-realm authenticator flow, you can now restrict access to administration, public and SCIM endpoints on a per-realm basis through environment variables of the underlying Java application. Four families of variables control these filters, each accepting a comma-separated list of IP addresses:

- `CC_KEYCLOAK_ADMIN_IPS_<REALM>`: restricts `/admin/<realm>/*` and `/admin/realms/<realm>/*` for a given realm
- `CC_KEYCLOAK_PUBLIC_IPS_<REALM>`: restricts `/realms/<realm>/*` (login pages, user authentication, tokens)
- `CC_KEYCLOAK_SCIM_IPS_<REALM>`: restricts `/realms/<realm>/scim/*` provisioning endpoints
- `CC_KEYCLOAK_ADMIN_IPS`: global fallback for any `/admin/*` endpoint not covered by a per-realm admin rule

The realm name in the variable suffix must match the realm name as it appears in URLs (case-sensitive). Per-realm filters take precedence over the global admin filter. Blocked requests receive an `HTTP 403` response. If no IP filtering variable is set, Keycloak keeps its standard public behavior.

For example, to allow only two office IPs to reach the `master` realm admin console and a dedicated server to call SCIM on the `production` realm:

```bash
CC_KEYCLOAK_ADMIN_IPS_master="203.0.113.10,203.0.113.11"
CC_KEYCLOAK_SCIM_IPS_production="198.51.100.42"
```

## Updating

You can update through the add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.6.1` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.6.1
```

- [Learn more about IP filtering on the Keycloak add-on](/doc/addons/keycloak#ip-filtering)
- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
