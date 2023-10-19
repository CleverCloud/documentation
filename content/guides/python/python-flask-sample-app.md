---
type: docs
title: Flask
shortdesc: The goal of this article is to show you how configure and deploy a simple Flask application on Clever Cloud.
tags:
- deploy
keywords:
- python
- flask
type: docs
---


## Overview

The goal of this article is to show you how to deploy a Flask application on Clever Cloud.
The application is a very basic one it just replies with a header dump to any request. More information about the application:  

*  [GitHub repo](https://GitHub.com/CleverCloud/demo-flask)

{{< readfile file="/content/partials/create-application.md" >}}

{{< readfile file="/content/partials/set-env-vars.md" >}}

## Configure your Flask application

### Build app in a subfolder

In the `/clevercloud/python.json` file, we have the `"build"."folder"` field that points to the `app` folder.
We will build & run the app from this `app` folder.

### Select your module

Clever Cloud runs the "app" Flask application defined in the `hello.py` file. So the "module" field is `hello:app`.

### Fine tuning the application

You can find a lot more configuration options such as choosing python version and so [here]({{< ref "doc/applications/python" >}})

{{< readfile file="/content/partials/new-relic.md" >}}

{{< readfile file="/content/partials/env-injection.md" >}}

To access [environment variables](#setting-up-environment-variables-on-clever-cloud) from your code, just get them from the environment with:

```python
import os
os.getenv("MY_VARIABLE")
```

{{< readfile file="/content/partials/deploy-git.md" >}}

{{< readfile file="/content/partials/link-addon.md" >}}

{{< readfile file="/content/partials/more-config.md" >}}
