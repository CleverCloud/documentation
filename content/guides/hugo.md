---
type: docs
linkTitle: Hugo
title: Deploy a Hugo website
description: Deploy Hugo Static Site Generator (SSG) websites on Clever Cloud with step-by-step tutorial and configuration guide
keywords:
- hugo
- static site generator
- golang
- markdown
- website hosting
- fast websites
aliases:
- /hugo
---

{{< hextra/hero-subtitle >}}
  Hugo is a fast and flexible static site generator that allows you to create modern websites with ease.
{{< /hextra/hero-subtitle >}}

## Requirements

To create an example website, install [Hugo](https://gohugo.io/installation/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), then initialize a site:

```bash
hugo new site myStaticApp
```

{{% content "static-create" %}}

Add the Ananke theme as a Git submodule and create a first page:

```bash
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
printf "theme = 'ananke'\n" >> hugo.toml
hugo new content content/posts/hello.md
```

The generated page is a draft by default. Open `content/posts/hello.md`, add some content and set `draft` to `false` before deployment.

### Automatic build

Hugo is one of the static site generators supported by the [Static runtime automatic build](/doc/applications/static/#static-site-generators-ssg-auto-build), so you don't need any additional build configuration.

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://gohugo.io/documentation/" title="Learn Hugo" subtitle="How to write and organize your content" icon="hugo" >}}
{{< /cards >}}
