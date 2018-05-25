---
title: Deploying Python apps
position: 1
shortdesc: Python 2.7 and 3.6 are available on our platform. You can use Git to deploy your application.
tags:
- python
---

Python is a programming language that lets you work more quickly and integrate your systems more effectively.
You can learn how to use Python and see almost immediate gains in productivity and lower maintenance costs.


## Overview

Python 2.7 and 3.6 are available on our platform. You can use Git to deploy your application.


## Create an application

Refer to the page [Deploy an application on Clever Cloud](/doc/clever-cloud-overview/add-application/).

## Dependencies

You are granted to install external libs. As you can do on your workstation you can easily use **pip** and **requirements.txt**.

For example to install *Flask* and various libs you have to create a file `/requirements.txt` :

```javascript
SQLAlchemy==0.7.8
Flask==0.9
Flask-Admin==1.0.2
Flask-Assets==0.8
Flask-DebugToolbar==0.7.1
Flask-KVSession==0.3.2
Flask-Mail==0.8.2
Flask-SQLAlchemy==0.16
Flask-Script==0.5.3
Flask-WTF==0.8.3
webassets==0.8
pytz==2012d
psycopg2==2.4.5
```

### Cache dependencies

You can cache dependencies to avoid the installation at each deployment. Define the `CACHE_DEPENDENCIES`
variable to `true` to activate it. If dependencies have changed between deployments, the cache
will be updated.
Remove the environment variable or set it to `false` to disable this feature.

