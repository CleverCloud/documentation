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

Clever Cloud supportes deploying both fully static and on-demand rendered Astro projects. Regardless of your `output` mode ([pre-rendered or on-demand](/en/basics/rendering-modes/)), you can choose to deploy as a **static application** which runs using a post-build hook, or as a **Node.js** application, which works out-of-the-box with your `package.json`.

If you need an example source code, get [Astrowind](https://github.com/onwidget/astrowind) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):
```bash
git clone https://github.com/onwidget/astrowind myStaticApp
```

## Port and host

Applications on Clever Cloud listen on port **8080**. If your project requires this configuration, set your port and host in Astro in one of two locations:

{{< tabs items="package.json scripts,astro.config.mjs" >}}

  {{< tab >}}

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

   ```javascript {filename="astro.config.mjs"}
    import { defineConfig } from 'astro/config';

    export default defineConfig({
      server: {
        port: 8080,
        host: true
      }
    });
    ```

  {{< /tab >}}


{{< /tabs >}}

## Deploy Astro from the Console

To deploy your Astro project to Clever Cloud, you will need to **create a new application**. The application wizard will walk you through the necessary configuration steps.

{{% steps %}}

### Create the application 

From the lateral menubar, click **Create** > **An application**

### Choose how to deploy:

 - **Create a brand new app**: to deploy from a local repository with Git

    or

 - **Select a GitHub repository**: to deploy from GitHub

### Select the type of application

Select a **Node.js** application, or a **static** one.

### Set up instance minimal size and scalability

Set up the minimal size for your instance and scalability options. Astro sites can typically be deployed using the **Nano** instance. Depending on your project's specifications and dependencies, you may need to adjust accordingly as you watch the metrics from the **Overview** page.

### Select the region

Select a **region** to deploy your instance.

### Connected services

Skip [connecting **Add-ons** to your Clever application](/doc/addons/) unless you're using a database or Keycloak.

### Inject **environment variables**

For **Node.js**, no specific environment variable is needed to deploy Astro if you're using **npm**. If you're using **yarn** or **pnpm**, or deploying on a Static application, set the following environment variables.

{{% /steps %}}

#### Node.js variables

{{< tabs items="pnpm,yarn" >}}
  
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

#### Static application variables

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

### Deploy!

If you're deploying from **GitHub**, your deployment should start automatically. If you're using **Git**, copy the remote and push on the **master** branch. 



{{< callout emoji="💡" >}}
  To deploy from branches other than `master`, use `git push clever <branch>:master`. For example, if you want to deploy your local `main` branch without renaming it, use `git push clever main:master`.
{{< /callout >}}

## Deploy an Astro site using the CLI

{{% content/language-specific-deploy/create-static %}}

## Configure environment variables

Next, we configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:

```bash
clever scale --build-flavor M
clever scale --flavor nano

clever env set CC_NODE_VERSION "20"
clever env set CC_WEBROOT "/dist"
clever env set CC_OVERRIDE_BUILDCACHE "/dist"
clever env set CC_PRE_BUILD_HOOK "npm install && npm run astro telemetry disable"
clever env set CC_POST_BUILD_HOOK "npm run build"
```

{{% content/git-push %}}

## Learn more

{{< cards >}}
  {{< card link="../doc/applications/javascript/nodejs" title="Deploy a Node.js application" subtitle="Learn more on deploying a Node.js application on Clever Cloud" icon="node" >}}
  {{< card link="../doc/applications/static" title="Deploy a Static application" subtitle="Learn more on deploying a Static application on Clever Cloud" icon="feather" >}}
  {{< card link="https://docs.astro.build/en/getting-started/" title="Learn Astro" subtitle="Astro full documentation" icon="rocket-launch" >}}
  
{{< /cards >}}
