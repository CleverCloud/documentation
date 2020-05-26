---
title: Environment Variable Reference
position: 3
tags:
- support
---

## Application-related environment variable

### Commons to all Applications

#### Set by the deployment process

These are read-only variables that are generated for each scaler before they build and start your application.

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Example value</center></th>
  </tr>
  <tr>
    <td>[INSTANCE_NUMBER](/doc/admin-console/environment-variables/#special-environment-variables)</td>
    <td>Allows your application to differentiate each running node on the application level.</td>
    <td>0, 1…</td>
  </tr>
  <tr>
    <td>INSTANCE_TYPE</td>
    <td>Whether this instance is a "build" instance or a "production" instance.</td>
    <td>build, production</td>
  </tr>
  <tr>
    <td>INSTANCE_ID</td>
    <td>The ID of the current instance (scaler) of your application. It's unique for each instance of your application and changes every time you deploy it.</td>
    <td>518c8d8f-e304-4310-81e0-9c4237d55645</td>
  </tr>
  <tr>
    <td>CC_PRETTY_INSTANCE_NAME</td>
    <td>The random generated string as instance pretty name using pokemon names.</td>
    <td>Tiny rhyhorn</td>
  </tr>
  <tr>
    <td>APP_ID</td>
    <td>The ID of your Clever Cloud application</td>
    <td>app_649a93d1-6677-44bc-aca7-6f46107d6e02</td>
  </tr>
  <tr>
    <td>APP_HOME</td>
    <td>The absolute path to your application folder</td>
    <td>/home/bas/app_649a93d1-6677-44bc-aca7-6f46107d6e02</td>
  </tr>
  <tr>
    <td>CC_DEPLOYMENT_ID</td>
    <td>Internal id of current deployment</td>
    <td>f7efaf04-1a63-45a1-8503-0de7c750ee48</td>
  </tr>
  <tr>
    <td>COMMIT_ID</td>
    <td>The id of the commit that's currently running</td>
    <td>d88cd2ae1aaa91923ed2bd689d95d713b6f3f45f</td>
  </tr>
  <tr>
    <td>CC_REVERSE_PROXY_IPS</td>
    <td>A comma separated list of trusted IP addresses. You should only accept requests
    coming from these IP addresses.</td>
    <td>x.y.z.z,x.y.z.z</td>
  </tr>
</table>

#### Variables you can define

So you can alter the build&start process for your application.

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
  </tr>
  <tr>
    <td>APP_FOLDER</td>
    <td>Folder in which the application is located (inside the git repository)</td>
    <td></td>
  </tr>
  <tr>
    <td>[CC_TROUBLESHOOT](/doc/clever-cloud-overview/troubleshoot-mode/)</td>
    <td>Enable debug log level, will also keep the VM up after failure for 15 minutes so you can SSH and debug. Don't forget to cancel deployment if you push a new commit.</td>
    <td>`false`</td>
  </tr>
  <tr>
    <td>[CC_WORKER_COMMAND](/doc/clever-cloud-overview/common-application-configuration/#workers)</td>
    <td>Command to run in background as a worker process. You can run multiple worker.</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_WORKER_RESTART</td>
    <td>One of `always`, `on-failure` or `no`. Control whether workers need to be restarted when they exit.
        This setting controls all workers.
    </td>
    <td>on-failure</td>
  </tr>
  <tr>
    <td>CC_PRE_BUILD_HOOK</td>
    <td>Ran before the dependencies are fetched. If it fails, the deployment fails.</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_POST_BUILD_HOOK</td>
    <td>Ran after the project is built, and before the cache archive is generated. If it fails, the deployment fails.</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PRE_RUN_HOOK</td>
    <td>Ran before the application is started, but after the cache archive has been generated. If it fails, the deployment fails.</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_RUN_SUCCEEDED_HOOK</td>
    <td>Ran once the application has started successfuly.</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_RUN_FAILED_HOOK</td>
    <td>Ran once the application has failed to start.</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_CACHE_DEPENDENCIES</td>
    <td>Enable caching of your build dependencies to speed up following builds.</td>
    <td>`false`</td>
  </tr>
  <tr>
    <td>CC_DISABLE_METRICS</td>
    <td>Disable metrics collection.</td>
    <td>`false`</td>
  </tr>
  <tr>
    <td>[IGNORE_FROM_BUILDCACHE](/doc/admin-console/environment-variables/#settings-you-can-define-using-environment-variables)</td>
    <td>Allows to specify paths to ignore when the build cache archive is created.</td>
    <td></td>
  </tr>
  <tr>
    <td>[CC_OVERRIDE_BUILDCACHE](/doc/admin-console/environment-variables/#settings-you-can-define-using-environment-variables)</td>
    <td>Allows to specify paths that will be in the build cache.
    Only those files / directories will be cached</td>
    <td></td>
  </tr>
  <tr>
    <td>[CC_METRICS_PROMETHEUS_PORT](/doc/tools/metrics#publish-your-own-metrics)
    <td>Define the port on which the Prometheus endpoint is available</td>
    <td>`8080`</td>
  </tr>
  <tr>
    <td>[CC_METRICS_PROMETHEUS_PATH](/doc/tools/metrics#publish-your-own-metrics)
    <td>Define the path on which the Prometheus endpoint is available</td>
    <td>`/metrics`</td>
  </tr>
</table>

### Docker

[Docker Documentation](/doc/docker/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>CC_MOUNT_DOCKER_SOCKET</td>
    <td>Set to true to access the host Docker socket from inside your container.</td>
    <td>`false`</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_DOCKER_EXPOSED_HTTP_PORT</td>
    <td>Set to custom HTTP port if your Docker container runs on custom port.</td>
    <td>`8080`</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_DOCKER_EXPOSED_TCP_PORT</td>
    <td>Set to custom TCP port if your Docker container runs on custom port but **it still needs a support request to make use of it.**</td>
    <td>`4040`</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_DOCKER_FIXED_CIDR_V6</td>
    <td>Activate the support of IPv6 with an IPv6 subnet int the docker daemon.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_DOCKERFILE</td>
    <td>Set an alternative Dockerfile name</td>
    <td></td>
    <td></td>
  </tr>
</table>

### Go

[Go Documentation](/doc/go/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>CC_GO_PKG</td>
    <td>Makes the deployer run go get ${CC_GO_PKG} instead of go get &lt;app_id&gt;. </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_GO_BUILD_TOOL</td>
    <td>Available values: `gomod`, `gobuild`, `goget`. Makes the deployer use `go modules`, `go get` or `go build` to build your application.</td>
    <td>`goget`</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_GO_RUNDIR</td>
    <td>Makes the deployer use the specified directory to run your binary.<br>If your application must be in `$GOPATH/src/company/project` for your vendored dependencies, set this variable to `company/project`</td>
    <td></td>
    <td></td>
</table>

### Haskell

[Haskell Documentation](/doc/haskell/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>CC_RUN_COMMAND</td>
    <td>Custom command to run your application.</td>
    <td></td>
    <td></td>
  </tr>
</table>

### Java

[Java Documentation](/doc/java/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>CC_SBT_TARGET_DIR</td>
    <td>Define where pick the bin to run.</td>
    <td>`.`</td>
    <td>Then `/target/universal/stage/bin` is concatenated.</td>
  </tr>
  <tr>
    <td>CC_SBT_TARGET_BIN</td>
    <td>Define the bin to pick in the `CC_SBT_TARGET_DIR`.</td>
    <td>The first bin found in the `CC_SBT_TARGET_DIR`.</td>
    <td></td>
  </tr>
  <tr>
    <td>GRADLE_DEPLOY_GOAL</td>
    <td>Define which gradle goals to run during build.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_JAVA_VERSION</td>
    <td>Choose the JVM version between 'graalvm-ce' or `8`, `11` or `13` for OpenJDK.</td>
    <td>`11`</td>
    <td></td>
  </tr>
  <tr>
    <td>MAVEN_DEPLOY_GOAL</td>
    <td>Define which maven goals to run during build.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_MAVEN_PROFILES</td>
    <td>Define which maven profile to use during default build.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>NUDGE_APPID</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>PLAY1_VERSION</td>
    <td>Define which play1 version to use between `1.2`, `1.3`, `1.4` and `1.5`</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>SBT_DEPLOY_GOAL</td>
    <td>Define which sbt goals to run during build.</td>
    <td>`stage`</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_JAR_PATH</td>
    <td>Define the path to your jar.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_EXTRA_JAVA_ARGS</td>
    <td>Define extra arguments to pass to 'java' for jars.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_JAR_ARGS</td>
    <td>Define arguments to pass to the jar we launch.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_RUN_COMMAND</td>
    <td>Custom command to run your application. Replaces the default behaviour.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_JAVA_APM_AGENT_ENABLE</td>
    <td>Attach the APM Java Agent to the currently running JVM processes</td>
    <td>false</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_JAVA_APM_AGENT_CONTINUOUS</td>
    <td>Periodically scan and attach the APM Java Agent to any JVM processes it can find over time</td>
    <td>false</td>
    <td></td>
  </tr>
</table>

### NodeJS

[NodeJS Documentation](/doc/nodejs/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>CC_NODE_DEV_DEPENDENCIES</td>
    <td>Control if development dependencies are installed or not. Values are either `install` or `ignore`</td>
    <td>`ignore`</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_NODE_START_GOAL</td>
    <td>Defines which node scripts to run</td>
    <td>`start`</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_RUN_COMMAND</td>
    <td>Define a custom command.</td>
    <td>Exemple for Meteor: `node .build/bundle/main.js &lt;options&gt;`</td>
    <td></td>
  </tr>
  <tr>
    <td>NODE_BUILD_TOOL</td>
    <td>Choose your build tool between `npm` and `yarn`</td>
    <td>`npm`</td>
    <td></td>
  </tr>
  <tr>
    <td>NPM_TOKEN</td>
    <td>Private repository token for npmjs.com</td>
    <td></td>
    <td></td>
  </tr>
</table>

### PHP

[PHP Documentation](/doc/php/)


<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>ALWAYS_POPULATE_RAW_POST_DATA</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_LDAP_CA_CERT</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_WEBROOT</td>
    <td>Define the `DocumentRoot` of your project</td>
    <td>.</td>
    <td></td>
  </tr>
  <tr>
    <td>LDAPTLS_CACERT</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ENABLE_REDIS</td>
    <td></td>
    <td>`false`</td>
    <td></td>
  </tr>
  <tr>
    <td>HTTP_TIMEOUT</td>
    <td>Define a custom HTTP timeout</td>
    <td>`180`</td>
    <td></td>
  </tr>
  <tr>
    <td>MAX_INPUT_VARS</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PHP_VERSION</td>
    <td>Choose your PHP version between `5.6`, `7.2`, `7.3` and `7.4`</td>
    <td>`7`</td>
    <td></td>
  </tr>
  <tr>
    <td>[SESSION_TYPE](/doc/php/php-apps/#use-redis-to-store-php-sessions)</td>
    <td>Choose `redis` to use it as session store</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>SOCKSIFY_EVERYTHING</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>USE_SOCKS</td>
    <td></td>
    <td>`false`</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_OPCACHE_MEMORY</td>
    <td>Set the shared opcache memory size</td>
    <td>Default is about 1/8 of the RAM</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_OPCACHE_MAX_ACCELERATED_FILES</td>
    <td>Maximum number of files handled by opcache.</td>
    <td>Default depends on the scaler size</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_MTA_SERVER_HOST</td>
    <td>Host of the SMTP server</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_MTA_SERVER_PORT</td>
    <td>Port of the SMTP server</td>
    <td>465</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_MTA_AUTH_USER</td>
    <td>User to authenticate to the SMTP server</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_MTA_AUTH_PASSWORD</td>
    <td>Password to authenticate to the SMTP server</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_MTA_USE_TLS</td>
    <td>Enable or disable TLS when connecting to the SMTP server</td>
    <td>true</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_MTA_AUTH_METHOD</td>
    <td>Enable or disable authentication to the SMTP server</td>
    <td>on</td>
    <td></td>
  </tr>
  <tr>
    <td>SQREEN_API_APP_NAME</td>
    <td>The name of your sqreen application.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>SQREEN_API_TOKEN</td>
    <td>Organization token.</td>
    <td></td>
    <td></td>
  </tr>
</table>

### Python

[Python Documentation](/doc/python/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>CC_PYTHON_CELERY_LOGFILE</td>
    <td>Relative path to your Celery logfile: `/path/to/logdir` </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PYTHON_CELERY_MODULE</td>
    <td>Specify the Celery module you want to start: `mymodule`</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PYTHON_CELERY_USE_BEAT</td>
    <td>Set to `true` to activate Beat support</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PYTHON_MODULE</td>
    <td>Select which module you want to start: `mymodule:app`. 'mymodule' refers to the path to the folder containing the app object. So a module called 'server.py' in a folder called 'app' would be used here as `app.server:app`</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PYTHON_USE_GEVENT</td>
    <td>Set to `true` to enable Gevent</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>HARAKIRI</td>
    <td>Timeout (in seconds) after which an unresponding process is killed</td>
    <td>`180`</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PYTHON_BACKEND</td>
    <td>Choose the Python backend to use between `uwsgi` and `gunicorn`</td>
    <td>`uwsgi`</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PYTHON_VERSION</td>
    <td>Choose the Python version between `2.7`, `3.6`, `3.7` and `3.8`</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>PYTHON_SETUP_PY_GOAL</td>
    <td>Custom setup goal to be launch after `requirements.txt` have been installed</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>STATIC_FILES_PATH</td>
    <td>Relative path to where your static files are stored: `path/to/static`</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>[STATIC_URL_PREFIX](/doc/python/python_apps/#manage-your-static-files)</td>
    <td>The URL path under which you want to serve static file, usually `/public`</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>STATIC_WEBROOT</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>UWSGI_INTERCEPT_ERRORS</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>[UWSGI_ASYNC](/doc/python/python_apps/#uwsgi-asynchronous-non-blocking-modes)</td>
    <td>Number of cores to use for uWSGI asynchronous/non-blocking modes</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>UWSGI_ASYNC_ENGINE</td>
    <td>Select the asynchronous engine for uWSGI (optional)</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>WSGI_WORKERS</td>
    <td>Number of workers. (Defaut: automatically setup with the scaler size)</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>WSGI_THREADS</td>
    <td>Number of threads per worker. (Defaut: automatically setup with the scaler size)</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>WSGI_BUFFER_SIZE</td>
    <td>Buffer size (in bytes) for uploads.</td>
    <td>`4096`</td>
    <td></td>
  </tr>
  <tr>
    <td>WSGI_POST_BUFFERING</td>
    <td>Maximal size (in bytes) for the headers of a request. </td>
    <td>`4096`</td>
    <td></td>
  </tr>
  <tr>
    <td>ENABLE_GZIP_COMPRESSION</td>
    <td>Set to `true` to gzip-compress the output of uwsgi</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>GZIP_TYPES</td>
    <td>Set the mime types to compress.</td>
    <td>`text/* application/json application/xml application/javascript image/svg+xml`</td>
    <td></td>
  </tr>
  <tr>
    <td>NGINX_READ_TIMEOUT</td>
    <td>Read timeout in seconds</td>
    <td>`300`</td>
    <td></td>
  </tr>
</table>

### Ruby

[Ruby Documentation](/doc/ruby/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>CC_RACKUP_SERVER</td>
    <td>The server to use for serving the ruby application</td>
    <td>puma</td>
    <td></td>
  </tr>
  <tr>
    <td>RACK_ENV</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>RAILS_ENV</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>RUBY_VERSION</td>
    <td>Choose the Ruby version to use.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>STATIC_FILES_PATH</td>
    <td>Relative path to where your static files are stored: `path/to/static`</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>[STATIC_URL_PREFIX](/doc/python/python_apps/#manage-your-static-files)</td>
    <td>The URL path under which you want to serve static file, usually `/public`</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>STATIC_WEBROOT</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>NGINX_READ_TIMEOUT</td>
    <td>Read timeout in seconds</td>
    <td>`300`</td>
    <td></td>
  </tr>
</table>

### Rust

[Rust Documentation](/doc/rust/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>CC_RUST_BIN</td>
    <td>The name of the binary to launch once built</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_RUSTUP_CHANNEL</td>
    <td>Require a specific channel version with `beta`, `nightly`, or a specifiv version like `1.13.0` </td>
    <td>stable</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_RUST_FEATURES</td>
    <td>The list of features to enable</td>
    <td></td>
    <td></td>
  </tr>
</table>

### Elixir

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>CC_ELIXIR_VERSION</td
    <td>Choose the Elixir version between '1.8' or `1.9`</td>
    <td>`1.9`</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_MIX_BUILD_GOAL</td
    <td>The mix goal to build the application (default compile)</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PHOENIX_ASSETS_DIR</td
    <td>Folder in which your Phoenix assets are located.</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PHOENIX_DIGEST_GOAL</td>
    <td>Phoenix digest goal.</td>
    <td>phx.digest</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PHOENIX_SERVER_GOAL</td>
    <td>Phoenix server goal.</td>
    <td>phx.server</td>
    <td></td>
  </tr>
  <tr>
    <td>CC_PHOENIX_RUN_ECTO_MIGRATE</td>
    <td>Whether to run 'mix ecto.migrate' or not.</td>
    <td>true</td>
    <td></td>
  </tr>
</table>


## Addons-related environment variable

### FS Bucket

[FS Bucket Documentation](/doc/addons/fs_buckets/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>BUCKET_HOST</td>
    <td>Hostname of the bucket</td>
    <td></td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
  <tr>
    <td>CC_FS_BUCKET</td>
    <td>Defines which bucket to mount on which path</td>
    <td></td>
    <td></td>
  </tr>
</table>

### MongoDB

[MongoDB Documentation](/doc/mongodb/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>MONGODB_ADDON_DB</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
  <tr>
    <td>MONGODB_ADDON_PASSWORD</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
  <tr>
    <td>MONGODB_ADDON_USER</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
</table>

### MySQL

[MySQL Documentation](/doc/mysql/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>MYSQL_ADDON_DB</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
  <tr>
    <td>MYSQL_ADDON_PASSWORD</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
  <tr>
    <td>MYSQL_ADDON_ROLE</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
  <tr>
    <td>MYSQL_ADDON_USER</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
</table>

### PostgreSQL

[PostgreSQL Documentation](/doc/postgresql/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>POSTGRESQL_ADDON_DB</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
  <tr>
    <td>POSTGRESQL_ADDON_PASSWORD</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
  <tr>
    <td>POSTGRESQL_ADDON_ROLE</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
  <tr>
    <td>POSTGRESQL_ADDON_USER</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
</table>

### Redis

[Redis Documentation](/doc/redis/)

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>REDIS_HOST</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
  <tr>
    <td>REDIS_PORT</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
  <tr>
    <td>REDIS_PASSWORD</td>
    <td></td>
    <td>Generated upon creation</td>
    <td class="cc-col__price "><span class="label cc-label__price label-info">X</span></td>
  </tr>
</table>

### New Relic

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>NEWRELIC_APPNAME</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>NEWRELIC_LICENSE</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

### Socks

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>SOCKS_ADDON_HOST</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>SOCKS_ADDON_PORT</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>SOCKS_ADDON_PRIVATE_KEY</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

### VPN

The VPN addon provides a fixed-ip outgoing node. This can be used to work
with services protected by ip address filtering. `VPN_ADDON_*` variables will
be provided by Clever Cloud upon setup, the only configuration you have to
provide is a list of CIDRs (eg. 1.2.3.0/24) for which you want the traffic
to be routed through the exit node.

<table class="table table-bordered" style="text-align:center">
  <tr>
    <th><center>Name</center></th>
    <th><center>Description</center></th>
    <th><center>Default value</center></th>
    <th><center>Read Only</center></th>
  </tr>
  <tr>
    <td>VPN_ADDON_CRT</td>
    <td>Client certificate</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>VPN_ADDON_CACRT</td>
    <td>Server CA certificate</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>VPN_ADDON_KEY</td>
    <td>Client certificate private key</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>VPN_ADDON_HOST</td>
    <td>Server host or IP address</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>VPN_ADDON_PORT</td>
    <td>Server port</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>VPN_ADDON_TAKEY</td>
    <td>Pre-shared secret</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>VPN_TARGETS</td>
    <td>Comma-separated list of CIDRs for which you want the traffic to be
    routed through the exit node</td>
    <td></td>
    <td></td>
  </tr>
</table>
