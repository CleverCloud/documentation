---
type: docs
linkTitle: Fluentd
title: Deploy a Fluentd data collector
description: Deploy a Fluentd data collector on Clever Cloud with the Linux runtime, Bundler and Mise
keywords:
- fluentd
- data collector
- logging
- linux
- ruby
aliases:
- /doc/deploy/application/docker/tutorials/fluentd
- /doc/docker/fluentd
- /fluentd
---

[Fluentd](https://www.fluentd.org/) is an open source data collector that unifies data from multiple sources and routes it to storage, analytics or monitoring services. This guide deploys a minimal HTTP collector that writes received events to the application logs. You can then adapt its [inputs, filters and outputs](https://docs.fluentd.org/configuration/config-file) to your needs.

## Prerequisites

- A [Clever Cloud account](https://console.clever-cloud.com/)
- [Clever Tools](/doc/cli/install/)
- [Git](https://git-scm.com/)
- Ruby 3.2 or later with [Bundler](https://bundler.io/)

## Create the Fluentd application

Create a project directory, initialize Git and create a Linux application:

```bash
mkdir myFluentd
cd myFluentd
git init
clever create -t linux -a myFluentd
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` to the `clever create` command.

Create a `Gemfile` to install the tested Fluentd version:

```ruby
source "https://rubygems.org"

gem "fluentd", "1.19.3"
```

Generate and commit the dependency lock file:

```bash
bundle lock
```

Create a `.gitignore` file to exclude local Bundler files:

```gitignore
.bundle/
vendor/
```

## Configure Fluentd

Create a `fluent.conf` file:

```aconf
<source>
  @type http
  bind 0.0.0.0
  port "#{ENV.fetch('PORT', 8080)}"
</source>

<match **>
  @type stdout
</match>

<label @FLUENT_LOG>
  <match **>
    @type stdout
  </match>
</label>
```

This configuration receives JSON events over HTTP and sends them to standard output. The `@FLUENT_LOG` label handles Fluentd's own logs separately.

Create a `mise.toml` file with the build and run tasks used by the Linux runtime:

```toml
[tasks.build]
description = "Install Fluentd and its dependencies"
run = "bundle config set --local path vendor/bundle && bundle install"

[tasks.run]
description = "Start Fluentd"
run = "bundle exec fluentd --no-supervisor -c fluent.conf"
```

[Mise](https://mise.jdx.dev/) is available on Clever Cloud. During deployment, the Linux runtime runs the task named `build` in the build phase and the task named `run` to start the application. See [Mise tasks](https://mise.jdx.dev/tasks/) and the [Linux runtime documentation](/doc/applications/linux/) for details.

## Deploy Fluentd

Commit and deploy the project:

```bash
git add .
git commit -m "Deploy Fluentd"

clever deploy
```

Display the application URL or add a custom domain. A custom domain also requires DNS configuration:

```bash
clever domain
clever domain add your.website.tld
```

Send a test event to the application, replacing the example hostname with its URL:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello from Fluentd"}' \
  https://your-fluentd.example.com/app.log
```

Display the application logs to confirm that Fluentd received the event:

```bash
clever logs
```

The minimal HTTP input in this guide is publicly reachable. Before using it in production, add access controls suitable for your clients and replace the standard-output match with the [Fluentd output plugins](https://www.fluentd.org/plugins) required by your architecture.

## Learn more

{{< cards >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://docs.fluentd.org/" title="Fluentd documentation" subtitle="Configure Fluentd inputs, filters and outputs" icon="external-link" >}}
  {{< card link="/doc/applications/linux/" title="Linux applications" subtitle="Configure and deploy any application" icon="linux" >}}
  {{< card link="/doc/cli/" title="Clever Tools" subtitle="Manage Clever Cloud resources from the command line" icon="terminal" >}}
{{< /cards >}}
