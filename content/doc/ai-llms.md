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

An AI agent is good at driving a platform when three things are true: the documentation is readable without a browser, every action has an API, and the feedback loop is short enough to correct itself. Clever Cloud was built that way before agents existed, for its own tooling, and the same properties now make it a good fit to operate from Claude Code, Cursor, Codex, or any assistant that can run a command.

Nothing here is an AI-specific product. The Console runs on the same public API your agent calls, the CLI it drives is the one your team uses, and the documentation it reads is this one. There is no separate surface to learn: an agent uses the same interfaces as your team.

## Documentation an agent can read

Every documentation page is also available as Markdown, either by asking for it in the HTTP request:

```bash
curl -H "Accept: text/markdown" https://www.clever.cloud/developers/doc/deploy/applications/nodejs/
```

or by appending `index.html.md` to any page URL. Both return the content of the page as Markdown, without its navigation, which spares the agent the parsing and the extra token cost of HTML pages.

An [`llms.txt`](https://www.clever.cloud/developers/llms.txt) index lists the documentation with a one-line description per page, so an agent picks what it needs instead of crawling. The [Clever Tools reference](/doc/cli-reference/) documents every command, option, and accepted value in a single page, where an agent looks up the arguments and options of each command. The whole documentation is [open source](https://github.com/CleverCloud/documentation).

## Teach your assistant Clever Tools

Clever Tools ships a [skill](https://github.com/CleverCloud/clever-tools/tree/master/skills/clever-tools), a package of instructions in the open [Agent Skills](https://agentskills.io) format. Claude Code, Cursor, Codex, GitHub Copilot, and other assistants support it. It holds a cheat sheet of the essentials and a reference of every command, option, runtime, add-on, and region. The assistant reads only its name and description at startup, and loads the rest when a task involves Clever Cloud.

Your local [Clever Tools](/doc/tools/cli/install/) carries out every action, so set it up and connect your account with `clever login` first. Then add the skill:

```bash
npx skills add CleverCloud/clever-tools
```

The command asks which assistants get the skill, and installs it in the current project: commit it with the code to give the whole team the same skill. Add `--global` to use it in all your projects, when you deploy from several of them.

The skill lives in the Clever Tools repository and follows its default branch, so it can describe options your version of the CLI doesn't support yet. Keep both current: list your skills with `npx skills list`, refresh this one with `npx skills update clever-tools`, and [update Clever Tools](/doc/tools/cli/install/update/). If your assistant stumbles on a command, open an issue or a pull request on [`SKILL.md`](https://github.com/CleverCloud/clever-tools/blob/master/skills/clever-tools/SKILL.md).

The skill and this documentation work together. The skill gives the assistant the right command and options, and the Markdown pages give it what the CLI doesn't describe, such as the [environment variables](/doc/manage/environment-variables/reference/) each runtime reads.

## Ways to drive the platform

Pick the interface that fits the agent: they all reach the same API.

| Interface                                                                | Best for                                   |
| ------------------------------------------------------------------------ | ------------------------------------------ |
| [Clever Tools](/doc/tools/cli/)                                          | Any agent that can run a shell command     |
| [Clever Tools skill](#teach-your-assistant-clever-tools)                 | Assistants that load Agent Skills          |
| [`mcp-simple-server`](https://github.com/CleverCloud/mcp-simple-server)  | Agents speaking the Model Context Protocol |
| [`@clevercloud/client`](https://github.com/CleverCloud/clever-client.js) | Generating code that talks to the API      |
| [The REST API](/api/)                                                    | Anything else, including raw HTTP calls    |
| [Terraform and OpenTofu](/doc/tools/terraform/)                          | Declaring infrastructure as code           |
| [Kubernetes operator](/doc/deploy/kubernetes/operator/)                  | Managing add-ons from an existing cluster  |

The MCP server suits operations the CLI doesn't expose. It takes a different route: instead of exposing hundreds of tools, one per endpoint, it offers three: `search` to discover commands, `execute` to run pre-authenticated JavaScript against the API, and `doc` to read the documentation. The agent composes a call rather than picking from a menu, which keeps its context small.

Clever Tools and the MCP server are both built on `@clevercloud/client`, the typed client the Console itself uses, with a command for each operation of the API, so they all share the same view of the platform.

## Disposable infrastructure

The shortest useful loop is create, deploy, check, destroy. From a Node.js project committed in Git, it starts with these commands:

```bash
clever create --type node my-experiment
clever deploy
clever domain
```

`clever domain` lists the URL to check. An agent can spin up an environment to reproduce a bug, test against a real database rather than a mock, or check that a migration applies. Applications are billed by the second, so an application that runs ten minutes is billed ten minutes.

The same loop covers backing services. A test that needs PostgreSQL creates a database, links it, lists the injected credentials, and restarts the application to load them, as it started before the link:

```bash
clever addon create postgresql-addon test-db --plan dev --link my-experiment
clever env
clever restart
```

Linking injects credentials as environment variables, so the same code runs in a throwaway environment and in production. Once the checks are done, delete the database first, then the application itself:

```bash
clever addon delete test-db --yes
clever delete --yes
```

[Docker](/doc/deploy/applications/docker/) widens what fits in that loop. The Docker runtime builds your Dockerfile and runs each instance in its own virtual machine rather than on a shared container host, so a stack no runtime covers still deploys with a `git push`. Point `CC_DOCKERFILE` at the file to build, and set the `CC_DOCKER_LOGIN_*` variables when the image comes from a private registry.

Conversely, Clever Tools ships as [a Docker image](https://hub.docker.com/r/clevercloud/clever-tools), so an agent in a container or a CI job drives the platform with nothing to install:

```bash
docker run --rm -e CLEVER_TOKEN -e CLEVER_SECRET clevercloud/clever-tools profile
```

## An ecosystem that fits together

Deployment is a `git push`: the platform builds and starts the application with the runtime chosen at its creation, behind a load balancer with TLS, as [how Clever Cloud works](/doc/how-it-works/) details. Runtimes cover a [static site](/doc/deploy/applications/static/) built automatically from its sources, [Node.js and Bun](/doc/deploy/applications/nodejs/), [Rust](/doc/deploy/applications/rust/), [Scala](/doc/deploy/applications/scala/), [Python with uv](/doc/deploy/applications/python/uv/), [V](/doc/deploy/applications/v/), and [Docker](/doc/deploy/applications/docker/) for the rest. The [Linux runtime](/doc/deploy/applications/linux/) with [Mise](/doc/manage/mise/) handles anything else: declare the tools and versions your build needs in a `mise.toml`, and Clever Cloud installs them before the build.

Around the application, the managed services are meant to be assembled. [PostgreSQL](/doc/deploy/databases/postgresql/), [MySQL](/doc/deploy/databases/mysql/), and [Redis](/doc/deploy/databases/redis/) for the classics, [Materia KV and TS](/doc/deploy/databases/) when a serverless store fits better, [Pulsar](/doc/deploy/pulsar/) for messaging, [Cellar](/doc/deploy/storage/cellar/) for object storage, [MailPace](/doc/deploy/services/mailpace/) for transactional email, [Keycloak](/doc/deploy/services/keycloak/) for identity.

Two of them deserve a mention for what they take off an agent's plate. [Otoroshi Gateway](/doc/deploy/services/otoroshi/) is an API gateway with a web application firewall, an LLM extension for routing and governing model calls, a workflow engine, and a long list of [bundled extensions](/doc/deploy/services/otoroshi/#bundled-extensions). [Redirection.io](/doc/manage/request-flow/redirectionio/) handles redirects, cache rules, and traffic analysis from an interface a marketing team can use without a deployment.

Each of them is driven by API, so an agent assembles a full stack rather than a single application.

## Production is the same platform

A throwaway environment and a production one differ by their plan, not by their nature. The same application gets [logs and access logs](/doc/observability/logs/), [metrics](/doc/observability/metrics/) stored in Warp 10, [automated backups](/doc/deploy/databases/postgresql/#database-daily-backup-and-retention) on its databases, [horizontal and vertical auto-scaling](/doc/manage/scaling/), and [Kubernetes](/doc/deploy/kubernetes/) when a cluster is the right shape.

An agent reads the logs, the deployment activity, and the status of an application through the same CLI it used to deploy:

```bash
clever logs --since 10m --until now
clever activity
clever status
```

When something needs to be checked inside a running instance rather than from the outside, one command runs it and returns:

```bash
clever ssh --instance any -c "node --version"
```

That closes the loop: the agent deploys, observes, inspects the instance, and corrects, without a human relaying the state between steps.

## Where to look next

Clever Cloud publishes its tooling openly, so an agent can read the source of what it drives rather than infer it.

| Resource                                                                                          | What it holds                                              |
| ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [`awesome-clever-cloud`](https://github.com/CleverCloud/awesome-clever-cloud)                     | Curated index of tools, libraries, and community resources |
| [`clever-components`](https://github.com/CleverCloud/clever-components)                           | The web components the Console is built from               |
| [`clever-kubernetes-operator`](https://github.com/CleverCloud/clever-kubernetes-operator)         | Add-ons as Kubernetes custom resources                     |
| [`clever-tools`](https://github.com/CleverCloud/clever-tools)                                     | The CLI, and the skill describing it                       |
| [`examples-and-demos`](https://github.com/CleverCloud/examples-and-demos)                         | Runnable example applications across runtimes              |
| [`mcp-simple-server`](https://github.com/CleverCloud/mcp-simple-server)                           | The MCP server, its catalog generator, and its tools       |
| [`terraform-provider-clevercloud`](https://github.com/CleverCloud/terraform-provider-clevercloud) | The Terraform and OpenTofu provider                        |

API clients exist beyond JavaScript, for [Python](https://github.com/CleverCloud/clevercloud-sdk-python), [Go](https://github.com/CleverCloud/clevercloud-client-go), and [Rust](https://github.com/CleverCloud/clevercloud-sdk-rust), so generated code fits the language of the project.

- [API documentation](/api/)
- [Clever Tools reference](/doc/cli-reference/)
- [Getting started](/doc/getting-started/)
- [How Clever Cloud works](/doc/how-it-works/)
