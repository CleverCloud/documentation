---
title: Astro
description: Build your website with the Astro Static Site Generator (SSG) and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- astro
- nodejs
- static
- ssg
- html
- js
- css
- website
type: "docs"
comments: false
draft: false
---

{{< hextra/hero-subtitle >}}
  Astro is an all-in-one web framework for building content-driven websites, that pioneers a new frontend architecture to reduce JavaScript overhead and complexity. Learn in this guide how to deploy an Astro site on Clever Cloud.
{{< /hextra/hero-subtitle >}}

## Overview

Clever Cloud supports deploying both [fully static and on-demand rendered](https://docs.astro.build/en/basics/rendering-modes/) Astro projects:
- The `static` output mode is ideal for most content-oriented website, for which you have no need for per-visitor server-side customisation. Consider using a [Static runtime](/developers/doc/applications/static/) when using this output mode, with the site generation in a post-build hook.
-  The `server` or `hybrid` output modes: consider using a [Node.js runtime](/developers/doc/applications/nodejs) runtime with [Astro’s Node adapter](https://docs.astro.build/en/guides/integrations-guide/node/)

If you need an example source code, get [Astrowind](https://github.com/onwidget/astrowind) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):
```bash
git clone https://github.com/onwidget/astrowind myStaticApp
```

## Deploy a static Astro site

To deploy your Astro project to Clever Cloud, you need to **create a new application**.

{{% steps %}}

### Create the application

In this step, you set up the following parameters:

- Deployment (using Git or GitHub)
- Application : Node.js or Static (both can serve a static site)
- Instance size and scalability options : You can usually deploy an Astro site using the **Nano** instance
- Region
- Dependencies, if needed

### Inject environment variables

Use environment variables to control the deployment behavior, which depends on the type of application and your package manager. Find right below the ones that apply for your application.

{{% /steps %}}

#### Node.js application environment variables

If you're using a **Node.js** application to serve a static Astro site, inject the following environment variables:

{{< tabs items="npm,pnpm,yarn" >}}
  {{< tab >}}

  ```shell
    CC_POST_BUILD_HOOK="npm run build"
    ```

  {{< /tab >}}

  {{< tab >}}

  ```shell
    CC_NODE_BUILD_TOOL="custom"
    CC_PRE_BUILD_HOOK="npm install -g pnpm && pnpm install"
    CC_CUSTOM_BUILD_TOOL="pnpm run astro telemetry disable && pnpm build"
    CC_RUN_COMMAND="pnpm run preview"
    ```

  {{< /tab >}}

  {{< tab >}}

  ```shell
    CC_NODE_BUILD_TOOL="yarn"
    CC_PRE_BUILD_HOOK="yarn && yarn run astro telemetry disable && yarn build"
    CC_RUN_COMMAND="yarn run preview"
    ```

  {{< /tab >}}

{{< /tabs >}}

#### Static application

If you're using a **Static** application to serve a static Astro site, inject the following environment variables:

{{< tabs items="npm,pnpm,yarn" >}}

  {{< tab >}}

  ```shell
    CC_POST_BUILD_HOOK="npm run build"
    CC_PRE_BUILD_HOOK="npm install && npm run astro telemetry disable"
    CC_WEBROOT="/dist"
  ```

  {{< /tab >}}

  {{< tab >}}

  ```shell
    CC_POST_BUILD_HOOK="pnpm build"
    CC_PRE_BUILD_HOOK="npm install -g pnpm && pnpm install && pnpm run astro telemetry disable"
    CC_WEBROOT="/dist"
  ```

  {{< /tab >}}

  {{< tab >}}

  ```shell
    CC_POST_BUILD_HOOK="yarn build"
    CC_PRE_BUILD_HOOK="yarn && yarn run astro telemetry disable"
    CC_WEBROOT="/dist"
  ```

  {{< /tab >}}

{{< /tabs >}}

### Deploy

If you're deploying from **GitHub**, your deployment should start automatically. If you're using **Git**, copy the remote and push on the **master** branch.

{{< callout emoji="💡" >}}
  To deploy from branches other than `master`, use `git push clever <branch>:master`. For example, if you want to deploy your local `main` branch without renaming it, use `git push clever main:master`.
{{< /callout >}}

## Deploy a static Astro site using the CLI

{{< content "language-specific-deploy/create-static" >}}

## Configure environment variables

Next, configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. Clever Cloud uses standard configurations, so you only need to define a few variables:

```bash
clever scale --build-flavor M
clever scale --flavor nano

clever env set CC_NODE_VERSION "20"
clever env set CC_WEBROOT "/dist"
clever env set CC_OVERRIDE_BUILDCACHE "/dist"
clever env set CC_PRE_BUILD_HOOK "npm install && npm run astro telemetry disable"
clever env set CC_POST_BUILD_HOOK "npm run build"
```

{{< content "git-push" >}}

## Deploying an Astro Project with Server-Side Rendering (SSR)

To deploy an Astro SSR project, consider using a **Node.js** application on Clever Cloud. This is especially useful if your project uses the [Node.js adapter](https://docs.astro.build/en/guides/integrations-guide/node/).

### Port and host

For SSR deployments, ensure to configure your application to listen on port **8080** as required by Clever Cloud. This differs from static deployments where such configurations are typically unnecessary.

Set your port and host in your `astro dev` script for development mode, and/or configure it directly for production:

{{< tabs items="development,production" >}}

  {{< tab >}}

  To quickly deploy on development mode:

   ```json {filename="package.json"}
    "scripts": {
      "dev": "astro dev",
      "start": "astro dev",
      "build": "astro check && astro build",
      "preview": "astro preview --host 0.0.0.0 --port 8080",
      "astro": "astro"
    }
    ```

  {{< /tab >}}

  {{< tab >}}

  When deploying for production:

   ```javascript {filename="astro.config.mjs"}
    import { defineConfig } from 'astro/config';

    export default defineConfig({
      server: {
        port: 8080,
        host: true
      }
    });
    ```
  ```json {filename="package.json"}
    "scripts": {
      "dev": "astro dev",
      "start": "astro build && node ./dist/server/entry.mjs",
      "build": "astro check && astro build",
      "preview": "astro preview --host 0.0.0.0 --port 8080",
      "astro": "astro"
    }
    ```

  {{< /tab >}}


{{< /tabs >}}



## Learn more

{{< cards >}}
  {{< card link="../../doc/applications/nodejs" title="Deploy a Node.js application" subtitle="Learn more on deploying a Node.js application on Clever Cloud" icon="node" >}}
  {{< card link="../../doc/applications/static" title="Deploy a Static application" subtitle="Learn more on deploying a Static application on Clever Cloud" icon="feather" >}}
  {{< card link="https://docs.astro.build/" title="Learn Astro" subtitle="Astro full documentation" icon="rocket-launch" >}}

{{< /cards >}}
