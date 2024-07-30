---
type: docs
title: Activity
description: Applications activity lifecycle explained
tags:
- lifecycle
keywords:
- activity
- unreachable
- timeout
- diskfull
- scaling
- maintenance
type: docs
---

Follow your application activities and lifecycle from the **Activity** option in the application menu. Every time your application restarts or rebuilds, a new block appears on the timeline. Here's what you might see on the timeline:

![Activity timeline](/images/doc/activity.png)

Each block indicates if the deployment was successful or unsuccessful, along with the following information:

- **Date**: when the activity happened and from where (`Console`, `Git`, `Github` or `Monitoring`)
- **Author**: which member of your organization triggered the activity
- **Commit ID**: on which commit the activity happened
- **Redeploy this commit**: the option to redeploy a previous commit (useful to quickly roll-back if needed)

## Re-deployments triggered by the monitoring

If the monitoring triggers a re-deployment, you'll see no author and the message explaining the reason, like `Monitoring/Unreachable`. The messages you might get are the following:

![Re-deployment triggered by the monitoring](/images/doc/monitoring.png)

- `Unreachable`: The monitoring couldn't open an HTTP connection with the application, assumed it has crashed, and restarted it.
- `Timeout`: Opening the HTTP connection took too long so the monitoring restarted the application in case the application has crashed.
- `Scaling`: The application restarted in a new VM more adjusted to the current consumption. For further details, see [Scalability](../scalability)
- `Maintenance`: Clever Cloud performed a maintenance operation on the VM (language version availability, libraries, etc) and restarted the VM to integrate the new configuration.
- `DiskFull`: Rarely appears, but you could see this message if you haven't enabled the auto-scalability, after the app crashed and the monitoring restarted it.
