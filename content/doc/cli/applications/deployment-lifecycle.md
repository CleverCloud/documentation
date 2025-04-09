---
type: docs
title: Deploy, Lifecycle
description: Manage your application using the Clever Cloud CLI tool
aliases:
- /developers/doc/clever-tools/ssh-access
- /developers/doc/cli/lifecycle
- /developers/doc/cli/manage
- /developers/doc/cli/ssh-access
- /doc/administrate/clever-tools/lifecycle
- /doc/administrate/clever-tools/manage
- /doc/administrate/clever-tools/ssh-access
- /doc/clever-tools/lifecycle
- /doc/clever-tools/ssh-access
- /doc/cli/manage
- /doc/cli/ssh-access
---

A Clever Cloud application can easily be deployed and accessed once created, through following commands. Most can target a specific application, adding `--app APP_ID_OR_NAME` or a local alias (`--alias`, `-a`).

## deploy

Once changes are committed in your local git repository, you can deploy it:

```
clever deploy
```

It will `git push` your code on the remote repository of your application on Clever Cloud automatically. You can, of course, use option to `force push` or use specific local branch for example:

```
[--branch, -b] BRANCH                 Branch to push (current branch by default) (default: )
[--tag, -t] TAG                       Tag to push (none by default) (default: )
[--quiet, -q]                         Don't show logs during deployment (default: false)
[--force, -f]                         Force deploy even if it's not fast-forwardable (default: false)
[--follow]                            Continue to follow logs after deployment has ended (default: false)
[--same-commit-policy, -p] POLICY     What to do when local and remote commit are identical (error, ignore, restart, rebuild) (default: error)
[--exit-on, -e] STEP                  Step at which the logs streaming is ended, steps are: deploy-start, deploy-end, never (default: deploy-end)
```

> [!TIP]
> You can cancel a deployment with `clever cancel-deploy` command. You can also [configure an application](/developers/doc/cli/applications/configuration/#config) so that a new deployment cancels the current one.

## console | open

Once deployed, you can open the application on your default browser or [Clever Cloud Console](https://console.clever-cloud.com):

```
clever open
clever console
```

## status

To get application state, options or running/scaling status, use:

```
clever status
clever status --format json
```

## restart

Once deployed, an application can be restarted:

```
clever restart
```

By default, it will use its build cache when available. But you can override it or use other available options:

```
[--commit] COMMIT ID       Restart the application with a specific commit ID
[--without-cache]          Restart the application without using cache (default: false)
[--quiet, -q]              Don't show logs during deployment (default: false)
[--follow]                 Continue to follow logs after deployment has ended (default: false)
[--exit-on, -e] STEP       Step at which the logs streaming is ended, steps are: deploy-start, deploy-end, never (default: deploy-end)
```

## stop | cancel-deploy

To stop an application or cancel any ongoing deployment, use:

```
clever stop
clever cancel-deploy
```

## ssh

A Clever Cloud application is a running virtual machine you can ssh to, as a user (`bas`). By default, it will use `OpenSSH` configuration, but you can target a specific identity file:

```
clever ssh [--identity-file, -i] IDENTITY-FILE
```

To ssh a specific application, use:

```
clever ssh --app APP_ID_OR_NAME
```

## activity

To get deployment activity, use:

```
clever activity
```

By default, it will show you last 10 deployments. You can show all or listen to a stream of incoming deployments through options:

```
[--follow, -f]             Track new deployments in activity list (default: false)
[--show-all]               Show all activity (default: false)
[--format, -F] FORMAT      Output format (human, json, json-stream)
```
