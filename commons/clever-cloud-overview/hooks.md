---
title: Hooks
shortdesc: Hooks allow to run custom tasks during deployment
tags:
- apps
- hooks
---

# Hooks

<div class="panel panel-warning">
  <div class="panel-heading">
     <h4>Hooks are not available everywhere yet</h4>
  </div>
  <div class="panel-body">
    Hooks are currently only available for Erlang, Haskell, Java, NodeJS, PHP and Rust
    applications. In the meantime, you can continue to use the postDeploy on
    the other runtimes.
  </div>
</div>

## Deployment lifecycle

An application deployed on Clever Cloud goes through two distinct phases. The
`build` phase where dependencies are fetched and the application built, and the
`run` phase where the application is launched. Hooks allow you to run specific
tasks before and after those phases.

The available hooks are:

 - `PRE_BUILD`
 - `POST_BUILD`
 - `PRE_RUN`
 - `RUN_SUCCEEDED`
 - `RUN_FAILED`

## Setting hooks up

Hooks are set up through [environment
variables](https://www.clever-cloud.com/doc/admin-console/environment-variables/).
To set up a `POST_BUILD` hook, you need to define a `CC_POST_BUILD_HOOK`
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

### `PRE_BUILD`

This hook is ran before the dependencies are fetched. If it fails, the
deployment fails.

This hook is ran every time.

This hook is perfect for:

 - build tool configuration (eg setting up a `.npmrc` with private tokens)
 - extra dependencies fetching (eg `npm install` for frontend deps)

### `POST_BUILD`

This hook is ran after the project is built, and before the cache archive is
generated. If it fails, the deployment fails.

This hook is not ran during deployments from cache.

This hook is perfect for:

 - extra build steps that you want to cache (eg bundling your frontend assets)

### `PRE_RUN`

This hook is ran before the application is started, but after the cache archive
has been generated. If it fails, the deployment fails.

This hook is ran every time.

This hook is perfect for:

 - preparation tasks that need to be ran every time (eg a database migration check)

### `RUN_SUCCEEDED` and `RUN_FAILED`

These hooks are ran once the application has started (or has failed starting).
Their failure doesn't cause the deployment to fail.

One of these hooks is ran every time.

These hooks are perfect for:

 - notifications
 - clean-up

### `hooks.postDeploy` is deprecated

These hooks replace the older `postDeploy` hook, which is now deprecated.
