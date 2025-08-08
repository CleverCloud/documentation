---
type: docs
title: Lume (Deno)
description: Build and deploy your website with Lume Static Site Generator (SSG) using Deno runtime on Clever Cloud platform with complete setup guide
keywords:
- deno
- lume
- static
- ssg
- html
- js
- css
- website
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

Next, configure the application with a pico instance with dedicated Medium build (needed for Deno), enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:

```bash
clever scale --flavor pico
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

It uses [Mise package manager](/developers/doc/reference/reference-environment-variables/#install-tools-with-mise-package-manager) to install Deno during deployment. You can replace `latest` with a specific version.

> [!TIP]
> If you use Mise locally, run `mise trust` to trust the created `mise.toml` file

{{% content "static-deploy" %}}

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static" title="Deploy a Static application" subtitle="How to configure your website" icon="static" >}}
  {{< card link="https://lume.land/docs/overview/about-lume/" title="Learn Lume" subtitle="How to write and organize your content" icon="deno" >}}
{{< /cards >}}
