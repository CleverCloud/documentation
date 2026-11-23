---
type: docs
linkTitle: pip
title: Deploy Python with pip
description: Deploy Python applications with pip on Clever Cloud, served by uWSGI, Gunicorn, Uvicorn, or Daphne behind NGINX, with static files, Django tasks, and Celery
keywords:
- celery
- daphne
- django
- gunicorn
- nginx
- pip
- static files
- uvicorn
- uwsgi
aliases:
- /doc/applications/python/servers
- /doc/deploy/applications/python/servers
---

## Overview

Without the [uv mode](/doc/deploy/applications/python/uv/), Clever Cloud installs the dependencies of `requirements.txt` with pip, in a virtual environment. It then serves your application module with a Web Server Gateway Interface (WSGI) or Asynchronous Server Gateway Interface (ASGI) server, behind NGINX. NGINX also serves your static files. The [Python page](/doc/deploy/applications/python/) describes the Python version, the caches, and the tasks.

## Configure your application

### Mandatory needs

A Python application in the pip mode needs:

- A `requirements.txt` file, at the root of the project or of the folder set in `CC_APP_FOLDER`
- The module and the object of your application, in `CC_PYTHON_MODULE`

For instance, a minimal [Flask](https://flask.palletsprojects.com) application:

```text {filename="requirements.txt"}
flask>=3.1
```

```python {filename="app.py"}
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Flask on Clever Cloud"
```

```bash
clever env set CC_PYTHON_MODULE app:app
```

`app:app` names the `app` object of `app.py`. With Django, it's the WSGI module of the project, such as `mysite.wsgi:application`. Clever Cloud starts the server, so your code doesn't listen on a port.

### Build phase

On a new build, Clever Cloud creates a virtual environment, runs the pre-build [hook](/doc/manage/build-hooks/), then installs your dependencies:

```bash
python -m venv ~/venv
pip install -r requirements.txt
```

To install another file, set its path in `CC_PIP_REQUIREMENTS_FILE`, such as `requirements/prod.txt`. To install a given version of pip before your dependencies, such as `26.3`, set it in `CC_PIP_VERSION`: otherwise, the build uses the pip of the virtual environment.

To run a goal of `setup.py` after the installation, such as `build_ext`, set it in `CC_PYTHON_SETUP_PY_GOAL`.

### Django tasks

To run tasks of `manage.py` after the installation, such as the migrations, list them in `CC_PYTHON_MANAGE_TASKS`, separated by commas. Each task runs as `python manage.py <task>`, and a failing task stops the build:

```bash
clever env set CC_PYTHON_MANAGE_TASKS "migrate, collectstatic --noinput"
```

## Select the server

`CC_PYTHON_BACKEND` selects the server that runs your application module behind NGINX:

- `daphne`, for an ASGI application
- `gunicorn`, for a WSGI application
- `uvicorn`, for an ASGI application, such as FastAPI
- `uwsgi`, for a WSGI application, by default

Add the server to `requirements.txt`, except uWSGI, which the image provides. Otherwise, the build fails with an error such as `gunicorn requested but not present in requirements.txt`, before installing the dependencies.

The image provides uWSGI for Python 3.9 to 3.13. With Python 3.14, uWSGI fails to start, and the deployment ends with `Nginx is not running`. To use this version, select another server, such as Gunicorn.

### Server settings

With a single core, Clever Cloud starts two workers, and otherwise twice the number of cores minus one. Gunicorn also uses this number for the threads of each worker. `CC_UWSGI_WORKERS` sets another number, for both servers. These variables change the settings of uWSGI:

| Name                            | Description                                                                   | Default |
| ------------------------------- | ----------------------------------------------------------------------------- | ------- |
| `CC_PYTHON_USE_GEVENT`          | Run the requests with the `gevent` package, which `requirements.txt` must add |         |
| `CC_UWSGI_ASYNC`                | Number of asynchronous cores per worker                                       |         |
| `CC_UWSGI_ASYNC_ENGINE`         | Line to add to the configuration with `CC_UWSGI_ASYNC`, such as `gevent=10`   |         |
| `CC_UWSGI_DISABLE_FILE_WRAPPER` | Disable the WSGI file wrapper                                                 |         |
| `CC_UWSGI_EXTRA_CONFIG`         | Lines to add to the configuration, such as `max-requests=1000`                |         |
| `CC_UWSGI_HARAKIRI`             | Time in seconds after which uWSGI recycles the worker of a request            | `180`   |

These variables change the settings of Gunicorn:

| Name                       | Description                                          | Default |
| -------------------------- | ---------------------------------------------------- | ------- |
| `CC_GUNICORN_LOGLEVEL`     | Log level                                            | `info`  |
| `CC_GUNICORN_TIMEOUT`      | Time in seconds after which a silent worker restarts | `30`    |
| `CC_GUNICORN_WORKER_CLASS` | Worker class, such as `gevent`                       | `sync`  |

### Custom run command

To start something else, set `CC_RUN_COMMAND`. Clever Cloud runs it without a shell: it doesn't expand variables, such as `$PORT`, nor interpret quotes. It doesn't check `CC_PYTHON_MODULE`, and doesn't start Celery or apply the server settings.

NGINX stays in front of your command, which listens on `127.0.0.1:9000`. If your command reads `PORT`, set `PORT=9000`: otherwise, it tries the port of NGINX, and the deployment fails with `address already in use`:

```bash
clever env set CC_RUN_COMMAND "gunicorn --bind 127.0.0.1:9000 app:app"
```

## NGINX

### Static files

NGINX serves your static files without your application: set their folder in `STATIC_FILES_PATH`, from the root of the repository:

```bash
clever env set STATIC_FILES_PATH static/
```

NGINX then serves the files of this folder with a usual static extension, such as `.css`, `.js`, or `.png`, at the same path: `static/robots.txt` at `/robots.txt`. It forwards the other requests to your application. To serve the whole folder under a path instead, set this path in `STATIC_URL_PREFIX`: with `/static`, `static/logo.png` is at `/static/logo.png`.

With `STATIC_URL_PREFIX=/`, NGINX looks for each request in the folder first, and forwards to your application the ones it doesn't find there. For the files that Django `collectstatic` gathers in its `STATIC_ROOT`, such as `staticfiles`:

```bash
clever env set STATIC_FILES_PATH staticfiles/
clever env set STATIC_URL_PREFIX /static
```

### NGINX settings

NGINX compresses the static files: set `ENABLE_GZIP_COMPRESSION=true` to compress the responses of your application too. `GZIP_TYPES` then sets the media types to compress, separated by spaces, such as `application/json`. `NGINX_READ_TIMEOUT` sets how long, in seconds, NGINX waits for data from your application, `300` by default.

To protect your application with HTTP basic authentication, set `CC_HTTP_BASIC_AUTH` to a `login:password` pair: NGINX asks for it before passing requests to your application. For more users, add `CC_HTTP_BASIC_AUTH_1`, `CC_HTTP_BASIC_AUTH_2`, and so on.

In `clevercloud/http.json`, `aliases` serve a path with another one, without a redirection:

```json {filename="clevercloud/http.json"}
{
  "aliases": {
    "/old-hello": "/"
  }
}
```

To redirect the browser instead, such as from an old path to a new one, use [Redirection.io](/doc/manage/request-flow/redirectionio/) through [Request Flow](/doc/manage/request-flow/).

## Celery

To run a [Celery](https://docs.celeryq.dev) worker next to your application, whatever its server, set its module in `CC_PYTHON_CELERY_MODULE`, the value of `celery -A`. Add Celery to `requirements.txt`, with the client of its broker, such as `celery[redis]` for a [Redis](/doc/deploy/databases/redis/) add-on:

```bash
clever env set CC_PYTHON_CELERY_MODULE mysite
```

With uWSGI, `CC_PYTHON_CELERY_LOGFILE` writes the logs of the worker to a file, from the root of your application, such as `logs/celery.log`. Don't set it with another server: the worker then fails to start.

To also run Celery beat, which sends the periodic tasks, set `CC_PYTHON_CELERY_USE_BEAT=true`. Clever Cloud starts them with your application, on each instance: with several instances, each one sends the periodic tasks, which then run more than once.

For a periodic job that doesn't run on every instance, use a [cron](/doc/manage/cron/#avoid-duplicate-runs) that checks `INSTANCE_NUMBER`, or a [Clever Task](/doc/deploy/tasks/).

## New Relic

To monitor your application with [New Relic](/doc/observability/new-relic/), add `newrelic` to `requirements.txt`, and set `NEW_RELIC_LICENSE_KEY`. Clever Cloud then starts the server with `newrelic-admin run-program`, which loads the agent.

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/python" title="Python" subtitle="Python version, caches, and tasks" icon="simple:python" >}}
  {{< card link="/developers/doc/deploy/applications/python/uv" title="uv" subtitle="Install with uv, and start your own web server" icon="simple:uv" >}}
  {{< card link="/developers/guides/frameworks/django" title="Django" subtitle="Deploy a Django application with uv and Uvicorn" icon="simple:django" >}}
  {{< card link="/developers/doc/observability/new-relic" title="New Relic" subtitle="Monitor your application with New Relic" icon="chart-pie" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
