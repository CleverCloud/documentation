---
type: docs
title: Eleventy (11ty)
description: Build your website with the Eleventy (11ty) Static Site Generator (SSG) and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- Eleventy
- 11ty
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
  Eleventy (11ty) is a simple static site generator that allows you to create fast, modern websites with minimal configuration.
{{< /hextra/hero-subtitle >}}

## Requirements

If you need an example source code, get [11ty base blog](https://github.com/11ty/eleventy-base-blog), you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git):

```bash
git clone https://github.com/11ty/eleventy-base-blog myStaticApp
```

{{% content "static-create" %}}

### Environment variables

Next, configure the application with a pico instance with dedicated build, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:

```bash
clever scale --flavor pico

# To select a bigger build instance, use:
clever scale --build-flavor M

clever env set CC_WEBROOT "/_site"
clever env set CC_PRE_BUILD_HOOK "npm install"
clever env set CC_BUILD_COMMAND "npx @11ty/eleventy"
```

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  {{< card link="https://www.11ty.dev/docs/" title="Learn Eleventy (11ty)" subtitle="How to write and organize your content" icon="11ty" >}}
{{< /cards >}}
