---
type: docs
linkTitle: Lume (Deno)
title: Deploy a Lume website with Deno
description: Build and deploy your website with Lume Static Site Generator (SSG) using Deno runtime on Clever Cloud platform with complete setup guide
keywords:
- lume
- deno
- static site generator
- typescript
- website deployment
---

{{< hextra/hero-subtitle >}}
  Lume is a fast and flexible static site generator built with Deno, designed to help you create modern websites with ease.
{{< /hextra/hero-subtitle >}}

## Requirements

If you need an example source code, use the [Lume website](https://github.com/lumeland/lume.land), you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git):

```bash
git clone https://github.com/lumeland/lume.land myStaticApp
```

{{% content "static-create" %}}

### Environment variables

The complete Lume website used in this example has a large dependency graph. Give its build phase a dedicated M instance, then configure the output directory and build command:

```bash
clever scale --build-flavor M

clever env set CC_WEBROOT "/_site"
clever env set CC_BUILD_COMMAND "deno task lume"
```

It defines `_site` as the folder to serve with the web server and `deno task lume` as the command to build the static files.

### Deno installation

Create a `mise.toml` file, add this content:

```toml {filename="mise.toml"}
[tools]
deno = "latest"
```

It uses [Mise package manager](/doc/reference/reference-environment-variables/#install-tools-with-mise-package-manager) to install Deno during deployment. You can replace `latest` with a specific version.

> [!TIP]
> If you use Mise locally, run `mise trust` to trust the created `mise.toml` file

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://lume.land/docs/overview/about-lume/" title="Learn Lume" subtitle="How to write and organize your content" icon="deno" >}}
{{< /cards >}}
