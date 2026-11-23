---
type: docs
linkTitle: Python
title: Python application runtime
description: Build and deploy Python applications on Clever Cloud with uv or pip, from a FastAPI or Flask application to Django with Celery, with the Python version of your choice
keywords:
- django
- fastapi
- flask
- gunicorn
- pip
- python
- python app hosting
- uv
aliases:
- /applications/python
- /deploy/application/python/python_apps
- /doc/applications/python
- /doc/deploy/application/python
- /doc/deploy/application/python/python-apps
- /doc/deploy/application/python/python/
- /doc/deploy/application/python/python_apps
- /doc/deploy/application/python/tutorials/python-flask-sample-app
- /doc/en/python-hosting
- /doc/getting-started/by-language/python
- /doc/partials/language-specific-deploy/python
- /doc/python
- /doc/python-hosting
- /doc/python/python_apps
- /doc/reference/python
- /python
- /python/python_apps
---

## Overview

[Python](https://www.python.org) is a dynamically typed language, used for web applications, APIs, and data processing. Clever Cloud installs the dependencies of your project with [uv](/doc/deploy/applications/python/uv/) or [pip](/doc/deploy/applications/python/pip/), then starts your application. It works with frameworks such as [Django](https://www.djangoproject.com), [FastAPI](https://fastapi.tiangolo.com), or [Flask](https://flask.palletsprojects.com).

## Create your Python application

To create a new Python application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](/doc/tools/cli/):

```bash
clever create --type python
```

The [getting started guide](/doc/getting-started/) describes each step of the creation of an application.

## Configure your Python application

### Mandatory needs

Clever Cloud deploys a Python application in one of two modes, from the files of your project and its variables:

- **uv**: with a `uv.lock` file and `CC_PYTHON_UV_RUN_COMMAND`, your application starts its own web server
- **pip**: otherwise, pip installs `requirements.txt`, and Clever Cloud starts a server behind NGINX

Prefer [uv](/doc/deploy/applications/python/uv/): your project sets its dependencies, its Python version, and its server. The [pip mode](/doc/deploy/applications/python/pip/) suits projects with a `requirements.txt` file and an application module, served by uWSGI, Gunicorn, Uvicorn, or Daphne.

For instance, a minimal [FastAPI](https://fastapi.tiangolo.com) application, which listens on `0.0.0.0` and on [the port in `PORT`](/doc/manage/#listen-on-the-right-port):

```toml {filename="pyproject.toml"}
[project]
name = "hello"
version = "1.0.0"
requires-python = ">=3.13"
dependencies = [
    "fastapi>=0.165",
    "uvicorn>=0.54",
]
```

```python {filename="main.py"}
import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello from FastAPI on Clever Cloud"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
```

Run `uv lock` to create `uv.lock`, commit it, then set the command that starts your application:

```bash
clever env set CC_PYTHON_UV_RUN_COMMAND "uv run --no-dev python main.py"
```

To try it locally, run `uv run python main.py`: it listens on port 8080. Your application reads its [environment variables](/doc/manage/environment-variables/) with `os.environ`, such as the credentials of the add-ons linked to it, or your own settings.

A [Clever Task](#python-applications-as-clever-tasks) doesn't need a web server.

### Python version

Clever Cloud uses Python {{< runtime_version python python3 >}} by default, `{{< runtime_version python >}}` in `CC_PYTHON_VERSION`. To use another version, set one of these values:

{{< runtimes_versions python >}}

In the uv mode, the version of a `.python-version` file, such as the one `uv python pin` writes, takes precedence. uv uses the Python of the image when it provides this version, and otherwise downloads it during the build.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit, with the installed dependencies. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

A new commit downloads the dependencies again: `CC_CACHE_DEPENDENCIES` doesn't keep the packages of pip or uv between commits.

## Python applications as Clever Tasks

A Python application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration. Clever Cloud installs its dependencies, then runs `CC_RUN_COMMAND` instead of starting a web server. The task stops when this command ends.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks). In the uv mode, set `CC_PYTHON_UV_RUN_COMMAND` too. A task doesn't run it, but it activates the uv mode: this example repeats the command of the task.

```bash
clever create --type python --task "uv run --no-dev python job.py"
clever env set CC_PYTHON_UV_RUN_COMMAND "uv run --no-dev python job.py"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/python/pip" title="pip" subtitle="Install with pip, and serve a WSGI or ASGI module behind NGINX" icon="server" >}}
  {{< card link="/developers/doc/deploy/applications/python/uv" title="uv" subtitle="Install with uv, and start your own web server" icon="simple:uv" >}}
{{< /cards >}}
