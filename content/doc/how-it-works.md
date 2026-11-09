---
type: docs
linkTitle: How it works
weight: 11
title: How Clever Cloud Works
description: What a Platform as a Service does for you, what happens between a push and a running application, why Clever Cloud runs each instance in its own virtual machine, from runtime images it builds, and which add-ons run next to it
keywords:
- paas
- platform as a service
- how it works
- virtual machine
- isolation
- runtime images
- exherbo
- immutable infrastructure
- mise
- add-ons
- managed services
---

Clever Cloud is a Platform as a Service (PaaS): you bring your code, and the platform builds it, runs it, scales it, and maintains the system it runs on. This page explains what the platform takes care of, and how, so that you know what to expect from it, and what stays in your hands.

## What a PaaS does for you

With virtual servers or a container orchestrator, you prepare the system, install the language, write the deployment scripts, configure a load balancer and its certificates, then patch and monitor all of it. On Clever Cloud, you push your code, and the platform does the rest:

- It installs your dependencies, builds your application, and starts it behind load balancers, with [TLS certificates](/doc/security/ssl/) it renews
- It replaces an instance that stops answering, adds instances or resizes them with [autoscaling](/doc/manage/scaling/), and bills the time they run
- It collects [logs and metrics](/doc/observability/), and gives your application the credentials of its [databases and services](#databases-and-services-next-to-your-applications), which it operates for you
- It updates the runtime images with new versions and security fixes

You choose your code, its dependencies, the versions of your languages, and the configuration in [environment variables](/doc/manage/environment-variables/). Your code deploys with Git and runs with standard languages and tools, so you keep it portable. Applications that follow the [twelve-factor principles](/doc/develop/12-factors/), such as keeping their configuration in the environment, get the most out of the platform.

## From a push to a running application

Each deployment starts in a new instance:

1. You push a commit, with Git, Clever Tools, or [from GitHub](/doc/tools/github/)
2. Clever Cloud starts a new instance from the runtime image of your application, in its [region](/doc/manage/regions/)
3. It selects the versions you ask for, installs the tools of your [Mise](/doc/manage/mise/) file, and runs your [deployment hooks](/doc/manage/build-hooks/) around the build
4. It starts your application, which listens on [its configured port](/doc/manage/#listen-on-the-right-port), and checks with the [health check](/doc/manage/healthcheck/) that it's ready to receive traffic
5. With [zero downtime deployment](/doc/manage/#zero-downtime-deployment), enabled by default, it sends the traffic to the new instance, then stops the previous one

[Blue/Green deployment](/doc/manage/#bluegreen-deployment) describes this switch, and what happens when the build or the health check fails. An instance is never updated in place: a deployment, a restart, or a change of size replaces it. What your application writes on its disk disappears with it, so store your data in add-ons, an [FS Bucket](/doc/deploy/storage/fs-bucket/), or [Cellar](/doc/deploy/storage/cellar/). [Immutable infrastructure](/doc/develop/immutable-infrastructure/) details this model, and what it brings: each deployment starts from a clean system, and changes made on an instance, such as a tampered file, disappear with it.

## Virtual machines, not containers

Each instance of your application runs in its own virtual machine, with its own kernel. On many platforms, applications of different customers run in containers that share the kernel of the same host. A virtual machine isolates your application with hardware virtualization: it shares neither its kernel nor its memory with other customers, even on the same physical server.

The [Docker runtime](/doc/deploy/applications/docker/) follows the same model: your container runs in a virtual machine of its own, with its own Docker daemon. Your Dockerfile then defines its system and its tools: the runtime images don't apply to it.

## Runtime images built by Clever Cloud

Clever Cloud builds and maintains its runtime images, based on [Exherbo](https://www.exherbo.org/), a Linux distribution to which the Clever Cloud team actively contributes, and where it packages the languages and tools it ships. Clever Cloud updates these packages every day, and publishes a new image about once a week, with a [changelog](/changelog/) entry that lists its changes: your application moves to the new image at its next deployment.

All runtimes except Docker share the same image, with several languages and tools: the runtime you choose sets how Clever Cloud builds and starts your application. Whatever this runtime, a non-Docker instance provides Node.js, Python, PHP, Ruby, and Java, with tools such as Mise, Clever Tools, SQLite, or FFmpeg, ready to use in your hooks and your application. So you can:

- Build the front end of a Go or Rust application with Node.js, in the version that `CC_NODE_VERSION` selects
- Run a Python script in a deployment hook of a Java application, with the version of `CC_PYTHON_VERSION`
- Add any other tool, or another version of a language, such as Ruby, in a [`mise.toml`](/doc/manage/mise/) file: Clever Cloud installs it before the build

The [environment variables reference](/doc/manage/environment-variables/reference/) lists the version variables, and each [runtime page](/doc/deploy/applications/) the versions it supports. When no runtime fits, the [Linux runtime](/doc/deploy/applications/linux/) runs what Mise installs, and the [Docker runtime](/doc/deploy/applications/docker/) runs your own image.

## Databases and services next to your applications

Your application rarely runs alone. Add-ons are the services you create next to it, in the same organisation, and that Clever Cloud or a partner operates. [Linking an add-on](/doc/manage/service-dependencies/#link-a-service) exposes the variables it provides to your application, such as connection credentials. Add-ons follow four models:

- **Managed databases and storage**: [PostgreSQL](/doc/deploy/databases/postgresql/), [MySQL](/doc/deploy/databases/mysql/), [MongoDB](/doc/deploy/databases/mongodb/), [Redis](/doc/deploy/databases/redis/), and [Elastic Stack](/doc/deploy/databases/elastic/) run on instances you size, with backups and monitoring. Your files go to [Cellar](/doc/deploy/storage/cellar/) object storage, or to an [FS Bucket](/doc/deploy/storage/fs-bucket/) file system
- **Serverless services**, with no instance to size: [Materia KV](/doc/deploy/databases/materia-kv/), in beta and compatible with Redis, replicates each write across three data centers in Paris, and [Pulsar](/doc/deploy/pulsar/) carries your messages and streams between your applications
- **Ready-to-use software**: [Keycloak](/doc/deploy/services/keycloak/), [Metabase](/doc/deploy/services/metabase/), [Matomo](/doc/deploy/services/matomo/), or [Otoroshi Gateway](/doc/deploy/services/otoroshi/) deploy in one command, on applications and add-ons of your organisation you see and resize like your own. Clever Cloud configures them and makes their new versions available, as each page details
- **Partner services**: [MailPace](/doc/deploy/services/mailpace/) sends the transactional emails of your applications from its own platform, and you create it, link it, and open its dashboard from the Console, like any other add-on of your organisation

Partners also help build the software that Clever Cloud runs for you: Keycloak with [Please Open-it](https://please-open.it/), and Otoroshi Gateway with the extensions of [Cloud APIM](https://www.cloud-apim.com/). [Services](/doc/deploy/services/) lists them all, and the [Marketplace](/doc/develop/marketplace/) lets other providers offer their own.

## Go further

- Deploy an application step by step with the [getting started tutorial](/doc/getting-started/)
- Learn the platform with the courses and certifications of [Clever Cloud Academy](https://academy.clever.cloud/?lang=en), starting with Cloud Concepts 101
- Read how Clever Cloud secures the platform, and which certifications it holds, in [Security & Compliance](/doc/security/)
