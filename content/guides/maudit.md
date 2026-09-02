---
type: docs
linkTitle: Maudit
title: Deploy a Maudit website
description: Deploy a Maudit static website built with Rust on Clever Cloud
keywords:
- maudit
- rust
- static site generator
- static website
- website deployment
---

{{< hextra/hero-subtitle >}}
  Deploy a static website built with Maudit and Rust on Clever Cloud.
{{< /hextra/hero-subtitle >}}

[Maudit](https://maudit.org/) is an open source Rust library for generating static websites. A Maudit project is a regular Rust program that generates its pages and assets during the build phase.

## Create a Maudit project

You need [Git](https://git-scm.com/downloads) and [Rust](https://www.rust-lang.org/tools/install) to follow this guide. Install the Maudit CLI and start its interactive project generator:

```bash
cargo install maudit-cli
maudit init
```

Enter `myMauditSite` as the project directory, select the `Basics` template and decline the Git repository initialization. Then move into the generated project:

```bash
cd myMauditSite
```

If you already have a Maudit project, run the following commands from its root directory.

## Create a Static application

Install [Clever Tools](/developers/doc/cli/), log in and create a Static application linked to your project folder:

```bash
npm i -g clever-tools
clever login

clever create -t static

# Or link an existing Clever Cloud application:
clever link your_app_name_or_ID
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

## Configure the application

Use a dedicated S build instance, then set the generated website directory and the command Clever Cloud runs during the build phase:

```bash
clever scale --build-flavor S
clever env set CC_WEBROOT "/dist"
clever env set CC_BUILD_COMMAND "cargo run --jobs 1 --config profile.dev.debug=0"
```

Some Maudit dependencies require significant memory to compile. On an S build instance, a plain `cargo run` can compile several dependencies in parallel and exhaust the available memory. The `--jobs 1` option compiles them sequentially, while `--config profile.dev.debug=0` omits debug information that is unnecessary for generating a static website.

These options allow the build to use the smallest tested instance size. The command then runs the Maudit project to generate the website in `dist/`, whose contents are served by the Static runtime from its default XS instance.

## Deploy the website

Commit the project and deploy it:

```bash
git init
git add .
git commit -m "First deploy"

clever deploy
clever open
```

You can display your website's URL or add a custom domain. A custom domain also requires [DNS configuration](/developers/doc/administrate/domain-names/):

```bash
clever domain
clever domain add your.website.tld
```

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/static/" title="Static applications" subtitle="Configure and deploy static applications" icon="static" >}}
  {{< card link="https://maudit.org/docs/" title="Maudit documentation" subtitle="Build static websites with Maudit and Rust" icon="maudit" >}}
{{< /cards >}}
