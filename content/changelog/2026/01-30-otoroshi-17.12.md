---
title: Otoroshi 17.12 is available with JWT Verification, new WAF engine and plugin improvements
description: JWT verification via OIDC with session extraction, JVM-native WAF engine with OWASP CRS, plugin development enhancements and LLM extensions updates
date: 2026-01-30
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

[Otoroshi v17.12](https://github.com/MAIF/otoroshi/releases/tag/v17.12.0) is available with multiple improvements. It brings JWT verification support based on the settings of an OIDC authentication module with optional user session extraction through OIDCJwtVerifier. The release also allows Fail2Ban to be triggered by other plugins that can't use the `requestError` phase.

This version also integrates a new WAF engine providing JVM-native implementation of ModSecurity SecLang with the OWASP Core Rule Set included. This eliminates binary dependencies and simplifies deployment in containerized environments, with flexible modes for comprehensive WAF inspection or lightweight request validation.

For plugin developers, this version introduces various internal improvements: Monaco editor support in classic forms for enhanced code editing experience, provider helpers to create customizable errors in plugins, and the ability to always display plugins even if missing from the JS plugins list.

This release includes LLM extensions [0.0.68](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.68) and [0.0.69](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.69), bringing OpenResponses-compatible endpoints for standardized LLM response handling through the [OpenResponses framework](https://www.openresponses.org/). These versions embed rate limit and budget consumption data in `GatewayEvents` and `LLMAuditEvents` for enhanced tracking, and support exposing any model with an Anthropic API compatible format.

You can update through add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.12.0_1769783775` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.12.0_1769783775
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
