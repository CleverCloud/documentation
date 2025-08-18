---
title: Keycloak 26.3.2 is available, including optimizations and new features
date: 2025-07-31
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
description: with lots of new features
excludeSearch: true
---

[The release 26.3.2](https://github.com/keycloak/keycloak/releases/26.3.2) of Keycloak is available on Clever Cloud. The `26.3` branch [brings](https://github.com/keycloak/keycloak/releases/26.3.0) lots of new features, enhancements and bug fixes. We fine tuned it, adding a conditional IP range-based authentication and dynamic cache sizing that automatically scales based on instance size and user count in database.

To update, just set `CC_KEYCLOAK_VERSION` of the add-on's Java application to `26.3.2` and rebuild it. You can also use [the new Clever Tools commands](/doc/cli/operators/), introduced in `3.13.0` release:

```bash
clever features enable operators

clever keycloak version check yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId
clever keycloak version update yourKeycloakNameOrId 26.3.2
```

- [Learn more about Keycloak on Clever Cloud](/doc/addons/keycloak)
