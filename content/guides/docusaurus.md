---
type: docs
title: Docusaurus
description: Build your website with the Docusaurus Static Site Generator (SSG) and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- docusaurus
- nodejs
- static
- ssg
- html
- js
- css
- website
aliases:
- /docusaurus
comments: false
---

{{< hextra/hero-subtitle >}}
  Docusaurus is a static site generator that helps you build optimized websites quickly. It is designed to help you create documentation, blogs, and other content-driven sites with ease.
{{< /hextra/hero-subtitle >}}

## Requirements

If you need an example source code, init a new project (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs)):

```bash
npx create-docusaurus@latest myStaticApp classic
```

{{% content "static-create" %}}

### Automatic build

Docusaurus is one of the many Static Site Generator (SSG) that [Clever Cloud automatic build](/developers/doc/applications/static/#static-site-generators-ssg-auto-build) supports in the `static` runtime, you don't have anything special to manage. To use a pico instance with a dedicated build instance change it in the [Console](https://console.clever-cloud.com) or with Clever Tools:

```bash
clever scale --flavor pico

# To select a bigger build instance, use:
clever scale --build-flavor M
```

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  {{< card link="https://docusaurus.io/docs" title="Learn Docusaurus" subtitle="How to write and organize your content" icon="docusaurus" >}}
{{< /cards >}}
