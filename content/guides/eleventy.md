---
type: docs
linkTitle: Eleventy (11ty)
title: Deploy an Eleventy website
description: Deploy Eleventy (11ty) Static Site Generator (SSG) websites on Clever Cloud with step-by-step tutorial and configuration guide
keywords:
- eleventy
- 11ty
- static site generator
- Node.js
- website deployment
aliases:
- /eleventy
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

Configure the output directory and build commands:

```bash
clever env set CC_WEBROOT "/_site"
clever env set CC_PRE_BUILD_HOOK "npm install"
clever env set CC_BUILD_COMMAND "npx @11ty/eleventy"
```

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://www.11ty.dev/docs/" title="Learn Eleventy (11ty)" subtitle="How to write and organize your content" icon="11ty" >}}
{{< /cards >}}
