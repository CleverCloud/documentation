---
type: docs
linkTitle: uv
title: Deploy Python with uv
description: Deploy Python applications with uv on Clever Cloud, from the uv.lock file of your project, with the command that starts your own web server
keywords:
- astral
- python uv
- uv
- uv deployment
- uv sync
aliases:
- /doc/applications/python/uv
---

## Overview

[uv](https://docs.astral.sh/uv/) is a package and project manager for Python. It installs the dependencies that `uv.lock` pins. With uv, your application starts its own web server, without NGINX in front of it. The [Python page](/doc/deploy/applications/python/) describes the Python version, the caches, and the tasks.

## Activate the uv mode

Clever Cloud deploys your application with uv when your project meets both conditions:

- A `uv.lock` file, at the root of the project or of the folder set in `CC_APP_FOLDER`
- `CC_PYTHON_UV_RUN_COMMAND`, which sets the command that starts your application

Otherwise, Clever Cloud deploys it in the [pip mode](/doc/deploy/applications/python/pip/). The `uv lock` command creates `uv.lock`, or updates it after a change of `pyproject.toml`.

## Build phase

On a new build, Clever Cloud runs the pre-build [hook](/doc/manage/build-hooks/), then installs the dependencies of `uv.lock`, without the development ones:

```bash
uv sync --locked --no-progress --no-dev
```

`--locked` fails the build when `uv.lock` doesn't match `pyproject.toml`: run `uv lock` and commit the result. To install the development dependencies too, such as for a test or preview application, set `ENVIRONMENT=development`.

## Start command

Clever Cloud runs `CC_PYTHON_UV_RUN_COMMAND` from the folder of your project. Start it with `uv run --no-dev`: without this option, `uv run` installs the development dependencies again when your application starts.

```bash
clever env set CC_PYTHON_UV_RUN_COMMAND "uv run --no-dev python main.py"
```

Your web server listens on `0.0.0.0`, on the port in `PORT`, `8080`. With a [Request Flow](/doc/manage/request-flow/) middleware, set `PORT=9000`. Read `PORT` in your code, as in the [example](/doc/deploy/applications/python/#mandatory-needs), or write the port in the command:

```bash
clever env set CC_PYTHON_UV_RUN_COMMAND "uv run --no-dev uvicorn main:app --host 0.0.0.0 --port 8080"
```

Clever Cloud runs this command without a shell: it doesn't expand variables, nor interpret quotes or operators such as `&&`. With `--port $PORT`, the deployment then fails with `'$PORT' is not a valid integer`.

## Shell command

`CC_RUN_COMMAND`, when set, replaces `CC_PYTHON_UV_RUN_COMMAND` at start, and runs in a shell, which expands `$PORT`. It starts from the root of the repository, even when `CC_APP_FOLDER` sets another folder, such as `app` here:

```bash
clever env set CC_RUN_COMMAND 'cd app && uv run --no-dev uvicorn main:app --host 0.0.0.0 --port $PORT'
```

The variables of the [pip mode](/doc/deploy/applications/python/pip/), such as `CC_PIP_REQUIREMENTS_FILE`, `CC_PYTHON_BACKEND`, or `CC_PYTHON_MODULE`, don't apply in the uv mode.

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/applications/python" title="Python" subtitle="Python version, caches, and tasks" icon="simple:python" >}}
  {{< card link="/developers/doc/deploy/applications/python/pip" title="pip" subtitle="Install with pip, and serve a WSGI or ASGI module behind NGINX" icon="server" >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
