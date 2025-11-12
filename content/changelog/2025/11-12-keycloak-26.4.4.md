---
title: Keycloak 26.4.4 is available, with two new plugins
description: Group regexp mapper and HTTP Get request mapper plugins are now available in Keycloak on Clever Cloud
date: 2025-11-12
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

[The release 26.4.4](https://github.com/keycloak/keycloak/releases/26.4.4) of Keycloak is available on Clever Cloud. It brings multiple enhancements and bug fixes. Starting with this release, Keycloak is deployed with two new plugins:
- [Groups regexp mapper](https://github.com/please-openit/keycloak-groups-regexp-mapper): map groups that only fit to a regexp (by name), it avoids mapping all user groups into a token
- [HTTP Get request mapper](https://github.com/please-openit/keycloak-http-get-request-mapper): add a result from an external service (HTTP GET request) to user's tokens

This release is now used as default for new created add-ons. To update an existing add-on, set `CC_KEYCLOAK_VERSION` of its Java application to `26.4.4` and rebuild it. You can also use [the new Clever Tools commands](/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.4.4
```

- [Learn more about Keycloak 26.4.4](https://www.keycloak.org/2025/11/keycloak-2644-released)
- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
