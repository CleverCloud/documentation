---
title: Otoroshi 18 is available, with new foundations, a Threat Protection Suite and AI Studio
description: Otoroshi 18.0.1 moves to Scala 3, Play 3 and Pekko, removes Service Descriptors and turns every API consumer into an API key. It ships LLM extension 0.0.90 with AI Studio, the Threat Protection Suite 1.0.0 and the new Clever Cloud Reaper
date: 2026-10-27
tags:
  - addons
  - otoroshi
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Otoroshi v18.0.1](https://github.com/MAIF/otoroshi/releases/tag/v18.0.1) is available on Clever Cloud. It brings the changes of [Otoroshi v18.0.0](https://github.com/MAIF/otoroshi/releases/tag/v18.0.0), the largest release of the project in years, and fixes the route designer when a plugin has a form field named `label`. Every bundled plugin has been rebuilt for this new major version.

## New foundations for Otoroshi

Otoroshi 18 moves from Scala 2.12 to Scala 3.8, from Play 2.8 to Play 3.0 and from Akka to Apache Pekko 1.6. The admin interface now builds with Vite and no longer uses jQuery. These new foundations improve the stability, performance and security of the gateway.

Service Descriptors are gone. At first startup, a job backs them up to `./service-descriptors-backup.json` and converts each one to a route with the same id. Every API consumer is now an API key, whatever the plan (`keyless`, `jwt`, `mtls`, `oauth2-remote`), so quotas, rate limits and analytics apply to every caller. A plan or a single API key can bring its own plugin chain, and conditional plugins only run when JSONPath predicates match on the API key, the user, the route, the request or the response.

This release also adds trusted proxies: Otoroshi reads the client address from the trusted end of the `X-Forwarded-For` chain. On Clever Cloud, it automatically trusts the platform reverse proxies listed in `CC_REVERSE_PROXY_IPS`, so you get the real client address without any configuration. OpenSearch support, ACME chain selection and a rewritten OpenAPI document for the admin API are also part of this release. Read the [Otoroshi 18 blog post](https://maif.github.io/otoroshi/manual/blog/otoroshi-18-new-foundations) and the [production checklist](https://maif.github.io/otoroshi/manual/docs/topics/production-checklist) for the details.

> [!NOTE] Check these changes before you upgrade
> Custom Scala plugins loaded through `CC_OTOROSHI_PLUGINS_URLS` must be recompiled against Scala 3 and `fr.maif:otoroshi_3`; WASM plugins are unaffected. SAML responses are now strictly validated, `NgServiceQuotas`, `NgCustomQuotas` and `NgCustomThrottling` answer `429` instead of `403`, and `_start` and `_stop` on APIs require a `POST`.

## LLM extension 0.0.90 and AI Studio

The bundled LLM extension moves to [0.0.90](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.90). It introduces AI Studio, an experimental console where a team gets its own workspace with an OpenAI-compatible endpoint, providers and keys, models, guardrails, routing, logs and cost reporting. It comes with chat and playgrounds for every model type, MCP servers per workspace and an admin API to manage workspaces without the interface.

Decision models are a new kind of model answering typed questions with probabilities, through the System One API or the OpenAI `POST /v1/decisions` API. The router gains `smart-router` and `intent-router` strategies, budgets can be partitioned per consumer with an Otoroshi expression, and cost tracking now covers every model type. The extension also supports the stateless MCP `2026-07-28` revision, sends the reasoning of previous turns back to each provider in its own format, and installs ten built-in dashboards when a User Analytics exporter is active.

Enhancements from releases [0.0.84](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.84) to [0.0.86](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.86) are included too. They added OpenAI-compatible tool calling for Anthropic providers, a native `/responses` endpoint on providers with the full gateway pipeline applied to it, and PDF and text file content parts.

## Threat Protection Suite 1.0.0

The WAF extension becomes the [Threat Protection Suite](https://github.com/cloud-apim/otoroshi-waf-extension/releases/tag/1.0.0). The SecLang engine with the OWASP Core Rule Set is still at its core, surrounded by IP reputation feeds, a CrowdSec bouncer, bot control with a built-in proof-of-work challenge, login and traffic guards, response protection and OpenAPI contract validation. All detectors feed one shared threat score, and Threat Studio manages the whole suite from a single console.

This version inspects traffic that 0.0.10 let through, such as compressed or `+json` bodies, and a WAF that can't run now refuses requests with a `503` instead of letting them pass. Set your blocking configurations to monitoring mode after the upgrade, then turn blocking back on once tuned. Set `CLOUD_APIM_EXTENSIONS_WAF_FAIL_OPEN` to `true` to keep the previous fail-open behavior.

## How to update

You can update through your add-on dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v18.0.1_1793044909` and rebuild it, or use [Clever Tools](/doc/tools/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId --target v18.0.1_1793044909
```

The 17.x line stays available if you need more time to prepare the upgrade:

```bash
clever otoroshi version update yourOtoroshiNameOrId --target v17.17.0_1784304500
```

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/deploy/services/otoroshi/)
