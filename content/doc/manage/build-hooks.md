---
type: docs
linkTitle: Hooks
title: Deployment Hooks
description: Run your own commands at fixed steps of a deployment on Clever Cloud, before and after the build, before the start, and once the application runs or fails, with environment variables
keywords:
- deployment
- hooks
- build-hooks
- pre-build
- post-build
- pre-run
- automation
- scripts
aliases:
- /clever-cloud-overview/hooks
- /develop/build-hooks/
- /doc/administrate/apps-management/build-hooks
- /doc/administrate/hooks/
- /doc/best-practices/build-hooks
- /doc/build-hooks
- /doc/clever-cloud-overview/hooks
- /doc/common-configuration/build-hooks
- /doc/deploy/build-hooks
- /doc/deploy/develop/build-hooks
- /doc/develop/build-hooks
- /doc/develop/common-configuration/build-hooks
- /doc/develop/common-configuration/deployment-hooks/
- /doc/develop/common-configuration/hooks/
- /doc/develop/hooks/
---

Hooks run your own commands at fixed steps of a deployment: before and after the build, before the start of the application, and once it runs or fails. You set each one in an [environment variable](/doc/manage/environment-variables/) of your application, such as `CC_POST_BUILD_HOOK`.

Use them for the steps your build tool doesn't cover, or that only make sense on Clever Cloud, such as generating a configuration file from your variables. When your build tool can do the job, prefer it: scripts of your `package.json`, a task of your [`mise.toml`](/doc/manage/mise/), or the build command of your runtime keep this logic in your repository, and run the same way on your computer.

## When hooks run

A deployment builds your application, then starts it. The five hooks frame these two steps:

