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

## Choose your stack

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

## How to deploy X if it is not natively supported

If your favorite runtime is not available, you can deploy it on Clever Cloud by Dockerizing it and make it run in a Docker instance.
You will probably find a basic Docker file for your technology on the Docker hub.

Refer to the [Docker](/doc/applications/docker) section of this documentation to know how to deploy your Dockerized application.

If you are out of options, contact our support team and we'll come up with a solution with you.

## Environment variables

Here goes common environment varibales applicables to all apps.

### Ports

Here goes a short explanation on port 8080.

## Immutability

Here goes a short explanation on immunatble deployments and how the server works.