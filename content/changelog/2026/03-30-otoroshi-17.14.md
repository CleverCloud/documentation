---
title: Otoroshi 17.14 enhances remote catalogs, adds PostgreSQL data export and MCP OAuth2 enforcement
description: Remote catalogs with Kubernetes manifests and YAML support, PostgreSQL data exporter, mandatory flags on plugins, expression language improvements and LLM extension with 40+ new providers and MCP OAuth2
date: 2026-03-30
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

[Otoroshi v17.14](https://github.com/MAIF/otoroshi/releases/tag/v17.14.0) is available with significant enhancements to [remote catalogs](https://maif.github.io/otoroshi/manual/docs/topics/remote-catalogs). They now support organisation scanning, additional GitHub-like providers, pattern-based and YAML-formatted descriptor files, as well as Kubernetes-like manifests. This release also introduces PostgreSQL as a data exporter target and adds Redis Sentinel password support with the Lettuce driver.

New mandatory flags are available on client certificate plugins and OIDC JWT verification for APIs, offering finer control over authentication requirements. The expression language has been improved with path-based read support for deep structures such as user profiles, with complex structure stringification. Several fixes address tunnel handler plugin visibility, Kafka data exporter host validation, and the "Override Location header" plugin behaviour.

This release includes LLM extension [0.0.74](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.74), adding over 40 new providers through an enhanced generic OpenAI client (including Minimax, Morph, Cloud Temple and many others). MCP exposition has been significantly strengthened with all missing methods now implemented (resources, templates, prompts), fine-grained per-tool scoped authorisations, and OAuth2 enforcement with a new MCP Protected Resource Metadata document plugin. This version also introduces an OpenAI Responses proxy plugin and [a new OpenAI API aggregator plugin](https://cloud-apim.github.io/otoroshi-llm-extension/docs/llm-gateway/openai-compat-api/) that unifies chat completions, responses, Anthropic /messages and context serving into a single endpoint.

You can update through add-on's dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v17.14.0_1774627527` and rebuild it, or use [Clever Tools](/doc/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId v17.14.0_1774627527
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/addons/otoroshi/)
