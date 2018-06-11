---
title: Deployment Hooks
shortdesc: Hooks allow to run custom tasks during deployment
tags:
- apps
- hooks
---
## Deployment lifecycle

An application deployed on Clever Cloud goes through two distinct phases. The
`build` phase where dependencies are fetched and the application built, and the
`run` phase where the application is launched. Hooks allow you to run specific
tasks before and after those phases.

The available hooks are:

 - Pre Build
 - Post Build
 - Pre Run
 - On Run Succeeded
 - On Run Failed

## Setting hooks up

Hooks are set up through [environment
variables](https://www.clever-cloud.com/doc/admin-console/environment-variables/).
To set up a Post Build hook, you need to define a `CC_POST_BUILD_HOOK`
variable:

	CC_POST_BUILD_HOOK=echo "it works!"

You can either directly put commands in the hook, but if you have complex
things to do, it's best to put them in a bash script (don't forget to make it
executable!). Hooks have access to environment variables as well as a working
NodeJS installation.

## Can't I use `$BUILD_TOOL`?

Hooks are designed as an escape hatch for steps you can't integrate properly in
your build tool. In many case, you can (and you should) integrate as much as
possible with your build tool, but sometimes it's not possible. Another reason
to use hooks is to integrate Clever Cloud-specific tasks which don't belong in
the project's build configuration.

## Hooks types

### Pre Build (`CC_PRE_BUILD_HOOK`)

This hook is ran before the dependencies are fetched. If it fails, the
deployment fails.

This hook is ran every time.

This hook is perfect for:

 - build tool configuration (eg setting up a `.npmrc` with private tokens)
 - extra dependencies fetching (eg `npm install` for frontend deps)

### Post Build (`CC_POST_BUILD_HOOK`)

This hook is ran after the project is built, and before the cache archive is
generated. If it fails, the deployment fails.

This hook is not ran during deployments from cache.

This hook is perfect for:

 - extra build steps that you want to cache (eg bundling your frontend assets)

### Pre Run (`CC_PRE_RUN_HOOK`)

This hook is ran before the application is started, but after the cache archive
has been generated. If it fails, the deployment fails.

This hook is ran every time.

This hook is perfect for:

 - preparation tasks that need to be ran every time (eg a database migration check)

### Run Succeeded (`CC_RUN_SUCCEEDED_HOOK`) or Failed (`CC_RUN_FAILED_HOOK`)

These hooks are ran once the application has started (or has failed starting).
Their failure doesn't cause the deployment to fail.

One of these hooks is ran every time.

These hooks are perfect for:

 - notifications
 - clean-up

### `hooks.postDeploy` is deprecated

These hooks replace the older `postDeploy` hook, which is now deprecated.
