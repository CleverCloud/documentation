---
type: docs
weight: 30
linkTitle: Redirection.io
title: Redirection.io
description: Manage redirections and HTTP traffic rules in front of your application with the Redirection.io middleware
keywords:
- redirection.io
- redirects
- seo
- request flow
- reverse proxy
- http
aliases:
- /doc/develop/redirectionio
- /doc/request-flow/redirectionio
---

[Redirection.io](https://redirection.io) moves HTTP traffic rules out of your codebase and into an interface your whole team can use. You edit rules there, its agent applies them to live traffic, and your application keeps serving the pages it knows about.

The point is who gets to act. Changing a redirect, fixing a broken link or adjusting a meta tag stops being a deployment and becomes an edit in a web interface, which puts SEO and marketing teams in control of the URLs they own without a developer in the loop. Rules are tested before they go live, and traffic keeps flowing during a site migration where hundreds of old URLs must keep resolving.

[Request Flow](/doc/develop/request-flow/) runs that agent in front of your application, with a single environment variable and no change to your code. A request matching a rule never reaches your application: the agent answers it directly, so a redirect costs nothing to your instances. Everything else passes through untouched.

## Redirection.io features

Redirects are the entry point rather than the whole product. Every request the agent handles is logged in real time, which turns the same deployment into a traffic analysis tool: which pages are hit, which return `404` or `5xx`, and which rules actually matched. A built-in crawler audits your site against more than sixty indicators per page, so broken links surface before your visitors find them.

Rules go beyond location changes. They rewrite HTML meta tags, add or alter HTTP response headers, serve a `robots.txt`, match on header values, and set cache lifetimes on static assets. Recipes package the common cases as one-click configurations, from forcing HTTPS to blocking unwanted bots or serving custom error pages, which is where access protection and caching come from without writing any rule by hand.

Everything is reachable through the Redirection.io API on the plans that include it, so rules can be generated from your own systems or kept in version control alongside the rest of your infrastructure.

- [Redirection.io: simplify and optimise your redirect management](https://www.youtube.com/watch?v=vvdUAS2ZCr0), a presentation in French on the Clever Cloud channel

## Enable Redirection.io

Set the project key found in your Redirection.io project settings, and Request Flow detects and starts the agent on its own:

```bash
CC_REDIRECTIONIO_PROJECT_KEY="your-project-key"
```

Automatic detection is enough in most cases. Set `CC_REQUEST_FLOW` explicitly when you chain several middleware services, listing them in the order you want from the public port to your application:

```bash
CC_REQUEST_FLOW="varnish,redirectionio"
```

Each running agent reports to your project under a name, which defaults to the name of your Clever Cloud application. Override it when several applications share a project, or when you want to tell environments apart:

```bash
CC_REDIRECTIONIO_INSTANCE_NAME="storefront-production"
```

The agent adds an `X-Forwarded-By` header carrying that name to every request it passes to your application, in the form `redirectionio-proxy/storefront-production`. It gives you a reliable way to confirm which instance handled a request.

## Listen on the right port

The agent takes the public port `8080` and forwards to your application on port `9000`. When your application manages its own HTTP server, it has to follow:

```bash
PORT="9000"
```

Clever Cloud configures the backend itself on runtimes with a managed web server or port. In every other runtime, an application still bound to `8080` fails to start, because the agent already holds that port:

```text
Error: listen EADDRINUSE: address already in use 0.0.0.0:8080
```

## Check that your rules apply

An invalid or revoked project key does not fail the deployment. The agent starts, your application serves traffic as usual, and no rule ever matches. Nothing in the logs reports the problem, so verify the behaviour rather than the absence of errors.

Request a URL covered by one of your rules and read the status line:

```bash
curl -sS -o /dev/null -w "%{http_code} %{redirect_url}\n" https://your-application.cleverapps.io/an-url-with-a-rule
```

A `301` and the target URL confirm the whole chain works, from your project down to the agent. A `200` from your application means the rule did not match. Check the project key first, then that the rule covers the domain you requested, because a rule scoped to `www.example.com` never fires on a `cleverapps.io` URL.

## Keep the health check working

The platform health check requests your application through the public port, where the agent answers first. The default check accepts any status from `200` to `500`, so a redirect on the checked path still counts as healthy.

Setting [`CC_HEALTH_CHECK_PATH`](/doc/develop/common-configuration/healthcheck/) narrows that range to `200` to `300`. A rule that redirects the health check path then fails the check on every attempt, until the deployment is cancelled:

```text
[ERROR] Response from GET {:url=>"/health", :expected_response=>200...300} is 301
```

Point `CC_HEALTH_CHECK_PATH` at a path no rule rewrites, and keep it out of the URL patterns you redirect.

## Troubleshooting

| Symptom                                             | Cause                                                                                                   |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Rules never apply, the application answers normally | The project key is wrong or revoked, or no rule covers the requested domain                             |
| `Some software are not listening as expected: 9000` | The agent runs, your application does not listen on port `9000`                                         |
| `EADDRINUSE` on port `8080` at startup              | Your application still binds the public port, see [Listen on the right port](#listen-on-the-right-port) |
| The deployment never turns healthy                  | A rule rewrites the path set in `CC_HEALTH_CHECK_PATH`                                                  |
| Two applications report as the same instance        | They share a project key without distinct `CC_REDIRECTIONIO_INSTANCE_NAME` values                       |

A redirect served by the agent leaves no trace in your application logs, since the request stops before it. Read the traffic in your Redirection.io project to follow what the rules matched.

- [Learn more about Request Flow](/doc/develop/request-flow/)
- [Learn more about Redirection.io](https://redirection.io/documentation)
- [Configure your health check](/doc/develop/common-configuration/healthcheck/)
