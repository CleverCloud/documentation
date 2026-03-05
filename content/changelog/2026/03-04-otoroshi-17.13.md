---
title: Otoroshi 17.13 brings Kubernetes Gateway API support, remote catalogs and audio STT extensions
description: Experimental Kubernetes Gateway API, remote catalogs, enhanced security headers, router fixes and LLM extension with audio STT support
date: 2026-03-04
tags:
  - addons
  - otoroshi
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Otoroshi v17.13](https://github.com/MAIF/otoroshi/releases/tag/v17.13.0) is available with experimental support for the [Kubernetes Gateway API](https://maif.github.io/otoroshi/manual/topics/kubernetes-gateway-api.html), enabling standardised Kubernetes-native traffic management. This release also introduces [remote catalogs](https://maif.github.io/otoroshi/manual/topics/remote-catalogs.html), allowing to fetch and manage plugin or configuration catalogs from external sources.

A webhook validator plugin is also included, providing HMAC signature verification for incoming webhook payloads. It supports multiple algorithms (SHA256, SHA512, SHA384, SHA1) and is provider-agnostic with configurable signature headers and signing templates, compatible with services such as GitHub, Stripe, Slack or YouSign.

Security headers plugin now supports `Referrer-Policy` and `Permissions-Policy` headers, and new configuration options allow exposing public keys with algorithms in JWKS endpoints. Several router fixes improve path matching with wildcard domains, query/header/cookie matching prioritisation, and trailing slash handling. The strict mode of the JWT user extractor plugin has also been fixed.

This release includes LLM extension [0.0.73](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.73), bringing audio speech-to-text support with [Mistral Voxtral model](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.70) and Azure OpenAI Audio API. It also includes various provider payload cleanups for Anthropic and xAI formats.

You can update through add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.13.0_1772616661` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.13.0_1772616661
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
