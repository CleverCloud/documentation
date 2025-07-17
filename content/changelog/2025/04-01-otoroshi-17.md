---
title: "Otoroshi v17.0.0 is available: OpenAI web search and ecological impact/cost tracking in LLM extension"
date: 2025-04-01
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
description: The feature easily in your hands
excludeSearch: true
---

[Otoroshi v17.0.0](https://github.com/MAIF/otoroshi/releases/tag/v17.0.0) is available. It fixes some bugs, adds target failover support and allows OpenAPI to be consumed as YAML. This release also brings the new API management feature, providing a way to create an API, flows, routes, backends, consumers and subscriptions. An API is created as draft, can be tested and deployed with lifecycle and version management. This feature is alpha and some functionalities are still early or yet to come. Share your feedback in [Otoroshi's GitHub discussions](https://github.com/MAIF/otoroshi/discussions).

Biscuit Studio [0.0.12](https://github.com/cloud-apim/otoroshi-biscuit-studio/releases/tag/0.0.12) is included with enhancements from [0.11](https://github.com/cloud-apim/otoroshi-biscuit-studio/releases/tag/0.0.11) release: Distributed revocation, a plugin to fetch a Biscuit from a remote location, new Biscuit extractor types and new admin API routes.

LLM Extension [0.0.43](https://github.com/cloud-apim/otoroshi-llm-extension/releases/tag/0.0.43) brings support for OpenAI web search and new ecological impact/cost tracking data linked to each request sent to an AI service provider. [The documentation](https://cloud-apim.github.io/otoroshi-llm-extension/docs/overview/) has been updated to reflect these changes.

To update just set `CC_OTOROSHI_VERSION` of the add-on's Java application to `v17.0.0_1743436155` and rebuild it. You can also delete `CC_OTOROSHI_APIM_VERSION`, `CC_OTOROSHI_SECRET` variables from the Java application, they are not used anymore.

- [Learn more about Otoroshi with LLM on Clever Cloud](/developers/doc/addons/otoroshi/)
