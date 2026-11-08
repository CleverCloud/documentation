---
type: docs
linkTitle: '{{ replace .File.ContentBaseName "-" " " | title }}'
title: 'Deploy {{ replace .File.ContentBaseName "-" " " | title }}'
description:
keywords:
draft: true
---

<!-- Prefer one clear path that uses platform defaults and native features. Follow every command from a fresh project, and test every behavior the guide promises. Add the guide to the index of its section, or, for a guide in guides/static-sites/, to content/shared/static-guides.md. Remove these comments before publication. -->

{{< hextra/hero-subtitle >}}
  Deploy {{ replace .File.ContentBaseName "-" " " | title }} on Clever Cloud.
{{< /hextra/hero-subtitle >}}

<!-- Introduce the software or the framework, then what this guide deploys: the runtime, the add-ons, and what each of them provides. -->

## Prepare the application

You need [Git](https://git-scm.com/downloads), [Clever Tools](/doc/tools/cli/), and a [Clever Cloud account](https://console.clever-cloud.com) to follow this guide.

<!-- Create or clone the project, move into its folder, and initialize its Git repository if needed. Then explain each file it needs, and what it does, at its first use. -->

## Create the application and add-ons

<!-- Replace <runtime> with the type of the runtime this guide deploys, such as node or linux. Show the domain right after the creation, then the add-ons and the environment variables. Omit -a when the current directory is linked to only one application. -->

Create the application, then show its domain:

```bash
clever create --type <runtime> {{ .File.ContentBaseName }}
clever domain
```

To use your own domain, add it, and [configure its DNS](/doc/manage/domain-names/):

```bash
clever domain add {{ .File.ContentBaseName }}.example.com
```

## Deploy {{ replace .File.ContentBaseName "-" " " | title }}

Commit the project, then deploy it:

```bash
git add .
git commit -m "Deploy {{ replace .File.ContentBaseName "-" " " | title }}"
clever deploy
```

<!-- Show how to check that the application works, such as a request to its domain. -->

## Learn more

<!-- Replace RUNTIME with the page of the runtime, then link the documentation of the software or the framework. -->

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/RUNTIME/" title="Runtime applications" subtitle="Configure the runtime of this guide" icon="cube" >}}
{{< /cards >}}
