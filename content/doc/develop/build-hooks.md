---
type: docs
title: Deployment Hooks
shortdesc: Hooks allow to run custom tasks during deployment
tags:
- develop
keywords:
- apps
- hooks
type: docs
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
variables]({{< ref "doc/develop/env-variables.md" >}}).
To set up a Post Build hook, you need to define a `CC_POST_BUILD_HOOK`
variable:

```shell
CC_POST_BUILD_HOOK=echo "it works!"
```

You can directly put commands in the hook. Hooks have access to the environnement variables as well as a working Node.js installation.

If you have complex things to do, the best way is to put the logic in a bash script *(dont forget to make it executable!)*
To use it, set the hook you want to trigger to the path of your script, relative to the root path of your repository.
E.g. if your script is in a clevercloud folder at the root of your project then you can define `CC_POST_BUILD_HOOK=./clevercloud/script.sh`

## Can't I use $BUILD_TOOL?

Hooks are designed as an escape hatch for steps you can't integrate properly in
your build tool. In many case, you can (and you should) integrate as much as
possible with your build tool, but sometimes it's not possible. Another reason
to use hooks is to integrate Clever Cloud-specific tasks which don't belong in
the project's build configuration.

## Exceptions

Some application types do not have hooks support or only some of them.

### Docker

For Docker, because you can do pretty much anything yourself inside your Dockerfile, only the following hooks are available:

- `CC_RUN_SUCCEEDED_HOOK`

If you need support for other hooks, please reach out to our support and explain your use case.

## Hooks types

### Pre Build

**By using `CC_PRE_BUILD_HOOK`**.

This hook is ran before the dependencies are fetched. If it fails, the
deployment fails.

This hook is ran every time.

This hook is perfect for:

- build tool configuration (eg setting up a `.npmrc` with private tokens)
- extra dependencies fetching (eg `npm install` for frontend deps)

### Post Build

**By using `CC_POST_BUILD_HOOK`.**

This hook is ran after the project is built, and before the cache archive is
generated. If it fails, the deployment fails.

This hook is not ran during deployments from cache.

This hook is perfect for:

- extra build steps that you want to cache (eg bundling your frontend assets)

{{< callout type="info" >}}
  If you set [`CC_DISABLE_BUILD_CACHE_UPLOAD`]({{< ref "/doc/develop/env-variables/#settings-you-can-define-using-environment-variables" >}}) environment variable to `true`, the cache archive won't be created nor uploaded.
{{< /callout >}}

### Pre Run

**By using `CC_PRE_RUN_HOOK`.**

This hook is ran before the application is started, but after the cache archive
has been generated. If it fails, the deployment fails.

This hook is ran every time.

This hook is perfect for:

- preparation tasks that need to be ran every time (eg a database migration check)

### Run Success/Fail

**By using `CC_RUN_SUCCEEDED_HOOK` or `CC_RUN_FAILED_HOOK`.**

These hooks are ran once the application has started (or has failed starting).
Their failure doesn't cause the deployment to fail.

One of these hooks is ran every time.

These hooks are perfect for:

- notifications
- clean-up

{{< callout emoji="🧹" >}}
**This hook is deprecated**  
These hooks replace the older `postDeploy` hook, which is now deprecated.
{{< /callout >}}