1. `CC_PRE_BUILD_HOOK` runs before your runtime installs the dependencies of your application and builds it
2. `CC_POST_BUILD_HOOK` runs after the build, before Clever Cloud creates the [build cache](/doc/manage/#start-restart-and-stop), so that its result can be part of this cache
3. `CC_PRE_RUN_HOOK` runs before your application starts
4. `CC_RUN_SUCCEEDED_HOOK` runs once your application starts and passes its [health check](/doc/manage/healthcheck/), or `CC_RUN_FAILED_HOOK` if the deployment fails

A pre-build, post-build, or pre-run hook that exits with a code other than `0` stops the deployment, with the error `Error during hook` and the name of the hook. Clever Cloud logs the errors of the two run hooks, but they can't change the outcome of the deployment.

### Deployments from the build cache

Clever Cloud skips the build when it finds a build cache for the commit it deploys: when you restart your application, when [scaling](/doc/manage/scaling/) adds an instance, or when a [dedicated build instance](/doc/manage/#dedicated-build-instance) has built it. The two build hooks then don't run. The pre-run hook and the run hooks still run on each instance, at each start. **Re-build and restart**, or `clever restart --without-cache`, runs a full build again, with its hooks.

On a dedicated build instance, only the pre-build and post-build hooks run: the other hooks run on the instances that start your application.

### Several instances

Each instance runs its own hooks. With several instances, a pre-run hook that changes a shared resource, such as a database migration, runs on each of them. To restrict it to the first instance, test the `INSTANCE_NUMBER` variable, which is `0` on this instance:

```bash
clever env set CC_PRE_RUN_HOOK 'if [ "$INSTANCE_NUMBER" = 0 ]; then bash clevercloud/migrate.sh; fi'
```

Write the test with `if`, not with `&&`: on other instances, `[ "$INSTANCE_NUMBER" = 0 ] && …` exits with `1`, which fails the deployment.

This test doesn't make the migration run only once: a restart or a new deployment runs it again, so make it safe to repeat. The other instances don't wait for it either: if your application needs the new schema to start, migrate before you deploy, for instance from a [Clever Task](/doc/deploy/tasks/). During a [Blue/Green deployment](/doc/manage/#bluegreen-deployment), the previous instances keep serving while the new ones start: a migration must work with both versions of your code.

## Write a hook

Except on [Docker](#docker-applications), the value of a hook is a command, which Bash runs as a login shell, as the `bas` user that runs your application, from the root of your repository. A hook starts from this root even when [`CC_APP_FOLDER`](/doc/manage/environment-variables/reference/) sets a folder of your repository as the root of your application. The command can use shell operators, such as `&&`, `|`, and `;`, and reads the environment variables of your application, those of its [linked add-ons](/doc/manage/service-dependencies/), and those that Clever Cloud sets, such as `APP_ID` or `INSTANCE_NUMBER`:

```bash
clever env set CC_PRE_BUILD_HOOK 'echo "//registry.npmjs.org/:_authToken=${NPM_TOKEN}" > .npmrc'
```

The tools of the [runtime image](/doc/how-it-works/#runtime-images-built-by-clever-cloud) are available, whatever your runtime: a hook of a PHP or Python application can build its front end with Node.js, for instance with `npm ci && npm run build`. A tool that the image doesn't provide can come from your [`mise.toml`](/doc/manage/mise/).

Clever Cloud splits the value of a hook on whitespace before Bash runs it: consecutive spaces become one, even between quotes. For more than a short command, commit a script and run it with `bash` and its path from the root of your repository. Its arguments follow the path:

```bash
clever env set CC_POST_BUILD_HOOK "bash clevercloud/post-build.sh --minify"
```

A script made executable with `chmod +x` before its commit also runs without `bash`, from its path: `clevercloud/post-build.sh --minify`.

Deployment logs show each hook and its command, such as `Running CC_POST_BUILD_HOOK: bash clevercloud/post-build.sh --minify`, then its output. Keep secrets in environment variables, as in the `.npmrc` example, rather than in the value of a hook, and don't print them.

## Pick the right hook

### Pre-build

`CC_PRE_BUILD_HOOK` prepares the build: it configures your build tool, such as a `.npmrc` or `auth.json` file with a token read from a variable, or fetches files that your build needs and your repository doesn't hold. The tools of your `mise.toml` are already installed when it runs. A file that a build hook writes can then come from the build cache: after you change the variable it reads, use **Re-build and restart** to write it again.

### Post-build

`CC_POST_BUILD_HOOK` completes the build with steps you want in the build cache, such as compiling front-end assets. Instances that start from this cache get its result without running the hook again, as long as the hook writes it in a folder that the cache keeps, which [`CC_OVERRIDE_BUILDCACHE` and `CC_IGNORE_FROM_BUILDCACHE`](/doc/manage/environment-variables/#settings-you-can-define-using-environment-variables) can change. [`CC_DISABLE_BUILD_CACHE_UPLOAD`](/doc/manage/environment-variables/reference/) set to `true` skips the creation of a new build cache, but doesn't prevent the use of an existing one: to force a build, use **Re-build and restart**.

> [!NOTE] Keep the build cache with a dedicated build instance
> Don't set `CC_DISABLE_BUILD_CACHE_UPLOAD` with a [dedicated build instance](/doc/manage/#dedicated-build-instance), which `pico` and `nano` instances always use: the instances of your application get the result of the build from the cache that it creates.

### Pre-run

`CC_PRE_RUN_HOOK` runs at each start of each instance, after the build or the download of the build cache. Use it for what depends on the instance or must happen at each start, such as a database migration or a file generated from the current variables. A slow pre-run hook delays each start of an instance, including the ones of a restart or of scaling.

### Run succeeded and run failed

`CC_RUN_SUCCEEDED_HOOK` and `CC_RUN_FAILED_HOOK` report the outcome of a deployment, for instance to a webhook. One of them runs on each instance, at the end of each deployment. For a [Clever Task](/doc/deploy/tasks/), `CC_RUN_SUCCEEDED_HOOK` runs once the task command succeeds. This script posts a message to the URL of the `ALERT_WEBHOOK_URL` variable:

```bash {filename="clevercloud/notify-failure.sh"}
#!/bin/bash
curl -fsS --max-time 10 -X POST "$ALERT_WEBHOOK_URL" \
  -d "Deployment of $APP_ID failed on instance $INSTANCE_NUMBER"
```

```bash
clever env set CC_RUN_FAILED_HOOK "bash clevercloud/notify-failure.sh"
```

The deployment waits for these hooks to end: give a network call a timeout, as `--max-time` does above.

Some failures at the very start of a deployment, while Clever Cloud sets up its instance, don't run `CC_RUN_FAILED_HOOK`: for instance, when an environment variable has an invalid value. To be notified of each deployment without a hook, use [notifications and webhooks](/doc/account-billing/notifications/).

## Build and start commands

Hooks add commands around the build and the start of your application, while two other variables replace these steps:

- `CC_BUILD_COMMAND` sets the build command, on the [Linux](/doc/deploy/applications/linux/) runtime as on the [Static](/doc/deploy/applications/static/) one
- `CC_RUN_COMMAND` replaces the command that starts your application, on most runtimes

`CC_BUILD_COMMAND` runs between the two build hooks, and `CC_RUN_COMMAND` after the pre-run hook. For each of them you don't set, the Linux runtime looks for a `build` or `run` task in your [`mise.toml`](/doc/manage/mise/), then in a Makefile. `CC_RUN_COMMAND` also sets the command of a [Clever Task](/doc/deploy/tasks/).

To serve a web application, the [PHP](/doc/deploy/applications/php/) runtime with Apache starts Apache, and the [Ruby](/doc/deploy/applications/ruby/) runtime starts Puma: they only use `CC_RUN_COMMAND` for a Clever Task. A Docker application starts the command of its image.

## Docker applications

The [Docker runtime](/doc/deploy/applications/docker/) only runs `CC_RUN_SUCCEEDED_HOOK`: your Dockerfile already defines how to build and prepare your image. This hook runs inside your container, with the user and the working directory of your image, and without a shell: Clever Cloud runs its value as a command and its arguments. Quotes, `&&`, or `|` reach the command as plain text. To run several commands, add a script to your image, then set its path:

```bash
clever env set CC_RUN_SUCCEEDED_HOOK /srv/notify.sh
```

A Docker [Clever Task](/doc/deploy/tasks/) can't use this hook: its container has stopped by then, so notify from the task command.
