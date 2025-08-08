---
type: docs
title: mdBook
description: Deploy mdBook Static Site Generator (SSG) websites on Clever Cloud with step-by-step tutorial and configuration guide
keywords:
- mdbook
- rust
- static
- ssg
- html
- js
- css
- website
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

mdBook is one of the many Static Site Generator (SSG) that [Clever Cloud automatic build](/developers/doc/applications/static/#static-site-generators-ssg-auto-build) supports in the `static` runtime, you don't have anything special to manage. To use a pico instance with a dedicated build instance change it in the [Console](https://console.clever-cloud.com) or with Clever Tools:

```bash
clever scale --flavor pico

# To select a bigger build instance, use:
clever scale --build-flavor M
```

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  {{< card link="https://rust-lang.github.io/mdBook/" title="Learn mdBook" subtitle="How to write and organize your content" icon="mdbook" >}}
{{< /cards >}}
