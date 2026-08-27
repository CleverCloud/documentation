---
type: docs
linkTitle: Hexo
title: Deploy a Hexo website
description: Deploy Hexo Static Site Generator (SSG) websites on Clever Cloud with step-by-step tutorial and configuration guide
keywords:
- hexo
- static site generator
- Node.js
- blog framework
- website deployment
---

{{< hextra/hero-subtitle >}}
  Hexo is a fast, simple and powerful blog framework that allows you to create static websites with ease.
{{< /hextra/hero-subtitle >}}

## Requirements

If you need example source code, initialize a Hexo project with the [Cactus theme](https://github.com/probberechts/hexo-theme-cactus), [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/download):

```bash
npx hexo init myStaticApp --no-install
```

{{% content "static-create" %}}

Import the theme as a submodule:

```bash
git submodule add https://github.com/probberechts/hexo-theme-cactus.git themes/cactus
```

### Environment variables

Configure the output directory and build commands:

```bash
clever env set CC_WEBROOT "/public"
clever env set CC_PRE_BUILD_HOOK "npm install"
clever env set CC_BUILD_COMMAND "npm run build"
```

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://hexo.io/docs/" title="Learn Hexo" subtitle="How to write and organize your content" icon="hexo" >}}
{{< /cards >}}
