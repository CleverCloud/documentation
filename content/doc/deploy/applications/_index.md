---
type: docs
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
- /doc/applications
- /doc/apps
- /doc/deploy/application
- /doc/getting-started/by-language
- /doc/reference/reference-runtimes
---

## Choose your Stack

Find here specific instructions related to your application's language.

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/dotnet" title=".NET" icon="dotnet" >}}
  {{< card link="/developers/doc/deploy/applications/docker" title="Docker" icon="simple:docker" >}}
  {{< card link="/developers/doc/deploy/applications/elixir" title="Elixir" icon="simple:elixir" >}}
  {{< card link="/developers/doc/deploy/applications/frankenphp" title="FrankenPHP" icon="frankenphp" >}}
  {{< card link="/developers/doc/deploy/applications/golang" title="Go" icon="simple:go" >}}
  {{< card link="/developers/doc/deploy/applications/haskell" title="Haskell" icon="simple:haskell" >}}
  {{< card link="/developers/doc/deploy/applications/java" title="Java (Gradle, JAR, Maven, WAR/EAR)" icon="java" >}}
  {{< card link="/developers/doc/deploy/applications/linux" title="Linux" icon="simple:linux" >}}
  {{< card link="/developers/doc/deploy/applications/meteor" title="Meteor.js" icon="simple:meteor" >}}
  {{< card link="/developers/doc/deploy/applications/nodejs" title="Node.js & Bun" icon="simple:nodedotjs" >}}
  {{< card link="/developers/doc/deploy/applications/php" title="PHP with Apache" icon="php" >}}
  {{< card link="/developers/doc/deploy/applications/python" title="Python with uv support" icon="simple:python" >}}
  {{< card link="/developers/doc/deploy/applications/ruby" title="Ruby" icon="ruby" >}}
  {{< card link="/developers/doc/deploy/applications/rust" title="Rust" icon="simple:rust" >}}
  {{< card link="/developers/doc/deploy/applications/scala" title="Scala" icon="simple:scala" >}}
  {{< card link="/developers/doc/deploy/applications/static" title="Static" icon="static" >}}
  {{< card link="/developers/doc/deploy/applications/static-apache" title="Static with Apache" icon="feather" >}}
  {{< card link="/developers/doc/deploy/applications/v" title="V (Vlang)" icon="simple:v" >}}
{{< /cards >}}

## Create and Deploy an Application

In the [Console](https://console.clever-cloud.com/), select **Create** at the top of the sidebar, pick the runtime of your application, and follow the wizard: choose its scaling, its region, and its name. With Clever Tools, run [`clever create`](/doc/tools/cli/applications/#create) with the type of your runtime from the Git repository of your code, such as `clever create --type node my-app`. [How Clever Cloud works](/doc/how-it-works/) explains how the runtime builds and runs your code, and which tools it provides.

To deploy your code, run `clever deploy` from this repository: an application created in the Console needs [`clever link`](/doc/tools/cli/applications/#unlink-and-make-default) first. You can also push with Git to the `master` branch of the **Deployment URL** in its **Information** menu, with an [SSH key](/doc/account-billing/ssh-keys/) in your profile, or [deploy from a GitHub repository](/doc/tools/github/), which redeploys on each push. [PHP applications](/doc/deploy/applications/php/) can also use FTP. For a first deployment, follow the [getting started tutorial](/doc/getting-started/).

### Git Submodules

Your repository records the commit of each submodule, not its files. If your repository has a `.gitmodules` file, Clever Cloud fetches the content of its submodules after the clone, before the build, with `git submodule update --init`. This fetch isn't recursive: it skips nested submodules.

For a private submodule, keep credentials out of `.gitmodules`: use its SSH URL, such as `git@github.com:my-org/my-library.git`, and give your application a [private SSH key](/doc/manage/#private-ssh-key) with read access to it. Clever Cloud installs this key before it fetches the submodules. If it can't fetch one, the deployment fails, and its logs show the Git error, such as `Permission denied (publickey)`.

To deploy without fetching the submodules, set `CC_DISABLE_GIT_SUBMODULES=true`.

## Deploying a Non-native Runtime

If your runtime isn't available natively, the [Linux runtime](/developers/doc/deploy/applications/linux) with [Mise](https://mise.jdx.dev/) can run many languages and tools — see examples in [our GitHub examples and demos](https://github.com/CleverCloud/examples-and-demos). Otherwise, use the [Docker runtime](/developers/doc/deploy/applications/docker) with a Dockerfile from [Docker Hub](https://hub.docker.com/) or your own.

If none of these options fit, contact [our support team](https://console.clever-cloud.com/ticket-center-choice) to find a solution together.

## Custom Runtime Extensions

Some runtimes can be extended with additional modules (such as extra PHP extensions). To request one, contact [our support team](https://console.clever-cloud.com/ticket-center-choice) with your use case so they can assess feasibility on the target operating system.

## Environment Variables

You can control deployments and set your application configuration with environment variables:
{{< cards >}}
  {{< card link="/developers/doc/manage/environment-variables" title="Environment variables" subtitle="Understand how variables are defined and used" icon="book-open" >}}
  {{< card link="/developers/doc/manage/environment-variables/reference/#set-by-the-deployment-process" title="Platform variables" subtitle="Review variables set by the deployment process" icon="server-stack" >}}
  {{< card link="/developers/doc/manage/environment-variables/reference/#variables-you-can-define" title="Configuration variables" subtitle="Review variables you can define" icon="pencil-square" >}}
  {{< card link="/developers/doc/manage/environment-variables/#settings-you-can-define-using-environment-variables" title="Build cache" subtitle="Control which files are included in the build cache" icon="arrow-up-on-square-stack" >}}
  {{< card link="/developers/doc/manage/environment-variables/reference/#variables-you-can-define" title="Run command" subtitle="Override the command used to run your application" icon="play-circle" >}}
  {{< card link="/developers/doc/manage/build-hooks" title="Deployment hooks" subtitle="Run commands during deployment phases" icon="rocket-launch" >}}
{{< /cards >}}

### Common to All Applications

- Applications on Clever Cloud listen on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port): `8080` by default, or `9000` with Request Flow.
- Deployments on Clever Cloud are immutable: each restart starts new instances, with your current environment variables.

> [!NOTE] Learn more
> Learn more about [immutable infrastructure](/doc/develop/immutable-infrastructure/) and [the lifecycle of an application](/doc/manage/#start-restart-and-stop).
