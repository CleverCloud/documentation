---
title: Otoroshi 18.1 brings fine-grained user rights and one API key for several APIs
description: Otoroshi 18.1.0 adds fine-grained rights for admin users, shared credentials across API subscriptions, GitOps filters, and trial requests from the admin API. It ships LLM extension 0.0.91 and the Threat Protection Suite 1.1.0
date: 2026-11-26
tags:
  - addons
  - otoroshi
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Otoroshi v18.1.0](https://github.com/MAIF/otoroshi/releases/tag/v18.1.0) is available on Clever Cloud. This release refines the access rights of the admin interface, extends API management, and hardens how plans and subscriptions control their consumers. It ships LLM extension [0.0.91](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.91) and the Threat Protection Suite [1.1.0](https://github.com/cloud-apim/otoroshi-waf-extension/releases/tag/1.1.0).

## Fine-grained rights for admin users

A right can now cover only some kinds of entities: a user can read everything in a team, but only write its backends and certificates. User rights policies set the rights of an admin user by email, either replacing the rights of the authentication module or capping them. Super admins manage them from the admin interface, the admin API, or Kubernetes resources. A change applies on the next call, without a new login.

Any admin user can also get a personal admin API key that always carries their current rights. A tenant admin can no longer modify or delete an admin or an API key with more rights than its own, which closes a privilege escalation.

## One API key for several APIs

A consumer can now call several APIs with a single client ID and secret, each through its own subscription, plan, quotas, and restrictions. Rotating, disabling, or expiring the shared credential applies to every API at once, while suspending a subscription only cuts its own API.

The `jwt`, `mtls`, and `oauth2-remote` plans can require a subscription, and Otoroshi now enforces the restrictions of these plans and of `keyless` ones. Plans gain conditions selecting the calls they apply to, a behavior when the quota counter is unreachable, and a circuit breaker per consumer. API key plans can give their keys a validity counted from the subscription. mTLS plans can name the authorities that must sign client certificates, and `oauth2-remote` plans can check the issuer and audiences of tokens.

## GitOps, APIs as code, and trial requests

Remote catalogs and the Kubernetes job can include or exclude kinds of entities, globally and per organisation, team, or namespace. A CI job can manage APIs as code and publish them. Deployments record their plans, and the source version set in `metadata.deployment_ref`.

`POST /apis/proxy.otoroshi.io/v1/routes/:id/_tryit` sends a trial request through a route, and returns the response with the full execution report. You can now script the route designer tester from a CI. Credential headers and secret fields are now masked in the events sent to data exporters; set `OTOROSHI_EVENTS_MASK_SECRETS` to `false` to turn it off.

This release also fixes a security issue: a caller with narrowed rights could read the secret of a super admin API key. A plugin failing in a chain no longer hangs the request, a stripped path no longer gets a double slash, and the `Content-Type` of a backend response is no longer lost. A `PUT` on a missing entity now answers `404` instead of `401`, and a `POST` with an ID already in use answers `409`.

## LLM extension 0.0.91

A provider can now spread its calls over several targets with weighted round robin, random, or least loaded balancing, and skips the saturated or failing ones. A time-to-first-token timeout drops slow streamed calls, so the fallback moves to the next provider. The Otoroshi router exposes several virtual models under names you choose, each with its own routing mode. Streaming now works through routers and load balancers.

The Anthropic `/v1/messages/count_tokens` endpoint now answers, and the OpenAI decisions API reaches general availability. Budgets and analytics now price cached prompt tokens, and no longer count reasoning tokens twice. Provider errors no longer all reach the caller as a `400`: a `429` keeps its `Retry-After` header, a `5xx` or a refused gateway credential becomes a `502`, and other `4xx` errors keep their status.

## Threat Protection Suite 1.1.0

The Threat Protection Suite moves to the OWASP Core Rule Set 4.31.0, from 4.30.0, and builds on Otoroshi 18.1.0.

## How to update

You can update through your add-on dashboard in the [Clever Cloud Console](https://console.clever-cloud.com). You can also set `CC_OTOROSHI_VERSION` of the underlying Java application to `v18.1.0_1795556052` and rebuild it, or use [Clever Tools](/doc/tools/cli/operators/):

```bash
clever features enable operators

clever otoroshi version check yourOtoroshiNameOrId
clever otoroshi version update yourOtoroshiNameOrId --target v18.1.0_1795556052
```

The `v18.0.1_1793044909` and `v17.17.0_1784304500` versions remain available if you need more time to prepare the upgrade.

- [Learn more about Otoroshi with LLM on Clever Cloud](/doc/deploy/services/otoroshi/)
