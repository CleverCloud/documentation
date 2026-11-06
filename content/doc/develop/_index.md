---
type: docs
weight: 60
linkTitle: Develop
title: Develop
description: Development guides and best practices for building applications on Clever Cloud including environment variables, build hooks, and deployment strategies
keywords:
- development
- applications
- environment-variables
- build-hooks
- deployment
- best-practices
aliases:
- /develop
---

Around your application, schedule CRON jobs, chain middleware in front of it, follow its logs and metrics, or open an SSH session on a running instance. Its settings, environment variables, and deployment hooks are in [Manage applications](/doc/manage/).

{{< cards >}}
  {{< card link="/developers/doc/develop/best-practices" title="Best practices" subtitle="What makes an application behave well on the platform" icon="checklist" >}}
  {{< card link="/developers/doc/develop/cron" title="CRON" subtitle="Schedule recurring jobs on your instances" icon="code-bracket" >}}
  {{< card link="/developers/doc/develop/login-with-clever-cloud" title="Login with Clever Cloud" subtitle="Authenticate your users with their Clever Cloud account" icon="key" >}}
  {{< card link="/developers/doc/develop/marketplace" title="Marketplace" subtitle="Publish your own service as an add-on" icon="puzzle" >}}
  {{< card link="/developers/doc/develop/database-migration" title="Migrate/Update Database" subtitle="Rebuild a database add-on on an up-to-date virtual machine" icon="circle-stack" >}}
  {{< card link="/developers/doc/develop/mise" title="Mise Package Manager" subtitle="Pin the tool versions your build needs" icon="cube" >}}
  {{< card link="/developers/doc/develop/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
  {{< card link="/developers/doc/develop/ssh-access" title="SSH access" subtitle="Connect to a running instance to debug it" icon="command-line" >}}
{{< /cards >}}
