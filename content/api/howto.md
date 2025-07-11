---
type: docs
title: Clever Cloud API Overview
weight: 1
shortdesc: Getting started with the Clever Cloud API
tags:
- extend
keywords:
- api
- authentication
type: docs
---

The [Clever Cloud Console](https://console.clever-cloud.com) and [Clever Tools](https://github.com/CleverCloud/clever-tools) allow you to manage your account and products with the same public API you can use for your own services and integrations. This article will explain how to connect to this API and use it.

{{< cards >}}
  {{< card link="/developers/api/v2/" title="Base v2 Endpoints" subtitle="Our base API endpoints with users, organisations, applications, add-ons, etc." icon="endpoints" >}}
  {{< card link="/developers/api/v4/" title="New v4 Endpoints" subtitle="More recent API endpoints with billing, deployments, load balancers, logs, etc." icon="new" >}}
{{< /cards >}}

## Request the API

Clever Cloud's REST API offers two authentication mechanisms to meet different integration needs:

* **API tokens** provide a straightforward way to authenticate requests on behalf of a specific user. These tokens operate similarly to passwords and should be handled with appropriate security measures. API tokens are ideal for personal scripts, CLI tools, and scenarios where you're accessing your own resources. Use them to request the API Bridge: https://api-bridge.clever-cloud.com

* **OAuth 1** is designed for third-party applications that need to access Clever Cloud resources on behalf of their users. This authentication flow allows applications to request permissions from users without requiring direct access to their credentials. OAuth 1 is recommended for public applications, services that integrate with multiple user accounts, or any scenario where user delegation is required.

Choose the authentication method that best aligns with your specific integration requirements and security considerations.

### API tokens

Clever Cloud Console allows you to easily create and manage API tokens.

![Manage API tokens in Clever Cloud Console](/images/doc/console-api-tokens.webp)

[Clever Tools](https://github.com/CleverCloud/clever-tools) provides a `clever tokens` set of commands. This feature needs to be enabled:

```bash
clever features enable tokens
clever tokens create "CI job Foobar"
clever tokens create "Quick local test" --expiration 1h
```

You can also list or revoke tokens:

```bash
clever tokens -F json
clever tokens revoke api_tokens_xxx
```

Once created, API tokens must be used through the bridge URL:

```bash
curl https://api-bridge.clever-cloud.com/v2/self -H "Authorization: Bearer [API_TOKEN]"
```

### clever curl

`clever curl` is a wrapper around `curl`, it supports the same arguments and handles the authentication automatically for you using the CLI account you're currently logged in with. It's a simple way to make requests to the Clever Cloud API if [Clever Tools](https://github.com/CleverCloud/clever-tools) are installed on your system.

```bash
clever curl https://api.clever-cloud.com/v2/self
clever curl https://api.clever-cloud.com/v2/summary
clever curl https://api.clever-cloud.com/v4/products/zones
clever curl https://api.clever-cloud.com/v2/organisations/<ORGANISATION_ID>/applications | jq '.[].id'
clever curl https://api.clever-cloud.com/v4/billing/organisations/<ORGANISATION_ID>/<INVOICE_NUMBER>.pdf > invoice.pdf
```

### Official clients/SDKs

You can request the Clever Cloud API from multiple languages through our official clients/SDKs:
- [Go](https://github.com/CleverCloud/clevercloud-client-go)
- [JavaScript](https://github.com/CleverCloud/clever-client.js)
- [Rust](https://github.com/CleverCloud/clevercloud-sdk-rust)

### OAuth1

If you have an application that needs to access Clever Cloud resources on behalf of your users, you can use OAuth1. This is the recommended way to authenticate third-party applications. To manage OAuth tokens linked to your account, use the [Clever Cloud Console](https://console.clever-cloud.com/users/me/oauth-tokens).

#### Create an OAuth consumer

First, you'll need to create an OAuth consumer for your application. This can be done in the [Clever Cloud console](https://console.clever-cloud.com). Go to your organisation, click on **Create…**, then on **an OAuth consumer** and fill the form. You will get a consumer key and a consumer secret for your application.

#### Integrate your application

Your application must implement the OAuth 1 dance. It mostly consists of the following steps:

* Get a "request token"
  * [`POST /oauth/request_token`](/developers/api/v2/#post-/oauth/request_token)
  * You will get a temporary `oauth_token` and `oauth_token_secret`
* Redirect the user to the authorization page with the `oauth_token`
  * [`GET /oauth/authorize`](/developers/api/v2/#get-/oauth/authorize)
  * Once the user is logged in, the browser will be redirected to your application with the query params `oauth_verifier` and `oauth_token`
* Make sure the `oauth_token` from the first step matches the one you get after the redirection
* Get the "access token" with the `oauth_token`, `oauth_token_secret` and `oauth_verifier`
  * [`POST /oauth/access_token`](/developers/api/v2/#post-/oauth/access_token)
  * You will get the user `oauth_token` and `oauth_token_secret`

Once done, your application can make API requests on behalf of the user with an OAuth 1 compatible client and the following tokens:

* Consumer key
* Consumer secret
* User token
* User token secret

More information about [OAuth dance](https://oauth.net/core/1.0/#anchor9).

#### About the OAuth1 signature

There are 3 supported methods for the signature: `PLAINTEXT`, `HMAC-SHA1` and `HMAC-SHA512`. While `PLAINTEXT` is way easier, `HMAC-SHA512` ensures that the request is totally verified. The `Authorization` header must start with `OAuth`, with a specific format for key/values:

```bash
Authorization: OAuth key="value", key2="value2"
```
