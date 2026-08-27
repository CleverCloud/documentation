---
type: docs
linkTitle: Docusaurus
title: Deploy a Docusaurus website
description: Deploy Docusaurus Static Site Generator (SSG) websites on Clever Cloud with step-by-step tutorial and configuration guide
keywords:
- docusaurus
- static site generator
- documentation site
- react framework
- Node.js
- website deployment
aliases:
- /docusaurus
---

{{< hextra/hero-subtitle >}}
  Docusaurus is a static site generator that helps you build optimized websites quickly. It is designed to help you create documentation, blogs, and other content-driven sites with ease.
{{< /hextra/hero-subtitle >}}

## Requirements

If you need example source code, initialize a new project with [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Node.js](https://nodejs.org/en/download):

```bash
npx create-docusaurus@latest myStaticApp classic --javascript
```

{{% content "static-create" %}}

### Automatic build

Docusaurus is one of the static site generators supported by the [Static runtime automatic build](/doc/applications/static/#static-site-generators-ssg-auto-build), so you don't need any additional build configuration.

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://docusaurus.io/docs" title="Learn Docusaurus" subtitle="How to write and organize your content" icon="docusaurus" >}}
{{< /cards >}}
