---
type: docs
linkTitle: CRON
title: Schedule jobs with CRON
description: Run commands on a schedule on your Clever Cloud applications with a cron.json file, in UTC or in your local time zone, with your environment variables loaded
keywords:
- cron jobs
- crontab
- scheduled tasks
- time zone
- daylight saving time
- background processing
aliases:
- /doc/administrate/cron
- /doc/cron
- /doc/crons
- /doc/develop/apps-configuration/cron/
- /doc/develop/common-configuration/cron
- /doc/develop/configure-applications/cron/
- /doc/tools/crons
---

To run a command at regular intervals, such as cleaning a cache every night or sending a report every Monday, add a `clevercloud/cron.json` file to your project. At each deployment, Clever Cloud installs its jobs on every instance of your application.

> [!NOTE] Not available on Docker and task applications
> Docker applications and [Clever Tasks](/doc/deploy/tasks/) don't run the jobs of `clevercloud/cron.json`. In a Docker application, run a scheduler inside your container. To run a task on a schedule, [restart it from a job of another application](/doc/deploy/tasks/#running-from-a-cron).

## Add a job

Create a `clevercloud/cron.json` file in your project. It holds a JSON array of strings, and each string is a line of the crontab: a schedule followed by the command to run. This file runs a PHP script every day at 03:00 UTC:

```json {filename="clevercloud/cron.json"}
[
  "0 3 * * * /usr/bin/php $ROOT/scripts/clean-cache.php"
]
```

`$ROOT` stands for the folder of your application on the instance, `/home/bas/<app_id>`, which your environment also exposes as `APP_HOME`. Clever Cloud replaces this token in the text of each line before it installs the crontab. Write `$ROOT` as is: `${ROOT}` isn't replaced.

Commit the file and deploy your application. Once it starts and responds, the deployment logs show `Starting crons setup` and `Importing cronjobs`. Each deployment starts new instances from the file of the deployed commit. Edit the file and redeploy to change or remove a job.

If the file isn't valid JSON, or doesn't hold an array, the deployment fails. Clever Cloud ignores array entries that aren't strings. The cron daemon then checks every line, and refuses the whole file if a single one is invalid, such as a minute set to `61`. The deployment still succeeds, but no job runs, and its logs show the error followed by `Invalid crontab file, can't install.`

## Write the schedule

A schedule has five fields, separated by spaces:

| Field            | Allowed values                                              |
| ---------------- | ----------------------------------------------------------- |
| Minute           | `0` to `59`                                                 |
| Hour             | `0` to `23`                                                 |
| Day of the month | `1` to `31`                                                 |
| Month            | `1` to `12`, or `jan` to `dec`                              |
| Day of the week  | `0` to `7`, where `0` and `7` are Sunday, or `sun` to `sat` |

In each field, `*` matches every value, `1,15` lists values, `1-5` sets a range, and `*/10` takes every tenth value. `0~59` draws a random value in a range each time the crontab loads. It spreads the jobs of several applications instead of starting them all at the same minute. You can also replace the five fields with `@hourly`, `@daily`, `@weekly`, `@monthly`, or `@yearly`.

| Schedule       | Runs                                                        |
| -------------- | ----------------------------------------------------------- |
| `*/15 * * * *` | Every 15 minutes                                            |
| `0 * * * *`    | Every hour, at minute 0, like `@hourly`                     |
| `30 2 * * *`   | Every day at 02:30                                          |
| `0 8 * * 1-5`  | At 08:00, from Monday to Friday                             |
| `0 6 * * mon`  | Every Monday at 06:00                                       |
| `0 0 1 * *`    | At midnight on the first day of each month, like `@monthly` |
| `0~59 4 * * *` | Once a day between 04:00 and 04:59                          |

When you restrict both the day of the month and the day of the week, instead of using `*`, a job runs when either one matches. `0 9 1 * mon` runs at 09:00 on the first day of each month, and also every Monday.

`@reboot` never runs: Clever Cloud installs the crontab after the cron daemon starts.

## Choose the time zone

Instances run in Coordinated Universal Time (UTC), and so do schedules. `0 9 * * *` runs at 09:00 UTC, that is 10:00 in Paris in winter and 11:00 in summer. To run a job at the same local time all year round, add a `CRON_TZ` line with the [name of a time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), such as `Europe/Paris`. The cron daemon then reads the schedules of the following lines in this time zone and follows its daylight saving time changes:

```json {filename="clevercloud/cron.json"}
[
  "CRON_TZ=Europe/Paris",
  "0 9 * * 1-5 /usr/bin/php $ROOT/scripts/send-daily-report.php"
]
```

A `CRON_TZ` line applies to the lines below it, up to the next `CRON_TZ` line. You can keep some jobs in UTC and schedule others in one or several local time zones. In this file, the synchronization stays in UTC, and each report leaves at 09:00 in its own time zone:

```json {filename="clevercloud/cron.json"}
[
  "*/10 * * * * /usr/bin/php $ROOT/scripts/sync-orders.php",
  "CRON_TZ=Europe/Paris",
  "0 9 * * 1-5 /usr/bin/php $ROOT/scripts/send-report.php --region=eu",
  "CRON_TZ=America/New_York",
  "0 9 * * 1-5 /usr/bin/php $ROOT/scripts/send-report.php --region=us"
]
```

`CRON_TZ` only sets when a job starts: the command itself still runs in UTC. Some commands rely on the local time, to name a file after the current date for example. For them, also add a `TZ` line, such as `"TZ=Europe/Paris"`, which sets the time zone of the commands below it.

When daylight saving time starts or ends, clocks skip an hour or go through it twice. In Paris, they jump from 02:00 to 03:00 on the last Sunday of March. They go back from 03:00 to 02:00 on the last Sunday of October. A job scheduled between 02:00 and 03:00 Paris time can then miss a run or run twice. Schedule it at another hour, or keep it in UTC.

## Write the commands

Jobs run as the `bas` user, from the `/home/bas` folder, through `/bin/sh`. Their environment is minimal: it holds none of your environment variables, and its `PATH` doesn't include the tools of your runtime, such as `node` or the tools you install with Mise. Write the absolute path of commands, such as `/usr/bin/php`, or load your environment as the next section shows.

The cron daemon turns any `%` character of a command into a line break, which cuts the command short. Escape it as `\%`, written `\\%` in JSON. For example, to archive the `uploads` folder every night in a file named after the current date, which `date +%F` returns as `YYYY-MM-DD`:

```json {filename="clevercloud/cron.json"}
[
  "0 1 * * * /usr/bin/tar -czf /tmp/uploads-$(/bin/date +\\%F).tar.gz -C $ROOT uploads"
]
```

### Load your environment variables

To give a job your environment variables and the tools of your runtime, run it through `bash -l`, which loads them before the command. For a single command, pass it to `bash -l -c` between single quotes:

```json {filename="clevercloud/cron.json"}
[
  "*/5 * * * * /bin/bash -l -c 'cd $ROOT && npm run sync-orders'"
]
```

For longer commands, write a script with a `#!/bin/bash -l` shebang:

