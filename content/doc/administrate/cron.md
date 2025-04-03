---
type: docs
title: CRON
position: 1
shortdesc: All you need to know about running crons on Clever Cloud
keywords:
- apps
- cron
- cronjob
- schedule
tags:
- administrate
type: docs
aliases:
- /developers/doc/tools/crons
- /doc/tools/crons
---

The configuration file used for crontab is `<PROJECT ROOT>/clevercloud/cron.json`.

{{< callout type="warning" >}}
  Crons are not available in the Docker environment as it would require to set them up inside the Docker container.
{{< /callout >}}

## Syntax

Here is the general syntax:

```json
[
  "<string>",
  "<string>"
]
```

The string `<string>` must use the cron format:

```javascript
M H d m Y command
```

- M: Minute [0,59]
- H: Hour [0,23]
- d: Day of the month [1,31]
- m: Month of the year [1,12]
- Y: Day of the week [0,6] (0 is Sunday)

{{< callout type="warning" >}}
  All the servers are configured to use Coordinated Universal Time (UTC), please keep it in mind when configuring cron tasks to run at a specific hour.
{{< /callout >}}

For more information about the syntax, you can check [the Wikipedia page of cron](https://en.wikipedia.org/wiki/Cron).

## Restrictions

There are two restrictions about the usage of crontab on our platform:

- The special date `@reboot` is not available since the crontab is added after the startup of the instance
- You must use the absolute path of commands

{{< callout type="warning" >}}
  We do not currently support the clustering of cron tasks, you must manage it yourself if your application requires more than one instance.
{{< /callout >}}

## $ROOT

You can use the special token `$ROOT` to refer to the root folder of your application.

Example of `clevercloud/cron.json` which executes the file `cron.php` every 5 minutes:

```json
[
  "*/5 * * * * /usr/bin/php $ROOT/cron.php"
]
```

Note: `$ROOT` is only a token (not an actual variable) which is replaced when setting up the crons by the equivalent of the `APP_HOME` variable (`/home/bas/<app_id>`). Do not write `${ROOT}`, only `$ROOT` will work.

## Access environment variables

To have access to environment variable, you must wrap your commands in a bash script. Let's say
your command is `bundle exec rake myapp:dosomething`.

You need to put it in a bash script, starting with `#!/bin/bash -l`. The *`-l`* is very
important:

```bash
#! /bin/bash -l

cd ${APP_HOME} # Which has been loaded by the env.
bundle exec rake myapp:dosomething
```

Then you need to commit an executable file:

```bash
chmod +x crons/mycron.sh
git add crons/mycron.sh

git diff --cached
$ diff --git a/crons/mycron.sh b/crons/mycron.sh
$ old mode 100644
$ new mode 100755

git commit -m "Make cron file executable"
```

Then, in `clevercloud/cron.json`:

```json
[
  "*/5 * * * * $ROOT/crons/mycron.sh"
]
```

### Avoiding double bash

You might be tempted to put the following in your cron.json file:

```json
[
  "*/5 * * * * /bin/bash $ROOT/crons/mycron.sh"
]
```

Do *NOT* do this. Invoking bash here will supersede the shebang and cancel the `bash -l` that
loads the env. So just put the path to your *executable* `mycron.sh`.

You can refer to [this list]({{< ref "doc/develop/env-variables.md#special-environment-variables" >}}) to see which variables are available.

## Deduplicating crons

Crons are installed and executed on every scaler of an application. This means the same cron may be executed more than once.

You can use your own techniques to avoid that, like a shared task queue or some other locking system.

If you do want to stay stateless and simple, just your bash wrapper script by:

```bash
#! /bin/bash -l

if [[ "$INSTANCE_NUMBER" != "0" ]]; then
  echo "Instance number is ${INSTANCE_NUMBER}. Stop here."
  exit 0
fi

cd ${APP_HOME} # Which has been loaded by the env.
# Your part here
```

{{< callout type="warning" >}}
  If [Zero downtime deployment]({{< ref "doc/administrate/apps-management.md#edit-application-configuration" >}}) is activated, Crons might overlap for a couple of minutes until the old instance are deleted as two instances would have the same instance number
  You can prevent this by deactivating it.
{{< /callout >}}

## Logs collection

Everything coming from stdout & stderr is forwarded to our logs collection system and is available in the web console / CLI logs.
