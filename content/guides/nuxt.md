---
type: docs
linkTitle: Nuxt
title: Deploy a Nuxt application
description: Deploy Nuxt as Static Site Generator (SSG) or with Node.js on Clever Cloud with step-by-step tutorial and configuration guide
keywords:
- nuxt
- Vue.js
- static site generator
- Node.js
- JavaScript framework
aliases:
- /doc/nuxt
- /nuxt
---

{{< hextra/hero-subtitle >}}
  Nuxt is a powerful and versatile web framework for building modern web applications, offering a seamless development experience with server-side rendering, static site generation, and hybrid capabilities.
{{< /hextra/hero-subtitle >}}

Clever Cloud supports Nuxt 4 projects as pre-rendered static sites or [on-demand rendered](https://nuxt.com/docs/4.x/guide/concepts/rendering) applications:

- A pre-rendered site is ideal for most content-oriented websites where you don't need per-visitor server-side customization. Use the [Static runtime](/developers/doc/deploy/applications/static/) to generate and serve it automatically. Learn more about [static hosting with Nuxt](https://nuxt.com/docs/4.x/getting-started/deployment#static-hosting).
- Server-side or hybrid rendering is better suited to dynamic applications requiring server-side customization or a mix of static and server-rendered pages. Use the [Node.js runtime](/developers/doc/deploy/applications/nodejs/) for these modes. Learn more about [Node.js hosting with Nuxt](https://nuxt.com/docs/4.x/getting-started/deployment#nodejs-server).

To follow this guide, clone [Nuxt Boilerplate](https://github.com/renegadevi/nuxt-boilerplate), then choose one of the two deployment methods below. You need [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/download):

```bash
git clone https://github.com/renegadevi/nuxt-boilerplate myStaticApp
```

{{% content "static-create" %}}

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

## Automatic build

The Static runtime automatically detects `nuxt.config.ts`, runs the Nuxt static generation command and serves the generated files.

{{% content "static-deploy" %}}

## Deploy a Node.js application

Use a Node.js application for Nuxt server-side rendering and hybrid rendering.

### Create a Node.js application

Install [Clever Tools](/developers/doc/manage/cli/), log in and create a Node.js application linked to the cloned repository:

```bash
npm i -g clever-tools
clever login

cd myStaticApp
clever create -t node

# Or link an existing Clever Cloud application:
clever link your_app_name_or_ID
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

### Environment variables

Install the development dependencies required by Nuxt and build the server after dependency installation:

```bash
clever env set CC_NODE_DEV_DEPENDENCIES install
clever env set CC_POST_BUILD_HOOK "npm run build"
```

The Node.js runtime installs the dependencies before running the post-build hook. It then starts the application with the `start` script from `package.json`, which runs the generated `.output/server/index.mjs` server. Nuxt reads the `PORT` environment variable injected by Clever Cloud, so you don't need to configure a listening port.

### Push your code

Once you complete these steps, commit your content to the local repository and deploy it:

```bash
git add .
git commit -m "First deploy"

clever deploy
clever open
```

You can display your application's domains or add a [custom domain](/developers/doc/develop/common-configuration/domain-names/):

```bash
clever domain
clever domain add your.website.tld
```

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/nodejs" title="Deploy a Node.js application" subtitle="Learn more on deploying a Node.js application" icon="node" >}}
  {{< card link="/developers/doc/deploy/applications/static" title="Deploy a Static application" subtitle="Learn more on deploying a Static application" icon="static" >}}
  {{< card link="https://nuxt.com/docs/4.x/getting-started/introduction" title="Learn Nuxt" subtitle="How to write and organize your content" icon="nuxt" >}}
{{< /cards >}}
