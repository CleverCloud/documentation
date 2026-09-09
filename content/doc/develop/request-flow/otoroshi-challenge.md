---
type: docs
weight: 20
linkTitle: Otoroshi Challenge
title: Otoroshi Challenge
description: Verify that traffic reaching your application comes from your Otoroshi gateway with the Otoroshi challenge middleware
keywords:
- otoroshi
- challenge
- request flow
- api gateway
- jwt
- reverse proxy
aliases:
- /doc/develop/otoroshi-challenge
- /doc/request-flow/otoroshi-challenge
---

Putting an [Otoroshi](/doc/deploy/services/otoroshi/) gateway in front of an application moves a whole class of concerns out of your code. Authentication through OAuth2, OpenID Connect, JWT verification or API keys, rate limiting and quotas, request and response transformation, canary releases, and a [Coraza web application firewall](/doc/deploy/services/otoroshi/#coraza-waf-web-application-firewall) all become route configuration, applied the same way to a website or to an API. Your teams change these behaviours from the gateway, without a deployment and without touching the applications behind it.

That model only holds if those applications cannot be reached any other way. An application deployed on Clever Cloud keeps its own public URL, and anyone who finds it bypasses the gateway along with everything it enforces.

The Otoroshi challenge closes that gap without a private network. [Request Flow](/doc/develop/request-flow/) runs a middleware in front of your application that answers `401 Unauthorized` to every request unable to prove it came through your gateway, and forwards the rest untouched. Your code changes in no way, and your application never sees the challenge headers.

A [Network Group](/doc/network/network-groups/) reaches the same result differently, by placing your Otoroshi add-on and your applications on a private WireGuard network and keeping those applications off the public internet. The challenge suits applications that stay on a public URL, or that you want to protect without changing their network topology. Nothing prevents combining both.

The mechanism is version 2 of the [Otoroshi communication protocol](https://www.otoroshi.io/manual/topics/otoroshi-protocol.html), a signed token exchange based on a secret shared between the gateway and the middleware.

## Enable the Otoroshi challenge

Set the shared secret, and Request Flow detects and starts the middleware on its own:

```bash
OTOROSHI_CHALLENGE_SECRET="a-secret-shared-with-your-gateway"
```

Use the same value in the secure communication settings of the Otoroshi route pointing at your application. Generate one with `openssl rand -base64 32`, and use a different secret for each application.

Automatic detection is enough in most cases. Set `CC_REQUEST_FLOW` explicitly when you chain several middleware services, listing them in the order you want from the public port to your application:

```bash
CC_REQUEST_FLOW="otoroshi-challenge,varnish"
```

## How the exchange works

Your gateway sends a JWT in an `Otoroshi-State` header on every request. The middleware verifies it, and answers with a second JWT in an `Otoroshi-State-Resp` header that proves it holds the same secret. A response without that header tells the gateway the backend is not the one it expects.

The incoming token is signed with `HS512` and must carry three claims. The `iss` claim has to be `Otoroshi` exactly, `state` holds the value the middleware echoes back, and `exp` has to be in the future. The `iat` and `nbf` claims are accepted but optional.

The middleware answers with a token signed the same way, carrying the received `state` value in a `state-resp` claim, an `aud` claim set to `Otoroshi`, and a 30 second validity:

```json
{
  "state-resp": "the value received in the state claim",
  "aud": "Otoroshi",
  "iat": 1788585098,
  "nbf": 1788585098,
  "exp": 1788585128
}
```

The `Otoroshi-State` header stops at the middleware and never reaches your application, so nothing downstream has to know about the protocol.

## Listen on the right port

The middleware takes the public port `8080` and forwards to your application on port `9000`. When your application manages its own HTTP server, it has to follow:

```bash
PORT="9000"
```

Clever Cloud configures the backend itself on runtimes with a managed web server or port. In every other runtime, an application still bound to `8080` fails to start, because the middleware already holds that port:

```text
Error: listen EADDRINUSE: address already in use 0.0.0.0:8080
```

> [!NOTE] Bind on the address the platform provides
> This works as long as your application listens on `0.0.0.0:$PORT` rather than on a hardcoded port. Read the [Request Flow port management](/doc/develop/request-flow/#port-management) section for the details of the whole chain.

## Keep the health check working

The platform health check requests your application through the public port, where the middleware now answers `401` to a request carrying no challenge. The default check accepts any status from `200` to `500`, so it keeps passing.

Setting [`CC_HEALTH_CHECK_PATH`](/doc/develop/common-configuration/healthcheck/) narrows that range to `200` to `300`, and the check then fails on every attempt until the deployment is cancelled:

```text
[ERROR] Response from GET {:url=>"/health", :expected_response=>200...300} is 401
```

The challenge applies to every request, and no setting excludes a path from it. Leave `CC_HEALTH_CHECK_PATH` unset on an application protected this way, and rely on the default check.

## Troubleshooting

The middleware answers rejected requests with a JSON body naming the reason, which is the fastest way to tell a configuration mistake from a gateway one:

| Response body                                          | Cause                                                                      |
| ------------------------------------------------------ | -------------------------------------------------------------------------- |
| `Missing Otoroshi-State header`                        | The request did not come from the gateway, or the route sends no challenge |
| `JWT verification failed: InvalidSignature`            | The gateway and the middleware hold different secrets                      |
| `JWT verification failed: InvalidIssuer`               | The `iss` claim is not `Otoroshi`                                          |
| `JWT verification failed: ExpiredSignature`            | The token expired, check the clock drift between gateway and platform      |
| `JWT verification failed: Missing required claim: exp` | The gateway sends a token with no expiry                                   |
| `JWT verification failed: InvalidToken`                | The header holds something that is not a JWT                               |

A `Some software are not listening as expected: 9000` error in the deployment logs means the middleware runs but your application does not listen on `9000`. Read [Listen on the right port](#listen-on-the-right-port).

Confirm the protection from your machine, where the challenge is missing by design:

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://your-application.cleverapps.io/
```

A `401` answer means only your gateway can reach the application. A `200` means the middleware is not running, so check that `OTOROSHI_CHALLENGE_SECRET` is set and that your runtime supports Request Flow.

- [Learn more about Request Flow](/doc/develop/request-flow/)
- [Deploy an Otoroshi add-on](/doc/deploy/services/otoroshi/)
- [Learn more about the Otoroshi communication protocol](https://www.otoroshi.io/manual/topics/otoroshi-protocol.html)
