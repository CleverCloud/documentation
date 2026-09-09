---
type: docs
weight: 12
linkTitle: AI & LLMs
title: Drive Clever Cloud from an AI agent
description: Deploy and operate Clever Cloud from any AI coding tool, through an API-first platform with machine-readable documentation
keywords:
- ai
- llm
- agent
- mcp
- automation
- api-first
---

An AI agent is good at driving a platform when three things are true: the documentation is readable without a browser, every action has an API, and the feedback loop is short enough to correct itself. Clever Cloud was built that way before agents existed, for its own tooling, and the same properties now make it straightforward to operate from Claude Code, Cursor, Codex or any assistant that can run a command.

Nothing here is an AI-specific product. The Console runs on the same public API your agent calls, the CLI it drives is the one your team uses, and the documentation it reads is the page you are reading. There is no separate surface to learn, and no gap between what a human and an agent can do.

## Documentation an agent can read

Every documentation page is available as raw Markdown, either by asking for it in the HTTP request:

```bash
curl -H "Accept: text/markdown" https://www.clever.cloud/developers/doc/deploy/applications/nodejs/
```

or by appending `index.html.md` to any page URL. Both return the Markdown source rather than the rendered page, which removes the parsing step and the token cost of HTML.

An [`llms.txt`](https://www.clever.cloud/developers/llms.txt) index lists the documentation with a one-line description per page, so an agent picks what it needs instead of crawling. The [Clever Tools reference](/doc/cli-reference/) documents every command, option and accepted value in a single page, which is enough for an agent to compose a correct command without trial and error. The whole documentation is [open source](https://github.com/CleverCloud/documentation).

## Ways to drive the platform

Pick the interface that fits the agent, they all reach the same API:

| Interface                                                                | Best for                                   |
| ------------------------------------------------------------------------ | ------------------------------------------ |
| [Clever Tools](/doc/manage/cli/)                                         | Any agent that can run a shell command     |
| [`mcp-simple-server`](https://github.com/CleverCloud/mcp-simple-server)  | Agents speaking the Model Context Protocol |
| [`@clevercloud/client`](https://github.com/CleverCloud/clever-client.js) | Generating code that talks to the API      |
| [The REST API](/api/)                                                    | Anything else, including raw HTTP calls    |
| [Terraform and OpenTofu](/doc/tools/terraform/)                          | Declaring infrastructure as code           |
| [Kubernetes operator](/doc/deploy/kubernetes/operator/)                  | Managing add-ons from an existing cluster  |

Clever Tools ships a [skill](https://github.com/CleverCloud/clever-tools/blob/master/skills/clever-tools/SKILL.md) in its own repository, so an assistant that reads skills learns the CLI from the source rather than from a guess. The MCP server takes a different route: instead of exposing hundreds of tools, one per endpoint, it offers three: `search` to discover commands, `execute` to run pre-authenticated JavaScript against the API, and `doc` to read the documentation. The agent composes a call rather than picking from a menu, which keeps its context small.

Both are built on `@clevercloud/client`, the typed client the Console itself uses, with a command per API operation across 46 families of resources.

## Disposable infrastructure

The shortest useful loop is create, deploy, verify, destroy. It runs in a handful of commands, which is what makes it worth automating:

```bash
clever create --type node my-experiment
clever deploy
clever domain
clever delete --yes
```

An agent can spin up an environment to reproduce a bug, run an integration test against a real database rather than a mock, check that a migration applies, then remove everything. Resources are billed by the second, so an environment that lives ten minutes costs ten minutes.

The same loop covers backing services. A test needing PostgreSQL, object storage and a message broker creates them, links them, and reads the injected credentials from the environment:

```bash
clever addon create postgresql-addon test-db
clever service link-addon test-db
clever env
```

Linking an add-on injects its credentials as environment variables, so the application code stays the same between a throwaway environment and production.

[Docker](/doc/deploy/applications/docker/) widens what fits in that loop. Any image the agent can build runs on the platform, inside a virtual machine rather than a shared container host, so a stack no runtime covers still deploys with a `git push`. Point `CC_DOCKERFILE` at the file to build, and `CC_DOCKER_LOGIN_*` at a private registry when the image is not public.

The reverse also works: Clever Tools ships as [a Docker image](https://hub.docker.com/r/clevercloud/clever-tools), so an agent running in a container or a CI job drives the platform without installing anything:

```bash
docker run --rm -e CLEVER_TOKEN -e CLEVER_SECRET clevercloud/clever-tools status
```

## An ecosystem that fits together

Deployment is a `git push`, and the platform detects the runtime, installs dependencies and starts the application behind a load balancer with TLS already configured. That covers a [static site](/doc/deploy/applications/static/) built automatically from its sources, [Node.js and Bun](/doc/deploy/applications/nodejs/), [Rust](/doc/deploy/applications/rust/), [Scala](/doc/deploy/applications/scala/), [Python with uv](/doc/deploy/applications/python/uv/), [V](/doc/deploy/applications/v/), and [Docker](/doc/deploy/applications/docker/) for the rest. The [Linux runtime](/doc/deploy/applications/linux/) with [Mise](/doc/develop/mise/) handles anything else: declare the tools and versions your build needs in a `mise.toml`, and they are installed before the build.

Around the application, the managed services are meant to be assembled. [PostgreSQL](/doc/deploy/databases/postgresql/), [MySQL](/doc/deploy/databases/mysql/) and [Redis](/doc/deploy/databases/redis/) for the classics, [Materia KV and TS](/doc/deploy/databases/) when a serverless store with nothing to size fits better, [Pulsar](/doc/deploy/pulsar/) for messaging, [Cellar](/doc/deploy/storage/cellar/) for S3-compatible object storage, [MailPace](/doc/deploy/services/mailpace/) for transactional email, [Keycloak](/doc/deploy/services/keycloak/) for identity.

Two of them deserve a mention for what they take off an agent's plate. [Otoroshi](/doc/deploy/services/otoroshi/) is an API gateway with a Coraza web application firewall, an LLM extension for routing and governing model calls, a workflow engine, and a long list of plugins covered in [a dedicated blog post](https://www.clever.cloud/blog/company/2025/12/08/otoroshi-17-9/). [Redirection.io](/doc/develop/request-flow/redirectionio/) handles redirects, cache rules and traffic analysis from an interface a marketing team can use without a deployment.

Each of them is driven by API, so an agent assembles a full stack rather than a single application.

## Production is the same platform

A throwaway environment and a production one differ by their plan, not by their nature. The same application gets [logs](/doc/develop/observability/logs/) and [access logs](/doc/develop/observability/access-logs/), [metrics](/doc/develop/observability/metrics/) stored in Warp 10, [automated backups](/doc/deploy/databases/) on its databases, [horizontal and vertical auto-scaling](/doc/develop/best-practices/), and [Kubernetes](/doc/deploy/kubernetes/) when a cluster is the right shape.

An agent reads all of it through the same CLI it used to deploy:

```bash
clever logs --since 10m
clever activity
clever status
```

When something needs to be checked inside a running instance rather than from the outside, one command runs it and returns:

```bash
clever ssh -c "node --version"
```

That closes the loop: the agent deploys, observes, inspects the instance, and corrects, without a human relaying the state between steps.

## Where to look next

Clever Cloud publishes its tooling openly, so an agent can read the source of what it drives rather than infer it.

| Resource                                                                                          | What it holds                                             |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| [`awesome-clever-cloud`](https://github.com/CleverCloud/awesome-clever-cloud)                     | Curated index of tools, libraries and community resources |
| [`examples-and-demos`](https://github.com/CleverCloud/examples-and-demos)                         | Runnable example applications across runtimes             |
| [`mcp-simple-server`](https://github.com/CleverCloud/mcp-simple-server)                           | The MCP server, its catalogue generator and its tools     |
| [`clever-tools`](https://github.com/CleverCloud/clever-tools)                                     | The CLI, and the skill describing it                      |
| [`clever-components`](https://github.com/CleverCloud/clever-components)                           | The web components the Console is built from              |
| [`terraform-provider-clevercloud`](https://github.com/CleverCloud/terraform-provider-clevercloud) | The Terraform and OpenTofu provider                       |
| [`clever-kubernetes-operator`](https://github.com/CleverCloud/clever-kubernetes-operator)         | Add-ons as Kubernetes custom resources                    |

API clients exist beyond JavaScript, for [Python](https://github.com/CleverCloud/clevercloud-sdk-python), [Go](https://github.com/CleverCloud/clevercloud-client-go) and [Rust](https://github.com/CleverCloud/clevercloud-sdk-rust), so generated code fits the language of the project rather than the other way round.

- [Clever Tools reference](/doc/cli-reference/)
- [API documentation](/api/)
- [Getting started](/doc/getting-started/)
