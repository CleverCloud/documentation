---
type: docs
linkTitle: Otoroshi Gateway
title: Otoroshi Gateway
description: Deploy the Otoroshi API gateway on Clever Cloud, with extensions to secure, route, and observe the traffic of your APIs and language models
keywords:
- otoroshi
- api gateway
- reverse proxy
- api keys
- llm gateway
- web application firewall
- api security
- traffic management
aliases:
- /doc/addons/otoroshi
- /doc/clever-cloud-overview/clevergrid-machine-learning
- /doc/deploy/clever-grid
- /doc/deploy/clever-grid/clevergrid
- /doc/extend/clever-grid
- /doc/otoroshi
- /doc/services/otoroshi
---

[Otoroshi](https://www.otoroshi.io/) is an open source API gateway, built by MAIF on a modern HTTP reverse proxy. It routes requests to your services, authenticates their callers with API keys, JWT tokens, OpenID Connect, or [Eclipse Biscuit](https://doc.biscuitsec.org/) tokens, enforces quotas, and transforms requests and responses. Its configuration changes at runtime, from its web interface or its API, without a restart.

Otoroshi Gateway is Otoroshi managed by Clever Cloud. Its distribution, built with [Cloud APIM](https://www.cloud-apim.com/), adds [extensions](#bundled-extensions) to the open source gateway, such as an LLM gateway, a threat protection suite, and Biscuit tokens.

## Create an Otoroshi Gateway add-on

### From the Console

1. [Create a new add-on](https://console.clever-cloud.com/users/me/addons/new) by clicking **Create** in the sidebar, then **Add-on**
2. Select the Otoroshi add-on
3. Skip the link to an application, Otoroshi doesn't need it
4. Enter a name for the add-on, and select its region

### With Clever Tools

Install [Clever Tools](/doc/tools/cli/install/), then create the add-on. Add `--org` to create it in an organisation, and `--region` to choose its region, `par` by default:

```bash
clever addon create otoroshi myOtoroshi
```

The command shows the URL of the web interface, and the credentials of its first administrator:

```text
Add-on created successfully!
ID: addon_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Real ID: otoroshi_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Name: myOtoroshi

Your Otoroshi with LLM is starting:
 - Access it: https://xxxxxxxxxxxx-ui-otoroshi.services.clever-cloud.com
 - Manage it: https://console.clever-cloud.com/goto/addon_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

An initial account has been created, change the password at first login (Security -> Administrators -> Edit user):
 - Admin user name: cc-account-admin
 - Password: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Learn more about Otoroshi with LLM on Clever Cloud: https://www.clever.cloud/developers/doc/addons/otoroshi/
```

### Creation options

Set options at creation with `--option name=value`, once per option. An unknown option fails the creation, and lists the available ones:

| Option          | Value                               | Effect                                                                                                                            |
| --------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `access-domain` | A domain, such as `example.com`     | Serves the web interface and the API under this domain instead of `services.clever-cloud.com`                                     |
| `routes-domain` | A domain, such as `api.example.com` | Serves the routes on this domain instead of the `cleverapps.io` domain of the Java application                                    |
| `networkgroup`  | `true`                              | Adds Otoroshi to a [Network Group](#use-otoroshi-in-a-network-group) at creation                                                  |
| `cellar`        | `true`                              | Creates a [Cellar](/doc/deploy/storage/cellar/) add-on, linked to the Java application                                            |
| `exporter`      | `pulsar` or `elastic`               | Creates a [Pulsar](/doc/deploy/pulsar/) or [Elastic Stack](/doc/deploy/databases/elastic/) add-on, linked to the Java application |

For instance, to serve Otoroshi and its routes on your own domains:

```bash
clever addon create otoroshi myOtoroshi --option access-domain=example.com --option routes-domain=api.example.com
```

With `access-domain`, Otoroshi gets four domains under this one: `<id>-ui-otoroshi.example.com` for the web interface, `<id>-api-otoroshi.example.com` for the API, and `<id>-sso-otoroshi.example.com` and `<id>-otoroshi.example.com` for its internal use.

The `<id>` is only known at creation, so point a wildcard record such as `*.example.com` to Clever Cloud. With `routes-domain`, point this exact domain the same way. In the `par` region, use a CNAME record to `domain.par.clever-cloud.com.`, as [Domain names](/doc/manage/domain-names/) details per region.

The `cellar` and `exporter` options create and link an add-on: the Java application gets its credentials in environment variables, such as `CELLAR_ADDON_HOST` or `ADDON_PULSAR_BINARY_URL`. They configure nothing in Otoroshi: use them in your routes, plugins, or [data exporters](https://maif.github.io/otoroshi/manual/docs/entities/data-exporters).

## Underlying resources

An Otoroshi Gateway add-on runs on resources of your organisation, which you see and manage [in the Console](https://console.clever-cloud.com/):

- A [Java](/doc/deploy/applications/java/java-jar/) application that runs Otoroshi, of size `S` with a single instance at creation
- A [Redis](/doc/deploy/databases/redis/) add-on of size `S`, which stores the configuration and the state of Otoroshi
- The add-ons of the `cellar` and `exporter` options, if you set them: Cellar `S`, Pulsar, or Elastic Stack `XS`

You can change these sizes afterwards, as for any application or add-on.

When you create routes in Otoroshi, they use the routes domain, set at creation or the `cleverapps.io` domain of the Java application. You can add other domains to the Java application, then use them in your routes.

## Access the web interface

Open the web interface from the dashboard of the add-on in the Console, or with Clever Tools. The first time you log in, with the `cc-account-admin` user and the password shown at creation, change this password in **Security** > **Administrators**:

```bash
clever features enable operators
clever otoroshi open webui myOtoroshi
clever otoroshi open logs myOtoroshi
```

`clever otoroshi get myOtoroshi` shows the URLs of the web interface and of the API, and the ID of its Network Group. Learn more about the [operators commands of Clever Tools](/doc/tools/cli/operators/), and about [how to use Otoroshi](https://maif.github.io/otoroshi/manual/docs/index.html).

## Version management

Check and update the version from the dashboard of the add-on in the Console, or with the operators commands of Clever Tools. With Clever Tools, set a supported version at creation with `--addon-version`:

```bash
clever addon create otoroshi myOtoroshi --addon-version VERSION

clever otoroshi version check myOtoroshi
clever otoroshi version check myOtoroshi --format json

# Update to a supported version, picked interactively or set with --target
clever otoroshi version update myOtoroshi
clever otoroshi version update myOtoroshi --target VERSION
```

The version is the `CC_OTOROSHI_VERSION` environment variable of the Java application, which you can also set before rebuilding the application.

## Configuration

Set these environment variables on the Java application of Otoroshi, in the Console or with `clever env set --app`, then rebuild Otoroshi:

| Name                                  | Description                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `CC_OTOROSHI_VERSION`                 | Version of Otoroshi to deploy                                                                          |
| `CC_OTOROSHI_PLUGINS_URLS`            | URLs of JAR files of plugins to load, separated by spaces                                              |
| `CLOUD_APIM_EXTENSIONS_WAF_FAIL_OPEN` | Set to `true` to let requests through when the WAF of the Threat Protection Suite can't run on a route |

```bash
clever otoroshi rebuild myOtoroshi
```

Before each build, Otoroshi downloads the JAR files of `CC_OTOROSHI_PLUGINS_URLS` and loads them at startup. The build fails if one of them can't be downloaded. Use plugins compatible with the Otoroshi and Scala versions of the instance.

## Use Otoroshi in a Network Group

With a [Network Group](/doc/network/network-groups/), Otoroshi reaches your applications through a private network, on ports they don't expose publicly. Your applications can then stay private, while Otoroshi exposes them with its protections, such as API keys, quotas, or its [web application firewall](#web-application-firewall). Enable it from the Otoroshi dashboard in the Console, or with Clever Tools:

```bash
clever features enable operators
clever otoroshi enable-ng myOtoroshi
```

Clever Cloud creates a Network Group labeled with the ID of the add-on, adds the Java application of Otoroshi to it, and restarts this application. Link your applications to this group from the Console, or with its ID, shown by `clever otoroshi get myOtoroshi`:

```bash
clever features enable ng
clever ng link app_xxx ng_xxx
```

In an Otoroshi route, set the backend to the domain name of a member of the group, such as `app_xxx.m.ng_xxx.cc-ng.cloud`, and to the port of its service. Disable TLS for a plain HTTP service, as WireGuard already encrypts the traffic between peers. The service must listen on `0.0.0.0` or on the address of the group, not only on `localhost`.

`clever otoroshi disable-ng myOtoroshi` deletes the group and the links to your applications, then restarts Otoroshi.

To keep an application private and expose it only through Otoroshi, follow the [Protect a private API with Otoroshi](/guides/security/otoroshi-private-api/) guide.

## Bundled extensions

Otoroshi Gateway comes with extensions of Cloud APIM, which add plugins and pages to the web interface:

- [LLM extension](#llm-extension), an OpenAI-compatible gateway in front of language model providers
- [Threat Protection Suite](#web-application-firewall), the web application firewall of Otoroshi Gateway, with its threat detectors
- [Biscuit Studio](https://cloud-apim.github.io/otoroshi-biscuit-studio/docs/overview), to issue, attenuate, and verify Biscuit tokens
- [API portal](https://cloud-apim.github.io/otoroshi-api-portal/), a developer portal with the documentation and the API keys of your APIs
- [Event brokers](https://cloud-apim.github.io/otoroshi-event-brokers-extension/), to publish and consume events of a broker through your routes
- [Mailer](https://github.com/cloud-apim/otoroshi-plugin-mailer), which turns an SMTP provider into a REST API to send emails

### LLM extension

The LLM extension exposes language models of many providers, such as Mistral AI, OpenAI, Anthropic, or Ollama instances, behind one OpenAI-compatible API. It adds failover and load balancing between providers, semantic caching, guardrails, budgets, and cost tracking, and it serves MCP servers. Its AI Studio, experimental, gives each team a workspace with its endpoint, providers, and keys.

- [LLM extension documentation](https://cloud-apim.github.io/otoroshi-llm-extension/docs/overview)

## Web application firewall

The firewall of Otoroshi Gateway is the Threat Protection Suite of Cloud APIM, a SecLang engine running the OWASP Core Rule Set (CRS).

Around it, detectors handle IP reputation, bots with a proof-of-work challenge, login and traffic abuse, API contracts from an OpenAPI document, and responses that leak data. They all feed one threat score, and Threat Studio, in the web interface, manages the whole suite.

When the WAF of a route has no configuration, or can't compile its rules in blocking mode, it refuses requests with a `503`, unless [`CLOUD_APIM_EXTENSIONS_WAF_FAIL_OPEN`](#configuration) is `true`. In monitoring mode, rules that fail to compile don't block requests.

- [Threat Protection Suite documentation](https://cloud-apim.github.io/otoroshi-waf-extension/)

## Manage Otoroshi from its API

Otoroshi exposes a REST API for everything its web interface does, which is itself a client of this API. The dashboard of the add-on in the Console shows its URL, its credentials, and the URL of its Swagger UI.

With Clever Tools, `clever otoroshi get myOtoroshi -F json` gives them in `api.url`, `api.user`, and `api.secret`:

```bash
OTOROSHI=$(clever otoroshi get myOtoroshi -F json)
API_URL=$(echo "$OTOROSHI" | jq -r .api.url)
API_AUTH=$(echo "$OTOROSHI" | jq -r '"\(.api.user):\(.api.secret)"')
curl -u "$API_AUTH" "$API_URL/api/routes"
```

The OpenAPI document of the API is at `/apis/openapi.json` on the domain of the web interface, and a Swagger UI at `/api/openapi/ui`, as `api.openapi` and `api.swaggerUrl` give. To manage Otoroshi from the command line, use [otoroshictl](/doc/tools/cli/operators/#otoroshictl), configured by Clever Tools.

To make sure that requests reach an application only through Otoroshi, use the [Otoroshi challenge](/doc/manage/request-flow/otoroshi-challenge/) of Request Flow.
