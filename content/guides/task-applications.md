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
run scalers for the duration of a single task and shutdown these scalers once the task is
done.

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

TODO: document how to do it.

### With the `CC_TASK=true` environment variable

You can temporarily turn a "normal" app to a "task" one. You just need to add the
`CC_TASK` environment variable with the value `true`. The deployment will be a "task" one
while the variable exists in the application.

## Define the actual command to run (mandatory)

To run your task, you need to define a `CC_RUN_COMMAND` variable with the command that
will be executed. If this variable is not set, the task deployment **will not** go through.

### Examples

Here are some ways to run your task script:

```
CC_RUN_COMMAND="php my-special-script.php"
CC_RUN_COMMAND="./my-special-script.sh"
CC_RUN_COMMAND="node my-special-script.js"
CC_RUN_COMMAND="cd mytask; ./task1.sh && ./task2.sh"
```

{{< readfile file="set-env-vars.md" >}}

{{< readfile file="new-relic.md" >}}

{{< readfile file="env-injection.md" >}}

{{< readfile file="link-addon.md" >}}

{{< readfile file="more-config.md" >}}
