---
title: Deploy Django application
shortdesc: The goal of this article is to show you how to deploy a Django application on Clever Cloud.
tags:
- deploy
keywords:
- python
- django
---


## Overview

The goal of this article is to show you how to deploy a Django application on Clever Cloud.
The application is a very basic one. More information about the application:  

*  [GitHub repo](https://github.com/CleverCloud/django-example)
*  [Clever Cloud demo](https://django.cleverapps.io/)

{{< readfile file="/content/partials/create-application.md" >}}

{{< readfile file="/content/partials/set-env-vars.md" >}}

## Configure your Django application

Note : 
- Select at least a `nano` instance (`pico` doesn't have enough resources for a Django project).
- Connect your Django project to Postgresql version 12+ if you're using django 4.2+ (postgresql 11 is deprecated since this version).

### My application does not exists already

If you want to test easily a Django deployment on Clever Cloud, just clone the [GitHub repo](https://github.com/CleverCloud/django-example) and go the next section.

### My application already exists

<br/><br/>
{{< alert "warning" "Reminder" >}}
  Do not forget to add the `CC_PYTHON_MODULE` environment variable  or the file [clevercloud/python.json](https://github.com/CleverCloud/django-example/blob/master/clevercloud/python.json) in any Python project so that we get your required modules.
{{< /alert >}}

### Fine tuning the application

You can find a lot more configuration options such as choosing python version and more on our dedicated [Python documentation]({{< ref "doc/deploy/application/python/python_apps.md" >}}).

{{< readfile file="/content/partials/new-relic.md" >}}

### Manage.py tasks

Clever Cloud supports execution of multiple [manage.py](https://docs.djangoproject.com/fr/3.2/ref/django-admin/) tasks.

The tasks are launched after the dependencies from `requirements.txt` have been installed, and before the web server starts.

You can declare the `manage.py` tasks with the [environment variable](#setting-up-environment-variables-on-clever-cloud) `CC_PYTHON_MANAGE_TASKS="migrate"`.

Values must be separated by a comma:

```bash
CC_PYTHON_MANAGE_TASKS="migrate, assets:precompile"
```

{{< readfile file="/content/partials/env-injection.md" >}}

To access [environment variables](#setting-up-environment-variables-on-clever-cloud) from your code, just get them from the environment with:

```python
import os
os.getenv("MY_VARIABLE")
```

{{< readfile file="/content/partials/deploy-git.md" >}}

{{< readfile file="/content/partials/link-addon.md" >}}

{{< readfile file="/content/partials/more-config.md" >}}
