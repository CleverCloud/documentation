---
type: docs
weight: 3
linkTitle: Applications
title: Applications
description: Deploy applications on Clever Cloud with support for popular languages, frameworks, and deployment configurations across modern runtimes
keywords:
- deploy applications
- app deployment
- app hosting
- runtime support
- programming languages
- cloud deployment
- development platforms
- app development
- modern runtimes
aliases:
- /applications
- /doc/apps
- /doc/deploy
- /doc/deploy/application
- /doc/deploy/application/ruby/by-framework
- /doc/getting-started/by-language
- /doc/java/select-java-version
- /doc/reference/reference-runtimes
---

## Choose your Stack

Find here specific instructions related to your application's language.

{{< cards >}}
  {{< card link="/developers/doc/applications/dotnet" title=".NET" icon="dotnet" >}}
  {{< card link="/developers/doc/applications/docker" title="Docker" icon="docker" >}}
  {{< card link="/developers/doc/applications/elixir" title="Elixir" icon="elixir" >}}
  {{< card link="/developers/doc/applications/frankenphp" title="FrankenPHP" icon="frankenphp" >}}
  {{< card link="/developers/doc/applications/golang" title="Go" icon="go" >}}
  {{< card link="/developers/doc/applications/haskell" title="Haskell" icon="haskell" >}}
  {{< card link="/developers/doc/applications/java" title="Java (Gradle, JAR, Maven, WAR/EAR)" icon="java" >}}
  {{< card link="/developers/doc/applications/linux" title="Linux" icon="linux" >}}
  {{< card link="/developers/doc/applications/meteor" title="Meteor.js" icon="meteor" >}}
  {{< card link="/developers/doc/applications/nodejs" title="Node.js & Bun" icon="node" >}}
  {{< card link="/developers/doc/applications/php" title="PHP with Apache" icon="php" >}}
  {{< card link="/developers/doc/applications/python" title="Python with uv support" icon="python" >}}
  {{< card link="/developers/doc/applications/ruby" title="Ruby" icon="ruby" >}}
  {{< card link="/developers/doc/applications/rust" title="Rust" icon="rust" >}}
  {{< card link="/developers/doc/applications/scala" title="Scala" icon="scala" >}}
  {{< card link="/developers/doc/applications/static" title="Static" icon="static" >}}
  {{< card link="/developers/doc/applications/static-apache" title="Static with Apache" icon="feather" >}}
  {{< card link="/developers/doc/applications/v" title="V (Vlang)" icon="v" >}}
{{< /cards >}}

## Deploying a Non-native Runtime

If your runtime isn't available natively, the [Linux runtime](/developers/doc/applications/linux) with [Mise](https://mise.jdx.dev/) can run many languages and tools — see examples in [our GitHub examples and demos](https://github.com/CleverCloud/examples-and-demos). Otherwise, use the [Docker runtime](/developers/doc/applications/docker) with a Dockerfile from [Docker Hub](https://hub.docker.com/) or your own.

If none of these options fit, contact [our support team](https://console.clever-cloud.com/ticket-center-choice) to find a solution together.

## Custom Runtime Extensions

Some runtimes can be extended with additional modules (such as extra PHP extensions). To request one, contact [our support team](https://console.clever-cloud.com/ticket-center-choice) with your use case so they can assess feasibility on the target operating system.

## Environment Variables

You can control deployments and set your application configuration with environment variables:
{{< cards >}}
  {{< card link="/developers/doc/develop/env-variables" title="Environment variables" subtitle="Understand how variables are defined and used" icon="book-open" >}}
  {{< card link="/developers/doc/reference/reference-environment-variables/#set-by-the-deployment-process" title="Platform variables" subtitle="Review variables set by the deployment process" icon="server-stack" >}}
  {{< card link="/developers/doc/reference/reference-environment-variables/#variables-you-can-define" title="Configuration variables" subtitle="Review variables you can define" icon="pencil-square" >}}
  {{< card link="/developers/doc/develop/env-variables/#settings-you-can-define-using-environment-variables" title="Build cache" subtitle="Control which files are included in the build cache" icon="arrow-up-on-square-stack" >}}
  {{< card link="/developers/doc/reference/reference-environment-variables/#variables-you-can-define" title="Run command" subtitle="Override the command used to run your application" icon="play-circle" >}}
  {{< card link="/developers/doc/develop/build-hooks" title="Deployment hooks" subtitle="Run commands during deployment phases" icon="rocket-launch" >}}
{{< /cards >}}

### Common to All Applications

- Applications on Clever Cloud listen on **port 8080**. Be sure you application is able to listen on port 8080 before deploying.
- Deployments on Clever Cloud are immutable: if your app restarts, last pushed commit will be deployed with your current environment variables.

{{< callout type="info" >}}
  Learn more about [immutablity and application management](/doc/administrate/apps-management).
{{< /callout >}}
