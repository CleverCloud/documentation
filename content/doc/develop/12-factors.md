---
type: docs
linkTitle: The Twelve-Factor App
title: The Twelve-Factor App
description: The twelve principles of the Twelve-Factor App methodology, why they matter on Clever Cloud, and how to apply each of them to your application
keywords:
- twelve-factor
- 12 factor
- cloud native
- best-practices
- methodology
- scalability
aliases:
- /doc/develop/best-practices/12-factors
- /doc/best-practices/12-factors
---

[The Twelve-Factor App](https://12factor.net/) is a methodology for applications delivered as a service. Its twelve principles make an application portable, simple to deploy, and ready to scale. They match how Clever Cloud runs applications on [immutable instances](/doc/develop/immutable-infrastructure/).

## Codebase

An application has one codebase, tracked in version control, and deployed several times. On Clever Cloud, each application deploys a Git repository. Use the same repository for your staging and production applications, and deploy the same commits to one, then to the other.

## Dependencies

An application declares all its dependencies, and doesn't rely on what the system provides. Clever Cloud installs them during the build, from the manifests and lock files of your runtime, such as `package.json` and its lock file, `uv.lock`, or `Cargo.lock`. Declare the tools your build needs with [Mise](/doc/manage/mise/) rather than installing them by hand on an instance: they wouldn't survive its replacement.

## Configuration

What changes between two deployments of the same code, such as credentials or the URL of a service, belongs to the environment, not to the code. Set it in the [environment variables](/doc/manage/environment-variables/) of each application: the same code then runs in staging and production with different values, and your secrets stay out of your repository. After a change, redeploy your application to use the new values.

## Backing services

A database, a cache, or a message broker is an attached resource, reached through an address in the configuration. On Clever Cloud, link an [add-on](/doc/deploy/addons/) to your application: it gets its credentials as environment variables, such as `POSTGRESQL_ADDON_URI`. To move to another PostgreSQL database, replace this link with one to the new add-on, then redeploy: your code doesn't change, but the link doesn't move your data. Avoid linking two add-ons that expose [the same variables](/doc/manage/service-dependencies/#conflicting-variable-names), such as two PostgreSQL databases.

## Build, release, run

Building the code, combining it with its configuration, and running it are separate stages. On Clever Cloud, the build installs your dependencies and compiles your code, then each deployment starts new instances with this build and the current configuration. [Deployment hooks](/doc/manage/build-hooks/) let you add commands to each stage, and the build cache speeds up the next deployments.

## Processes

The processes of an application are stateless, and share nothing. Clever Cloud can replace an instance at any time, and its local disk isn't shared with the others: store your files in an [FS Bucket](/doc/deploy/storage/fs-bucket/) or [Cellar Object Storage](/doc/deploy/storage/cellar/), and your sessions in a [Materia KV](/doc/deploy/databases/materia-kv/) or [Redis®](/doc/deploy/databases/redis/) add-on.

## Port binding

An application serves HTTP by listening on a port, where the load balancer sends the traffic of your domains. If your application starts its own HTTP server, make it listen on [`0.0.0.0:$PORT`](/doc/manage/#listen-on-the-right-port). Clever Cloud configures managed web servers, such as the one of PHP.

## Concurrency

An application scales out by running more processes. Separate the processes that serve requests from those that run background jobs: on Clever Cloud, [workers](/doc/manage/workers/) run the latter next to your application, and [horizontal scaling](/doc/manage/scaling/#horizontal-scaling) adds instances that run both. A runtime that handles requests on a single thread, such as Node.js, needs several processes to use all the vCPU of an instance.

## Disposability

Processes start fast and stop cleanly. Clever Cloud replaces instances during deployments, scaling, and maintenance: a fast start shortens each replacement, and [zero downtime deployment](/doc/manage/#zero-downtime-deployment) waits for the [health check](/doc/manage/healthcheck/). When an instance stops, its processes receive `SIGTERM`, and it shuts down shortly after, without waiting for your jobs: stop taking new work, keep requests short, and make interrupted [jobs](/doc/manage/workers/) safe to run again.

## Dev/prod parity

Development, staging, and production stay as similar as possible. Use the same runtime version and the same database engine and version on your workstation, in staging, and in production: a query that works locally on another engine can fail once deployed. Review apps, with [GitHub](/doc/tools/github/) or [GitLab](/doc/tools/gitlab/), then test each change on the platform before it reaches production.

## Logs

An application writes its logs as a stream of events on its standard output, and lets the platform collect them. Clever Cloud gathers the output of your application: read it in the [logs](/doc/observability/logs/), or send it to another tool with [drains](/doc/observability/drains/). Don't write log files on the disk of an instance.

## Admin processes

One-off administration commands run in the same environment as the application. On Clever Cloud, run a database migration or a data import as a [Clever Task](/doc/deploy/tasks/): an application that runs one command, then stops. Deploy it from the same commit as your application, and give it the same variables and add-ons, so that it runs the same code against the same services. To inspect a running instance, connect to it through [SSH](/doc/manage/ssh-access/).

- [Read The Twelve-Factor App](https://12factor.net/)
