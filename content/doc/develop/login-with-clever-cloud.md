---
type: docs
weight: 70
linkTitle: Login with Clever Cloud
title: Login with Clever Cloud
description: Let your users authenticate with their Clever Cloud account through OAuth
keywords:
- oauth
- login
- authentication
- sso
- oauth consumer
- api
---

An OAuth consumer lets your application authenticate people with their Clever Cloud account, in the same way a "Sign in with GitHub" button works. The user lands on a Clever Cloud page, reviews what your application asks for, and grants or refuses it. Your application receives an access token instead of a password, and the user revokes it whenever they want.

Authentication is only half of what the token carries. The same grant gives your application scoped access to the resources of the person who authorised it: their organisations, applications, add-ons, invoices or SSH keys, depending on the rights you requested. A login button and an API integration are the same mechanism, and you decide how far it reaches.

That combination is what makes a custom interface possible. Teams build internal portals where developers deploy without ever opening the Console, self-service platforms that provision applications for their own customers, agency dashboards that group the consumption of several client organisations, or editor and CI integrations that deploy on behalf of a signed-in user. [`@clevercloud/components`](https://github.com/CleverCloud/clever-components) and [`@clevercloud/client`](https://github.com/CleverCloud/clever-client.js) are published under the Apache 2.0 licence, so the web components and the API client the Console itself runs on are available to build those interfaces rather than starting from an empty page.

This page covers creating and managing consumers. The [API documentation](/api/#oauth1) describes the OAuth 1.0a exchange your application then implements, with a [working Node.js example](https://github.com/CleverCloud/oauth1-example).

## Create an OAuth consumer

A consumer represents your application. Creating one gives you a **consumer key**, the public identifier your application sends, and a **consumer secret**, which signs its requests and never leaves your server.

From the [Console](https://console.clever-cloud.com), open your organisation, click **Create…**, then **an OAuth consumer**, and fill the form.

From Clever Tools, the `oauth-consumers` command set covers the whole lifecycle:

```bash
clever oauth-consumers create my-portal \
  --description "Internal deployment portal" \
  --url https://portal.example.com \
  --base-url https://portal.example.com/oauth/callback \
  --picture https://portal.example.com/logo.png \
  --rights access-personal-information,access-organisations
```

The command prompts for any missing value, including the logo URL, so pass every option when you script it. Target an organisation rather than your personal account with `--org`, which decides who owns and administers the consumer.

## Choose the rights

Rights are independent flags rather than a hierarchy. A `manage-` right does not imply the matching `access-` one, and the API checks each of them separately: reading an organisation's invoices requires both `access-organisations` and `access-organisations-bills`.

| Right                                         | Grants                                                       |
| --------------------------------------------- | ------------------------------------------------------------ |
| `access-organisations`                        | Read organisations the user belongs to, and their resources  |
| `access-organisations-bills`                  | Read invoices, alongside `access-organisations`              |
| `access-organisations-consumption-statistics` | Read consumption metrics, alongside `access-organisations`   |
| `access-organisations-credit-count`           | Read credit balance, alongside `access-organisations`        |
| `access-personal-information`                 | Read the user's profile                                      |
| `manage-organisations`                        | Create, configure and delete organisations                   |
| `manage-organisations-applications`           | Deploy, scale and delete applications                        |
| `manage-organisations-members`                | Add, remove and change the role of members                   |
| `manage-organisations-services`               | Create, configure and delete add-ons                         |
| `manage-personal-information`                 | Change the user's profile                                    |
| `manage-ssh-keys`                             | Add and remove the user's SSH keys                           |
| `all`                                         | Every right, including those added later                     |

Request the smallest set that does the job. A login button needs `access-personal-information` alone, and a deployment portal adds `access-organisations` and `manage-organisations-applications`. Users see this list on the authorisation screen, so a consumer asking for `all` to display a name gets refused more often than one asking for what it uses.

## Set the callback base URL

The base URL you register bounds where Clever Cloud agrees to send users back after they authorise your application. The check compares the **scheme and the host** of your callback against it, and ignores the port and the path. A consumer registered with `http://localhost:3000` therefore accepts a callback on `http://localhost:8080/oauth/done`, while `https://localhost:3000/cb` is rejected on the scheme alone:

```text
400 {"id":13502,"message":"OAuth callback is invalid","type":"error"}
```

One consumer covers every port of a local setup, which is enough to develop several interfaces side by side. Production runs on another host, so register a second consumer for it: two consumers also mean two secrets, and a leaked development secret stays away from production.

## Retrieve the consumer secret

The secret is not shown again after creation. Read it back with:

```bash
clever oauth-consumers get my-portal --with-secret
```

Treat it as a server-side credential. It signs every OAuth request your application makes, so a browser bundle, a public repository or a client-side environment variable must never carry it. If it leaks, delete the consumer and create another one, since rotating the secret alone is not possible.

## Build your own Clever Cloud interface

An access token reaches the same API the Console runs on, so anything the Console does, your own interface can do too, restricted to the rights the user granted. Three small examples show how differently that plays out, each built on Node's standard library alone:

| Interface           | What it does                                                             | Rights it needs                                             |
| ------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Sign-in button      | Signs a user in and shows their profile, nothing else                    | `access-personal-information`                               |
| Fleet overview      | Aggregates every application across organisations, by runtime and region | `access-organisations`                                      |
| Application console | Lists applications and restarts one of them                              | `access-organisations`, `manage-organisations-applications` |

The first is an authentication feature, the second a read-only dashboard the Console does not offer, and the third an operator tool that acts on resources. They share one OAuth implementation and differ only in the endpoints they call, which is a fair picture of how far the same token can go.

Building the interface itself is where [`@clevercloud/components`](https://github.com/CleverCloud/clever-components) helps. The web components the Console is made of are published under the Apache 2.0 licence, so an application card, an add-on form or a logs viewer comes ready-made rather than rebuilt. [`@clevercloud/client`](https://github.com/CleverCloud/clever-client.js) wraps the API endpoints under the same licence, and handles the OAuth signature for you.

Actions taken through a consumer are attributed to it. A restart triggered by an integration shows the consumer name rather than the CLI in the application's activity log, which keeps an audit trail of what acted on behalf of whom.

## Manage consumers over time

List what exists, inspect a consumer, change its metadata or rights, open its Console page, and delete it:

```bash
clever oauth-consumers list
clever oauth-consumers get my-portal
clever oauth-consumers update my-portal --description "Deployment portal"
clever oauth-consumers open my-portal
clever oauth-consumers delete my-portal
```

Every subcommand accepts the consumer name, or its key when several consumers share a name. Add `-F json` to any read command to feed the output to a script.

Deleting a consumer invalidates every token issued through it, which signs out all its users at once. On the other side, each user reviews and revokes the applications they authorised from their [OAuth tokens page](https://console.clever-cloud.com/users/me/oauth-tokens), so a grant never outlives their consent.

- [Implement the OAuth1 flow](/api/#oauth1)
- [Working example in Node.js](https://github.com/CleverCloud/oauth1-example)
- [Clever Cloud web components](https://github.com/CleverCloud/clever-components)
