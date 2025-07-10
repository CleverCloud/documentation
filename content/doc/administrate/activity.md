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

Follow your application activities and lifecycle from the **Activity** option in the application menu. Every time your application redeploys, a new block appears on the timeline. Re-deployment triggers can be either:

 - An action performed by you or by a member of your organisation
 - An action performed by Clever Cloud

 ## Re-deployment triggered by you

This happens when you or a member of your organisation performs an action on the application, like:

- [Restart or rebuild](../apps-management/#start-restart-and-stop) from the Console or [the CLI](../../cli/)
- Push a new commit from Git or GitHub

 Here's what you might see on the timeline:

![Activity timeline](/images/doc/activity.png)

Each block indicates if the deployment was successful or unsuccessful, along with the following information:

- **Date**: when the activity happened and from where (`Console`, `Git`, `Github` or `Monitoring`)
- **Author**: which member of your organisation triggered the activity
- **Commit ID**: on which commit the activity happened
- **Redeploy this commit**: the option to redeploy a previous commit (useful to quickly roll-back if needed)

## Re-deployments triggered by Clever Cloud

Clever Cloud might also trigger re-deployments, either when you're being assisted by the Support, or automatically by the monitoring system. If the monitoring triggers a re-deployment, you'll see no author and the message explaining the reason, like `Monitoring/Unreachable`. The messages you might get are the following:

![Re-deployment triggered by the monitoring](/images/doc/monitoring.png)

- `Unreachable`: The monitoring servers couldn't open a TCP connection with at least one monitoring agent hosted on instances of the application.
- `Timeout`: The monitoring servers has succeed to open TCP connections on all monitoring agents hosted on instances of the application, but at least one did not send its probes in time.
- `Scaling`: Clever Cloud triggers a new deployment with more instances (virtual machines) or more resources of the application as the platform detects that the consumption is greater that the determined threshold on memory or CPU usage. For further details, see [Scalability](../scalability)
- `Maintenance`: Clever Cloud performed a maintenance deployment of the application to integrate new configurations, security patches, operating system updates, runtime updates and so on…
- `DiskFull`: Rarely appears, but you could see this message if you haven't enabled the auto-scalability, after the app crashed and the monitoring restarted it.
