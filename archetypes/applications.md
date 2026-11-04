---
type: docs
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
linkTitle:
description:
keywords:
draft: true
---

## Overview

## Create your {{ replace .File.ContentBaseName "-" " " | title }} application

To create a new {{ replace .File.ContentBaseName "-" " " | title }} application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type {{ .File.ContentBaseName }}
```

- [Learn more about Clever Tools](/doc/manage/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

## Configure your {{ replace .File.ContentBaseName "-" " " | title }} application

### Mandatory needs

The {{ replace .File.ContentBaseName "-" " " | title }} runtime only requires a working application listening on `0.0.0.0:8080`.

- [Learn more about environment variables on Clever Cloud](/doc/develop/common-configuration/environment-variables/reference/)

### Build phase

During the build phase,

- [Learn more about deployment hooks](/doc/develop/common-configuration/build-hooks/)

### {{ replace .File.ContentBaseName "-" " " | title }} version

## Clever Tasks

```bash
clever create --type {{ .File.ContentBaseName }} --task "./run-task.sh"
clever deploy # or clever restart if there is no code change
```

- [Learn more about Clever Tasks](/doc/develop/tasks/)
