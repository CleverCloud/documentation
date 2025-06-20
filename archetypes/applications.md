---
type: docs
linkTitle: '{{ replace .File.ContentBaseName "-" " " | title }}'
title:
description:
type: docs
---

## Overview

## Create your XXX application

To create a new XXX application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type XXX
```
* [Learn more about Clever Tools](/developers/doc/cli/)
* [Learn more about Clever Cloud application deployment](/developers/doc/quickstart/#create-an-application-step-by-step)

## Configure your XXX application

### Mandatory needs

XXX runtime only requires a working application listening on `0.0.0.0:8080`.

* [Learn more about environment variables on Clever Cloud](/developers/doc/reference/reference-environment-variables/)

### Build phase

During the build phase,

- [Learn more about Deployment hooks](/developers/doc/develop/build-hooks/)

### XXX version



## Clever Tasks


```bash
clever create --type XXX --task "XXX"
clever deploy # or clever restart if there is no code change
```

- [Learn more about Clever Tasks](/developers/doc/develop/tasks/)
