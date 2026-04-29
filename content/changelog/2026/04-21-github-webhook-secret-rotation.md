---
title: "API update: rotate GitHub webhook secrets for your applications"
date: 2026-04-21
description: A new CC API endpoint lets you rotate the GitHub webhook secret of an application and its linked siblings, without recreating the hook.
tags:
  - api
  - api-update
  - github
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The Clever Cloud API now exposes a dedicated endpoint to rotate the GitHub webhook secret of an application linked to a GitHub repository.

The rotation applies to the target application and its siblings sharing the same webhook, so a single call keeps every linked deployment in sync with the new secret. Until now, rotating a webhook secret meant creating a new application, which was cumbersome and error-prone. The new endpoint replaces that workflow with a single authenticated call.

## How to use it

You can call this endpoint through any [authenticated request to the Clever Cloud API](/doc/cli/#tokens), or through the [`clever curl` command](/doc/cli/#curl) of Clever Tools, which signs the request using the active user profile:

```bash
clever curl -X POST https://api.clever-cloud.com/v2/organisations/{orgId}/applications/{appId}/github-webhook/secret
```

The response confirms the rotation. Any existing GitHub push event already in flight keeps working with the previous secret until GitHub picks up the new configuration; subsequent deliveries use the rotated secret automatically.

Refer to the [v2 API reference](/api/v2) for the full request and response schema.
