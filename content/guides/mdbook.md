---
type: docs
linkTitle: mdBook
title: Deploy an mdBook website
description: Deploy mdBook Static Site Generator (SSG) websites on Clever Cloud with step-by-step tutorial and configuration guide
keywords:
- mdbook
- rust
- static site generator
- documentation tool
- website deployment
---

{{< hextra/hero-subtitle >}}
  mdBook is a command-line tool for creating modern online books and documentation. It is designed to help you write and organize your content in a structured way.
{{< /hextra/hero-subtitle >}}

## Requirements

If you need an example source code, init a new project (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Rust](https://www.rust-lang.org/tools/install)):

```bash
cargo install mdbook
mdbook init myStaticApp --title="my mdBook" --ignore=git
```

{{% content "static-create" %}}

### Automatic build

mdBook is one of the static site generators supported by the [Static runtime automatic build](/doc/applications/static/#static-site-generators-ssg-auto-build), so you don't need any additional build configuration.

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://rust-lang.github.io/mdBook/" title="Learn mdBook" subtitle="How to write and organize your content" icon="mdbook" >}}
{{< /cards >}}
