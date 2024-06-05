---
type: docs
title: Run oneshot tasks on dedicated scalers
Description: This article shows you how to setup and run single-job scalers on Clever Cloud
tags:
- deploy
keywords:
- task
- worker
- jobs
---

## Overview

This will guide you in the process of creating a "task-only" application that will just
run scalers for the duration of a given command and shutdown these scalers once the task is
done. This type of application is not expected to listen to incoming requests. As such, no
HTTP or TCP traffic from outside is routed towards the scalers.

## Create a "task" application

### With the Clever Tools CLI

1. Make sure you have clever-tools installed locally or follow our [CLI getting started]({{< ref "doc/cli/getting_started.md" >}}) guide.
2. In your code folder, do `clever create --type <type> <app-name> --region <zone> --org <org> --task` where :
   1. `type` is the type of technology you rely on
   2. `app-name` the name you want for your application,
   3. `zone` deployment zone (`par` for Paris and `mtl` for Montreal)
   4. `org` the organization ID the application will be created under.

With the `--task` flag, your application will be marked as "task" in our internal database.
This means that every deployment will be handled as a task. More on that later.

Refer to [clever create]({{< ref "doc/cli/create.md" >}}) for more details on application creation with Clever Tools.

### With the console

To declare an application as a Task, check the corresponding box in the `Information` tab.

{{< figure src="/images/changelog/clever-tasks.webp" caption="Defines a Clever Cloud application as a Task in Console" width="800px">}}

## Define the actual command to run (mandatory)

To run your task, you **have to** define a `CC_RUN_COMMAND` variable with the command that
will be executed. If this variable is not set, the task deployment **will not** go through.

### Examples

Here are some example commands to run:

```
CC_RUN_COMMAND="php my-special-script.php"
CC_RUN_COMMAND="python manage.py migrate"
CC_RUN_COMMAND="npm run app:test"
CC_RUN_COMMAND="./my-special-script.sh"
CC_RUN_COMMAND="node my-special-script.js"
CC_RUN_COMMAND="cd mytask; ./task1.sh && ./task2.sh"
```

Note that you can only set **one** `CC_RUN_COMMAND`.
If you need to run multiple commands, separate them with `;`, `&&` or put them in a bash script.

Your environment is loaded before running your commands, so you have access to all the
environment variables you might have set.

{{< readfile file="set-env-vars.md" >}}

## What's in tasks apps? What is not?

"Task" apps are a quick way to run a script.
When deploying, Clever Cloud just starts VMs, run the given command and then stop the VM.

### Current limitation

At the time of publishing this doc, here are some limitations around tasks:

- You cannot deploy the same app multiple times in parallel, executing different tasks.
  We will start the latter one after the former one ends.
- Due to this limitation, running a task deployment on an existing app will block "normal"
  deployments for the duration of the command. Event the ones from the monitoring.
- There is no out-of-the-box cron definition at the moment.
  You'll have to do that on your own.

### Tips and examples

#### Running from a cron

`clever-tools` is available on all our VMs.
You can trigger the deployment of a task by running a few `clever` commands.
For example, you can setup a cron on your web application that runs as a normal app, and
run something like this:

```bash
#!/bin/bash

mkdir task
pushd task

# Make sure to have CLEVER_TOKEN and CLEVER_SECRET in your env

clever link {task app_id}
clever restart --quiet # That's if you don't care for the logs to show in here

popd
rm -rf task
```

#### Running a script with different parameters

You can write a script that takes specific environment variables and acts on it.

Let's say your app needs to trigger the processing of a specific file after a customer
uploaded it.

Make your processing script use the value from `FILE_TO_PROCESS` as the source:

```bash
#!/bin/bash

wget "${FILE_TO_PROCESS}" -O "to-process.csv"

process-my-file "to-process.csv"
```

Then in your main app, trigger the task like this:

```bash
#!/bin/bash

mkdir task
pushd task

# Make sure to have CLEVER_TOKEN and CLEVER_SECRET in your env

clever link {task app_id}
clever env set FILE_TO_PROCESS "https://mybucket.cellar-c2.services.clever-cloud.com/some-file-20240231.csv"
clever restart --quiet # That's if you don't care for the logs to show in here

popd
rm -rf task
```

{{< readfile file="link-addon.md" >}}

{{< readfile file="more-config.md" >}}
