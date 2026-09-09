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

Once an application runs, most of your work happens through its configuration rather than its code: environment variables, build hooks, health checks and the tool versions pinned for the build. Around it you can schedule CRON jobs, run one-off tasks, chain middleware in front of your application, or open an SSH session on a running instance.

{{< cards >}}
  {{< card link="/developers/doc/develop/best-practices" title="Best practices" subtitle="What makes an application behave well on the platform" icon="checklist" >}}
  {{< card link="/developers/doc/develop/tasks" title="Clever Tasks" subtitle="Run one-off jobs with single-job scalers" icon="play-circle" >}}
  {{< card link="/developers/doc/develop/common-configuration" title="Configure applications" subtitle="Settings shared by every runtime" icon="cog-6-tooth" >}}
  {{< card link="/developers/doc/develop/cron" title="CRON" subtitle="Schedule recurring jobs on your instances" icon="code-bracket" >}}
  {{< card link="/developers/doc/develop/login-with-clever-cloud" title="Login with Clever Cloud" subtitle="Authenticate your users with their Clever Cloud account" icon="key" >}}
  {{< card link="/developers/doc/develop/common-configuration/environment-variables" title="Environment variables" subtitle="Configure your application and inject its credentials" icon="question-mark-circle" >}}
  {{< card link="/developers/doc/develop/marketplace" title="Marketplace" subtitle="Publish your own service as an add-on" icon="puzzle" >}}
  {{< card link="/developers/doc/develop/mise" title="Mise Package Manager" subtitle="Pin the tool versions your build needs" icon="cube" >}}
  {{< card link="/developers/doc/develop/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
  {{< card link="/developers/doc/develop/ssh-access" title="SSH access" subtitle="Connect to a running instance to debug it" icon="command-line" >}}
{{< /cards >}}
