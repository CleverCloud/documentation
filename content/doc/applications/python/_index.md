---
type: docs
title: Python

shortdesc: Python 2.7 and 3.11 are available on our platform. You can use Git to deploy your application.
tags:
- deploy
keywords:
- python
str_replace_dict:
  "@application-type@": "Python"
type: docs
aliases:
- /doc/deploy/application/python
- /doc/deploy/application/python/python_apps/
- /doc/getting-started/by-language/python
- /doc/partials/language-specific-deploy/python
comments: false
---

## Overview

Python is a programming language that lets you work more quickly and integrate your systems more efficiently.

### Supported versions

The supported versions are: {{< runtimes_versions python >}}

{{% content/create-application %}}

{{% content/set-env-vars %}}

{{< readfile file="language-specific-deploy/python.md" >}}

{{% content/deploy-git %}}

{{% content/link-addon %}}

{{% content/more-config %}}

{{< readfile file="url_healthcheck.md" >}}
