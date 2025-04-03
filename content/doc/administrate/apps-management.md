---
type: docs
title: Application Management
position: 7
shortdesc: Starting, restarting, stopping your applications
tags:
- dashboard-setup
keywords:
- stop
- deploy
- restart
- logs
type: docs
aliases:
- /developers/doc/admin-console/apps-management
- /doc/admin-console/apps-management
---

## Start, restart and stop

You can start, restart, and stop your application in the **Overview** menu of your application in the Clever Cloud console.

- **Start**: will restart a stopped application. This will not trigger a rebuild phase as it will use the build cache.
- **Re-build and restart**: Same as start but with a build phase and without using using the build cache.
- **Restart last pushed commit**: will start last commit on the tree even if you reverted deployments to a previous commit.
- **Stop**: will stop currently running instances of your application.

Stop functionality is useful during the development of the application to limit its credit consumption.

{{< imgproc link="/" caption="Manage your application from the Console" image="/images/app-management.png" method="resize" options="900x q80 webp">}}


{{< callout type="info" >}}
  If you set [`CC_DISABLE_BUILD_CACHE_UPLOAD`](../../develop/env-variables/#settings-you-can-define-using-environment-variables) environment variable to `true`, the cache archive won't be created nor uploaded.
{{< /callout >}}

## Deploy an old commit

If you want to revert to a previous version of your code, you can go to the **Activity** menu of your application in the Clever Cloud console. You will find here all your previous commits. Just select **redeploy this commit** on the desired one. This will trigger a redeploy of your application at this version.

## Edit application configuration

You can edit your application in the **Information** menu of your application in the Clever Cloud console. You can rename it, change description and deployment zone.
You can also enable/disable:

- **Zero downtime deployment**: During a deployment, old scalers are kept up until the new instances work. Updates are thus transparent to the user. Your application has to work correctly with several scalers in parallel (e.g. for connections to databases). *`pico` and `nano` scalers are using this feature by default.*
- **Sticky sessions**: When horizontal scalability is enabled, a user is always served by the same scaler. Some frameworks or technologies require this option.
- **Dedicated build instance**: Your application will build on a dedicated machine allowing you to use a small scaler to run your application. But, using this option will make your deployment slower (by ~10 seconds)
- **Cancel ongoing deployment on new push**: A "git push" will cancel any ongoing deployment and start a new one with the last available commit.
- **Force HTTPS**: Any non secured HTTP request to this application will be redirected to HTTPS with a 301 Moved Permanently status code.

Do not forget to save after editing your configuration.

![Edit your application](/images/doc/application-edit.png)

## Archiving/Unarchiving your application

You can perform this operation in the **Overview** menu of your application in the Clever Cloud console. You will find an **archive** button. This will remove it from your application's list, but you will stil be able to access your application and push to its git remote.
If you want to unarchieve your application simply click the **un-archive** button where the **archive** button was.

## Deleting your application

You can perform this operation in the **Information** menu of your application in the Clever Cloud console. You will find a red **remove this application** button at the bottom. This will open a modal where you should type the name of your application. Click **remove** to finish the process. Your application will be deleted and no longer accessible.
