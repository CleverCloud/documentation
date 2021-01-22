---
title: Environment Variable Reference
position: 3
shortdesc: List of all the environment variable references
tags:
- reference
keywords:
- env
- env variables
---

## Commons to all Applications

### Set by the deployment process

These are read-only variables that are generated for each scaler before they build and start your application.

 {{<table "table table- bordered" "text-align : center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Example value</center> |
 |-----------------------|------------------------------|--------------------------------|
 |[INSTANCE_NUMBER]({{< ref "develop/env-variables.md" >}}) | Allows your application to differentiate each running node on the application level. | 0, 1… |
 |INSTANCE_TYPE | Whether this instance is a "build" instance or a "production" instance. | build, production |
 |INSTANCE_ID | The ID of the current instance (scaler) of your application. It's unique for each instance of your application and changes every time you deploy it. | 518c8d8f-e304-4310-81e0-9c4237d55645 |
 |CC_PRETTY_INSTANCE_NAME | The random generated string as instance pretty name using pokemon names. | Tiny rhyhorn |
 |APP_ID | The ID of your Clever Cloud application | app_649a93d1-6677-44bc-aca7-6f46107d6e02 |
 |APP_HOME | The absolute path to your application folder | /home/bas/app_649a93d1-6677-44bc-aca7-6f46107d6e02 |
 |CC_DEPLOYMENT_ID | Internal id of current deployment | f7efaf04-1a63-45a1-8503-0de7c750ee48 |
 |COMMIT_ID | The id of the commit that's currently running | d88cd2ae1aaa91923ed2bd689d95d713b6f3f45f |
 |CC_REVERSE_PROXY_IPS | A comma separated list of trusted IP addresses. You should only accept requests  coming from these IP addresses. | x.y.z.z,x.y.z.z |
 |ELASTIC_APM_SERVICE_NAME | Sets the name of your service/application in Elastic APM. Automatically defined when you have linked an Elastic APM service to your application. You can override it by defining it yourself | Your application's name conforming to Elastic APM naming convention |
 |CC_CLAMAV | Start the clamav and clamav-freshclam services (the database is updated every 2 hours). WARNING: Clamscan consumes a lot of resources (~ 1GB of memory), make sure you have a scaler with enough memory to avoid OOM. | false, true |
 {{< /table >}}

### Variables you can define

So you can alter the build&start process for your application.

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> |
 |-----------------------|------------------------------|--------------------------------|
 |APP_FOLDER | Folder in which the application is located (inside the git repository) |  |
 |[CC_TROUBLESHOOT](({{< ref "find-help/troubleshooting.md" >}}) | Enable debug log level, will also keep the VM up after failure for 15 minutes so you can SSH and debug. Don't forget to cancel deployment if you push a new commit. | `false` |
 |[CC_WORKER_COMMAND]({{< ref "reference/common-configuration.md#workers" >}}) | Command to run in background as a worker process. You can run multiple worker. |  |
 |CC_WORKER_RESTART | One of `always`, `on-failure` or `no`. Control whether workers need to be restarted when they exit.<br />This setting controls all workers. | on-failure |
 |CC_PRE_BUILD_HOOK | Ran before the dependencies are fetched. If it fails, the deployment fails. |  |
 |CC_POST_BUILD_HOOK | Ran after the project is built, and before the cache archive is generated. If it fails, the deployment fails. |  |
 |CC_PRE_RUN_HOOK | Ran before the application is started, but after the cache archive has been generated. If it fails, the deployment fails. |  |
 |CC_RUN_SUCCEEDED_HOOK | Ran once the application has started successfuly. |  |
 |CC_RUN_FAILED_HOOK | Ran once the application has failed to start. |  |
 |CC_CACHE_DEPENDENCIES | Enable caching of your build dependencies to speed up following builds. | `false` |
 |CC_SSH_PRIVATE_KEY | A ssh private key to setup for the user running your application |  |
 |CC_SSH_PRIVATE_KEY_FILE | The name to use for the file containing the private ssh key | id_ed25519 |
 |CC_DISABLE_METRICS | Disable metrics collection. | `false` |
 |[IGNORE_FROM_BUILDCACHE]({{< ref "develop/env-variables.md#settings-you-can-define-using-environment-variables" >}}) | Allows to specify paths to ignore when the build cache archive is created. |  |
 |[CC_OVERRIDE_BUILDCACHE]({{< ref "develop/env-variables.md#settings-you-can-define-using-environment-variables" >}}) | Allows to specify paths that will be in the build cache. <br />Only those files / directories will be cached |  |
 |[CC_METRICS_PROMETHEUS_PORT]({{< ref "administrate/metrics/overview.md#publish-your-own-metrics" >}}) | Define the port on which the Prometheus endpoint is available | `8080` |
 |[CC_METRICS_PROMETHEUS_PATH](({{< ref "administrate/metrics/overview.md#publish-your-own-metrics" >}}) | Define the path on which the Prometheus endpoint is available | `/metrics` |
 {{< /table >}}

## Docker

[Docker Documentation]({{< ref "deploy/application/docker/docker.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |CC_MOUNT_DOCKER_SOCKET | Set to true to access the host Docker socket from inside your container. | `false` |  |
 |CC_DOCKER_EXPOSED_HTTP_PORT | Set to custom HTTP port if your Docker container runs on custom port. | `8080` |  |
 |CC_DOCKER_EXPOSED_TCP_PORT | Set to custom TCP port if your Docker container runs on custom port but **it still needs a support request to make use of it.** | `4040` |  |
 |CC_DOCKER_FIXED_CIDR_V6 | Activate the support of IPv6 with an IPv6 subnet int the docker daemon. |  |  |
 {{< /table >}}

## Go

[Go Documentation]({{< ref "deploy/application/golang/go.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |CC_GO_PKG | Makes the deployer run go get ${CC_GO_PKG} instead of go get &lt;app_id&gt;.  |  |  |
 |CC_GO_BUILD_TOOL |Available values: `gomod`, `gobuild`, `goget`. Makes the deployer use `go modules`, `go get` or `go build` to build your application. |`goget` | |
 |CC_GO_RUNDIR | Makes the deployer use the specified directory to run your binary.<br>If your application must be in `$GOPATH/src/company/project` for your vendored dependencies, set this variable to `company/project` |  | |
 {{< /table >}}

## Haskell

[Haskell Documentation]({{< ref "deploy/application/haskell/haskell.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |CC_RUN_COMMAND | Custom command to run your application. |  |  |
 {{< /table >}}

## Java

[Java Documentation]({{< ref "deploy/application/java/java-jar.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |CC_SBT_TARGET_DIR | Define where pick the bin to run. | `.` | Then `/target/universal/stage/bin` is concatenated. |
 |CC_SBT_TARGET_BIN | Define the bin to pick in the `CC_SBT_TARGET_DIR`. | The first bin found in the `CC_SBT_TARGET_DIR`. |  |
 |GRADLE_DEPLOY_GOAL | Define which gradle goals to run during build. |  |  |
 |CC_JAVA_VERSION | Choose the JVM version between `7` to `14` for OpenJDK or `graalvm-ce` for GraalVM 20.1.0 (based on OpenJDK 11.0). | `11` |  |
 |MAVEN_DEPLOY_GOAL | Define which maven goals to run during build. |  |  |
 |CC_MAVEN_PROFILES | Define which maven profile to use during default build. |  |  |
 |NUDGE_APPID |  |  |  |
 |PLAY1_VERSION | Define which play1 version to use between `1.2`, `1.3`, `1.4` and `1.5` |  |  |
 |SBT_DEPLOY_GOAL | Define which sbt goals to run during build. | `stage` |  |
 |CC_JAR_PATH | Define the path to your jar. |  |  |
 |CC_EXTRA_JAVA_ARGS | Define extra arguments to pass to 'java' for jars. |  |  |
 |CC_JAR_ARGS | Define arguments to pass to the jar we launch. |  |  |
 |CC_RUN_COMMAND | Custom command to run your application. Replaces the default behaviour. |  |  |
 {{< /table >}}

## NodeJS

[NodeJS Documentation]({{< ref "deploy/application/javascript/by-framework/nodejs.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |CC_NODE_DEV_DEPENDENCIES | Control if development dependencies are installed or not. Values are either `install` or `ignore` | `ignore` |  |
 |CC_NODE_START_GOAL | Defines which node scripts to run | `start` |  |
 |CC_RUN_COMMAND | Define a custom command. | Example for Meteor: `node .build/bundle/main.js &lt;options&gt;` |  |
 |NODE_BUILD_TOOL | Choose your build tool between `npm` and `yarn` | `npm` |  |
 |CC_NPM_REGISTRY | The host of your private repository, available values: `github` or the registry host. | registry.npmjs.org |  |
 |NPM_TOKEN | Private repository token |  |  |
 {{< /table >}}

## PHP

[PHP Documentation]({{< ref "deploy/application/php/php-apps.md" >}})


 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |ALWAYS_POPULATE_RAW_POST_DATA |  |  |  |
 |CC_LDAP_CA_CERT |  |  |  |
 |CC_WEBROOT | Define the `DocumentRoot` of your project | . |  |
 |LDAPTLS_CACERT |  |  |  |
 |ENABLE_REDIS |  | `false` |  |
 |HTTP_TIMEOUT | Define a custom HTTP timeout | `180` |  |
 |MAX_INPUT_VARS |  |  |  |
 |CC_PHP_VERSION | Choose your PHP version between `5.6`, `7.2`, `7.3`, `7.4` and `8.0` | `7` |  |
 |CC_COMPOSER_VERSION | Choose your composer version between `1` and `2` | `2` |  |
 |[SESSION_TYPE]({{< ref "deploy/application/php/php-apps.md#use-redis-to-store-php-sessions" >}}) | Choose `redis` to use it as session store |  |  |
 |SOCKSIFY_EVERYTHING |  |  |  |
 |USE_SOCKS |  | `false` |  |
 |CC_OPCACHE_MEMORY | Set the shared opcache memory size | Default is about 1/8 of the RAM |  |
 |CC_OPCACHE_MAX_ACCELERATED_FILES | Maximum number of files handled by opcache. | Default depends on the scaler size |  |
 |CC_OPCACHE_INTERNED_STRINGS_BUFFER | The amount of memory used to store interned strings, in megabytes. | Default 4 (PHP5), 8 (PHP7) |  |
 |CC_MTA_SERVER_HOST | Host of the SMTP server |  |  |
 |CC_MTA_SERVER_PORT | Port of the SMTP server | 465 |  |
 |CC_MTA_AUTH_USER | User to authenticate to the SMTP server |  |  |
 |CC_MTA_AUTH_PASSWORD | Password to authenticate to the SMTP server |  |  |
 |CC_MTA_USE_TLS | Enable or disable TLS when connecting to the SMTP server | true |  |
 |CC_MTA_AUTH_METHOD | Enable or disable authentication to the SMTP server | on |  |
 |SQREEN_API_APP_NAME | The name of your sqreen application. |  |  |
 |SQREEN_API_TOKEN | Organization token. |  |  |
 {{< /table >}}

## Python

[Python Documentation]({{< ref "deploy/application/python/python_apps.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |CC_PYTHON_CELERY_LOGFILE | Relative path to your Celery logfile: `/path/to/logdir`  |  |  |
 |CC_PYTHON_CELERY_MODULE | Specify the Celery module you want to start: `mymodule` |  |  |
 |CC_PYTHON_CELERY_USE_BEAT | Set to `true` to activate Beat support |  |  |
 |CC_PYTHON_MODULE | Select which module you want to start: `mymodule:app`. 'mymodule' refers to the path to the folder containing the app object. So a module called 'server.py' in a folder called 'app' would be used here as `app.server:app` |  |  |
 |CC_PYTHON_USE_GEVENT | Set to `true` to enable Gevent |  |  |
 |HARAKIRI | Timeout (in seconds) after which an unresponding process is killed | `180` |  |
 |CC_PYTHON_BACKEND | Choose the Python backend to use between `uwsgi` and `gunicorn` | `uwsgi` |  |
 |CC_PYTHON_VERSION | Choose the Python version between `2.7`, `3.6`, `3.7` and `3.8` |  |  |
 |PYTHON_SETUP_PY_GOAL | Custom setup goal to be launch after `requirements.txt` have been installed |  |  |
 |STATIC_FILES_PATH | Relative path to where your static files are stored: `path/to/static` |  |  |
 |[STATIC_URL_PREFIX]({{< ref "deploy/application/python/python_apps.md#configure-your-python-application" >}}) | The URL path under which you want to serve static file, usually `/public` |  |  |
 |STATIC_WEBROOT |  |  |  |
 |UWSGI_INTERCEPT_ERRORS |  |  |  |
 |[UWSGI_ASYNC](/{{< ref "deploy/application/python/python_apps.md#configure-your-python-application" >}}) | Number of cores to use for uWSGI asynchronous/non-blocking modes |  |  |
 |UWSGI_ASYNC_ENGINE | Select the asynchronous engine for uWSGI (optional) |  |  |
 |WSGI_WORKERS | Number of workers. (Defaut: automatically setup with the scaler size) |  |  |
 |WSGI_THREADS | Number of threads per worker. (Defaut: automatically setup with the scaler size) |  |  |
 |WSGI_BUFFER_SIZE | Buffer size (in bytes) for uploads. | `4096` |  |
 |WSGI_POST_BUFFERING | Maximal size (in bytes) for the headers of a request.  | `4096` |  |
 |ENABLE_GZIP_COMPRESSION | Set to `true` to gzip-compress the output of uwsgi |  |  |
 |GZIP_TYPES | Set the mime types to compress. | `text/* application/json application/xml application/javascript image/svg+xml` |  |
 |NGINX_READ_TIMEOUT | Read timeout in seconds | `300` |  |
 |CC_NGINX_PROXY_BUFFER_SIZE | Sets the size of the buffer used for reading the first part of the response received from the proxied server. <a href="https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_buffer_size" target="_blank" rel="noreferrer noopener">Nginx documentation</a> |  |  |
 |CC_NGINX_PROXY_BUFFERS | Sets the number and size of the buffers used for reading a response from the proxied server, for a single connection. <a href="https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_buffers" target="_blank" rel="noreferrer noopener">Nginx documentation</a> |  |  |
 {{< /table >}}

## Ruby

[Ruby Documentation]({{< ref "deploy/application/ruby/ruby-rack.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |CC_RACKUP_SERVER | The server to use for serving the ruby application | puma |  |
 |RACK_ENV |  |  |  |
 |RAILS_ENV |  |  |  |
 |RUBY_VERSION | Choose the Ruby version to use. |  |  |
 |STATIC_FILES_PATH | Relative path to where your static files are stored: `path/to/static` |  |  |
 |[STATIC_URL_PREFIX]({{< ref "deploy/application/python/python_apps.md#configure-your-python-application" >}}) | The URL path under which you want to serve static file, usually `/public` |  |  |
 |STATIC_WEBROOT |  |  |  |
 |NGINX_READ_TIMEOUT | Read timeout in seconds | `300` |  |
 |CC_NGINX_PROXY_BUFFER_SIZE | Sets the size of the buffer used for reading the first part of the response received from the proxied server. <a href="https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_buffer_size" target="_blank" rel="noreferrer noopener">Nginx documentation</a> |  |  |
 |CC_NGINX_PROXY_BUFFERS | Sets the number and size of the buffers used for reading a response from the proxied server, for a single connection. <a href="https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_buffers" target="_blank" rel="noreferrer noopener">Nginx documentation</a> |  |  |
 {{< /table >}}

## Rust

[Rust Documentation]({{< ref "deploy/application/rust/rust.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |CC_RUST_BIN | The name of the binary to launch once built |  |  |
 |CC_RUSTUP_CHANNEL | RUSTUP_CHANNEL | Require a specific channel version with `beta`, `nightly`, or a specifiv version like `1.13.0`  | stable |  |
 |CC_RUST_FEATURES | The list of features to enable |  |  |
 {{< /table >}}

## .NET

[.NET Documentation]({{< ref "deploy/application/dotnet/dotnet.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |CC_DOTNET_VERSION | Choose the .NET Core version between `3.1`,`5.0`. | 5.0 |  |
 |CC_DOTNET_PROJ | The name of your project file to use for the build, without the .csproj / .fsproj / .vbproj extension. |  |  |
 |CC_DOTNET_TFM | Compiles for a specific framework. The framework must be defined in the project file. Example : `netcoreapp3.1` |  |  |
 |CC_DOTNET_PROFILE | Override the build configuration settings in your project. | Release |  |
 {{< /table >}}

## [Elixir]({{< ref "deploy/application/elixir/elixir.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |CC_ELIXIR_VERSION | Choose the Elixir version between `1.8`, `1.9`, `1.10` or `1.11` | `1.11` |  |
 |CC_MIX_BUILD_GOAL | The mix goal to build the application (default compile) |  |  |
 |CC_PHOENIX_ASSETS_DIR | Folder in which your Phoenix assets are located. |  |  |
 |CC_PHOENIX_DIGEST_GOAL | Phoenix digest goal. | phx.digest |  |
 |CC_PHOENIX_SERVER_GOAL | Phoenix server goal. | phx.server |  |
 |CC_PHOENIX_RUN_ECTO_MIGRATE | Whether to run 'mix ecto.migrate' or not. | true |  |
 |CC_RUN_COMMAND | Custom command to run your application. Replaces the default behaviour. |  |  |
 {{< /table >}}


## Addons-related environment variable

## FS Bucket

[FS Bucket Documentation]({{< ref "deploy/addon/fs-bucket.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |BUCKET_HOST | Hostname of the bucket |  | X |
 |CC_FS_BUCKET | Defines which bucket to mount on which path |  |  |
 {{< /table >}}

## MongoDB

[MongoDB Documentation]({{< ref "deploy/addon/mongodb.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |MONGODB_ADDON_DB |  | Generated upon creation | X |
 |MONGODB_ADDON_PASSWORD |  | Generated upon creation | X  |
 |MONGODB_ADDON_USER |  | Generated upon creation | X  |
 {{< /table >}}

## MySQL

[MySQL Documentation]({{< ref "deploy/addon/mysql.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |MYSQL_ADDON_DB |  | Generated upon creation | X  |
 |MYSQL_ADDON_PASSWORD |  | Generated upon creation | X  |
 |MYSQL_ADDON_ROLE |  | Generated upon creation | X  |
 |MYSQL_ADDON_USER |  | Generated upon creation | X  |
 {{< /table >}}

## PostgreSQL

[PostgreSQL Documentation]({{< ref "deploy/addon/postgresql.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |POSTGRESQL_ADDON_DB |  | Generated upon creation | X  |
 |POSTGRESQL_ADDON_PASSWORD |  | Generated upon creation | X  |
 |POSTGRESQL_ADDON_ROLE |  | Generated upon creation | X  |
 |POSTGRESQL_ADDON_USER |  | Generated upon creation | X  |
 {{< /table >}}

## Redis

[Redis Documentation]({{< ref "deploy/addon/redis.md" >}})

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |REDIS_HOST |  | Generated upon creation | X  |
 |REDIS_PORT |  | Generated upon creation | X  |
 |REDIS_PASSWORD |  | Generated upon creation | X  |
 {{< /table >}}


## New Relic

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |NEWRELIC_APPNAME |  |  |  |
 |NEWRELIC_LICENSE |  |  |  |
 {{< /table >}}


## Socks

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |SOCKS_ADDON_HOST |  |  |  |
 |SOCKS_ADDON_PORT |  |  |  |
 |SOCKS_ADDON_PRIVATE_KEY |  |  |  |
 {{< /table >}}

## VPN

The VPN addon provides a fixed-ip outgoing node. This can be used to work
with services protected by ip address filtering. `VPN_ADDON_*` variables will
be provided by Clever Cloud upon setup, the only configuration you have to
provide is a list of CIDRs (eg. 1.2.3.0/24) for which you want the traffic
to be routed through the exit node.

 {{<table "table table- bordered" "text-align:center" >}}
 | <center>Name</center> | <center>Description</center> | <center>Default value</center> | <center>Read Only</center> |
 |-----------------------|------------------------------|--------------------------------|--------------------------------|
 |VPN_ADDON_CRT | Client certificate |  |  |
 |VPN_ADDON_CACRT | Server CA certificate |  |  |
 |VPN_ADDON_KEY | Client certificate private key |  |  |
 |VPN_ADDON_HOST | Server host or IP address |  |  |
 |VPN_ADDON_PORT | Server port |  |  |
 |VPN_ADDON_TAKEY | Pre-shared secret |  |  |
 |VPN_TARGETS | Comma-separated list of CIDRs for which you want the traffic to be routed through the exit node |  |  |
 {{< /table >}}
