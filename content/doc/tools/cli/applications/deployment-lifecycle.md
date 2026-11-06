---
type: docs
linkTitle: Deploy, Lifecycle
title: Deploy, Lifecycle
description: Manage application deployment lifecycle using Clever Cloud CLI tools including builds, deployments, rollbacks, and scaling operations
keywords:
- deployment
- lifecycle
- cli
- builds
- rollbacks
- scaling
aliases:
- /doc/manage/cli/applications/deployment-lifecycle
- /doc/administrate/clever-tools/lifecycle
- /doc/administrate/clever-tools/manage
- /doc/administrate/clever-tools/ssh-access
- /doc/clever-tools/lifecycle
- /doc/clever-tools/ssh-access
- /doc/cli/applications/deployment-lifecycle
- /doc/cli/commands/restart
- /doc/cli/lifecycle
- /doc/cli/manage
- /doc/cli/ssh-access
---

A Clever Cloud application can easily be deployed and accessed once created, through following commands. Most can target a specific application, adding `--app APP_ID_OR_NAME` or a local alias (`--alias`, `-a`).

## deploy

Once changes are committed in your local git repository, you can deploy it:

```console
clever deploy
```

It will `git push` your code on the remote repository of your application on Clever Cloud automatically. You can, of course, use option to `force push` or use specific local branch for example:

```text
[--branch, -b] BRANCH                 Branch to push (current branch by default) (default: )
[--tag, -t] TAG                       Tag to push (none by default) (default: )
[--quiet, -q]                         Don't show logs during deployment (default: false)
[--force, -f]                         Force deploy even if it's not fast-forwardable (default: false)
[--same-commit-policy, -p] POLICY     What to do when local and remote commit are identical (error, ignore, restart, rebuild) (default: error)
[--exit-on, -e] STEP                  Step at which the logs streaming is ended, steps are: deploy-start, deploy-end, never (default: deploy-end)
```

> [!TIP]
> You can cancel a deployment with `clever cancel-deploy` command. You can also [configure an application](/doc/tools/cli/applications/configuration/#config) so that a new deployment cancels the current one.

Since Clever Tools 5.0.0, `clever deploy` uses the `git` command installed on your system, which must be available in your `PATH`. If `git` isn't available, or if you experience an issue with this backend, fall back to the previous pure JavaScript implementation. It works without `git` installed on your system, but it only supports HTTP, slows down on repositories with rewritten history, can time out on large repositories or big files, and can't deploy from a linked Git worktree:

```console
clever features disable system-git
```

To switch back to the system Git backend, use `clever features enable system-git`.

## console | open

Once deployed, you can open the application on your default browser or [Clever Cloud Console](https://console.clever-cloud.com):

```console
clever open
clever console
```

## status

To get application state, options or running/scaling status, use:

```console
clever status
clever status --format json
```

## restart

Once deployed, an application can be restarted:

```console
clever restart
```

By default, it will use its build cache when available. But you can override it or use other available options:

```text
[--commit] COMMIT ID       Restart the application with a specific commit ID
[--without-cache]          Restart the application without using cache (default: false)
[--quiet, -q]              Don't show logs during deployment (default: false)
[--exit-on, -e] STEP       Step at which the logs streaming is ended, steps are: deploy-start, deploy-end, never (default: deploy-end)
```

## stop | cancel-deploy

To stop an application or cancel any ongoing deployment, use:

```console
clever stop
clever cancel-deploy
```

## ssh

Use SSH to inspect a running instance or execute a command:

```console
clever ssh
clever ssh --app my-api --instance any -c hostname
```

The [SSH access guide](/doc/manage/ssh-access/) covers prerequisites, identity files, instance selection, remote commands, and troubleshooting.

`clever instances` lists the running instances of your application, including build instances. Add `--all` to include instances in any state. The `--since`, `--until`, and `--deployment-id` filters also include past instances:

```console
clever instances --all
clever instances --since 1d --format json
```

The command returns the 100 most recent matches by default. Use `--limit` to request up to 1,000.

## logs

When you deploy an application on Clever Cloud, we collect its logs, hosted in our internal Pulsar stack, all included. To listen to the stream, use:

```console
clever logs
```

You can also get logs from a specific timeline, deployment or add-on through options:

```text
[--before, --until] BEFORE          Fetch logs before this date/time (ISO8601 date, positive number in seconds, duration, e.g.: 1h, or now)
[--after, --since] AFTER            Fetch logs after this date/time (ISO8601 date, positive number in seconds, duration, e.g.: 1h, or now)
[--search] SEARCH                   Fetch logs matching this pattern
[--deployment-id] DEPLOYMENT_ID     Fetch logs for a given deployment
[--addon] ADDON_ID                  Add-on ID or real ID
[--format, -F] FORMAT               Output format (human, json, json-stream) (default: human)
```

By default, logs keep streaming. Use `--until` to set an end time. To read the last 15 minutes and exit, use:

```console
clever logs --since 15m --until now
```

## access logs

When you deploy an application on Clever Cloud, we collect its access logs, hosted in our internal Pulsar stack, all included. To listen to the stream, use:

```console
clever accesslogs
```

You can also get access logs from a specific timeline through options, in multiple formats:

```text
[--before, --until] BEFORE     Fetch logs before this date/time (ISO8601 date, positive number in seconds, duration, e.g.: 1h, or now)
[--after, --since] AFTER       Fetch logs after this date/time (ISO8601 date, positive number in seconds, duration, e.g.: 1h, or now)
[--format, -F] FORMAT          Output format (human, json, json-stream, clf) (default: human)
```

Besides HTTP requests, access logs include TCP redirections and SSH connections to your instances. In the `human` format, a column shows the transport of each line, `HTTP`, `TCP` or `SSH`, and HTTP methods and paths get their own columns so they stay aligned. The `clf` format, for Common Log Format, only outputs HTTP access logs.

You can for example follow access logs in JSON stream format, starting from the last hour, with:

```console
clever accesslogs --format json-stream --since 1h
clever accesslogs -F json-stream | jq '.source.ip'
```

or JSON if you add a date/time end limit:

```console
clever accesslogs --app APP_NAME --since 2025-04-21T13:37:42 --until 1d -F json | jq '[.[] | {date, countryCode: .source.countryCode, ip: .source.ip, port: .source.port}]'
clever accesslogs --app APP_NAME --since 2025-04-21T13:37:42 --until 1d -F json | jq '.[] | [.date, .source.countryCode, .source.ip, .source.port] | @sh'
```

> [!TIP]
> `jq` offers multiple table formatting options, like `@csv`, `@tsv`, `@json`, `@html`, `@uri`, `@base64`, etc.

## activity

To get deployment activity, use:

```console
clever activity
```

By default, it will show you last 10 deployments. You can show all or listen to a stream of incoming deployments through options:

```text
[--follow, -f]             Track new deployments in activity list (default: false)
[--show-all]               Show all activity (default: false)
[--format, -F] FORMAT      Output format (human, json, json-stream)
```
