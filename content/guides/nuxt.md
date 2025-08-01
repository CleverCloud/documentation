---
type: docs
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
comments: false
---

{{< hextra/hero-subtitle >}}
  Nuxt is a powerful and versatile web framework for building modern web applications, offering a seamless development experience with server-side rendering, static site generation, and hybrid capabilities.
{{< /hextra/hero-subtitle >}}

Clever Cloud supports deploying both [fully static and on-demand rendered](https://nuxt.com/docs/guide/concepts/rendering) Nuxt 4 projects:

- The `static` rendering mode is ideal for most content-oriented websites where you don't need per-visitor server-side customization. Consider using a [Static runtime](/developers/doc/applications/static/) when using this mode, with the automatic site generation. Learn more about [static hosting with Nuxt](https://nuxt.com/docs/getting-started/deployment#static-hosting).
- The `server` or `hybrid` rendering modes are optimal for dynamic applications requiring server-side customization or a mix of static and server-rendered pages. For these modes, consider using a [Node.js runtime](/developers/doc/applications/nodejs). Learn more about [Node.js hosting with Nuxt](https://nuxt.com/docs/getting-started/deployment#nodejs-server).

If you need an example source code compatible with Nuxt static generation, get [Nuxt Boilerplate](https://github.com/renegadevi/nuxt-boilerplate) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):

```bash
git clone https://github.com/renegadevi/nuxt-boilerplate myStaticApp
```

{{% content "static-create" %}}

### Automatic build

Nuxt is one of the many Static Site Generator (SSG) that [Clever Cloud automatic build](/developers/doc/applications/static/#static-site-generators-ssg-auto-build) supports in the `static` runtime. Then, you don't have anything special to manage. To use a pico instance with a dedicated build instance change it in the [Console](https://console.clever-cloud.com) or with Clever Tools:

```bash
clever scale --flavor pico

# To select a bigger build instance, use:
clever scale --build-flavor M
```

{{% content "static-deploy" %}}

## Deploy a Node.js application

To deploy your Nuxt project to Clever Cloud, you need to **create a new application**.

### Create a Node.js application

You can create an application from the [Console](https://console.clever-cloud.com) or through [Clever Tools](https://github.com/CleverCloud/clever-tools/):

```bash
npm i -g clever-tools
clever login

cd myStaticApp
clever create -t node
```

To deploy on Clever Cloud, your local folder needs to be a git repository (if not, `git init`) linked to an application. If you already have an application on Clever Cloud and want to link it to the current local folder:

```bash
clever link your_app_name_or_ID
```

### Environment variables

Next, configure the application with a medium build instance. The host instance is XS, enough for a simple website. As Clever Cloud uses industry standards, you only need to define a few variables:

```bash
clever scale --build-flavor M
clever scale --flavor XS

clever env set CC_PRE_BUILD_HOOK "npm run build"
clever env set CC_RUN_COMMAND "node .output/server/index.mjs"
```

### Push your code

Once you complete these steps, commit your content to the local repository and deploy it:

```bash
git add .
git commit -m "First deploy"
clever deploy
clever open
```

You can display your website's URL or add a custom domain to it (you'll need to configure DNS):

```bash
clever domain
clever domain add your.website.tld
```

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/nodejs" title="Deploy a Node.js application" subtitle="Learn more on deploying a Node.js application" icon="node" >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="Learn more on deploying a Static application" icon="static" >}}
  {{< card link="https://nuxt.com/docs" title="Learn Nuxt" subtitle="How to write and organize your content" icon="nuxt" >}}
{{< /cards >}}
