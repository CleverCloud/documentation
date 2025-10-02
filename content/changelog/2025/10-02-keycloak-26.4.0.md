---
title: Keycloak 26.4 is available with auth for MCP, Passkeys, FAPI 2, DPoP
description: Keycloak 26.4 brings great performances, features and a new plugin to filter email domains on user registration
date: 2025-10-02
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

[The release 26.4.0](https://github.com/keycloak/keycloak/releases/26.4.0) of Keycloak is available on Clever Cloud. It brings multiple bug fixes and great new features:

- Authorization server for MCP
- Passkeys are now seamlessly integrated
- Automatic certificate management for SAML clients
- Federated client authentication is available in preview
- FAPI 2.0 Security Profile and Message Signing Final support
- OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP) is now fully supported

The Clever Cloud Keycloak add-on now includes a plugin that allows filtering email domains when users register.

This release is now used as default for new created add-ons. To update an existing add-on, set `CC_KEYCLOAK_VERSION` of its Java application to `26.3.3` and rebuild it. You can also use [the new Clever Tools commands](/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.4.0
```

- [Learn more about Keycloak 26.4](https://www.keycloak.org/2025/09/keycloak-2640-released)
- [Learn more about Keycloak 26.4 performances](https://www.keycloak.org/2025/10/keycloak-benchmark)
- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
