---
title: Clever Tools 3.5.2 is available with cURL, KV, Tasks and more!
date: 2024-04-11
tags:
  - clever-tools
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
description: Lots of new features included!
aliases:
- /changelog/2024-04-11-clever-tools-3.5.2
excludeSearch: true
---

Clever Tools 3.5 is now available, and this branch brings lots of new important features. First, `clever curl` is now public and listed as an official command. It helps you to send curl requests with the auth context of your Clever Tools configuration. Thus, you can use Clever Cloud [API v2 or v4](/developers/api/).

JSON format is supported for more commands, the `--since` option now supports a duration value. For example if you want to get logs since 2 hours ago, you can use `clever logs --since 2h`. This command documentation is available [there](/developers/doc/cli/logs-drains/#logs).

Clever Tasks can now be directly created and configured from Clever Tools. They're applications which can be run on demand, not awaiting any HTTP request on the `8080` port, but needing a `CC_RUN_COMMAND` to execute. Once it's done, the application stops. You're just billed for the execution time. It can help you to make some checks, compilation, file conversions, etc.

To create a Clever Task using Python for example:

```
# We create a Python App and its Git repository
mkdir pythonTask && cd pythonTask
echo 'print("Hello, from a Clever Cloud Task!")' > task.py
git init && git add . && git commit -m "Initial commit"

# We deploy this app as a Task
clever create -t python --task 'python task.py'
clever deploy
```

If you want to check if an application will deploy as a `TASK` or the `REGULAR` way, use `clever status`. Change the executed command using an environment variable. Set another value, for example with a bash script:

```
clever env set CC_RUN_COMMAND "bash a_bash_script.sh"
```
Clever Tasks will evolve with enhancements planed over the coming months. Feel free to tell us about your needs or ideas on this!

* [Learn more about Clever Tasks](/developers/doc/develop/tasks/)

Last but not least, we're introducing the access to Materia KV. Those granted with alpha access can now create a serverless, synchronously-replicated (over our 3 data centers in Paris) key-value add-on. You'll be able to use it with multiples kind of clients. First to be supported is Redis API. Thus, you can run:

````
clever addon create kv myKV
source <(clever addon env addon_myKV_id -F shell)
redis-cli -h $KV_HOST -p $KV_PORT --tls PING
````
* [Learn more about Materia KV](https://www.clever-cloud.com/blog/company/2024/04/16/materiadb-kv-materia-functions/) ([FR](https://www.clever-cloud.com/fr/blog/entreprise/2024/04/16/materiadb-kv-functions/))

To upgrade Clever Tools, [use your favorite package manager](/developers/doc/cli/install)

```
npm update -g clever-tools
clever version
```
