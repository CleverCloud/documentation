---
type: docs
linkTitle: Blue/Green Deployment
title: Blue/Green Deployment
description: How each Clever Cloud deployment switches traffic to new instances, how to roll back, and how to validate a version before production
keywords:
- blue-green
- deployment
- zero downtime
- rollback
- staging
- environments
aliases:
- /doc/best-practices/blue-green
- /doc/develop/best-practices/blue-green-deployments/
- /doc/develop/blue-green
---

A Blue/Green deployment starts the new version, *green*, next to the current one, *blue*, then moves the traffic to *green* once it works.

## Each deployment on Clever Cloud

With [zero downtime deployment](/doc/manage/#zero-downtime-deployment), enabled by default, each deployment follows this pattern on new [immutable instances](/doc/develop/best-practices/immutable-infrastructure/):

1. Clever Cloud builds your code and starts new instances, next to the running ones
2. The new instances must pass the [health check](/doc/manage/healthcheck/)
3. The load balancer sends the traffic to the new instances, then the old ones stop

Old and new instances share the same add-ons during the switch: make your database schema changes work with both versions.

If the build or the health check fails, the old instances keep the traffic, and the owners of the application get an email by default. To roll back after a successful deployment, redeploy a previous commit from the [activity](/doc/develop/observability/activity/) of your application, or with Clever Tools:

```bash
clever restart --commit COMMIT_ID
```

Replace `COMMIT_ID` with the commit of a successful deployment. This restores your code, not your variables nor your databases.

- [Learn more about deployment notifications](/doc/account-billing/notifications/)

## Validate a version before production

Passing the health check doesn't prove that every user journey works. Test a new version first on a staging application with its own add-ons. Once it's linked to your repository as `staging`, deploy your `develop` branch to it:

```bash
clever deploy --alias staging --branch develop
```

Review apps create a test application for each pull request, with [GitHub](/doc/tools/github/) or [GitLab](/doc/tools/gitlab/).
