---
type: docs
linkTitle: Deploy with uv
title: Deploy Python with uv
description: Deploy Python applications with native uv support on Clever Cloud, using uv.lock for dependency management and direct HTTP server binding
keywords:
- uv
- python uv
- uv deployment
- uv sync
- astral
---

## Overview

[uv](https://docs.astral.sh/uv/) is a modern package and project manager for Python, built in Rust. Clever Cloud provides native uv deployment support as an alternative to the legacy WSGI-based deployment (uWSGI/Gunicorn + Nginx). With uv, your application manages its own HTTP server.

## Activation

Native uv deployment activates when both conditions are met:

- A `uv.lock` file exists at the root of your project
- The `CC_PYTHON_UV_RUN_COMMAND` environment variable is set to a valid command

If either condition is missing, the application deploys with the [legacy Python backend](/doc/applications/python/#select-the-python-backend).

## Build phase

During the build phase, dependencies are installed with:

```bash
uv sync --locked --no-progress --no-dev
```

To install development dependencies, set `ENVIRONMENT=development`. The `--no-dev` flag is then removed.

The uv cache (`~/.cache/uv`) is included in the build cache to speed up subsequent deployments.

- [Learn more about Deployment hooks](/doc/develop/build-hooks/)

## Run phase

The application starts with the command defined in `CC_PYTHON_UV_RUN_COMMAND`. It must start an HTTP server listening on `0.0.0.0:8080`.

`CC_RUN_COMMAND` takes precedence over `CC_PYTHON_UV_RUN_COMMAND` if both are set.

| Name | Description | Required | Default |
|------|-------------|----------|---------|
| `CC_PYTHON_UV_RUN_COMMAND` | Command to start the application (e.g. `uv run python app.py`) | Yes | - |
| `CC_RUN_COMMAND` | Overrides `CC_PYTHON_UV_RUN_COMMAND` if set | No | - |
| `ENVIRONMENT` | Set to `development` to include dev dependencies during build | No | `production` |

## Differences with legacy Python deployment

With native uv deployment:

- No Nginx, uWSGI, or Gunicorn is involved
- Your application listens on port `8080` (not `9000`)
- `CC_PYTHON_MODULE` and `CC_PYTHON_BACKEND` are ignored
- [Redirection.io, Varnish and custom proxies](/doc/develop/request-flow/) are configured through Request Flow, not Nginx
- [Server configuration](/doc/applications/python/servers/) settings do not apply

- [Learn more about uv](https://docs.astral.sh/uv/)

{{% content "url_healthcheck" %}}
{{% content "request-flow" %}}
