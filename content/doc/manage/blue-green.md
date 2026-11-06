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
- /doc/develop/best-practices/blue-green
- /doc/best-practices/blue-green
- /doc/develop/best-practices/blue-green-deployments/
- /doc/develop/blue-green
---

Each deployment starts new [immutable instances](/doc/develop/immutable-infrastructure/). With [zero downtime deployment](/doc/manage/#zero-downtime-deployment), it follows a Blue/Green pattern:

1. Clever Cloud builds your code or reuses its build cache, then starts new instances next to the running ones
2. The new instances must pass the [health check](/doc/manage/healthcheck/)
3. The load balancer sends the traffic to the new instances, then the old ones stop

Old and new instances share the same add-ons during the switch: make your database schema changes work with both versions. If the build or the health check fails, the old instances keep the traffic, and the owners of the application get an email by default.

- [Learn more about deployment notifications](/doc/account-billing/notifications/)

## Roll back

To roll back, click **Redeploy this commit** next to a previous deployment in the [activity](/doc/manage/activity/) of your application, or use Clever Tools:

```bash
clever restart --commit COMMIT_ID
```

Replace `COMMIT_ID` with the commit of a successful deployment. This restores your code, not your variables nor your databases.

## Validate a version before production

Passing the health check doesn't prove that every user journey works. Test a new version first on a staging application with its own add-ons. Once it's linked to your repository as `staging`, deploy your `develop` branch to it:

```bash
clever deploy --alias staging --branch develop
```

Review apps create a test application for each pull request, with [GitHub](/doc/tools/github/) or [GitLab](/doc/tools/gitlab/).
