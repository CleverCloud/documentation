---
type: docs
title: Workers
shortdesc: Workers allow to run background tasks running in parallel of your application
tags:
- develop
keywords:
- apps
- workers
type: docs
---

## Workers

{{< callout type="info" >}}
Workers are not available for docker applications.
{{< /callout >}}

You can run background tasks running in parallel of your application. They will be restarted automatically on error.
Those are especially useful for environments where you can't have long-running processes such as PHP, Ruby or Python.

The workers run in the same environment as your application. They are launched as services by systemd, in the application's directory.

All you need to do is add one (or several) environment variables as such:

```bash
CC_WORKER_COMMAND=my-awesome-worker
```

Or

```bash
CC_WORKER_COMMAND_0=my-awesome-worker
CC_WORKER_COMMAND_1=my-other-worker
```

By default, workers will be restarted if they exit with an error code. You can customise this behavior by setting the
environment variable `CC_WORKER_RESTART` to one of `always`, `on-failure` (the default) or `no`.

You can define a delay to restart your worker with the environement variable `CC_WORKER_RESTART_DELAY`, the value is in seconds with a default value of `1`. It will apply to all registered workers.

{{< callout type="warning" >}}
If the `CC_WORKER_RESTART_DELAY` value is too low and the restart policy is set to `always`, your worker might hit the restart burst limit, which may prevent your worker from being correctly restarted.
{{< /callout >}}

If you want to have a restart delay less than 1 second and expect your script to restart multiple times in a very short time, please let us know on our support.
