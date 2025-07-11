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

- The `static` rendering mode is ideal for most content-oriented websites where you don't need per-visitor server-side customization. Consider using a [Static runtime](/developers/doc/applications/static/) when using this mode, with the site generation handled in a post-build hook. Learn more about [static hosting with Nuxt](https://nuxt.com/docs/getting-started/deployment#static-hosting).
- The `server` or `hybrid` rendering modes are optimal for dynamic applications requiring server-side customization or a mix of static and server-rendered pages. For these modes, consider using a [Node.js runtime](/developers/doc/applications/nodejs). Learn more about [Node.js hosting with Nuxt](https://nuxt.com/docs/getting-started/deployment#nodejs-server).

If you need an example source code compatible with Nuxt static generation, get [Zooper](https://github.com/fayazara/zooper) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):

```bash
git clone https://github.com/fayazara/zooper myStaticApp
```

## Deploy a static Nuxt site

To deploy your Nuxt project to Clever Cloud, you need to **create a new application**.

{{< content "language-specific-deploy/create-static" >}}

### Configure environment variables

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

## Deploy a server Nuxt site

To deploy your Nuxt project to Clever Cloud, you need to **create a new application**.


### Create a Node.js application

You can create an application from the [Console](https://console.clever-cloud.com) or through [Clever Tools](https://github.com/CleverCloud/clever-tools/):

```bash
npm i -g clever-tools
clever login

cd myStaticApp
clever create -t node mNuxtApp
```

To deploy on Clever Cloud, your local folder needs to be a git repository (if not, `git init`) linked to an application. If you already have an application on Clever Cloud and want to link it to the current local folder:

```bash
clever link your_app_name_or_ID
```

### Configure environment variables

Next, configure the application with a medium build instance. The host instance is XS, enough for a simple website. As Clever Cloud uses industry standards, you only need to define a few variables:

```bash
clever scale --build-flavor M
clever scale --flavor xs

clever env set CC_PRE_BUILD_HOOK "npm run build"
clever env set CC_RUN_COMMAND "node .output/server/index.mjs"
```

{{< content "git-push" >}}

## Learn more

{{< cards >}}
  {{< card link="../../doc/applications/nodejs" title="Deploy a Node.js application" subtitle="Learn more on deploying a Node.js application on Clever Cloud" icon="node" >}}
  {{< card link="../../doc/applications/static" title="Deploy a Static application" subtitle="Learn more on deploying a Static application on Clever Cloud" icon="feather" >}}
  {{< card link="https://nuxt.com/docs" title="Learn Nuxt" subtitle="Nuxt full documentation" icon="rocket-launch" >}}
{{< /cards >}}
