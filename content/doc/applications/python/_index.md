---
type: docs
linkTitle: Python
title: Python application runtime
description: Deploy Python 2 and 3 applications with uv support, Django, Flask, various frameworks, and configurable runtime settings
keywords:
- django
- fastapi
- flask
- pip
- python app hosting
- python cloud
- uv deployment
- uv native support
aliases:
- /applications/python
- /deploy/application/python/python_apps
- /doc/applications/python
- /doc/deploy/application/python
- /doc/deploy/application/python/python_apps
- /doc/en/python-hosting
- /doc/getting-started/by-language/python
- /doc/partials/language-specific-deploy/python
- /doc/python
- /doc/python/python_apps
- /doc/python-hosting
- /doc/reference/python
- /python
- /python/python_apps
---

## Overview

Python is a programming language that lets you work more quickly and integrate your systems more efficiently.

## Create your Python application

To create a new Python application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type python
```
- [Learn more about Clever Tools](/doc/cli/)
- [Learn more about Clever Cloud application deployment](/doc/quickstart/#create-an-application-step-by-step)

## Configure your Python application

### Mandatory needs

Python apps can be launched in a variety of ways. To select which module you want to start, use the `CC_PYTHON_MODULE` environment variable.

```bash
CC_PYTHON_MODULE="mymodule:app"
```

The module (without .py) must be importable, that is, be in `PYTHONPATH`. You should point to a WSGI-capable object.

For example, with *Flask*, this is the name of your main server file, followed by your Flask object: `server:app`, if you have a `server.py` file at the root of your project with a Flask `app` object inside.

You can also use `CC_RUN_COMMAND` to launch a Python application with a custom command. In such case, it must listen on port `9000`.

- [Learn more about environment variables on Clever Cloud](/doc/reference/reference-environment-variables/)

### Python version

The default version of Python on Clever Cloud is the latest supported from branch `3.x`. If you want to use Python `2.x`, set `CC_PYTHON_VERSION` to `2`, it will default to Python 2.7. Other supported values are:

{{< runtimes_versions python >}}

### Build phase

#### Dependencies

If you do not have a `requirements.txt` file to commit you can obtain it via the command `pip freeze > requirements.txt` (or `pip3 freeze > requirements.txt` if you use Python 3.x) at the root of your project folder in your terminal.

For example, if you want to install *PostgreSQL* without using the `pip freeze` command above, create a `requirements.txt` file at the root of your application folder:

```txt
psycopg2>=2.7 --no-binary psycopg2
```

> [!NOTE]
> Using `psycopg2>=2.7 --no-binary psycopg2` is recommended to avoid WSGI issues.

You can define a custom `requirements.txt` file with the environment variable `CC_PIP_REQUIREMENTS_FILE` for example: `CC_PIP_REQUIREMENTS_FILE=config/production.txt`.

{{% content "cached-dependencies" %}}

#### Use setup.py

Execution of a single `setup.py` goal is supported. Usually, this would be to execute custom tasks after the installation of dependencies.

The goal will be launched after the dependencies from `requirements.txt` have been installed.

To execute a goal, define the environment variable `PYTHON_SETUP_PY_GOAL="<your goal>"`.

- [Learn more about Deployment hooks](/doc/develop/build-hooks/)

### Select the Python backend

Currently, `daphne`, `gunicorn`, `uvicorn` and `uwsgi` are supported for Python backends. If not specified, the default backend is `uwsgi`.

To select one, set the `CC_PYTHON_BACKEND` environment variable with either `daphne`, `gunicorn`, `uvicorn` or `uwsgi`.

Contact the support if you need another backend.

> [!NOTE]
> Backend selection only applies to the legacy deployment mode (without `uv.lock`). [Native uv deployments](/doc/applications/python/uv/) manage their own HTTP server.

### Using the Gevent loop engine

Whether you use uwsgi or gunicorn, you can enable the Gevent loop engine.

To do so, add the `CC_PYTHON_USE_GEVENT` environment variable to your application, with the `true` value.

## Celery apps

Celery apps are supported out of the box. To deploy a celery app, use the `CC_PYTHON_CELERY_MODULE` environment variable:

```bash
CC_PYTHON_CELERY_MODULE="mymodule"
```

> [!WARNING]
> Celery needs to be defined as a dependency in your requirements.txt. Otherwise the deployment will be aborted if Celery support is enabled.

You can also activate beat with `CC_PYTHON_CELERY_USE_BEAT=true` and provide a given log dir for celery with `CC_PYTHON_CELERY_LOGFILE="/path/to/logdir"`.

The `CC_PYTHON_CELERY_LOGFILE` path is relative to the application's path.

> [!WARNING]
> There is a bug in versions <4.2 of Celery. You need to add the `CELERY_TIMEZONE = 'UTC'` environment variable. The bug is documented here: [https://github.com/celery/celery/issues/4184](https://github.com/celery/celery/issues/4184).

{{% content "new-relic" %}}

{{% content "url_healthcheck" %}}
{{% content "request-flow" %}}
