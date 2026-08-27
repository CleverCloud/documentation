---
type: docs
linkTitle: Moodle
title: Deploy a Moodle learning platform
description: Deploy Moodle with PHP, MySQL, persistent file storage and scheduled tasks
keywords:
- learning management system
- moodle
- mysql
- php
aliases:
- /moodle
---

{{< hextra/hero-subtitle >}}
  Deploy Moodle on Clever Cloud with a managed MySQL database, persistent data files and scheduled tasks.
{{< /hextra/hero-subtitle >}}

[Moodle](https://moodle.org/) is an open source learning management system for creating courses and personalised learning environments. It runs on Clever Cloud's [PHP runtime](/developers/doc/applications/php/) with a managed database and persistent storage outside the application code.

This guide was tested with Moodle 5.2.2, PHP 8.4 and MySQL 8.4. Check the [requirements for your Moodle release](https://moodledev.io/general/releases) before selecting other versions.

## Prepare Moodle

Download the release you want to deploy, then initialise a Git repository:

```bash
MOODLE_VERSION=5.2.2
mkdir myMoodle
cd myMoodle
curl -L "https://github.com/moodle/moodle/archive/refs/tags/v${MOODLE_VERSION}.tar.gz" | tar -xz --strip-components=1
git init
```

Create `config.php` at the project root. It reads the linked MySQL credentials and the public URL from environment variables, and keeps Moodle data outside the public directory:

```php {filename="config.php"}
<?php

unset($CFG);
global $CFG;
$CFG = new stdClass();

$CFG->dbtype = 'mysqli';
$CFG->dblibrary = 'native';
$CFG->dbhost = getenv('MYSQL_ADDON_HOST');
$CFG->dbname = getenv('MYSQL_ADDON_DB');
$CFG->dbuser = getenv('MYSQL_ADDON_USER');
$CFG->dbpass = getenv('MYSQL_ADDON_PASSWORD');
$CFG->prefix = 'mdl_';
$CFG->dboptions = [
    'dbpersist' => false,
    'dbport' => getenv('MYSQL_ADDON_PORT'),
    'dbsocket' => '',
    'dbcollation' => 'utf8mb4_unicode_ci',
];

$CFG->wwwroot = getenv('MOODLE_URL');
$CFG->dataroot = getenv('APP_HOME') . '/moodledata';
$CFG->admin = 'admin';
$CFG->directorypermissions = 02777;
$CFG->sslproxy = true;

require_once(__DIR__ . '/public/lib/setup.php');
```

Moodle ignores `config.php` by default to prevent accidental credential commits. This version contains no credentials, only environment variable references, so the deployment step adds it explicitly.

## Create the application and services

Install [Clever Tools](/developers/doc/cli/), log in, then create a PHP application and a linked MySQL add-on:

```bash
npm i -g clever-tools
clever login

clever create -t php -a myMoodle
clever addon create mysql-addon myMoodleDatabase -p xs_sml --link myMoodle
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link a resource.

Display the generated application domain:

```bash
clever domain
```

Set `MOODLE_URL` to that HTTPS URL. You can instead add a custom domain, which also requires [DNS configuration](/developers/doc/administrate/domain-names/):

```bash
clever domain add your.website.tld
```

Configure the public directory, supported PHP version, Moodle URL and required PHP input limit:

```bash
clever env set CC_WEBROOT /public
clever env set CC_PHP_VERSION 8.4
clever env set MAX_INPUT_VARS 5000
clever env set MOODLE_URL https://your-application.cleverapps.io
```

Create and link an FS Bucket for `moodledata`, then mount it into the absent directory expected by `config.php`:

```bash
clever addon create fs-bucket myMoodleData --link myMoodle

FS_BUCKET_HOST="$(clever env -F json | jq -er 'first(.fromAddons[] | select(.addonName == "myMoodleData") | .env[] | select(.name == "BUCKET_HOST") | .value)')"
clever env set CC_FS_BUCKET "/moodledata:${FS_BUCKET_HOST}"
unset FS_BUCKET_HOST
```

The name lookup expects the add-on name to be unique. If several add-ons use that name, retrieve the host with `clever addon env ADDON_ID -F json` and the ID returned when the add-on was created. Do not create or commit the mount target, because an existing non-empty directory prevents the FS Bucket from being mounted.

You can also create and link these resources from the [Clever Cloud Console](https://console.clever-cloud.com/).

## Schedule Moodle tasks

Moodle recommends running its [cron task](https://docs.moodle.org/en/Cron) every minute. Create a login-shell script so the scheduled process receives the application environment:

```bash {filename="cron.sh"}
#!/bin/bash -l

cd "$APP_HOME"
php admin/cli/cron.php
```

Declare the schedule in `clevercloud/cron.json`:

```json {filename="clevercloud/cron.json"}
[
  "* * * * * $ROOT/cron.sh"
]
```

Make the script executable:

```bash
chmod u+x cron.sh
```

## Deploy and install Moodle

Commit and deploy the project. Use `git add -f` for the environment-backed `config.php`, which Moodle's default ignore rules exclude:

```bash
git add .
git add -f config.php
git commit -m "Deploy Moodle"

clever deploy
clever open
```

The browser opens Moodle's installer. Confirm the environment checks, then define the site and administrator account. Database connectivity, the public URL and `moodledata` are already configured. The scheduled task starts succeeding after installation creates the database schema.

The MySQL add-on preserves courses, users and configuration while the FS Bucket preserves uploads, caches and other data files when application instances are replaced.

## Update Moodle

Before an update, back up MySQL and the FS Bucket, then follow Moodle's [upgrade procedure](https://docs.moodle.org/en/Upgrading). Replace the application sources with a compatible release while preserving `config.php`, `cron.sh` and `clevercloud/cron.json`, commit the changes and deploy them:

```bash
clever deploy
```

Moodle applies required database changes after deployment through its web or CLI upgrade process. Review release-specific requirements before changing the PHP or database version.

## Learn more

{{< cards >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://docs.moodle.org/en/Installation_quick_guide" title="Moodle installation" subtitle="Install and configure a Moodle site" icon="moodle" >}}
  {{< card link="/developers/doc/applications/php/" title="PHP applications" subtitle="Configure and deploy PHP applications" icon="php" >}}
  {{< card link="/developers/doc/addons/mysql/" title="MySQL" subtitle="Create and administer a managed database" icon="mysql" >}}
  {{< card link="/developers/doc/addons/fs-bucket/" title="FS Buckets" subtitle="Mount persistent file storage in an application" icon="fsbucket" >}}
  {{< card link="/developers/doc/administrate/cron/" title="Scheduled tasks" subtitle="Run recurring commands in an application" icon="clock" >}}
{{< /cards >}}
