---
title: "Keycloak: CA certificates, better IP filtering, and the end of Keycloak 24"
description: Keycloak 26.7.5 and 26.8 add-ons now trust the CA certificates of their FS Bucket and get better IP filtering, while Keycloak 24 can no longer be deployed and Keycloak 25 is deprecated
date: 2026-11-20
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

Keycloak add-ons running 26.7.5, 26.8.0, 26.8.1, or 26.8.2 get new features and enhancements. Keycloak now trusts the CA certificates you put in the FS Bucket, and IP filtering supports clients behind a proxy. Rebuild your add-on to apply these changes. Keycloak 24 releases can no longer be deployed, and Keycloak 25 releases are deprecated.

## Keycloak 24 removed, Keycloak 25 deprecated

Keycloak 24 releases are no longer available on Clever Cloud: the next deployment of an add-on running one of them fails. Keycloak 25 releases are now deprecated, and we'll remove them in the coming weeks. The Keycloak project no longer fixes these releases, which have known vulnerabilities. Review the [upgrading guide](https://www.keycloak.org/docs/latest/upgrading/), then update these add-ons to Keycloak 26.8.2.

## CA certificates from the FS Bucket

Keycloak now trusts the CA certificates of the `truststores` folder of the add-on's FS Bucket. Use it when Keycloak calls a server signed by an internal certificate authority, such as an LDAPS directory, an identity provider, or a webhook. The rebuild creates this folder. Upload your certificates there, then restart the add-on with `clever keycloak restart yourKeycloakNameOrId`: Keycloak loads them at each start.

Keycloak reads PEM files holding one or more certificates, single DER certificates, and PKCS12 files without password. It also reads the folders inside `truststores`, and ignores private keys and the files without a `.pem`, `.crt`, `.cer`, `.ca`, `.p12`, `.pfx`, or `.pkcs12` extension. The logs report each file as installed or rejected: a rejected file doesn't prevent Keycloak from starting. `KC_TRUSTSTORE_PATHS` still applies.

## Clients behind a proxy

IP filtering takes the client IP from the address the Clever Cloud load balancer adds to the `X-Forwarded-For` header. Behind a CDN, a web application firewall (WAF), or a corporate proxy, this address is the proxy's.

List these proxies in `CC_KEYCLOAK_TRUSTED_PROXIES`, as comma-separated IP addresses and Classless Inter-Domain Routing (CIDR) ranges. Keycloak events, brute force detection, and IP allowlists then see the client IP, through up to three proxies in a row:

```bash
CC_KEYCLOAK_TRUSTED_PROXIES="198.51.100.0/24, 203.0.113.25"
```

## Better IP filtering

We improved IP filtering in Keycloak 26.7.5, which now works as in the 26.8 branch. If you use IP filtering on an older release, update it to 26.8.2.

## Fixes

- An instance stops when its reverse proxy fails to start, instead of running a Keycloak nobody can reach
- Without [Secured Multi Instances](/doc/deploy/services/keycloak/#secured-multi-instances), Keycloak uses local caches, so a redeployment no longer marks `/health/ready` as `DOWN`
- The deployment refuses an admin allowlist of a realm named `realms` or `serverinfo`, as it would apply to global admin endpoints

## How to apply these changes

Rebuild your add-on from the Console, or with [Clever Tools](/doc/tools/cli/operators/):

```bash
clever features enable operators
clever keycloak rebuild yourKeycloakNameOrId
```

To update an add-on running Keycloak 25, or a release older than 26.7.5, check its current version, then update it:

```bash
clever keycloak version check yourKeycloakNameOrId --format json
clever keycloak version update yourKeycloakNameOrId --target 26.8.2
```

- [Trust custom CA certificates in Keycloak](/doc/deploy/services/keycloak/#trust-custom-ca-certificates)
- [Learn more about IP filtering in Keycloak](/doc/deploy/services/keycloak/#ip-filtering)
