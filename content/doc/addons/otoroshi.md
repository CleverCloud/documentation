---
type: docs
linkTitle: Otoroshi with LLM
title: Otoroshi with LLM
description: Deploy Otoroshi API gateway on Clever Cloud for advanced API management, security, traffic control, and LLM models management
keywords:
- otoroshi
- api gateway
- llm management
- reverse proxy
- web application firewall
- api security
- traffic management
aliases:
- /doc/clever-cloud-overview/clevergrid-machine-learning
- /doc/otoroshi
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

Make sure you have `clever-tools` installed locally. Please refer to the [setup guide](/doc/cli/install/) if needed. In your terminal, run `clever addon create otoroshi <name> --org <org>` (`--org` is optional). You'll get URLs to manage your Otoroshi with LLM instance and the temporary credentials:

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

Learn more about Otoroshi with LLM on Clever Cloud: https://www.clever.cloud/developers/doc/addons/otoroshi/
```

By default we use Clever Cloud's domain names for both the admin interface and the routes you'll manage through Otoroshi, but you can set custom domains at creation through the `base-domain` and `routes-domain` options that you can use independently:

```bash
clever addon create otoroshi myOtoroshiName --option base-domain=otoroshi.example.com
clever addon create otoroshi myOtoroshiName2 --option routes-domain=routes.example.com
clever addon create otoroshi myOtoroshiName3 --option base-domain=otoroshi.example.com --option routes-domain=routes.example.com
```

These domains' DNS configuration needs to point to Clever Cloud's servers. For example, if the Otoroshi add-on is deployed in the `par` (Paris) region, you need to create CNAME records pointing to `domain.par.clever-cloud.com.`.

Refer to the [Clever Tools documentation](/doc/cli/addons/) for more details on add-on management.

> [!TIP] Routes management
> When you create routes in Otoroshi, they will use the routes domain you set at creation, or `app-id.cleverapps.io`. But you can add as many custom domains as you need on the underlying Java application and use them in Otoroshi routes.

## Version management

To change the version of an Otoroshi add-on on Clever Cloud, you can use the `CC_OTOROSHI_VERSION` environment variable of its Java Application and rebuild it. But there are various ways to do it simpler with [Clever Tools](/doc/cli/):

```bash
# Set a specific supported version at creation
# You can add options to set base or routes domains if needed
clever addon create otoroshi myOtoroshi --addon-version <version>

# Enable Operators commands
clever features enable operators

# Check the current version
clever otoroshi version check otoroshi_name_or_id
clever otoroshi version check otoroshi_name_or_id --format json

# Update to a specific supported version
clever otoroshi version update myOtoroshi
clever otoroshi version update myOtoroshi <new_version>
```

- Learn more about [Operators commands in Clever Tools](/doc/cli/operators/)

## Accessing the Otoroshi with LLM interface

Once you created your add-on, open the management URL in the Otoroshi with LLM dashboard from the Console. You can also use Clever Tools to open Java underlying application logs or the Otoroshi web UI directly:

```bash
# Enable Operators commands
clever features enable operators

clever otoroshi open logs myOtoroshi
clever otoroshi open webui myOtoroshi
```

The first time you connect, change the initial password (Security -> Administrators -> Edit user).

* [Learn how to use Otoroshi](https://maif.github.io/otoroshi/manual/how-to-s/index.html)

## Underlying resources

When you create the Otoroshi add-on, Clever Cloud automatically deploys:

- A [Java](/doc/applications/java/java-jar/) instance with Otoroshi with LLM pre-loaded
- A [Redis](/doc/addons/postgresql/) database (for internal Otoroshi use)

## Plan sizing

By default, Otoroshi with LLM on Clever Cloud uses small-size resources, i.e:

- S Java
- S Redis®

They are dimensioned to suit a majority of needs. You can however manage and adjust them directly [in the Console](https://console.clever-cloud.com/).

## LLM extension

Otoroshi on Clever Cloud comes with LLM Extension. It provides a unified gateway for managing and interacting with Large Language Models through an OpenAI-compatible API interface, with [MCP support](https://www.clever.cloud/blog/company/2025/01/21/create-your-own-mcp-client-server-as-easy-as-1-2-3-with-otoroshi/). This extension streamlines the integration and management of multiple LLM providers including Ollama instances, OpenAI, Mistral, Anthropic, DeepSeek, Eleven Labs, Gemini, Groq, Hive, Hugging Face, Leonardo AI, Luma, OVH and Scaleway AI Endpoints. It supports audio, image, moderation and text generation models.

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
