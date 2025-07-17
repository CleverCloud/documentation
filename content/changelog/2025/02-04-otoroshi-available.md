---
title: "Otoroshi v16.23.2 is available, with Biscuit Studio and LLM updates"
date: 2025-02-04
tags:
  - addons
  - Otoroshi
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: Discover and use Biscuit, the easy way
excludeSearch: true
---

Otoroshi `v16.23.2` is now available on Clever Cloud for new add-ons. You can also update `CC_OTOROSHI_VERSION` to `v16.23.2`, `CC_OTOROSHI_APIM_VERSION` to `1738687356` in the Java application and rebuild it.

This version includes the brand new Biscuit Studio, allowing you to use such tokens (we use in production for Materia KV and Pulsar) in your routes. It comes with key pair generator, Biscuit verifier, attenuation and roles management tools. The [client credentials plugin](https://cloud-apim.github.io/otoroshi-biscuit-studio/docs/plugins/clientcredentials) supports Biscuit to add a OAuth2 `client_credentials` flow to your routes.

Web Application Firewall (WAF) plugin and interface are also enhanced in this release. Otoroshi can now use secrets management services declared with environment variables. This allows an easy integration of Clever KMS, our secrets management service available in private alpha for dedicated customers.

LLM plugin includes a better models management, compatible with OVHcloud AI endpoints. Functions calling is enabled in Anthropic and Cohere, DeepSeek is available as a provider, [Citations from Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/citations) are handled, such as reasoning models and tokens.

- [Learn more about Biscuit](https://doc.biscuitsec.org/home)
- [Learn more about Otoroshi Biscuit Studio](https://cloud-apim.github.io/otoroshi-biscuit-studio/docs/overview)
- [Learn more about Otoroshi with LLM on Clever Cloud](/developers/doc/addons/otoroshi/)
- [Otoroshi LLM on Clever Cloud video streams](https://www.youtube.com/@Clevercloud-platform/search?query=Otoroshi)
