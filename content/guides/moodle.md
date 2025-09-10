---
type: docs
linkTitle: Moodle
title: Moodle
description: Deploy Moodle open source learning platform on Clever Cloud with detailed tutorials and best practices
keywords:
- moodle
- learning platform
- php
- mysql
- educational software
aliases:
- /moodle
---

[Moodle](https://moodle.org) is a learning platform designed to provide
educators, administrators and learners with a single robust, secure and
integrated system to create personalised learning environments.

This doc explains how to configure Moodle from source. Alternatively, an already configured repository exists as well on [Clever Cloud's GitHub page](https://github.com/CleverCloud/moodle).

## How to Configure and Deploy Moodle on Clever Cloud

{{% steps %}}

### Download Moodle

You can download Moodle from <https://download.moodle.org> and initialize a Git repository at root with `git init`.

### Configure `config.php`

Duplicate `config-dist.php` and rename it `config.php`. Update the following variables as follows:

```php {filename="config.php", linenos=table}
<?php  // Moodle configuration file

unset($CFG);
global $CFG;
$CFG = new stdClass();

$CFG->dbtype    = 'mysqli';
$CFG->dblibrary = 'native';
$CFG->dbhost    = getenv("MYSQL_ADDON_HOST");
$CFG->dbname    = getenv("MYSQL_ADDON_DB");
$CFG->dbuser    = getenv("MYSQL_ADDON_USER");
$CFG->dbpass    = getenv("MYSQL_ADDON_PASSWORD");
$CFG->prefix    = 'mdl_';
$CFG->dboptions = array (
  'dbpersist' => 0,
  'dbport' => getenv("MYSQL_ADDON_PORT"),
  'dbsocket' => '',
  'dbcollation' => 'utf8mb4_0900_ai_ci',
);

$CFG->wwwroot   = getenv("URL");
$CFG->dataroot  = '/app/moodledata';
$CFG->admin     = 'admin';

$CFG->directorypermissions = 0777;

$CFG->sslproxy = true;

require_once(__DIR__ . '/lib/setup.php');

// There is no php closing tag in this file,
// it is intentional because it prevents trailing whitespace problems!
```

Commit changes.

### Declare the PHP Application

On Clever Cloud Console, click **Create** > **An application** and choose a [PHP](/doc/applications/php) application with Git deployment. Add a [MySQL](/doc/addons/mysql) add-on during the process.

### Set Up Environment Variables

Add the following [environment variables](/doc/develop/env-variables) to tour PHP application:

```shell
CC_PHP_VERSION="8"
MAX_INPUT_VARS="5000"
URL="<your-url"
```

If you don't have an domain for your Moodle application yet, you'll be able to add a test domain provided by Clever Cloud in step 6.

### Set Up `moodledata` Folder

In this step you enable storage outside of your application, which [Moodle requires to run](https://docs.moodle.org/en/Site_backup). Use a [File System Bucket](/doc/addons/fs-bucket) to store all uploaded files and appearance set ups away from the application server, as recommended by Moodle.

Create an **FS Bucket add-on** and link it to your PHP application. In your FS Bucket dashboard, find the path variable. It should look like this: `CC_FS_BUCKET=/some/empty/folder:bucket-<bucket_id>`.

Add this variable to your **PHP application** and replace `/some/empty/folder` by `/moodledata`. Don't forget to **update changes**.

### Set Up Domain

Moodle needs an URL declared in variables to work properly. You can set it up in **Domains names**, from your PHP application menu. If you don't have a domain name yet, you can use a `cleverapp.io` subdomain provided by Clever Cloud for test purposes.

Don't forget to update `URL="<your-url"` if you haven't yet.

### Deploy

Get the remote in your application menu > **Information** > **Deployment URL** and add it to Git with `git remote add clever <clever-remote-url>`. Then, push your code with `git push clever -u master`

💡 If you get a reference error when pushing, try this: `git push clever main:master`.

{{% /steps %}}

## Cron for Moodle

Moodle [recommends to set up a Cron job](https://docs.moodle.org/en/Cron) that runs every minute. As explained in the [Clever Cloud cron documentation](https://www.clever.cloud/developers/doc/administrate/cron/#access-environment-variables), to have access to environment variable, you must wrap your commands in a bash script with [login shell](https://linux.die.net/man/1/bash) (`bash -l`).

Add a `cron.sh` file to the root of the application:

```bash {filename="cron.sh"}
#!/bin/bash -l
cd ${APP_HOME}
php admin/cli/cron.php
```

And make it executable:

```bash
chmod u+x cron.sh
```

### Declare the cron in Clever Cloud

Create a `clevercloud/cron.json` file with a string to run `cron.sh`every minute:

```json {filename="clevercloud/cron.json"}
[
  "* * * * * $ROOT/cron.sh"
]
```

You might encounter errors when the Cron tries to access `moodledata` in your FS Bucket. For FS Bucket backups, look for a dedicated tool like [rclone](https://rclone.org).


## 🎓 Further Help

{{< cards >}}
  {{< card link="/developers/doc/applications/php" title="PHP" subtitle="Deploy a PHP application on Clever Cloud" icon="php" >}}
  {{< card link="/developers/doc/administrate/cron" title="CRON" subtitle="Set up a CRON job for your app" icon="code-bracket" >}}
  {{< card link="/developers/doc/addons/fs-bucket" title="FS Bucket" subtitle="External File System for your apps" icon="fsbucket" >}}
  {{< card link="/developers/doc/addons/mysql" title="MySQL" icon="mysql" subtitle="Your self-hosted managed relational database" >}}
  {{< card link="https://docs.moodle.org/en/Installation_quick_guide" title="Moodle Documentation" subtitle="Check Moodle installation guide" icon="moodle" >}}
{{< /cards >}}

See [Moodle installation documentation](https://docs.moodle.org/en/Installation_quick_guide) for further help and development configuration.
