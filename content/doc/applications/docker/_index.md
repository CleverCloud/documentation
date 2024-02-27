---
type: docs
title: Docker
shortdesc: Docker is an easy, lightweight virtualized environment for portable applications.
keywords:
- docker
tags:
- deploy
str_replace_dict:
  "@application-type@": "Docker"
type: docs
aliases:
- /doc/deploy/application/docker
- /doc/deploy/application/docker/docker
- /doc/getting-started/by-language/docker/
- /doc/partials/language-specific-deploy/docker
---
{{< hextra/hero-subtitle style="margin:.3rem 0 2rem 0">}}
  Clever Cloud offers support for Docker containers. These are deployed inside virtual machines to guarantee a secure level of isolation.
{{< /hextra/hero-subtitle >}}

## Overview

Docker containers can encapsulate any payload, and will run consistently on and between virtually any server. The same container that a developer builds and tests on a laptop will run at scale, in production, on VMs, bare-metal servers, public instances, or combinations of the above.

Clever Cloud allows you to deploy any application running inside a Docker container. This page will explain how to set up your application to run it on our service.

{{< callout type="info" >}}
  Clever Cloud supports many languages, but some users have specific application needs. With Docker, they can create custom stacks without relying on Clever Cloud's specific support.
{{< /callout >}}

{{< callout type="warning" >}}
[FS Buckets](/doc/best-practices/cloud-storage/#what-is-fs-bucket) access, Dockerfile validation, and Docker Compose functionalities are not supported.
{{< /callout >}}

 {{% content/set-env-vars %}}

{{< readfile file="language-specific-deploy/docker.md" >}}

 {{% content/env-injection %}}

 {{% content/deploy-git %}}

 {{% content/link-addon %}}


{{% content/more-config %}}

{{< readfile file="url_healthcheck.md" >}}
