---
type: docs
linkTitle: MkDocs
title: Deploy a MkDocs website
description: Deploy MkDocs Static Site Generator (SSG) websites on Clever Cloud with step-by-step tutorial and configuration guide
keywords:
- mkdocs
- python
- static site generator
- documentation platform
- website deployment
---

{{< hextra/hero-subtitle >}}
  MkDocs is a static site generator that's geared towards project documentation. It allows you to write your documentation in Markdown and build a static website from it.
{{< /hextra/hero-subtitle >}}

## Requirements

To create an example project, install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [`uv`](https://docs.astral.sh/uv/getting-started/installation/), then run MkDocs with `uvx`:

```bash
uvx mkdocs new myStaticApp
```

{{% content "static-create" %}}

### Automatic build

MkDocs is one of the static site generators supported by the [Static runtime automatic build](/doc/applications/static/#static-site-generators-ssg-auto-build), so you don't need any additional build configuration.

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Static runtime documentation" subtitle="How to configure your website" icon="static" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://www.mkdocs.org/getting-started/" title="MkDocs documentation" subtitle="How to write and organize your content" icon="docs" >}}
{{< /cards >}}
