---
weight: 2
title: Applications
shortdesc: Deploy an application on Clever Cloud
tags:
- applications
keywords:
- deploy

aliases:
- /doc/deploy/application
type: "docs"
comments: false
---

## Choose your Stack

Find here specific instructions related to your application's language.

{{< cards >}}
  {{< card link="/doc/applications/docker" title="Docker" icon="docker" >}}
  {{< card link="/doc/applications/golang" title="Go" icon="go" >}}
  {{< card link="/doc/applications/haskell" title="Haskell" icon= "haskell">}}
  {{< card link="/doc/applications/java" title="Java" icon="java" >}}
  {{< card link="/doc/applications/javascript" title="Node.js" icon="node" >}}
  {{< card link="/doc/applications/ruby" title="Ruby" icon="ruby" >}}
  {{< card link="/doc/applications/php" title="PHP" icon="php" >}}
  {{< card link="/doc/applications/python" title="Python" icon="python" >}}
  {{< card link="/doc/applications/rust" title="Rust" icon="rust" >}}
  {{< card link="/doc/applications/scala" title="Scala" icon="scala" >}}
  {{< card link="/doc/applications/elixir" title="Elixir" icon="elixir" >}}
  {{< card link="/doc/applications/dotnet" title=".NET" icon="dotnet" >}}
  
{{< /cards >}}

## How To Deploy X if It Isn't Natively Supported

If your favorite runtime is not available, you can deploy it on Clever Cloud by Dockerizing it and make it run in a Docker instance.
You will probably find a basic Docker file for your technology on the Docker hub.

Refer to the [Docker](/doc/applications/docker) section of this documentation to know how to deploy your Dockerized application.

If you are out of options, contact our support team and we'll come up with a solution with you.

## Environment Variables

You can control deployments and set your application configuration with environment variables:
{{< cards >}}
  {{< card link="/doc/reference/reference-environment-variables/#set-by-the-deployment-process" title="Common to all applications" subtitle="Set by the deployment process." icon="server-stack" >}}
  {{< card link="/doc/reference/reference-environment-variables/#variables-you-can-define" title="Define" subtitle="Variables you can define." icon="pencil-square" >}}
  {{< card link="/doc/reference/reference-environment-variables/#control-build-and-dependencies-cache" title="Cache" subtitle="Control the build and deployment cache." icon="arrow-up-on-square-stack" >}}
  {{< card link="/doc/reference/reference-environment-variables/#control-the-deployments-behavior" title="Run" subtitle="Control the deployment behavior." icon="play-circle" >}}
  {{< card link="/doc/reference/reference-environment-variables/#deployment-hooks" title="Hooks" subtitle="Define commands to run between various steps of the deployment." icon="eye-dropper" >}}
  {{< card link="/doc/reference/reference-environment-variables" title="How to" subtitle="How to to configure your application with environment variables." icon="book-open" >}}
{{< /cards >}}

### Common to All Applications

- Applications on Clever Cloud listen on **port 8080**. Be sure you application is able to listen on port 8080 before deploying.
- Deployments on Clever Cloud are immutable: if your app restarts, last pushed commit will be deployed with your current environment variables. 

💡 [Learn more about immutablity and application management](/doc/administrate/apps-management).

