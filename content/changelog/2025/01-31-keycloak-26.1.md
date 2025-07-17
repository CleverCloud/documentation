---
title: "Keycloak 26.1 is available"
date: 2025-01-31
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
description: Lots of new features and improvements
excludeSearch: true
---

The release `26.1.0` of Keycloak is available on Clever Cloud. [It fixes](https://github.com/keycloak/keycloak/releases/26.1.0) some bugs, but also brings lots of new features and improvements, such as OpenTelemetry tracing, virtual thread pool support (embedded Infinispan and JGroups) when running on OpenJDK 21, a different way to discover other nodes of the same cluster (`jdbc-ping`) and a better OpenID for Verifiable Credential Issuance (OID4VCI) experimental support.

To update, just set `CC_KEYCLOAK_VERSION` of the add-on's Java application to `26.1.0` and rebuild it.

- [Learn more about Keycloak on Clever Cloud](/developers/doc/addons/keycloak)
