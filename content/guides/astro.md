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

Macro description of the needed setup (type of runtime, possible add-ons) to deploy <framework> on Clever Cloud.

If you need an example source code, get [Example application](https://github.examplec.com/something/framework) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)):
```bash
git clone https://github.example.com/something/framework myApp
```

## Overview

Clever Cloud supports deploying both [fully static and on-demand rendered](https://docs.astro.build/en/basics/rendering-modes/) Astro projects:
- The `static` output mode is ideal for most content-oriented website, for which you have no need for per-visitor server-side customisation
  We recommend using our [Static runtime](/doc/applications/static/) when using this output mode, with the site generation in a post-build hook
- The `server` or `hybrid` output modes
  We recommend using our [Node.js runtime](/doc/applications/javascript/nodejs/) runtime with [Astro’s Node adapter](https://docs.astro.build/en/guides/integrations-guide/node/)

If you need an example source code, get [Astrowind](https://github.com/onwidget/astrowind) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):
```bash
git clone https://github.com/onwidget/astrowind myApp
```

## Use case: Static site generation

{{% steps %}}

{{% content/guides/create-application framework="Astro" runtime="Static" flavor="nano" %}}

{{< content/guides/set-environment >}}
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
{{< /content/guides/set-environment >}}

{{% content/guides/deploy-application %}}

## Use case: Server-side rendering

We will be using the [Node.js adapter](https://docs.astro.build/en/guides/integrations-guide/node/) here.

{{% steps %}}

{{% content/guides/create-application framework="Astro" runtime="Node" flavor="nano" %}}

{{< content/guides/set-environment >}}
  {{< tabs items="npm,pnpm,yarn" >}}

  {{< tab >}}
  ```shell
  CC_RUN_COMMAND="./dist/server/entry.mjs"
    ```
  {{< /tab >}}

  {{< tab >}}
  ```shell
  CC_NODE_BUILD_TOOL="custom"
  CC_PRE_BUILD_HOOK="npm install -g pnpm && pnpm install"
  CC_CUSTOM_BUILD_TOOL="pnpm run astro telemetry disable && pnpm build"
  CC_RUN_COMMAND="./dist/server/entry.mjs"
    ```
  {{< /tab >}}

  {{< tab >}}
  ```shell
  CC_NODE_BUILD_TOOL="yarn"
  CC_PRE_BUILD_HOOK="yarn && yarn run astro telemetry disable && yarn build"
  CC_RUN_COMMAND="./dist/server/entry.mjs"
    ```
  {{< /tab >}}
  {{< /tabs >}}
{{< /content/guides/set-environment >}}

{{% content/guides/deploy-application %}}


## Learn more

{{< cards >}}
  {{< card link="../../doc/applications/javascript/nodejs" title="Deploy a Node.js application" subtitle="Learn more on deploying a Node.js application on Clever Cloud" icon="node" >}}
  {{< card link="../../doc/applications/static" title="Deploy a Static application" subtitle="Learn more on deploying a Static application on Clever Cloud" icon="feather" >}}
  {{< card link="https://docs.astro.build/" title="Learn Astro" subtitle="Astro full documentation" icon="rocket-launch" >}}

{{< /cards >}}
