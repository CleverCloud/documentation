---
type: docs
title: Hugo
description: Build your website with the Hugo Static Site Generator (SSG) and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- hugo
- static
- ssg
- html
- js
- css
- website
comments: false
aliases:
- /hugo
---

{{< hextra/hero-subtitle >}}
  Hugo is a fast and flexible static site generator that allows you to create modern websites with ease.
{{< /hextra/hero-subtitle >}}

## Requirements

If you need an example source code, use the [Hugo Profile theme](https://github.com/gurusabarish/hugo-profile) example, you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git):

```bash
git clone https://github.com/gurusabarish/hugo-profile/

# Just keep exampleSite directory content to deploy the Hugo website
mv hugo-profile/exampleSite myStaticApp && rm -rf hugo-profile
```

{{% content "static-create" %}}

Import the theme as a submodule:

```bash
git submodule add https://github.com/gurusabarish/hugo-profile.git themes/hugo-profile
```

### Automatic build

Hugo is one of the many Static Site Generator (SSG) that [Clever Cloud automatic build](/developers/doc/applications/static/#static-site-generators-ssg-auto-build) supports in the `static` runtime, you don't have anything special to manage. To use a pico instance with a dedicated build instance change it in the [Console](https://console.clever-cloud.com) or with Clever Tools:

```bash
clever scale --flavor pico

# To select a bigger build instance, use:
clever scale --build-flavor M
```

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  {{< card link="https://gohugo.io/documentation/" title="Learn Hugo" subtitle="How to write and organize your content" icon="hugo" >}}
{{< /cards >}}
