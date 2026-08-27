---
type: docs
linkTitle: Django
title: Deploy a Django application
description: Configure and deploy a Django application with uv and Uvicorn on Clever Cloud
keywords:
- django
- python
- uv
- uvicorn
- web framework
aliases:
- /doc/deploy/application/python/tutorials/python-django-sample
- /doc/python/python-django-sample
- /guides/django
- /python/python-django-sample
- /python-django-sample
---

{{< hextra/hero-subtitle >}}
  Deploy a Django application with uv and Uvicorn
{{< /hextra/hero-subtitle >}}

This guide uses the maintained [Clever Cloud Django example](https://github.com/CleverCloud/python-django-uv-example). Its committed `uv.lock` file lets the Python runtime install the exact dependency versions with [uv](https://docs.astral.sh/uv/).

## Prerequisites

- A [Clever Cloud account](https://console.clever-cloud.com)
- [Git](https://git-scm.com/downloads)
- [Clever Tools](/doc/cli), installed and connected to your account

## Clone the example application

Clone the repository and move into its directory:

```bash
git clone https://github.com/CleverCloud/python-django-uv-example.git myDjangoApp
cd myDjangoApp
```

## Create and configure the application

Create a Python application:

```bash
clever create -t python -a myDjangoApp
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

You can display your application’s URL or add a custom domain. A custom domain also requires DNS configuration:

```bash
clever domain
clever domain add your.website.tld
```

Configure the command used to start Uvicorn on the port expected by Clever Cloud:

```bash
clever env set CC_PYTHON_UV_RUN_COMMAND "uv run uvicorn --host 0.0.0.0 --port 8080 myDjango.asgi:application"
```

Native uv deployment is enabled by the combination of `uv.lock` and `CC_PYTHON_UV_RUN_COMMAND`. If you later add a [Request Flow middleware](/doc/develop/request-flow/#port-management), change the command to listen on port `9000`.

## Deploy the application

Deploy the repository and display the application:

```bash
clever deploy
clever open
```

The example uses SQLite for demonstration purposes. Local application files are not persistent on Clever Cloud, so configure a managed database such as [PostgreSQL](/doc/addons/postgresql/) before storing production data. Django documents the required [database settings and drivers](https://docs.djangoproject.com/en/stable/ref/databases/).

## Deploy an existing Django project

For an existing uv project, commit `pyproject.toml` and `uv.lock`, then adapt the module in `CC_PYTHON_UV_RUN_COMMAND` to your ASGI application. Configure hosts, secrets, static files and databases through [environment variables](/doc/develop/env-variables/) rather than committing production values.

Projects using `requirements.txt` instead of uv use the [legacy Python deployment mode](/doc/applications/python/#select-the-python-backend). Set `CC_PYTHON_MODULE` to the WSGI or ASGI module expected by the selected backend.

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/python/uv/" title="Python with uv" subtitle="Configure native uv deployment" icon="python" >}}
  {{< card link="/developers/doc/applications/python/" title="Python runtime" subtitle="Configure Python applications" icon="python" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://docs.djangoproject.com/en/stable/" title="Django documentation" subtitle="Build and configure Django applications" icon="django" >}}
{{< /cards >}}
