---
title: "Otoroshi with LLM is available as an add-on on Clever Cloud"
date: 2024-12-04
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
description: Make the AI enterprise-grade
aliases:
- /changelog/2024-12-04-otoroshi-available
excludeSearch: true
---

After some weeks of testing, the Clever Cloud's Otoroshi with LLM add-on, is available in public beta. Thus, you can deploy the service, from [Console](https://console.clever-cloud.com/users/me/addons/new), [API](/developers/api) or [Clever Tools](https://github.com/CleverCloud/clever-tools), and use it in minutes.

We developed this product with its creator and core developer: [Mathieu Ancelin](https://github.com/mathieuancelin) from [Cloud APIM](https://www.cloud-apim.com/). Otoroshi is an open source reverse proxy that allows you to create your own routes, manage authentication, authorization, and rate limiting. It helps you to expose services with enterprise needs in mind, as you can manage organisations, teams, service groups, with event management, data export, multiple secret stores support, etc. And it can be managed from a web interface or [as an API](https://maif.github.io/otoroshi/manual/api.html).

On Clever Cloud, it comes batteries included, pre-configured with features such as [Coraza Web Appplication Firewall](https://maif.github.io/otoroshi/manual/how-to-s/instantiate-waf-coraza.html) or [LLM extension](https://cloud-apim.github.io/otoroshi-llm-extension/docs/overview). The latter allows you to manage AI services from many providers (Anthropic, Groq, Hugging Face, Mistral, OpenAI, OVHcloud), Ollama instances or any OpenAI API compatible endpoints.

All this with a unique interface, adding token management, rate limit, context, validation, moderation, etc. Create your own agents and flows with an only URL, distributing tokens to your team or customers, for cURL requests or integrations to many services and tools… or your own applications hosted on Clever Cloud.

It's based on a Java application and a Redis® database. Once deployed you'll get a management URL with credentials. Want to learn more? Feel free to let us know what you think and ask your questions in [our GitHub Community](https://github.com/CleverCloud/Community/discussions/categories/otoroshi).

- [Learn more about Otoroshi](https://maif.github.io/otoroshi/manual/how-to-s/index.html)
- [Learn more about Otoroshi with LLM on Clever Cloud](/developers/doc/addons/otoroshi/)
- [Otoroshi LLM extension video tutorials](https://www.youtube.com/watch?v=M8PbydxPw4A&list=PLNHaf5rXAx3FWk7dn2fKGwQXxeLCPhZCh)