If you have any question, feel free to [contact our support](https://www.clever-cloud.com/doc/get-help/support/).


## Configuring the application

Python apps can be launched in a variety of ways. You can specify how to start your application
(for instance which module to run) by setting environment variables (in the "Environment variables" section of the console).

### Select your module

To select which module you want to start, use the `CC_PYTHON_MODULE` variable.

```
CC_PYTHON_MODULE="mymodule:app"
```

The module (without .py) must be importable, i.e. be in `PYTHONPATH`. For example with *Flask*, it's gonna be the name of
your main server file followed by your Flask object: `server:app` for example if you have a `server.py` file at the root
of your project with a Flask `app` object inside.

Basically, you should just point to a WSGI capable object.

### Celery apps

**Note**: Please note that Celery support is not available yet for `gunicorn`.

We also support celery apps out of the box. To deploy a celery app, use the
`CC_PYTHON_CELERY_MODULE` variable:

```
CC_PYTHON_CELERY_MODULE="mymodule"
```

You can also activate beat with `CC_PYTHON_CELERY_USE_BEAT=true` and provide a given log
dir for celery with `CC_PYTHON_CELERY_LOGFILE="/path/to/logdir"`.

The `CC_PYTHON_CELERY_LOGFILE` path is relative to the application's path.

## Select the python backend

Currently, we support `uwsgi` and `gunicorn` for python backends. To select one, set the
`PYTHON_BACKEND` environment variable with either `uwsgi` or `gunicorn`.

If not specified, the default backend is `uwsgi`.

## Using the Gevent loop engine

Whether you use uwsgi or gunicorn, you can enable the Gevent loop engine.

To do so, add the `CC_PYTHON_USE_GEVENT` environment variable to your application, with the `true` value.

## Manage your static files

To enable Nginx to serve your static resources, you have to set two environment variables.

`STATIC_FILES_PATH`: should point to a directory where your static files are stored.

`STATIC_URL_PREFIX`: the URL path under which you want to serve static files (e.g. `/public`)

Also, you are able to use a Filesystem Bucket to store your static files. Please refer to the
[File System Buckets](/doc/addons/clever-cloud-addons/#fs-buckets-file-system-with-persistance/) section.

**Note**: the path of your folder must be absolute regarding the root of your application.

**Note**: setting the `STATIC_URL_PREFIX` to `/` will make the deployment to fail.

### Example

Here is how to serve the static files, the `test.png` being the static file:
```
├── app
│   ├── flask-app.py
│   ├── static
│   │   └── test.png
│   └── requirements.txt
```

Using the environment variables:
```
STATIC_FILES_PATH=static/
STATIC_URL_PREFIX=/public
```

The `test.png` file will be accessed under: `https://<domain.tld>/public/test.png`

## Choose Python version

The default version of python on Clever Cloud is **2.7**. If you want to use python **3.6** instead,
create an environment variable `PYTHON_VERSION` equals to either `2` or `3`.

Also, the file `/clevercloud/python_version` is still supported for backward compatibility.
You have to write either `2` or `3` in it to select the python version. Please prefer the environment variable.

**Note**: the version is an integer, do not use quotes. values allowed are `2` and `3`.

## uWSGI, Gunicorn and Nginx configuration

uWSGI, gunicorn and nginx settings can be configured by setting environment variables:

### uWSGI

 - `HARAKIRI`: timeout (in seconds) after which an unresponding process is killed. (Default: 180)
 - `WSGI_BUFFER_SIZE`: maximal size (in bytes) for the headers of a request. (Defaut: 4096)
 - `WSGI_POST_BUFFERING`: buffer size (in bytes) for uploads. (Defaut: 4096)
 - `WSGI_WORKERS`: number of workers. (Defaut: depends on the scaler)
 - `WSGI_THREADS`: number of threads per worker. (Defaut: depends on the scaler)

### Gunicorn

 - `GUNICORN_WORKER_CLASS`: type of worker to use. Default to `sync`. [Available workers](http://docs.gunicorn.org/en/stable/settings.html#worker-class)

### Nginx

 - `NGINX_READ_TIMEOUT`: a bit like HARAKIRI, the response timeout in seconds. (Defaut: 300)
 - `ENABLE_GZIP_COMPRESSION`: "on|yes|true" gzip-compress the output of uwsgi.

## Nginx configuration

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

## Environment injection

Clever Cloud can inject environment variables that are defined in the dashboard and by add-ons linked to your application.

The access to these variables is simple: just get them as you would with any environment variable:

```python
import os
os.getenv("MY_VARIABLE")
```

## uWSGI asynchronous/non-blocking modes

To enable [uWSGI asynchronous](https://uwsgi-docs.readthedocs.io/en/latest/Async.html) mode, you can use these two environment variables:

 - `UWSGI_ASYNC`: [number of cores](https://uwsgi-docs.readthedocs.io/en/latest/Async.html#async-switches) to use for uWSGI asynchronous/non-blocking modes.
 - `UWSGI_ASYNC_ENGINE`: select the [asynchronous engine for uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/Async.html#suspend-resume-engines) (optional)

## Use setup.py

We support execution of a single `setup.py` goal. Usually, this would be to execute custom tasks after
the installation of dependencies.
To execute a goal, you can define the environment variable `PYTHON_SETUP_PY_GOAL="build"` (or any other goal).

The goal will be launched after the dependencies from `requirements.txt` have been installed.

## Manage.py tasks

We support execution of multiple `manage.py` tasks.

You can declare the `manage.py` tasks in `clevercloud/python.json`:

```json
{ "deploy": { "managetasks": [ "migrate" ]}}
```

The tasks are launched after the dependencies from `requirements.txt` have been installed.

## Git Deployment

*You will need git on your computer to deploy via this tool. Here is the official website of Git to get more
information: [git-scm.com](http://git-scm.com)*

### Setting up your remotes

1. The "Information" page of your app gives you your git deployment URL. It looks like this:
``git+ssh://git@push.clever-cloud.com/<your_app_id>.git``. Copy it in your clipboard.

2. On your computer, go into your application repository. 
If you didn't already track your app with **git**, start by typing:

    ```bash
    $ git init
    ```

3. Then, use the `git remote` command to add the deploy URL:

    ```bash
    $ git remote add <name> <your-git-deployment-url>
    ```

4. The last step is to push your application:

    ```bash
    $ git push <name> master
    ```

<div class="alert alert-hot-problems">
<h4>Warning:</h4>
  <p>The remote branch on Clever Cloud is <strong>ALWAYS</strong> master. If your local branch is not "master", use this syntax:</p>
  <pre>git push < name > yourbranch:master</pre>
</div>
