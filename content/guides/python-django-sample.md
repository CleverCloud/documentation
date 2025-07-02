---
type: docs
title: Django
shortdesc: The goal of this article is to show you how to deploy a Django application on Clever Cloud.
tags:
- deploy
keywords:
- python
- django
aliases:
- /developers/doc/python/python-django-sample
- /doc/deploy/application/python/tutorials/python-django-sample
- /doc/python/python-django-sample
type: docs
---


## Overview

The goal of this article is to show you how to deploy a Django application on Clever Cloud.
The application is a very basic one. More information about the application in the[GitHub repo](https://github.com/CleverCloud/django-example).

{{< content "create-application" >}}

 {{< content "set-env-vars" >}}

## Configure your Django application

Note :

- Select at least a `nano` instance (`pico` doesn't have enough resources for a Django project).
- Connect your Django project to Postgresql version 12+ if you're using django 4.2+ (postgresql 11 is deprecated since this version).

### My application does not exists already

If you want to test easily a Django deployment on Clever Cloud, just clone the [GitHub repo](https://github.com/CleverCloud/django-example) and go the next section.

### My application already exists

{{< callout type="warning" >}}
  Do not forget to add the `CC_PYTHON_MODULE` environment variable in any Python project so that we get your required modules.
{{< /callout >}}

### Fine tuning the application

You can find a lot more configuration options such as choosing python version and more on our dedicated [Python documentation]({{< ref "doc/applications/python" >}}).

 {{< content "new-relic" >}}

### Manage.py tasks

Clever Cloud supports execution of multiple [manage.py](https://docs.djangoproject.com/fr/3.2/ref/django-admin/) tasks.

The tasks are launched after the dependencies from `requirements.txt` have been installed, and before the web server starts.

You can declare the `manage.py` tasks with the environment variable `CC_PYTHON_MANAGE_TASKS="migrate"`.

Values must be separated by a comma:

```bash
CC_PYTHON_MANAGE_TASKS="migrate, assets:precompile"
```

 {{< content "env-injection" >}}

To access environment variables from your code, just get them from the environment with:

```python
import os
os.getenv("MY_VARIABLE")
```

 {{< content "deploy-git" >}}

 {{< content "link-addon" >}}

{{< content "more-config" >}}
