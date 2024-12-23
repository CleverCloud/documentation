---
title: Nuxt
description: Build your website with Nuxt, either as a static site or using a NodeJs app, and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- nuxt
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
  Nuxt is a powerful and versatile web framework for building modern web applications, offering a seamless development experience with server-side rendering, static site generation, and hybrid capabilities. Learn in this guide how to deploy a Nuxt site on Clever Cloud.
{{< /hextra/hero-subtitle >}}

Clever Cloud supports deploying both [fully static and on-demand rendered](https://nuxt.com/docs/guide/concepts/rendering) Nuxt 3 projects:   

- The `static` rendering mode is ideal for most content-oriented websites where you don't need per-visitor server-side customization. Consider using a [Static runtime](/doc/applications/static/) when using this mode, with the site generation handled in a post-build hook. Learn more about [static hosting with Nuxt](https://nuxt.com/docs/getting-started/deployment#static-hosting). 
- The `server` or `hybrid` rendering modes are suited for dynamic applications requiring server-side customization or a mix of static and server-rendered pages. For these modes, consider using a [Node.js runtime](/doc/applications/javascript/nodejs/). Learn more about [Node.js hosting with Nuxt](https://nuxt.com/docs/getting-started/deployment#nodejs-server).

If you need an example source code compatible with Nuxt static generation, get [Zooper](https://github.com/fayazara/zooper) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):

```bash
git clone https://github.com/fayazara/zooper myStaticApp
```

## Deploy a static Nuxt site

To deploy your Nuxt project to Clever Cloud, you need to **create a new application**. 

### Create a static application from the Console

In this step, you set up the following parameters:

- Deployment (using Git or GitHub)
- Application : Static
- Instance size and scalability options : You can usually deploy an Nuxt site using the **Nano** instance
- Region
- Dependencies, if needed
- Change build option to **M** instance 

{{% content/language-specific-deploy/create-static %}}

Next, we configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:

```bash
clever scale --build-flavor M
clever scale --flavor nano
```

### Inject environment variables

Use environment variables to control the deployment behavior, which depends on the type of application and your package manager. Find right below the ones that apply for your application.

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
    CC_CUSTOM_BUILD_TOOL="pnpm build"
    CC_POST_BUILD_HOOK="npx nuxi generate"
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

{{% content/language-specific-deploy/create-static %}}

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

{{% content/git-push %}}

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





{{% content/language-specific-deploy/create-static %}}

## Configure environment variables

Next, we configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:

```bash
clever scale --build-flavor M
clever scale --flavor nano

clever env set CC_NODE_VERSION "20"
clever env set CC_WEBROOT "/.output/public"
clever env set CC_OVERRIDE_BUILDCACHE "/.output/public"
clever env set CC_PRE_BUILD_HOOK "npm install"
clever env set CC_POST_BUILD_HOOK "npx nuxi generate"
```

{{% content/git-push %}}

## Learn more

{{< cards >}}
  {{< card link="../../doc/applications/javascript/nodejs" title="Deploy a Node.js application" subtitle="Learn more on deploying a Node.js application on Clever Cloud" icon="node" >}}
  {{< card link="../../doc/applications/static" title="Deploy a Static application" subtitle="Learn more on deploying a Static application on Clever Cloud" icon="feather" >}}
  {{< card link="https://nuxt.com/docs" title="Learn Nuxt" subtitle="Nuxt full documentation" icon="rocket-launch" >}}
{{< /cards >}}
