---
type: docs
linkTitle: Servers
title: Python servers configuration
description: Configure uWSGI, Gunicorn, and Nginx settings for Python applications on Clever Cloud including static files, HTTPS, and basic authentication
keywords:
- uwsgi
- gunicorn
- nginx
- python server
- static files
---

## uWSGI, Gunicorn and Nginx configuration

> [!NOTE]
> This page applies to the legacy Python deployment mode (without `uv.lock`). [Native uv deployments](/doc/applications/python/uv/) manage their own HTTP server and do not use uWSGI, Gunicorn, or Nginx.

uWSGI, Gunicorn and Nginx settings can be configured by setting environment variables.

### uWSGI

| Name | Description | Default |
|------|-------------|---------|
| `HARAKIRI` | Timeout (in seconds) after which an unresponsive process is killed | `180` |
| `WSGI_BUFFER_SIZE` | Maximal size (in bytes) for the headers of a request | `4096` |
| `WSGI_POST_BUFFERING` | Buffer size (in bytes) for uploads | `4096` |
| `WSGI_WORKERS` | Number of workers | depends on the scaler |
| `WSGI_THREADS` | Number of threads per worker | depends on the scaler |

You can inject additional uWSGI configuration directives with `CC_UWSGI_EXTRA_CONFIG`. To disable the file wrapper, set `CC_UWSGI_DISABLE_FILE_WRAPPER` to `true`.

#### uWSGI asynchronous/non-blocking modes

To enable [uWSGI asynchronous](https://uwsgi-docs.readthedocs.io/en/latest/Async.html) mode, you can use these two environment variables:

- `UWSGI_ASYNC`: [number of cores](https://uwsgi-docs.readthedocs.io/en/latest/Async.html#async-switches) to use for uWSGI asynchronous/non-blocking modes.
- `UWSGI_ASYNC_ENGINE`: select the [asynchronous engine for uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/Async.html#suspend-resume-engines) (optional).

### Gunicorn

| Name | Description | Default |
|------|-------------|---------|
| `CC_GUNICORN_WORKER_CLASS` | Type of worker to use. [Available workers](https://docs.gunicorn.org/en/stable/settings.html#worker-class) | `sync` |
| `CC_GUNICORN_TIMEOUT` | Gunicorn timeout (in seconds) | `30` |
| `CC_GUNICORN_LOGLEVEL` | Gunicorn log level | `info` |

### Nginx

| Name | Description | Default |
|------|-------------|---------|
| `NGINX_READ_TIMEOUT` | Response timeout in seconds (similar to `HARAKIRI`) | `300` |
| `ENABLE_GZIP_COMPRESSION` | Enable gzip compression (`on`, `yes`, or `true`) | |
| `GZIP_TYPES` | The mime types to gzip | `text/plain text/css text/xml text/javascript application/json application/xml application/javascript image/svg+xml` |

#### Basic authentication

If you need basic authentication, you can enable it using [environment variables](/doc/reference/reference-environment-variables#python). Set `CC_HTTP_BASIC_AUTH` variable to your own `login:password` pair. If you need to allow access to multiple users, you can create additional environment `CC_HTTP_BASIC_AUTH_n` (where `n` is a number) variables.

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
        "/path": "redirection"
    },
    "charset": "latin-1"
}
```

## Manage static files

To enable Nginx to serve your static resources, you have to set two environment variables.

| Name | Description |
|------|-------------|
| `STATIC_FILES_PATH` | Directory where your static files are stored (absolute path relative to the application root) |
| `STATIC_URL_PREFIX` | URL path under which you want to serve static files (e.g. `/public`) |

You can also use a [Filesystem Bucket](/doc/addons/fs-bucket) to store your static files.

> [!WARNING]
> Setting `STATIC_URL_PREFIX` to `/` makes static files override the default application location. The static configuration replaces the main `location /` block in Nginx, and your application becomes accessible only through the `@app` fallback.

### Static files example

Here is how to serve static files, the `test.png` being the static file you want to serve:

```txt
├── <app_root>
│   ├── flask-app.py
│   ├── static
│   │   └── test.png
│   └── requirements.txt
```

Using the environment variables `STATIC_FILES_PATH=static/` and `STATIC_URL_PREFIX=/public` the `test.png` file will be accessed under: `https://<domain.tld>/public/test.png`.
