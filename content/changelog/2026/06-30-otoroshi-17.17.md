---
title: Otoroshi 17.17 brings RFC 7662 token introspection and an LLM extension with A2A and MCP virtual servers
description: Otoroshi 17.17.0 adds RFC 7662 token introspection, hardened API key validation and Elasticsearch 8 compatibility, and ships LLM extension 0.0.82 with A2A, MCP virtual servers, gateway discovery and local PII redaction
date: 2026-06-30
tags:
  - addons
  - otoroshi
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Otoroshi v17.17.0](https://github.com/MAIF/otoroshi/releases/tag/v17.17.0) is available on Clever Cloud. This release adds standards-based token introspection, hardens API key validation and improves Elasticsearch compatibility. It also ships LLM extension [0.0.82](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.82), which builds on [0.0.81](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.81) and [0.0.80](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.80).

### RFC 7662 token introspection and admin bootstrap

Otoroshi now implements the [RFC 7662](https://datatracker.ietf.org/doc/html/rfc7662) introspection flow, so you can validate opaque access tokens against an introspection endpoint. The `OIDCJwtVerifier` also reads the audience from an array, aligning it with providers that emit `aud` as a list.

The initial admin password can now be generated and stored in a temporary file at first startup, which makes automated and reproducible bootstrap of a fresh instance easier.

### Hardened API key validation

Several fixes tighten how API keys are accepted. Disabled API keys are no longer accepted in client-id-only mode, and a bearer signature validation bypass in that same mode has been corrected. Legacy quota declarations are now reported on the API key quotas endpoint, so quota reporting stays consistent across key formats.

### Elasticsearch 8 and Expression Language

Writes to Elasticsearch 8 no longer include the deprecated `_type` field, and the cluster version can be auto-filled from the interface. The Expression Language handles default values more reliably and fixes the ordering of `ctx.geolocation.*` and `ctx.useragent.*` expressions. The `NgErrorRewriter` plugin also receives several improvements, and ingress fetching now targets the correct API group.

### LLM extension: A2A, MCP virtual servers and gateway discovery

The bundled LLM extension reaches [0.0.82](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.82) and includes the features introduced in 0.0.81 and 0.0.80. The provider and capability catalogs are now exposed through the authenticated admin API, and a new `RampartBodyRedactionBackend` terminal plugin reads the request body, redacts PII with the local Rampart model and returns the redacted body directly. The Mistral provider adopts the OpenAI content representation for chat messages, improving support for structured and multi-part content.

The extension also gains a self-describing gateway: two endpoints, `GET /providers` and `GET /model-capabilities`, let clients discover available providers and model types at runtime, with filtering across text, audio, image, OCR, embedding, moderation and video capabilities. Both are also available as standalone plugins. Embeddings now work with OpenAI-compatible endpoints and OVH AI Endpoints, and the OpenAI-compatible plugin extends to image, audio and moderation on top of chat and embeddings.

The 0.0.80 release added bidirectional Agent-to-Agent (A2A) support, so Otoroshi agents can be published as standards-compliant services and consume remote A2A agents as tools. MCP virtual servers bundle tool functions, filtering, OAuth security, rate limiting and Zero-Trust controls into a single persisted entity that can be published to the MCP registry. Zero-Trust controls add anti-rug-pull pinning to detect tool definition changes, along with tool-poisoning and prompt-injection scanning. A local Rampart PII guardrail redacts personally identifiable information offline through an ONNX model, and OAuth hardening brings audience validation ([RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707)) and opaque token introspection ([RFC 7662](https://datatracker.ietf.org/doc/html/rfc7662)). An Exa search engine provider and real-time MCP and LLM gateway metrics round out the release.

You can update through your add-on dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.17.0_1782983608` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.17.0_1782983608
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
