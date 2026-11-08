---
type: docs
linkTitle: '{{ replace .File.ContentBaseName "-" " " | title }}'
title: '{{ replace .File.ContentBaseName "-" " " | title }} application runtime'
description:
keywords:
draft: true
---

<!-- Write for a reader new to this language or runtime: explain each tool, file, or concept of its ecosystem in a few words at its first use. Deploy every example and test every behavior the page describes. The file name sets the type in clever create, the anchors, and the key of the version table: adjust them if they differ. Remove these comments before publication. -->

## Overview

<!-- One sentence on the language, or on what the runtime runs, one on what Clever Cloud builds and starts, then the main frameworks it works with. -->

## Create your {{ replace .File.ContentBaseName "-" " " | title }} application

To create a new {{ replace .File.ContentBaseName "-" " " | title }} application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type {{ .File.ContentBaseName }}
```

The [getting started guide](/doc/getting-started/#create-an-application-step-by-step) describes each step of the creation of an application.

## Configure your {{ replace .File.ContentBaseName "-" " " | title }} application

### Mandatory needs

A {{ replace .File.ContentBaseName "-" " " | title }} application needs:

- A project file, at the root of the project or of the folder set in `APP_FOLDER`
- A web server listening on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port)

<!-- If the runtime doesn't need a project file, replace or remove its item. Explain what the project file and its lock file, if the ecosystem has one, are for. Then show a minimal application that reads PORT, with the command to try it locally. If Clever Cloud starts a managed web server, such as Puma for Ruby, replace the web server item and explain this server instead. -->

A [Clever Task](#{{ .File.ContentBaseName }}-applications-as-clever-tasks) doesn't need a web server.

### Build phase

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/), then builds your project:

```bash
# The commands the build runs, in order
```

<!-- Explain what each command does, and the variables that change them. -->

### {{ replace .File.ContentBaseName "-" " " | title }} version

<!-- If Clever Cloud provides a list of versions, add it to data/runtime_versions.yml first: the shortcode renders nothing without it. If Clever Cloud installs a single version, add it to this file too, and replace runtimes_versions with the runtime_version shortcode. If the project sets its version, explain how instead, and remove the shortcode. If the runtime has no version of its own, remove this section. -->

{{< runtimes_versions {{ .File.ContentBaseName }} >}}

### Start command

<!-- Describe the command Clever Cloud starts by default, the folder it runs from, and how CC_RUN_COMMAND or another variable changes it. If Clever Cloud starts a managed server, describe it and its settings. -->

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

<!-- Describe what CC_CACHE_DEPENDENCIES=true keeps between commits, and from which folder. -->

## {{ replace .File.ContentBaseName "-" " " | title }} applications as Clever Tasks

A {{ replace .File.ContentBaseName "-" " " | title }} application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration: Clever Cloud builds it, then runs `CC_RUN_COMMAND`.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks):

<!-- Replace <command> with a command of this runtime that runs a job, such as a migration script. -->

```bash
clever create --type {{ .File.ContentBaseName }} --task "<command>"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
