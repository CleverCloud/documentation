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

The Clever Cloud console and clever-tools are built on top of an API that
allows you to manage your account and products. This article will explain how
to connect to this API and use it.

## HTTP calls

### **Authentication**

Clever Cloud API has an OAuth1 based authentication.

There are 3 supported methods for the signature: `PLAINTEXT`, `HMAC-SHA1` and `HMAC-SHA512`.

While `PLAINTEXT` is way easier for testing, you **should** use `HMAC-SHA512` when it comes to production. This ensures that the request is totally verified.

We have a [JavaScript client on GitHub](https://gitHub.com/CleverCloud/clever-client.js) where you can find a lot of informations.
Especially in the [esm/login.js file](https://gitHub.com/CleverCloud/clever-client.js/blob/master/esm/login.js)

This client is being used by our web Console and CLI. Also, the Console gives you a lot of information in the "Network" panel of the devtools. If you're stuck, this is one way for debugging.

For the Authorization header, make sure to have something like:

```bash
Authorization: OAuth key="value", key2="value2"
```

The `OAuth` and doubles quotes around values are mandatory.

#### **Create consumers tokens**

You need to create an OAuth consumer token in the Clever Cloud console.

A link **Create an oauth consumer** is available under your organization's addons list.

All created consumers will appear below that link, like your applications and addons.

These consumers allow you to register an application. By creating a consumer, users will be able to grant (or decline) privileges for your application.

For example, the Clever Cloud Console is using an oauth consumer.
You (most of the time) give it full access to manage your account.

You need to set a callback URL, this is the url your user will be redirected to after he has been authenticated.

#### **Get a request token**

You have to make a `POST`request to get a [request token](/api/v2/#post-/oauth/request_token) to the API.

#### **Get the authorization URL**

Ask the API for the [authorization URL](/api/v2/#get-/oauth/authorize) and go to this URL with a browser. Log in with your account and it will send you to the callback URL.

#### **Get the verifier token**

In the callback URL, you have the verifier token:

`https://www.example.com/callback?oauth_verifier=<verifierToken>`

Where `<verifierToken>` is your token.

#### **Get the access token**

Make a `POST`  request to get the [access token](/api/v2/#post-/oauth/access_token) with your request token and the verifier.
You can use this access token to make OAuth1 signed requests.

More information about [OAuth dance](https://oauth.net/core/1.0/#anchor9).

#### This seems cumbersome, is there an easier way?

Yes the OAuth dance can be complicated, we created a small application that you can deploy on Clever Cloud. It will automate most of the pain away from you.

The code and tutorial are on [https://github.com/CleverCloud/oauth-consumer-server](https://github.com/CleverCloud/oauth-consumer-server).

### **API endpoints documentation**

All the API endpoints are referenced in a swagger documentation. **The base URL for the API is V2**.

{{< cards >}}

  {{< card link="/api/v2" title="Base v2 Endpoints" subtitle="Our base API endpoints with users, organisations, applications, add-ons, etc." icon="endpoints" >}}
  {{< card link="/api/v4" title="New v4 Endpoints" subtitle="More recent API endpoints with billing, deployments, load balancers, logs, etc." icon="new" >}}
  
{{< /cards >}}

## WebSocket API requests

### **Connection protocol**

Clever Cloud API can handle WebSocket-Security requests for the logs or events.
To connect to a WebSocket API URL follow this guide.

- Take a URL in the API for the WebSocket.
  - Ex: `https://api.clever-cloud.com/v2/events/event-socket`
- Sign the OAuth request with this URL.
- Replace `https://` by `wss://`
  - `wss://api.clever-cloud.com/v2/events/event-socket`
- Connect to this URL in WebSocket.

When the WebSocket connection is opened, you need to send the OAuth1 header in this format :

```json
{
    "message_type": "oauth",
    "authorization": "<oauth_header>"
}
```

You need to replace `<oauth_header>` by the signed OAuth1 header.

### WebSocket endpoints

#### Logs

[This endpoint](https://www.clever-cloud.com/api/#!/logs/logs_logs-socket_appId_get)
allows you to receive real-time logs of an application via WebSocket.

#### Events

[This endpoint](https://www.clever-cloud.com/doc/api/#!/events/events_event-socket_get)
allows you to receive a stream of events emitted on your account.

Events like git push, add or remove an application / addon, deployments success / failed
are available.
