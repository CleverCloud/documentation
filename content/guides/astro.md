---
type: docs
title: Astro
description: Deploy Astro as Static Site Generator (SSG) or with Node.js on Clever Cloud with step-by-step tutorial and configuration guide
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
aliases:
- /doc/astro
- /astro
comments: false
---

{{< hextra/hero-subtitle >}}
  Astro is an all-in-one web framework for building content-driven websites, that pioneers a new frontend architecture to reduce JavaScript overhead and complexity. Learn in this guide how to deploy an Astro site on Clever Cloud.
{{< /hextra/hero-subtitle >}}

## Overview

Clever Cloud supports deploying both [fully static and on-demand rendered](https://docs.astro.build/en/basics/rendering-modes/) Astro projects:
- The `static` output mode is ideal for most content-oriented website, for which you have no need for per-visitor server-side customization. Consider using a [Static runtime](/developers/doc/applications/static/) when using this output mode, with the automatic site generation.
-  The `server` or `hybrid` output modes: consider using a [Node.js runtime](/developers/doc/applications/nodejs) with [Astro’s Node adapter](https://docs.astro.build/en/guides/integrations-guide/node/)

If you need an example source code, get [Astrowind](https://github.com/onwidget/astrowind) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):
```bash
git clone https://github.com/onwidget/astrowind myStaticApp
```
To deploy your Astro project to Clever Cloud, you need to **create a new application**.

{{% steps %}}

### Deployment

- Source: Git or GitHub

### Application

- Type: Static
- Instance size: you can usually deploy an Astro site using the `pico` instance
- Scalability options: if you need a bigger build instance, multiple instances, etc.

### Options

- Region
- Dependencies, if needed

{{% /steps %}}

If you're deploying from **GitHub**, your deployment should start automatically. If you're using **Git**, copy the remote and push on the **master** branch.

{{< callout emoji="💡" >}}
  To deploy from branches other than `master`, use `git push clever <branch>:master`. For example, if you want to deploy your local `main` branch without renaming it, use `git push clever main:master`.
{{< /callout >}}

{{% content "static-create" %}}

### Automatic build

Astro is one of the many Static Site Generator (SSG) that [Clever Cloud automatic build](/developers/doc/applications/static/#static-site-generators-ssg-auto-build) supports in the `static` runtime, you don't have anything special to manage. To use a pico instance with a dedicated build instance change it in the [Console](https://console.clever-cloud.com) or with Clever Tools:

```bash
clever scale --flavor pico

# To select a bigger build instance, use:
clever scale --build-flavor M
```

{{% content "static-deploy" %}}

## Deploying a Node.js application with Server-Side Rendering

To deploy an Astro project with Server-Side Rendering (SSR), use a **Node.js** application on Clever Cloud and the [Node.js adapter](https://docs.astro.build/en/guides/integrations-guide/node/).

### Inject environment variables

Depending on your package manager, use the following environment variables:

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

> [!TIP]
> You can also use `package.json` scripts [to define commands to run](/developers/doc/applications/nodejs/#about-packagejson  ) during the build and start phases.

### Port and host

As you manage the server, ensure to configure your application to listen on port **8080** as required by Clever Cloud. Set your port and host in your `astro dev` script for development mode, and/or configure it directly for production:

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
  {{< card link="/developers/doc/applications/nodejs" title="Deploy a Node.js application" subtitle="Learn more on deploying a Node.js application" icon="node" >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="Learn more on deploying a Static application" icon="static" >}}
  {{< card link="https://docs.astro.build/" title="Learn Astro" subtitle="How to write and organize your content" icon="astro" >}}
{{< /cards >}}
