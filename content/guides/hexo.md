---
type: docs
title: Hexo
description: Deploy Hexo Static Site Generator (SSG) websites on Clever Cloud with step-by-step tutorial and configuration guide
tags:
- guides
keywords:
- hexo
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
  Hexo is a fast, simple and powerful blog framework that allows you to create static websites with ease.
{{< /hextra/hero-subtitle >}}

## Requirements

If you need an example source code, initialize an Hexo project with [Cactus theme](https://github.com/probberechts/hexo-theme-cactus) (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):
```bash
npx hexo init myStaticApp --no-install
```

{{% content "static-create" %}}

Import the theme as a submodule:

```bash
git submodule add https://github.com/probberechts/hexo-theme-cactus.git themes/cactus
```

### Environment variables

Next, configure the application with a pico instance with dedicated build, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:

```bash
clever scale --flavor pico

# To select a bigger build instance, use:
clever scale --build-flavor M

clever env set CC_WEBROOT "/public"
clever env set CC_PRE_BUILD_HOOK "npm install"
clever env set CC_BUILD_COMMAND "npm run build"
```

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  {{< card link="https://hexo.io/docs/" title="Learn Hexo" subtitle="How to write and organize your content" icon="hexo" >}}
{{< /cards >}}
