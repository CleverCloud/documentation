---
title: Otoroshi 17.16 brings user analytics, distributed rate limiting and new HTTP standards plugins
description: User analytics dashboards and alerts, distributed rate limiting, RFC 9421/9440/9728 plugins, reworked Kubernetes deployments and an LLM AI Assistant
date: 2026-05-29
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

[Otoroshi v17.16.0](https://github.com/MAIF/otoroshi/releases/tag/v17.16.0) is available. This release focuses on observability, API lifecycle management, Kubernetes deployments and a set of brand-new HTTP standards plugins. It also ships an updated LLM extension featuring an AI Assistant for the admin interface and an updated WAF extension. The Otoroshi documentation has been substantially expanded as well.

### User analytics, dashboards and a global event stream

Otoroshi gains a complete user analytics stack. A PostgreSQL-based analytics exporter stores and queries events at scale, and you can now build your own dashboards with a graphical widget editor, drill-down support and a set of default dashboards shipped out of the box. User-defined alerts are built from analytics queries through a graphical condition editor, with a dedicated alerting interface and a scheduled evaluation job. Dashboards, alerts and analytics queries are all integrated with RBAC.

A new global node event stream page in the back office streams audit, alert and analytics events from current node, with pagination, capped buffers and per-type filtering. Data exporters also accept pluggable custom filters and a project phase, and no longer generate one event per filtered event.

- [Learn more about dashboards, analytics queries and alerts](https://maif.github.io/otoroshi/manual/docs/topics/user-analytics/)

### API management and new HTTP standards plugins

API management hardens the split between draft and production: a clear version banner, read-only production views and plan lifecycle enforcement that locks the `Api` entity fields once a plan is published. A getting-started stepper guides newcomers, and the draft subscription listing, top bar search and API key plan editor have all been cleaned up.

This release introduces three plugins implementing recent HTTP standards. The HTTP Message Signatures plugins ([RFC 9421](https://datatracker.ietf.org/doc/html/rfc9421)) sign and verify requests and responses, the `NgRfc9440ClientCertHeader` plugin forwards client certificates through the standard `Client-Cert` and `Client-Cert-Chain` headers ([RFC 9440](https://datatracker.ietf.org/doc/html/rfc9440)), and an OAuth 2.0 Protected Resource Metadata plugin implements [RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728). New JSON validator plugins based on JSON Schemas are also available, and the `OAuth2Caller` plugin can now target a specific resource for the generated token or rely on an OAuth2 authentication module.

- [HTTP Message Signatures (RFC 9421) tutorial](https://maif.github.io/otoroshi/manual/docs/tutorials/http-message-signatures-rfc9421/)
- [Learn more about RFC 9440 Client-Cert headers](https://maif.github.io/otoroshi/manual/docs/topics/tls/#rfc-9440--client-cert--client-cert-chain-headers)

### Distributed rate limiting, mailers and exporters

A new distributed rate-limiting strategy backed by atomic Lua scripts on Redis provides predictable, cluster-aware quotas across nodes. It is a drop-in alternative to the previous distributed strategy and is configurable per route. Scaleway TEM and MailPace join the supported mailers.

### Reworked Kubernetes deployments

The Helm chart has been almost entirely rewritten with first-class cluster mode (leader and worker deployments), a Redis secured by default based on the CloudPirates Redis chart, and proper HPA, PDB, NetworkPolicies, RBAC, webhooks and certificate templates. The Kustomize manifests reach feature parity with Helm through a component-based split, and the generated CRDs now expose previously missing entities, including APIs, dashboards, alerts and the new analytics resources.

### LLM extension: an AI Assistant and Meta MCP

This release includes LLM extension [0.0.76](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.76), which adds an AI Assistant to the Otoroshi admin interface. The assistant can search the documentation, query the admin API and run administrative tasks through its Search, Doc and Execute tools, with a conversational chat window, streaming responses, light and dark themes and API key-based access. A hybrid semantic and lexical search engine backs documentation queries.

The extension also introduces a Meta MCP connector that aggregates and proxies multiple MCP servers with dynamic capabilities, an Otoroshi MCP server plugin exposing the assistant tools, and image generation support in the `Response` and `OpenResponse` plugins. The Monaco editor is now used across all administration pages of the extension.

### Updated bundled plugins

Every plugin delivered with Otoroshi on Clever Cloud has been rebuilt against 17.16.0. The WAF extension ([0.0.9](https://github.com/cloud-apim/otoroshi-waf-extension/releases/tag/0.0.9)) upgrades the OWASP Core Rule Set to v4.26.0.

You can update through your add-on dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.16.0_1779982854` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.16.0_1779982854
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
