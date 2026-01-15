---
title: Keycloak 26.5 is available with CORS enhancements, logout confirmation, workflows
description: Keycloak 26.5.1 brings bug fixes and new features including organization invitation management, and JWT Authorization Grants
date: 2026-01-08
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

[The release 26.5.1](https://github.com/keycloak/keycloak/releases/26.5.1) of Keycloak is available on Clever Cloud. It brings bug fixes and new features from the [26.5.0 release](https://github.com/keycloak/keycloak/releases/26.5.0):

- CORS enhancements
- Logout confirmation page
- Organization invitation management
- Enhanced HTTP performance (preview)
- Hiding OpenID Connect scopes from the discovery endpoint
- Workflows (preview) to automate administrative tasks and processes within a realm
- OpenTelemetry support for metrics and logging, combining all observability information in this popular standard
- JWT Authorization Grants (preview), the recommended alternative to external to internal token exchange ([RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523))

You can update through add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_KEYCLOAK_VERSION` of the underlying Java application to `26.5.1` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.5.1
```

- [Learn more about Keycloak 26.5](https://www.keycloak.org/2026/01/keycloak-2650-released)
- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