```bash {filename="crons/sync-orders.sh"}
#!/bin/bash -l
cd "${APP_HOME}" || exit 1
bundle exec rake orders:sync
```

Make the script executable, and commit this permission with it:

```bash
chmod +x crons/sync-orders.sh
git add crons/sync-orders.sh
git commit -m "Add the orders synchronization job"
```

If you commit from a Windows computer, where Git doesn't record the permissions of files, run `git update-index --chmod=+x crons/sync-orders.sh` before you commit. Then call the script by its path:

```json {filename="clevercloud/cron.json"}
[
  "*/5 * * * * $ROOT/crons/sync-orders.sh"
]
```

Don't write `/bin/bash $ROOT/crons/sync-orders.sh`: this command starts a shell that ignores the shebang and its `-l` option, so the script runs without your environment variables. The [environment variables page](/doc/manage/environment-variables/#special-environment-variables) lists the variables Clever Cloud adds to yours.

### Read the output

The standard output and error of your jobs go to the logs of your application. You find them in the Console, in `clever logs`, and in your [log drains](/doc/observability/drains/). The cron daemon adds a line when each job starts and ends, and prefixes each line of output with `CMDOUT`:

```text
(bas) CMD (/home/bas/app_7d3f0c2e-5b1a-4c8e-9f2d-6a4b8e1c3f90/crons/sync-orders.sh)
(bas) CMDOUT (Synchronized 42 orders)
(bas) CMDEND (/home/bas/app_7d3f0c2e-5b1a-4c8e-9f2d-6a4b8e1c3f90/crons/sync-orders.sh)
```

To keep your logs readable, add `> /dev/null` to a command to drop its output, or `> /dev/null 2>&1` to drop its errors too.

## Avoid duplicate runs

Every instance of your application runs all the jobs of its crontab: with three instances, each job runs three times. For a job that must run on a single instance, such as sending a newsletter, check the `INSTANCE_NUMBER` variable at the start of your script. Its value is `0` on the first instance:

```bash {filename="crons/send-newsletter.sh"}
#!/bin/bash -l
if [[ "${INSTANCE_NUMBER}" != "0" ]]; then
  exit 0
fi

cd "${APP_HOME}" || exit 1
bundle exec rake newsletter:send
```

During a deployment, the instances of the previous deployment keep running until the new ones are ready, and both sets of instances number from `0`. For a few minutes, a job can then run twice: once on an old instance, once on a new one.

A lock shared by all instances, in your database for example, prevents two simultaneous runs. It doesn't prevent a second run once the first one ends. A job that must run only once per occurrence, such as a newsletter, can record each occurrence it handles to skip the ones already done. Record them atomically, in storage that all instances share. You can also make the job safe to run again.

A job can also last longer than its interval, and start again while the previous run goes on. The `flock` command skips a run when the previous one still holds its lock file. This lock file lives on the instance, so it only prevents overlapping runs on the same instance:

```json {filename="clevercloud/cron.json"}
[
  "*/5 * * * * /usr/bin/flock -n /tmp/sync-orders.lock $ROOT/crons/sync-orders.sh"
]
```

A job stops with its instance, at the end of a deployment or when the application scales down. The cron daemon doesn't catch up on occurrences it misses: if your application is stopped at the scheduled time, the job waits for its next occurrence. For long or heavy work, such as a large import, run a [Clever Task](/doc/deploy/tasks/) from a short job instead. The task then doesn't share the resources of the instances that serve your application.
