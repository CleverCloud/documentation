---
type: docs
title: Otoroshi with LLM
description: Otoroshi is a lightweight proxy that helps you to connect your services to your clients
tags:
- addons
keywords:
- otoroshi
- reverse
- proxy
- llm
- waf
type: docs
draft: false
---

Otoroshi is a lightweight API management solution built on a modern HTTP reverse proxy. It serves as a flexible and powerful API gateway for your microservices architecture and operates as a technology-agnostic platform, embracing HTTP as its universal language and providing real-time configuration capabilities. The platform follows an API-first approach, ensuring all features are accessible programmatically.

The solution excels at dynamic service management, offering essential API gateway functionalities including request routing, security enforcement, traffic management, and comprehensive monitoring. Its event-driven architecture and flexible deployment model make it particularly effective in cloud-native and PaaS environments.

On Clever Cloud, it comes with pre-configured with features included such as [Coraza Web Appplication Firewall](#coraza-waf-web-application-firewall) or the [LLM extension](#llm-extension).

{{< callout type="info" >}}Share your feedback on Otoroshi operator through [our community page](https://github.com/CleverCloud/Community/discussions/categories/otoroshi){{< /callout >}}

## Create an Otoroshi with LLM add-on

### From the Console

1. [Create a new add-on](https://console.clever-cloud.com/users/me/addons/new) by clicking the **Create…** dropdown in the sidebar and then **an add-on**
2. Select the Otoroshi with LLM add-on
3. You can skip linking the add-on to an application, it won't be needed
4. Enter a name for your Otoroshi with LLM add-on and select the zone where you want it to be deployed

### Using the CLI

Make sure you have `clever-tools` installed locally. Please refer to the [setup guide](/developers/doc/cli/install/) if needed. In your terminal, run `clever addon create otoroshi <name> --org <org>` (`--org` is optional). You'll get URLs to manage your Otoroshi with LLM instance and the temporary credentials:

```
$ clever addon create otoroshi myOtoroshi
Add-on created successfully!
ID: addon_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Real ID: otoroshi_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Name: myOtoroshi

Your Otoroshi with LLM is starting:
 - Access it: https://xxxxxxxxxxxx-api-otoroshi.services.clever-cloud.com
 - Manage it: https://console.clever-cloud.com/addon_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

An initial account has been created, change the password at first login (Security -> Administrators -> Edit user):
 - Admin user name: cc-account-admin
 - Temporary password: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Learn more about Otoroshi with LLM on Clever Cloud: https://www.clever-cloud.com/developers/doc/addons/otoroshi/
```

Refer to the [Clever Tools documentation](/developers/doc/cli/addons/) for more details on add-on management.

## Accessing the Otoroshi with LLM interface

Once you created your add-on, open the management URL or look for `CC_OTOROSHI_URL` value in the Otoroshi with LLM dashboard from the Console. The first time you connect, change the initial password (Security -> Administrators -> Edit user).

* [Learn how to use Otoroshi](https://maif.github.io/otoroshi/manual/how-to-s/index.html)

## Underlying resources

When you create the Otoroshi add-on, Clever Cloud automatically deploys:

- A [Java](/developers/doc/applications/java/java-jar/) instance with Otoroshi with LLM pre-loaded
- A [Redis](/developers/doc/addons/postgresql/) database (for internal Otoroshi use)

## Plan sizing

By default, Otoroshi with LLM on Clever Cloud uses small-size resources, i.e:

- S Java
- S Redis®

They are dimensioned to suit a majority of needs. You can however manage and adjust them directly [in the Console](https://console.clever-cloud.com/).

## LLM extension

Otoroshi on Clever Cloud comes with LLM Extension. It provides a unified gateway for managing and interacting with Large Language Models through an OpenAI-compatible API interface, with [MCP support](https://www.clever-cloud.com/blog/company/2025/01/21/create-your-own-mcp-client-server-as-easy-as-1-2-3-with-otoroshi/). This extension streamlines the integration and management of multiple LLM providers including Ollama instances, OpenAI, Mistral, Anthropic, DeepSeek, Eleven Labs, Gemini, Groq, Hive, Hugging Face, Leonardo AI, Luma, OVH and Scaleway AI Endpoints. It supports audio, image, moderation and text generation models.

### Smarter AI operations
The extension enhances your LLM operations with intelligent workload distribution and automatic failover mechanisms, ensuring consistent service availability. It implements sophisticated features such as semantic caching to optimize response times and reduce costs, while providing comprehensive quota management capabilities for effective resource allocation.

{{< youtube id="M8sA9xuE3gs">}}

### Security and Management
Security is paramount with built-in features for API key management through Otoroshi's secure vault system. The extension leverages Otoroshi's advanced authorization framework to implement fine-grained access controls based on user identity, API keys, consumer metadata, and request parameters. Additionally, prompt fencing technology helps prevent sensitive information leakage and ensures response quality.

### Observability and Enhancement
Every LLM interaction is thoroughly audited, capturing detailed information about consumers, providers, and usage patterns. The extension also includes robust prompt engineering capabilities, allowing you to create and maintain a library of contextually enhanced prompts and templates for improved efficiency and consistency in LLM interactions.

- [Otoroshi LLM extension documentation](https://cloud-apim.github.io/otoroshi-llm-extension/docs/overview)
- [Otoroshi LLM extension video tutorials](https://www.youtube.com/watch?v=M8PbydxPw4A&list=PLNHaf5rXAx3FWk7dn2fKGwQXxeLCPhZCh)

## Coraza WAF (Web Application Firewall)

Otoroshi on Clever Cloud integrates Coraza, a high-performance Web Application Firewall (WAF), through a WebAssembly-based plugin. This integration provides enterprise-grade security features to protect your applications using the OWASP Core Rule Set (CRS).

### Security features
The Coraza WAF plugin enables robust security policy enforcement while maintaining high performance across deployments of any scale. It seamlessly integrates with Otoroshi's existing infrastructure to provide comprehensive protection against web application threats.

The integration provides advanced security capabilities through OWASP CRS implementation, allowing you to create and enforce custom security policies. The system generates detailed audit logs for security monitoring and compliance purposes, with full integration into Otoroshi's existing logging and monitoring infrastructure.

### Enterprise Capabilities
Designed for production environments, the Coraza WAF plugin offers flexible configuration options, supporting both detection and prevention modes. It enables customized rule sets per domain and provides detailed security event tracking through Otoroshi's event management system. The implementation is optimized for minimal performance impact while maintaining robust security controls.

- [Otoroshi Coraza WAF documentation](https://maif.github.io/otoroshi/manual/how-to-s/instantiate-waf-coraza.html)

## Manage Otoroshi from its API

Otoroshi exposes a comprehensive REST API that enables programmatic control over all operations available through the Otoroshi dashboard. The dashboard itself operates as a client of this API. It gives you full control over your Otoroshi instances, enabling you to build custom integrations and extensions tailored to your infrastructure needs. [A Swagger UI detailing available endpoints is available](https://maif.github.io/otoroshi/swagger-ui/index.html).

An OpenAPI descriptor is available from your instance:

```
https://xxxxxxxxxxxx-api-otoroshi.services/apis/openapi.json
```
