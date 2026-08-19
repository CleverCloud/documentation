---
type: docs
linkTitle: OAuth2 Proxy
title: OAuth2 Proxy
description: Add OAuth2 Proxy authentication to applications through Request Flow on Clever Cloud without changing application code
keywords:
- oauth2-proxy
- authentication
- oidc
- sso
- request flow
- reverse proxy
---

## Overview

[Request Flow](/doc/develop/request-flow/) puts authentication in front of any application through [OAuth2 Proxy](https://oauth2-proxy.github.io/oauth2-proxy/), with no change to your code: a few environment variables are enough. Clever Cloud starts the middleware, allocates its port, points it at your application, and keeps it in the chain alongside Varnish, Redirection.io or a proxy of your own with the same flexibility. It's available on every runtime that supports Request Flow.

OAuth2 Proxy redirects unauthenticated visitors to the identity provider you configure, and only authenticated requests reach your application. This suits a staging environment, an internal dashboard or an administration interface.

Clever Cloud sets the port OAuth2 Proxy listens on and the address of your application. Every other setting comes from `OAUTH2_PROXY_*` environment variables, which map one to one to the [OAuth2 Proxy configuration options](https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview).

## Enable OAuth2 Proxy

Add `oauth2-proxy` to the `CC_REQUEST_FLOW` environment variable:

```bash
CC_REQUEST_FLOW="oauth2-proxy"
```

Request Flow allows you to use OAuth2 Proxy with other middleware such as [Varnish](/doc/develop/varnish/) or [Redirection.io](https://redirection.io/) for example. List every middleware in the order you want, from the public port to your application:

```bash
CC_REQUEST_FLOW="oauth2-proxy,varnish"
```

## Minimal configuration

OAuth2 Proxy validates its configuration at startup and exits when a required setting is missing, which fails your deployment. The following variables are the smallest working set for a GitHub identity provider, and the same structure applies to every provider. Replace every value with your own:

```bash
CC_REQUEST_FLOW="oauth2-proxy"
OAUTH2_PROXY_PROVIDER="github"
OAUTH2_PROXY_CLIENT_ID="<your-client-id>"
OAUTH2_PROXY_CLIENT_SECRET="<your-client-secret>"
OAUTH2_PROXY_COOKIE_SECRET="<your-cookie-secret>"
OAUTH2_PROXY_EMAIL_DOMAINS="example.com"
OAUTH2_PROXY_REDIRECT_URL="https://app.example.com/oauth2/callback"
```

The redirect URL must point to the public domain of your application, followed by `/oauth2/callback`. Declare that exact URL in your identity provider as an authorised callback, otherwise the provider rejects the login with a `redirect_uri mismatch` error.

For an OpenID Connect provider such as Okta or Microsoft Entra ID, set the provider to `oidc` and give the issuer URL. The `email` scope feeds the address that authorization rules check, so request it explicitly:

```bash
OAUTH2_PROXY_PROVIDER="oidc"
OAUTH2_PROXY_OIDC_ISSUER_URL="https://sso.example.com"
OAUTH2_PROXY_SCOPE="openid email profile"
```

Keycloak has a provider of its own, `keycloak-oidc`, pointing at the realm you want:

```bash
OAUTH2_PROXY_PROVIDER="keycloak-oidc"
OAUTH2_PROXY_OIDC_ISSUER_URL="https://sso.example.com/realms/internal"
OAUTH2_PROXY_SCOPE="openid email profile"
```

> [!NOTE]
> The [OAuth2 Proxy client installation provider](https://github.com/please-openit/keycloak-oauth2proxy-client-installation-provider) writes these variables for you from your Keycloak client settings. Install the extension in the `providers` folder of your [Keycloak add-on](/doc/addons/keycloak/#custom-themes-and-plugins), then download "Oauth2-proxy environment variables" from the Installation tab of your client. [This video](https://www.youtube.com/watch?v=Jo-Njxsxq-8) presents it, in French.

## Generate the cookie secret

OAuth2 Proxy encrypts session cookies with an AES cipher and accepts a secret of 16, 24, or 32 bytes only. A hexadecimal string generated with `openssl rand -hex 32` counts as 64 bytes and gets rejected at startup. Generate a valid secret with:

```bash
openssl rand -base64 32 | tr '+/' '-_'
```

Use a different secret for each application. Changing the secret invalidates every existing session and signs all users out.

## Authorize users

Authenticating a visitor and authorizing them are two different steps. Once the identity provider confirms who the visitor is, OAuth2 Proxy compares the email address it received against your authorization rules, and answers `403 Forbidden` when no rule matches, even though the login succeeded.

One of these rules is mandatory at startup, which prevents an accidentally open proxy. Set `OAUTH2_PROXY_EMAIL_DOMAINS` to a comma-separated list of domains, prefixing a domain with a dot to include its subdomains, or set `OAUTH2_PROXY_AUTHENTICATED_EMAILS_FILE` to the path of a file listing one authorized address per line:

```bash
OAUTH2_PROXY_EMAIL_DOMAINS="example.com,.corp.example.com"
```

The value `*` authorizes any address the provider validates, which means you rely entirely on the provider for identity checks. With an identity provider restricted to your organisation, this is the expected setting. With a public provider such as GitHub or Google, it accepts every account of that provider, so pick the scope you want: a domain list, an authenticated emails file, or a provider-level rule such as `OAUTH2_PROXY_GITHUB_ORG`.

## Pass the identity to your application

OAuth2 Proxy forwards the visitor identity to your application by default through `X-Forwarded-User`, `X-Forwarded-Groups`, `X-Forwarded-Email` and `X-Forwarded-Preferred-Username` headers.

To also forward the OpenID Connect ID token in the `Authorization` header, enable:

```bash
OAUTH2_PROXY_PASS_AUTHORIZATION_HEADER="true"
```

This suits an application that validates the token itself. Only trust these identity headers on requests that have passed through OAuth2 Proxy.

## Listen on the right port

When your application manages its own HTTP server, it must listen on port `9000` while Request Flow is active. Clever Cloud handles the backend configuration for runtimes with a managed web server or port. In every other runtime, set the port yourself:

```bash
PORT="9000"
```

> [!NOTE]
> This works as long as your application listens on `0.0.0.0:$PORT` rather than on a hardcoded port. Read the [Request Flow port management](/doc/develop/request-flow/#port-management) section for the details of the whole chain.

## Keep the health check working

The platform health check requests your application through the public port, which OAuth2 Proxy now answers. A redirect to the login page still counts as a healthy answer, so the default health check keeps working.

This changes as soon as you configure [`CC_HEALTH_CHECK_PATH`](/doc/develop/healthcheck/), which expects a `2xx` status. An authenticated path never returns one to the health check, so exclude it from authentication:

```bash
CC_HEALTH_CHECK_PATH="/health"
OAUTH2_PROXY_SKIP_AUTH_ROUTES="^/health$"
```

This exclusion makes the health check path publicly accessible. Limit its response to the application's health status and don't expose sensitive data.

## Scale to several instances

OAuth2 Proxy stores sessions in the cookie by default, so every instance of your application validates them without shared state. Horizontal scaling and instance replacement need no extra configuration.

Tokens with many claims, particularly Microsoft Entra ID tokens carrying group memberships, can make sessions exceed the 4 kB limit for a single cookie. OAuth2 Proxy splits large sessions across several cookies, but the resulting headers can still exceed browser or proxy limits. In that case, store sessions in a [Redis add-on](/doc/addons/redis/) and copy its connection URL into the variable:

```bash
OAUTH2_PROXY_SESSION_STORE_TYPE="redis"
OAUTH2_PROXY_REDIS_CONNECTION_URL="redis://:password@host:port"
```

## Troubleshooting

OAuth2 Proxy logs its configuration errors and exits, so read the deployment logs from the bottom up. The health check reports the public port as closed, which is a consequence of the middleware being down rather than a problem with your application:

| Log message | Cause |
| ----------- | ----- |
| `cookie_secret must be 16, 24, or 32 bytes` | The secret has the wrong length, see [Generate the cookie secret](#generate-the-cookie-secret) |
| `missing setting for email validation` | The configuration carries neither `OAUTH2_PROXY_EMAIL_DOMAINS` nor `OAUTH2_PROXY_AUTHENTICATED_EMAILS_FILE` |
| `Your application is not listening on 8080` | OAuth2 Proxy failed to start, the preceding message holds the reason |
| `Some software are not listening as expected: 9000` | OAuth2 Proxy runs, your application doesn't listen on port `9000` |

A login that loops between your application and the identity provider points to `OAUTH2_PROXY_REDIRECT_URL` not matching the callback declared in the provider. A `403 Forbidden` after a successful login points to an email address outside your authorization rules, or to a missing `email` scope.

- [Learn more about Request Flow](/doc/develop/request-flow/)
- [Learn more about OAuth2 Proxy configuration](https://oauth2-proxy.github.io/oauth2-proxy/)
- [Configure your health check](/doc/develop/healthcheck/)
