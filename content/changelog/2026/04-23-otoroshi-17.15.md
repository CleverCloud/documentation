---
title: Otoroshi 17.15 brings agents with tools and memory, OAuth2 token exchange, PluginPresets and requires Java 25
description: Agents built-in tools and persistent memory, new embedding and memory storage backends, Kreuzberg OCR support, OAuth2 token exchange plugin, PluginPresets and workflow auth modules
date: 2026-04-23
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

[Otoroshi v17.15.1](https://github.com/MAIF/otoroshi/releases/tag/v17.15.1) is available with several additions for zero trust and plugin composition. It introduces an OAuth2 token exchange plugin implementing [RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693) for secure service-to-service API communication, a new `PluginPreset` kind to package and reuse plugin configurations, a `MandatoryConsumerPreset` plugin and a workflow-based authentication module. The `OAuth2Caller` plugin can now rely on an authentication module for the client credentials flow, and `$2b$` / `$2y$` Bcrypt hashes are now accepted.

### A redesigned admin interface and manual

The admin interface has been redesigned with refreshed themes, a new home page, a reworked API editor with sticky actions and form views capped at 1000 px to improve readability. The UI also now only displays entities a user is actually authorized to see. The full manual has been reworked as well, with ditaa schemas replaced by mermaid ones and can be protected behind an optional access secret.

### API management, data exporters and plugin development

API management gains direct plan subscription on a plan and a new consistency service. The PostgreSQL data exporter now supports retention and plugin developers can rely on a reusable stateful clients internal API. Several fixes address a race condition in data exporters loading, legacy audit event layouts, body consumption handling and the `OAuth2Caller` password grant type.

### LLM extension: agents, memory and Kreuzberg

This release includes LLM extension [0.0.75](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.75), which significantly expands agent capabilities with built-in tools (`system_exec`, `file_read`, `file_write`, `http_call`), a per-session working memory, autonomous persistent memory on Redis and PostgreSQL and a new agent OpenAI proxy plugin. Embedding stores and persistent memories now support many backends (PostgreSQL, Redis, Elasticsearch, OpenSearch, Qdrant, Weaviate, Pinecone, ChromaDB), a semantic cache on Redis with a custom embedding model and MCP audit events. The Anthropic provider exposes version and beta settings, and [Kreuzberg](https://kreuzberg.dev) is now available as a content-to-markdown and OCR backend.

### Java 25 is now required

Otoroshi 17.15 requires Java 25 to load the Kreuzberg content-to-markdown and OCR backend. Starting with this release, all new Otoroshi add-ons are created with `CC_JAVA_VERSION=25`, and any update to Otoroshi 17.15 automatically switches the underlying Java application to Java 25. If you prefer to handle this manually, you can set `CC_JAVA_VERSION` to `25` on the Java application backing your Otoroshi add-on and rebuild it before updating Otoroshi itself.

You can update through add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.15.1_1776891995` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.15.1_1776891995
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
