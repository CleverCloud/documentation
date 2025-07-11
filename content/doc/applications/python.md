---
type: docs
title: Python

shortdesc: Python 2.7 and 3.12 are available on our platform. You can use git to deploy your application.
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

### Supported Versions

The default version of Python on Clever Cloud is the latest we support from branch `3.x`. If you want to use Python `2.x`, create an [environment variable](#setting-up-environment-variables-on-clever-cloud) `CC_PYTHON_VERSION` set to `2`, it will default to Python 2.7. Other supported values are :

{{< runtimes_versions python >}}

{{< content "create-application" >}}

{{< content "set-env-vars" >}}

## Configure your Python application

### General configuration

Python apps can be launched in a variety of ways. You can specify how to start your application (for instance which module to run) by setting [environment variables](#setting-up-environment-variables-on-clever-cloud).

To select which module you want to start, use the `CC_PYTHON_MODULE` environment variable.

```bash
CC_PYTHON_MODULE="mymodule:app"
```

The module (without .py) must be importable, i.e. be in `PYTHONPATH`. Basically, you should just point to a WSGI capable object.

For example with *Flask*, it's gonna be the name of your main server file, followed by your Flask object: `server:app` for instance if you have a `server.py` file at the root of your project with a Flask `app` object inside.

You can also use `CC_RUN_COMMAND` to launch Python application your way. In such case, it must listen on port `9000`.

### Use uv as a package manager

Built in Rust, `uv` is a modern package and project manager for Python. It's fast to install dependencies, can be used as a drop-in replacement for `pip` and to sideload unsupported versions of Python. For example to use it with a `app.py` file, you just need to set `CC_RUN_COMMAND="uv run app.py"`. If your application listens on port `9000` with `0.0.0.0` as host, it will work fine on Clever Cloud.

* [Learn more about uv](https://github.com/astral-sh/uv)

{{< callout type="info" >}}
  `uv` is part of our Enthusiast tools initiative, it's included and can be used, but there is no active support for it yet.
{{< /callout >}}

### Select the python backend

Currently, we support `daphne`, `gunicorn`, `uvicorn` and `uwsgi` for Python backends. If not specified, the default backend is `uwsgi`.

To select one, set the `CC_PYTHON_BACKEND` [environment variable](#setting-up-environment-variables-on-clever-cloud) with either `daphne`, `gunicorn`, `uvicorn` or `uwsgi`.

Please contact the support if you need another backend.

### Dependencies

If you do not have a `requirements.txt` file to commit you can obtain it via the command `pip freeze > requirements.txt` (or `pip3 freeze > requirements.txt` if you use Python 3.x) at the root of your project folder in your terminal.

For example to install *PostgreSQL* and don't want to use the `pip freeze` command above you have to create a file `requirements.txt` at the root of your application folder:

```txt
psycopg2>=2.7 --no-binary psycopg2
```

**Note**: We recommend using `psycopg2>=2.7 --no-binary psycopg2` to avoid wsgi issues.

You can define a custom `requirements.txt` file with the environnement variable `CC_PIP_REQUIREMENTS_FILE` for example: `CC_PIP_REQUIREMENTS_FILE=config/production.txt`.

{{< content "cached-dependencies" >}}

### Use setup.py

We support execution of a single `setup.py` goal. Usually, this would be to execute custom tasks after the installation of dependencies.

The goal will be launched after the dependencies from `requirements.txt` have been installed.

To execute a goal, you can define the [environment variable](#setting-up-environment-variables-on-clever-cloud) `PYTHON_SETUP_PY_GOAL="<your goal>"`.

 {{< content "env-injection" >}}

To access [environment variables](#setting-up-environment-variables-on-clever-cloud) from your code, just get them from the environment with:

```python
import os
os.getenv("MY_VARIABLE")
```

### Manage your static files

To enable Nginx to serve your static resources, you have to set two [environment variables](#setting-up-environment-variables-on-clever-cloud).

`STATIC_FILES_PATH`: should point to a directory where your static files are stored.

`STATIC_URL_PREFIX`: the URL path under which you want to serve static files (e.g. `/public`).

Also, you are able to use a Filesystem Bucket to store your static files. Please refer to the [File System Buckets]({{< ref "doc/addons/fs-bucket" >}}) section.

**Note**: the path of your folder must be absolute regarding the root of your application.

**Note**: setting the `STATIC_URL_PREFIX` to `/` will cause the deployment failure.

#### Static files example

Here is how to serve static files, the `test.png` being the static file you want to serve:

```txt
├── <app_root>
│   ├── flask-app.py
│   ├── static
│   │   └── test.png
│   └── requirements.txt
```

Using the environment variables `STATIC_FILES_PATH=static/` and `STATIC_URL_PREFIX=/public` the `test.png` file will be accessed under: `https://<domain.tld>/public/test.png`.

### uWSGI, Gunicorn and Nginx configuration

uWSGI, gunicorn and nginx settings can be configured by setting [environment variables](#setting-up-environment-variables-on-clever-cloud):

#### uWSGI

- `HARAKIRI`: timeout (in seconds) after which an unresponding process is killed. (Default: 180)
- `WSGI_BUFFER_SIZE`: maximal size (in bytes) for the headers of a request. (Default: 4096)
- `WSGI_POST_BUFFERING`: buffer size (in bytes) for uploads. (Default: 4096)
- `WSGI_WORKERS`: number of workers. (Default: depends on the scaler)
- `WSGI_THREADS`: number of threads per worker. (Default: depends on the scaler)

##### uWSGI asynchronous/non-blocking modes

To enable [uWSGI asynchronous](https://uwsgi-docs.readthedocs.io/en/latest/Async.html) mode, you can use these two environment variables:

- `UWSGI_ASYNC`: [number of cores](https://uwsgi-docs.readthedocs.io/en/latest/Async.html#async-switches) to use for uWSGI asynchronous/non-blocking modes.
- `UWSGI_ASYNC_ENGINE`: select the [asynchronous engine for uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/Async.html#suspend-resume-engines) (optional).

#### Gunicorn

- `GUNICORN_WORKER_CLASS`: type of worker to use. Default to `sync`. [Available workers](https://docs.gunicorn.org/en/stable/settings.html#worker-class)
- `CC_GUNICORN_TIMEOUT`: gunicorn timeout. Defaults to `30`

#### Nginx

- `NGINX_READ_TIMEOUT`: a bit like `HARAKIRI`, the response timeout in seconds. (Default: 300)
- `ENABLE_GZIP_COMPRESSION`: "on|yes|true" gzip-compress the output.
- `GZIP_TYPES`: the mime types to gzip. Defaults to `text/* application/json application/xml application/javascript image/svg+xml`.

##### Basic authentication

If you need basic authentication, you can enable it using [environment variables]({{< ref "doc/reference/reference-environment-variables.md#python" >}}). You will need to set `CC_HTTP_BASIC_AUTH` variable to your own `login:password` pair. If you need to allow access to multiple users, you can create additional environment `CC_HTTP_BASIC_AUTH_n` (where `n` is a number) variables.

#### Nginx optional configuration with `clevercloud/http.json`

Nginx settings can be configured further in `clevercloud/http.json`. All its fields are optional.

- `languages`: configure a default language and redirections
- `error_pages`: configure custom files for error pages
- `force_https`: automatically redirect HTTP traffic to HTTPS
- `aliases`: set up redirections
- `charset`: force a specific charset

```json
{
    "languages": {
        "default": {"rewrite": "en"},
        "fr": {"rewrite": "en"}
    },
    "error_pages": {
        "404": "path/to/page"
    },
    "force_https": true,
    "aliases": {
        "/path": "redirection"
    },
    "charset": "latin-1"
}
```

### Using the Gevent loop engine

Whether you use uwsgi or gunicorn, you can enable the Gevent loop engine.

To do so, add the `CC_PYTHON_USE_GEVENT` [environment variable](#setting-up-environment-variables-on-clever-cloud) to your application, with the `true` value.

 {{< content "new-relic" >}}

## Celery apps

**Note**: Please note that Celery support is not available yet for `gunicorn`.

We also support celery apps out of the box. To deploy a celery app, use the `CC_PYTHON_CELERY_MODULE` [environment variable](#setting-up-environment-variables-on-clever-cloud):

```bash
CC_PYTHON_CELERY_MODULE="mymodule"
```

{{< callout type="warning" >}}
Celery needs to be defined as a dependency in your requirements.txt. Otherwise the deployment will be aborted if Celery support is enabled.
{{< /callout >}}

You can also activate beat with `CC_PYTHON_CELERY_USE_BEAT=true` and provide a given log dir for celery with `CC_PYTHON_CELERY_LOGFILE="/path/to/logdir"`.

The `CC_PYTHON_CELERY_LOGFILE` path is relative to the application's path.

{{< callout type="warning"  >}}
There is a bug in versions <4.2 of Celery. You need to add the `CELERY_TIMEZONE = 'UTC'` environment variable. The bug is documented here: [https://GitHub.com/celery/celery/issues/4184](https://GitHub.com/celery/celery/issues/4184).
{{< /callout >}}

{{< content "deploy-git" >}}

{{< content "link-addon" >}}

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}
