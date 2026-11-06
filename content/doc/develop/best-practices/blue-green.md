---
type: docs
linkTitle: Blue/Green Deployments
title: Blue/Green Deployments
description: How each Clever Cloud deployment switches traffic to new instances, and how to run a new version in a second application before moving your domain to it
keywords:
- blue-green
- deployment
- zero downtime
- rollback
- domain switch
- environments
aliases:
- /doc/best-practices/blue-green
- /doc/develop/best-practices/blue-green-deployments/
- /doc/develop/blue-green
---

A Blue/Green deployment runs two versions of an application side by side: the current one, *blue*, keeps the traffic while the new one, *green*, starts. Traffic moves to *green* once it works, and *blue* remains available to roll back.

## Each deployment on Clever Cloud

With [zero downtime deployment](/doc/develop/common-configuration/#zero-downtime-deployment), enabled by default, each deployment follows this pattern on new [immutable instances](/doc/develop/best-practices/immutable-infrastructure/):

1. Clever Cloud builds your code and starts new instances, next to the running ones
2. The new instances must pass the [health check](/doc/develop/common-configuration/healthcheck/)
3. The load balancer sends the traffic to the new instances, then the old ones stop

If the build or the health check fails, the old instances keep the traffic, and the owners of the application get an email by default. To roll back after a successful deployment, redeploy a previous commit from the [activity](/doc/develop/observability/activity/) of your application, or with Clever Tools:

```bash
clever restart --commit COMMIT_ID
```

Replace `COMMIT_ID` with the commit of a successful deployment. This restores your code, not your variables nor your databases.

- [Learn more about deployment notifications](/doc/account-billing/notifications/)

## Blue/Green with two applications

A second application lets you test the new version before production traffic reaches it, and keeps the old one running to roll back without rebuilding. Here, `myapp-blue` is a Node.js application in `par`, and you run the commands from its Git repository.

Create the second application in the same region, to keep your DNS records valid. Clever Tools links it to the repository as `green`:

```bash
clever create --type node myapp-green --region par --alias green
```

With `jq`, copy the environment variables you set on the first application, without those of its add-ons, then link the same add-ons:

```bash
clever env --app myapp-blue --format json | jq '.env' | clever env import --json --app myapp-green
clever service link-addon my-database --app myapp-green
```

They don't copy the other settings, such as [scaling](/doc/develop/common-configuration/scaling/), [application settings](/doc/develop/common-configuration/#application-settings), or links to other applications: set them too.

Once it starts, the second application runs its own [CRON jobs](/doc/develop/cron/) and [workers](/doc/develop/common-configuration/workers/), on the same add-ons as the first one. Keep your database schema compatible with both versions, and make sure that tasks which mustn't run twice don't run on both applications.

Deploy the new version to the second application, and test it on its `cleverapps.io` domain:

```bash
clever deploy --alias green
```

Then move your domain. Between the two commands, the domain has no route, so run them one after the other:

```bash
clever domain rm example.com --app myapp-blue
clever domain add example.com --app myapp-green
```

The same domain and path can only point to one application at a time. To roll back, move the domain back to the first application. Once you no longer need it, stop it with `clever stop --app myapp-blue`.

- [Learn more about domain names](/doc/develop/common-configuration/domain-names/)
- [Learn more about service dependencies](/doc/manage/service-dependencies/)
