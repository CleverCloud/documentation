---
type: docs
linkTitle: Load balancers
title: Load balancers
description: How the Sōzu load balancers of Clever Cloud forward HTTP requests to your application, the headers they add to find the client address and protocol, and dedicated load balancers
keywords:
- load balancer
- sozu
- request headers
- x-forwarded-for
- x-forwarded-proto
- forwarded
- client ip
- trusted proxies
- cc_reverse_proxy_ips
- inbound ip
- redundancy
- high availability
aliases:
- /doc/administrate/load-balancers
- /doc/load-balancers
- /doc/network/dedicated-load-balancers
---

The load balancers of Clever Cloud run [Sōzu](https://www.sozu.io/), the open-source reverse proxy that Clever Cloud created and develops. Each HTTP request to your application goes through them. They terminate TLS with the [certificate](/doc/security/ssl/) of the domain, then forward the request in plain HTTP to port `8080` of one of your instances. [TCP redirections](/doc/manage/tcp-redirections/) go through the same load balancers, for other protocols.

## How a request reaches your application

The `cleverapps.io` domains have their own load balancers, apart from those of your [custom domains](/doc/manage/domain-names/). Both forward requests in a similar way:

- Clients can use HTTP/2 on `cleverapps.io` domains, and your application receives HTTP/1.1
- [Force HTTPS](/doc/manage/#force-https), enabled by default, answers HTTP requests with a redirection to HTTPS
- The connection comes from the address of the load balancer, not from the client
- With several instances, any of them can get a request, unless you enable [sticky sessions](/doc/manage/#sticky-sessions)

A [Request Flow](/doc/manage/request-flow/) middleware, such as Varnish, sits between the load balancer and your application: the connection then comes from `127.0.0.1`. A request that runs for more than 180 seconds fails on the [backend timeout](/doc/find-help/troubleshooting/#network) of the load balancers.

## Request headers

The load balancers set these headers on each request, so that your application knows the client and the protocol it used:

| Header              | Value                                                                    | Load balancers                 |
| ------------------- | ------------------------------------------------------------------------ | ------------------------------ |
| `X-Forwarded-For`   | Address of the client, at the end of the list                            | All                            |
| `Forwarded`         | Protocol, address and port of the client, at the end of the list         | All                            |
| `X-Forwarded-Proto` | `http` or `https`, unless the client sends its own                       | All                            |
| `X-Forwarded-Port`  | `80` or `443`, unless the client sends its own                           | All                            |
| `Sozu-Id`           | Unique ID of the request, also in the headers of the response            | All                            |
| `X-Request-Id`      | Same value as `Sozu-Id`, unless the client sends its own                 | Some, such as `cleverapps.io`  |
| `traceparent`       | [W3C Trace Context](https://www.w3.org/TR/trace-context/) of the request | Some, such as `cleverapps.io`  |

`Forwarded` follows [RFC 7239](https://www.rfc-editor.org/rfc/rfc7239): each element holds the protocol, the client as `for`, and the load balancer as `by`. On `cleverapps.io` domains, when a client sends a `traceparent` header, the load balancers keep its trace ID and replace its parent ID. To ask the support team about a request, give its `Sozu-Id`: the last one, if the client sent its own.

A request to a `cleverapps.io` domain over HTTPS reaches your application with these headers:

```http
GET / HTTP/1.1
Host: app-<uuid>.cleverapps.io
User-Agent: curl/8.7.1
Accept: */*
X-Forwarded-For: 203.0.113.42
Forwarded: proto=https;for="203.0.113.42:62560";by=198.51.100.10
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
X-Forwarded-Port: 443
X-Forwarded-Proto: https
X-Request-Id: 01JD4R8Z6K3M7Q2W9X5T1V0B8N
Sozu-Id: 01JD4R8Z6K3M7Q2W9X5T1V0B8N
```

## Get the address of the client

A client can send its own `X-Forwarded-For` and `Forwarded` headers: the load balancer adds its element at the end of their list, without removing the others. Only the end of the list is reliable, while its start holds what the client sent:

- Without Request Flow, the address of the client is the last one of `X-Forwarded-For`
- With Varnish alone in your Request Flow, it's the second to last: Varnish adds the address of the load balancer after it

With other middleware, start from the end of the list. Skip the addresses of the proxies you trust: the next one is the address of the client. The `for` parameter of the last element of `Forwarded` also holds the address of the client, with its port, and Varnish doesn't change this header.

Frameworks read these headers for you, from the proxies you declare as trusted. The `CC_REVERSE_PROXY_IPS` [environment variable](/doc/manage/environment-variables/reference/) lists the addresses of the load balancers, separated by commas: declare them, and add `127.0.0.1` if you use Request Flow. With Symfony, for instance, build the list in your `.env` file. On your computer, where the variable doesn't exist, it holds only `127.0.0.1`:

```bash {filename=".env"}
TRUSTED_PROXIES=127.0.0.1,${CC_REVERSE_PROXY_IPS}
```

```yaml {filename="config/packages/framework.yaml"}
framework:
  trusted_proxies: '%env(TRUSTED_PROXIES)%'
```

## Get the protocol

With Force HTTPS, each request that reaches your application through the load balancers came over HTTPS. Without it, read the `proto` parameter of the last element of `Forwarded`, which the load balancer always adds.

The load balancers pass the `X-Forwarded-Proto`, `X-Forwarded-Port`, `X-Forwarded-Host`, and `X-Real-IP` headers that a client sends unchanged. They only add `X-Forwarded-Proto` and `X-Forwarded-Port` when these headers are missing. Don't rely on them for a security decision, such as a `Secure` cookie or a redirection to HTTPS, or to build URLs. Don't let your framework trust `X-Forwarded-Host` either.

## Add-ons

The host of a dedicated database add-on, such as `POSTGRESQL_ADDON_HOST`, usually points to other proxies, for TCP connections. They forward the connection to the server of the add-on, which sees the address of the proxy, not of your application. The shared `DEV` plan of PostgreSQL connects directly to a server of its cluster, without these proxies.

To bypass these proxies, generate a direct host and port for [MySQL](/doc/deploy/databases/mysql/#direct-access) or [PostgreSQL](/doc/deploy/databases/postgresql/#direct-access), or reach the add-on through a [Network Group](/doc/network/network-groups/).

A PostgreSQL [private database](/doc/network/private-databases/) is reachable only from a Network Group, through a dedicated load balancer.

## Dedicated load balancers

By default, your applications share the load balancers of their region with other customers. For workloads that need isolated capacity, fixed inbound IP addresses or additional redundancy, you can request **dedicated load balancers**.

Dedicated load balancers are especially relevant if you need to:

- **Isolate your traffic** from other customers
- **Isolate a PostgreSQL add-on** from the internet, as a [private database](/doc/network/private-databases/)
- **Add redundancy** to the network entry point of critical architectures
- **Use fixed inbound IP addresses** for allowlists or compliance requirements
- **Handle high traffic volumes** without sharing load balancer capacity with other organisations

Two configurations are available, the second one for critical architectures:

- **Single load balancer**: one load balancer dedicated to your organisation
- **High availability**: two dedicated load balancers, so that your entry point doesn't depend on one of them

They're a quote-based option: contact your sales representative or [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice) with your use case and region.
