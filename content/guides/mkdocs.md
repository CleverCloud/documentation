---
type: docs
title: MkDocs
description: Deploy MkDocs Static Site Generator (SSG) websites on Clever Cloud with step-by-step tutorial and configuration guide
tags:
- guides
keywords:
- mkdocs
- python
- static
- ssg
- html
- js
- css
- website
---

{{< hextra/hero-subtitle >}}
  MkDocs is a static site generator that's geared towards project documentation. It allows you to write your documentation in Markdown and build a static website from it.
{{< /hextra/hero-subtitle >}}

## Requirements

If you need an example source code, init a new project (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [Python](https://wiki.python.org/moin/BeginnersGuide/Download) and [pipx](https://pipx.pypa.io/stable/)):

```bash
pipx mkdocs new myStaticApp
```

You can also use [uvx](https://docs.astral.sh/uv/guides/tools/):
```bash
uvx mkdocs new myStaticApp
```

{{% content "static-create" %}}

### Automatic build

MkDocs is one of the many Static Site Generator (SSG) that [Clever Cloud automatic build](/developers/doc/applications/static/#static-site-generators-ssg-auto-build) supports in the `static` runtime, you don't have anything special to manage. To use a pico instance with a dedicated build instance change it in the [Console](https://console.clever-cloud.com) or with Clever Tools:

```bash
clever scale --flavor pico

# To select a bigger build instance, use:
clever scale --build-flavor M
```

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Static runtime documentation" subtitle="How to configure your website" icon="static" >}}
  {{< card link="https://www.mkdocs.org/getting-started/" title="MkDocs documentation" subtitle="How to write and organize your content" icon="docs" >}}
{{< /cards >}}
