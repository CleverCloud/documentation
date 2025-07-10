---
type: docs
title: Clever Tasks
Description: How to setup and run single-job scalers on Clever Cloud
tags:
- deploy
- task
- worker
- jobs
- cron
keywords:
- task
- worker
- jobs
- cron
---

## Overview

This will guide you in the process of creating a Clever Task: an application that will just run scalers for the duration of a given command and shutdown these scalers once the task is done. This type of application is not expected to listen to incoming requests. As such, no HTTP or TCP traffic from outside is routed towards the scalers.

## Create a "task" application

### With the Clever Tools CLI

Make sure you have [Clever Tools installed](/developers/doc/cli/) and in your project folder, run `clever create --type <type> --task <command>`. You can also add options such as `<app-name> --region <zone> --org <org>` where:
   1. `app-name` the name you want for your application,
   2. `zone` deployment zone (`par` for Paris or `mtl` for Montreal for example)
   3. `org` the organisation ID the application will be created under

You can create an application as a task without command to execute and define it later with the `CC_RUN_COMMAND` [environment variable](/developers/doc/reference/reference-environment-variables/).

### With the console

To declare an application as a Task, check the corresponding box in the `Information` tab.

{{< figure src="/developers/images/changelog/clever-tasks.webp" caption="Defines a Clever Cloud application as a Task in Console" width="800px">}}

## Define the command to run (mandatory)

To run your task, you **have to** define a `CC_RUN_COMMAND` variable with the command that will be executed.

{{%callout type="warning" %}}
If `CC_RUN_COMMAND` is not set during creation or later, the task deployment **will not** go through.
{{% /callout %}}

### Examples

Here are some example commands to run:

```bash
CC_RUN_COMMAND="php my-special-script.php"
CC_RUN_COMMAND="python manage.py migrate"
CC_RUN_COMMAND="npm run app:test"
CC_RUN_COMMAND="./my-special-script.sh"
CC_RUN_COMMAND="node my-special-script.js"
CC_RUN_COMMAND="cd mytask; ./task1.sh && ./task2.sh"
```

Note that you can only set **one** `CC_RUN_COMMAND`. If you need to run multiple commands, separate them with `;`, `&&` or put them in a bash script. Your environment is loaded before running your commands, so you have access to all the environment variables you might have set.

## What's in tasks apps? What is not?

Clever Tasks are a quick way to run a script. When deploying, Clever Cloud just starts a VM, run the given command and then stop the VM.

### Current limitation

At the time of publishing this documentation, here are some limitations around tasks:

- You cannot deploy the same app multiple times in parallel, executing different tasks. We will start the latter one after the former one ends.
- Due to this limitation, running a task deployment on an existing app will block "normal" deployments for the duration of the command. Event the ones from the monitoring.
- There is no out-of-the-box CRON trigger at the moment. You'll have set it up on your own.

### Tips and examples

#### Running from a CRON

`Clever Tools` is available on all our VMs. You can trigger the deployment of a task by running a few `clever` commands. For example, setup a CRON on a web application that run such a script/command:

```bash
#!/bin/bash

# Make sure to setup CLEVER_TOKEN and CLEVER_SECRET
# These environment variables are required to authenticate with Clever Tools
# We restart the task app, it will start it and execute the CC_RUN_COMMAND
# Use the --quiet flag if you don't care for the logs to show in here
clever restart --app TASK_APP_ID --quiet
```

- [Learn more about CRON on Clever Cloud](/developers/doc/administrate/cron/)

#### Running a script with different parameters

You can write a script that takes specific environment variables and acts on it. Let's say your application needs to trigger the processing of a specific file after a customer uploaded it. Make your task script use the value from `FILE_TO_PROCESS` as the source:

```bash
#!/bin/bash

wget "${FILE_TO_PROCESS}" -O "to-process.csv"
process-my-file "to-process.csv"
```

Then in your main app, trigger the task like this:

```bash
#!/bin/bash

# We set the FILE_TO_PROCESS environment variable to the URL of the file to process
clever env set --app TASK_APP_ID FILE_TO_PROCESS "https://mybucket.cellar-c2.services.clever-cloud.com/some-file.csv"
clever restart --app TASK_APP_ID --quiet # That's if you don't care for the logs to show in here
```

{{< content "link-addon" >}}

{{< content "more-config" >}}

{{< content "env-injection" >}}
