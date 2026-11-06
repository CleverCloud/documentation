---
type: docs
linkTitle: Lifecycle
title: Application lifecycle
description: Manage your applications on Clever Cloud including deployment configuration, scaling settings, and operational controls
keywords:
- application management
- deployment configuration
- app lifecycle
- scaling settings
- operational controls
- zero downtime deployment
aliases:
- /doc/develop/common-configuration/lifecycle
- /administrate/apps-management
- /doc/admin-console/apps-management
- /doc/administrate/apps-management
- /doc/common-configuration/lifecycle
- /admin-console/apps-management
- /doc/develop/build-instances
- /doc/develop/deployment-lifecycle
---

## Start, restart, and stop

The **Overview** menu of your application in the [Console](https://console.clever-cloud.com) holds its lifecycle actions:

- **Restart**: deploys the current commit of your application again, with its build cache when available
- **Restart last pushed commit**: deploys the last commit you pushed, rather than one you redeployed to roll back
- **Re-build and restart**: deploys the current commit again, without the build cache
- **Stop app**: stops the instances of your application, and their billing

Once your application is stopped, **Start**, **Start last pushed commit**, and **Re-build and start** do the same. With Clever Tools:

```bash
clever restart
clever restart --without-cache
clever stop
```

[`CC_DISABLE_BUILD_CACHE_UPLOAD`](/doc/manage/environment-variables/reference/) set to `true` skips creating the build cache. To force a build, use **Re-build and restart**.

## Archive and delete

In the **Information** menu, **Archive** hides your application from your list: it keeps running, and stays deployable. **Un-archive** brings it back.

**Remove this application**, at the bottom of this menu, deletes it once you type its name. With Clever Tools, run `clever delete`.
