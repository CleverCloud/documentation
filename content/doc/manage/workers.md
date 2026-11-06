---
type: docs
linkTitle: Workers
title: Run background workers alongside your application
description: Run queue consumers and other long-running background processes next to your application on each instance, and choose how Clever Cloud restarts them
keywords:
- workers
- background processes
- queue consumers
- CC_WORKER_COMMAND
- CC_WORKER_RESTART
- long-running tasks
aliases:
- /doc/develop/common-configuration/workers
- /doc/common-configuration/workers
- /doc/develop/configuration/workers
- /doc/develop/workers
- /doc/develop/configure-applications/workers/
- /doc/workers
---

A worker is a command that runs in the background next to your application, such as a queue consumer that processes jobs your application publishes. Clever Cloud starts it on each instance once your application runs, and restarts it when it fails. To run a command on a schedule, use [CRON](/doc/develop/cron/) instead, and to run a command once, use a [Clever Task](/doc/deploy/tasks/).

> [!NOTE] Not available for Docker applications
> Clever Cloud doesn't start workers in Docker applications. Start your background processes from your image instead.

## Add a worker

A worker runs a command that stays in the foreground. This script, at the root of your application, stands for a queue consumer: it takes the name of a queue, then writes a message every ten seconds. Replace its loop with your consumer:

```bash {filename="worker.sh"}
#!/bin/bash
queue="${1:-default}"
while true; do
  echo "Processing the $queue queue as $(whoami) from $(pwd)"
  sleep 10
done
```

From the folder of your application linked with Clever Tools, make the script executable and commit it. Then set the command in `CC_WORKER_COMMAND`, and deploy:

```bash
chmod +x worker.sh
git add worker.sh && git commit -m "Add a worker"
clever env set CC_WORKER_COMMAND "./worker.sh"
clever deploy
```

To run several workers, number them from `CC_WORKER_COMMAND_0` instead. The numbers identify the workers and don't have to follow each other: don't rely on them to start one worker before another. `CC_WORKER_COMMAND` and `CC_WORKER_COMMAND_0` are two distinct workers, so remove `CC_WORKER_COMMAND` when you switch to numbered workers:

```bash
clever env rm CC_WORKER_COMMAND
clever env set CC_WORKER_COMMAND_0 "./worker.sh emails"
clever env set CC_WORKER_COMMAND_1 "./worker.sh exports"
clever restart
```

## How workers run

Clever Cloud starts the workers at the end of each deployment, once your application passes its startup checks. Each worker:

- Runs as the `bas` user, from `$APP_HOME`, the root of your application, even when `APP_FOLDER` selects a subdirectory
- Runs in a `bash` login shell, with your environment variables loaded
- Reads your environment variables when it starts: redeploy your application after you change one
- Writes its standard output and error to the [logs of your application](/doc/develop/observability/logs/)

The command must keep running: when it exits, the worker stops, and so do the processes it started. Don't start your consumer in the background with `&`.

## Choose the restart policy

`CC_WORKER_RESTART` sets when Clever Cloud restarts a worker whose command exited:

| Value                  | Behavior                                                                                       |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| `on-failure` (default) | Restarts the worker after a non-zero exit status or an abnormal termination, such as `SIGKILL` |
| `always`               | Restarts the worker after any exit, including a successful one                                 |
| `no`                   | Doesn't restart the worker until the next deployment                                           |

Clever Cloud waits `CC_WORKER_RESTART_DELAY` seconds before restarting a worker, 1 by default. This value is a whole number, and applies to all the workers of the application. The startup of the shell adds to this delay.

With `on-failure` or `always`, Clever Cloud doesn't limit the number of restarts: a worker that fails each time it starts keeps restarting. Set a delay that suits the failure, such as a few seconds when a worker can't reach a service.

An invalid value of `CC_WORKER_RESTART` or `CC_WORKER_RESTART_DELAY`, such as `0.5`, makes the deployment fail at its first step.

## Plan for several copies

Each instance runs its own copy of every worker: with two instances, each worker runs twice. During a deployment, the workers of the previous instances keep running next to the new ones until these instances stop.

When an instance stops, its workers receive a `SIGTERM` signal, and the instance shuts down shortly after, without waiting for them to finish. Design your workers for this:

- Take jobs from a queue that waits for an acknowledgment before it removes a job. A job that a stopped worker didn't finish then goes back to the queue
- Make each job safe to run twice, since a job can run again after an interruption
- Handle `SIGTERM` to stop taking new jobs, and keep each job short
