---
type: docs
weight: 20
linkTitle: Deploy
title: Deploy
description: Deploy applications, databases, storage and managed services on Clever Cloud
keywords:
- deploy
- applications
- databases
- add-ons
- runtimes
- managed services
aliases:
- /doc/cli/deploy/

---

Push your source, and the platform detects the runtime, installs your dependencies, then starts your application behind a load balancer with TLS configured. Databases, storage and services are add-ons you create alongside it. Several of them run on Materia, the serverless layer Clever Cloud built on FoundationDB: nothing to size or back up, data replicated across three data centers, and access through the protocols you already use.

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications" title="Applications" subtitle="Language runtimes for your code, from Node.js to Rust" icon="rocket-launch" >}}
  {{< card link="/developers/doc/deploy/databases" title="Databases" subtitle="Managed SQL and NoSQL instances, or serverless Materia stores" icon="circle-stack" >}}
  {{< card link="/developers/doc/deploy/functions" title="Functions" subtitle="Serverless execution for anything that compiles to WebAssembly" icon="code-bracket" >}}
  {{< card link="/developers/doc/deploy/kubernetes" title="Kubernetes" subtitle="Managed control plane on Materia etcd, vanilla Kubernetes" icon="kubernetes" >}}
  {{< card link="/developers/doc/deploy/pulsar" title="Pulsar" subtitle="Pub/sub messaging and real-time data streaming" icon="pulsar" >}}
  {{< card link="/developers/doc/deploy/services" title="Services" subtitle="Analytics, BI, identity, email and CI/CD around your code" icon="puzzle" >}}
  {{< card link="/developers/doc/deploy/storage" title="Storage" subtitle="S3-compatible object storage and persistent file systems" icon="cloud-arrow-up" >}}
{{< /cards >}}
