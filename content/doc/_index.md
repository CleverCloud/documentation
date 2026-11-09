---
type: docs
weight: 2
linkTitle: Documentation
title: Clever Cloud Documentation
description: Learn how to deploy, configure, and run your applications, databases, and services on Clever Cloud, from a first deployment to production
keywords:
- documentation
- getting started
- deploy
- applications
- add-ons
- runtimes
- clever tools
- academy
aliases:
- /clever-cloud-overview
- /doc/clever
- /doc/clever-cloud-overview
- /doc/en
- /doc/get
- /doc/site
- /doc.
- /doci
- /docs
- /documentation
- /documentation-old
---

{{< hextra/hero-subtitle >}}
  Push your code: Clever Cloud builds it, runs it, and scales it, with managed databases and services next to it
{{< /hextra/hero-subtitle >}}

Clever Cloud is a European Platform as a Service (PaaS): it maintains the system your code runs on, so you focus on your application. Each instance runs in its own virtual machine, isolated from other customers. [How Clever Cloud works](/doc/how-it-works/) explains what the platform takes care of.

## Deploy in minutes

With a [Clever Cloud account](/doc/account-billing/user/#create-an-account) and Git, install [Clever Tools](/doc/tools/cli/install/) with npm, Homebrew, a package, or a binary, sign in, and deploy a ready-made example:

```bash
npm install -g clever-tools
clever login
git clone https://github.com/CleverCloud/nodejs-example
cd nodejs-example
clever create --type node my-app
clever deploy
```

`clever deploy` ends with the URL of your application, which [consumes credits](/doc/account-billing/consumption/) until you run `clever delete`. To deploy your own project, run `clever create` with [its runtime](#choose-your-runtime) and `clever deploy` from its Git repository, once your code is committed and [listens on the right port](/doc/manage/#listen-on-the-right-port).

Watch a deployment in the [interactive demo](https://www.clever.cloud/quickstart/), or follow the tutorial, which builds an application from scratch. Your code is on GitHub? [Deploy it from its repository](/doc/tools/github/), and each push redeploys it. To try another stack, fork one of the [examples and demos](https://github.com/CleverCloud/examples-and-demos), ready to deploy for each runtime.

{{< cards cols="2" >}}
  {{< card link="/developers/doc/getting-started" title="Deploy your first application" subtitle="Deploy, link a database, and ship a change in about ten minutes" icon="rocket-launch" >}}
  {{< card link="/developers/doc/how-it-works" title="How Clever Cloud works" subtitle="What the platform does for you, from a push to a running instance" icon="light-bulb" >}}
  {{< card link="https://academy.clever.cloud/?lang=en" title="Clever Cloud Academy" subtitle="Learn the platform with courses, hands-on practice, and certifications" icon="academic-cap" >}}
  {{< card link="/developers/doc/ai-llms" title="AI & LLMs" subtitle="Drive the platform from your AI coding assistant" icon="sparkles" >}}
{{< /cards >}}

## Choose your runtime

Each runtime page explains how Clever Cloud builds and runs your code, and how to configure it.

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/nodejs" title="Node.js & Bun" icon="simple:nodedotjs" >}}
  {{< card link="/developers/doc/deploy/applications/python" title="Python" icon="simple:python" >}}
  {{< card link="/developers/doc/deploy/applications/php" title="PHP" icon="php" >}}
  {{< card link="/developers/doc/deploy/applications/java" title="Java" icon="java" >}}
  {{< card link="/developers/doc/deploy/applications/golang" title="Go" icon="simple:go" >}}
  {{< card link="/developers/doc/deploy/applications/ruby" title="Ruby" icon="ruby" >}}
  {{< card link="/developers/doc/deploy/applications/rust" title="Rust" icon="simple:rust" >}}
  {{< card link="/developers/doc/deploy/applications/docker" title="Docker" icon="simple:docker" >}}
  {{< card link="/developers/doc/deploy/applications" title="All runtimes" icon="arrow-circle-right" >}}
{{< /cards >}}

## Get ready for production

Once your application runs, the platform gives you what production needs:

- **Scale with the load**: set the size and number of instances, or let [autoscaling](/doc/manage/scaling/) adjust them
- **Deploy without downtime, roll back in one click**: with [zero downtime deployment](/doc/manage/#zero-downtime-deployment), new instances get the traffic once they pass the [health check](/doc/manage/healthcheck/), and you [redeploy a previous commit](/doc/manage/activity/#roll-back-to-a-previous-version) from the activity of your application
- **Update your versions**: change a [variable](/doc/manage/environment-variables/reference/) such as `CC_NODE_VERSION`, then redeploy, while Clever Cloud keeps the [runtime images](/doc/how-it-works/#runtime-images-built-by-clever-cloud) up to date
- **Observe**: read your [logs](/doc/observability/logs/), explore your [metrics in Grafana](/doc/observability/metrics/), send logs to your tools with [drains](/doc/observability/drains/), or profile with [Blackfire](/doc/observability/blackfire/) and [New Relic](/doc/observability/new-relic/)
- **Shape your traffic**: add a cache, redirections, or authentication before your application with [Request Flow](/doc/manage/request-flow/), on [your domains](/doc/manage/domain-names/)
- **Connect privately**: link applications, add-ons, and your own machines over WireGuard with [Network Groups](/doc/network/network-groups/)

## A service for each need

Create databases and services next to your applications, operated by Clever Cloud or its partners: linking one to an application passes its credentials and settings through [environment variables](/doc/manage/environment-variables/).

{{< cards >}}
  {{< card link="/developers/doc/deploy/databases" title="Databases" subtitle="PostgreSQL, MySQL, MongoDB, Redis, and Elastic Stack with its Platinum features" icon="circle-stack" >}}
  {{< card link="/developers/doc/deploy/databases/materia-kv" title="Materia KV" subtitle="Serverless key-value database compatible with Redis, replicated across three data centers in Paris" icon="materia" tag="Beta" >}}
  {{< card link="/developers/doc/deploy/pulsar" title="Pulsar" subtitle="Serverless messaging and streaming, with no cluster to manage" icon="simple:apachepulsar" >}}
  {{< card link="/developers/doc/deploy/storage" title="Storage" subtitle="S3-compatible object storage, and persistent file systems" icon="cloud-arrow-up" >}}
  {{< card link="/developers/doc/deploy/services" title="Ready-to-use software" subtitle="Keycloak, Otoroshi, Matomo, Metabase, and MailPace, deployed in one command, ready to connect to your applications" icon="puzzle" >}}
  {{< card link="/developers/doc/deploy/kubernetes" title="Kubernetes" subtitle="A managed cluster, to migrate workloads or run software that needs it" icon="simple:kubernetes" tag="Beta" >}}
{{< /cards >}}

## Automate everything

Clever Cloud is API-first: the Console uses the same public [API](/api/) as your tools. Drive your infrastructure as code with [Clever Tools](/doc/tools/cli/), [Terraform](/doc/tools/terraform/), or your [CI/CD pipelines](/doc/tools/ci-cd/), and let your [AI assistant](/doc/ai-llms/) operate it too.

## Need more?

Clever Cloud also provides, on request, [dedicated load balancers](/doc/network/load-balancers/), [VPN connections](/doc/network/vpn/) to your data centers with WireGuard, IPsec, or OpenVPN, and a [managed GitLab](https://www.clever.cloud/product/gitlab/). Contact the [sales team](mailto:sales@clever-cloud.com) to discuss your needs.

## Explore the documentation

{{< cards >}}
  {{< card link="/developers/doc/deploy" title="Deploy" subtitle="Applications, databases, storage and managed services" icon="rocket-launch" >}}
  {{< card link="/developers/doc/manage" title="Manage applications" subtitle="Settings, environment variables, domains, scaling, and lifecycle" icon="cog-6-tooth" >}}
  {{< card link="/developers/doc/observability" title="Observability" subtitle="Logs, metrics, access logs, drains, and monitoring tools" icon="chart-bar" >}}
  {{< card link="/developers/doc/tools" title="Tools & Integrations" subtitle="Clever Tools, CI/CD, GitHub, GitLab and Terraform" icon="git" >}}
  {{< card link="/developers/doc/develop" title="Develop" subtitle="Best practices, Clever Cloud login, Marketplace, and database migration" icon="code" >}}
  {{< card link="/developers/doc/network" title="Network" subtitle="Private networks, IP ranges and network services" icon="globe-alt" >}}
  {{< card link="/developers/doc/security" title="Security & Compliance" subtitle="Certifications, encryption, TLS and secrets" icon="lock-closed" >}}
  {{< card link="/developers/doc/account-billing" title="Account & Billing" subtitle="Account, organisations, invoices and payments" icon="user-circle" >}}
  {{< card link="/developers/doc/tips-and-tricks" title="Tips & Tricks" subtitle="Shortcuts and lesser-known platform behaviors" icon="light-bulb" >}}
{{< /cards >}}

## Follow a step-by-step guide

{{< cards >}}
  {{< card link="/developers/guides" title="Starter tutorials" subtitle="Create a starter project and deploy it on Clever Cloud" icon="academic-cap" >}}
  {{< card link="/developers/guides/frameworks" title="Frameworks" subtitle="Deploy an application built with Astro, Django, Laravel, Nuxt, Rails, or Symfony" icon="code" >}}
  {{< card link="/developers/guides/self-hosted" title="Self-hosted software" subtitle="Deploy Ghost, Moodle, Outline, or WordPress with the add-ons it needs" icon="cube" >}}
{{< /cards >}}

## Get help and stay informed

{{< cards >}}
  {{< card link="/developers/doc/find-help" title="Find help" subtitle="Contact the support team, read the FAQ, or troubleshoot an issue" icon="support" >}}
  {{< card link="/developers/changelog" title="Changelog" subtitle="New features, runtime updates, and changes of the platform" icon="newspaper" >}}
  {{< card link="https://www.clevercloudstatus.com/" title="Status" subtitle="Follow incidents and scheduled maintenance" icon="chart-pie" >}}
{{< /cards >}}
