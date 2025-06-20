---
title: "Keycloak 26.2.5 is available, with two new plugins"
date: 2025-06-20
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
description: bug fix release
excludeSearch: true
---

The release `26.2.5` of Keycloak is available on Clever Cloud which [fixes](https://github.com/keycloak/keycloak/releases/26.2.5) some bugs. Starting with this release, we provide Keycloak with [2fa-email-authenticator](https://github.com/please-openit/keycloak-2fa-email-authenticator) and [Limit user agents](https://github.com/please-openit/keycloak-authenticator-limit-user-agents) plugins.

To update, just set `CC_KEYCLOAK_VERSION` of the add-on's Java application to `26.2.5` and rebuild it. You can also use [the new Clever Tools commands](/developers/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.2.5
```

- [Learn more about Keycloak on Clever Cloud](/developers/doc/addons/keycloak)
