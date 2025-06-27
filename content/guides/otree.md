---
title: oTree
description: The powerful framework for multiplayer strategy games and complex surveys
tags:
- guides
keywords:
- otree
- python
type: "docs"
comments: false
draft: false
---

oTree is a powerful framework for multiplayer strategy games and complex surveys. It is built on Python and Django, and it allows you to create interactive web applications with ease.

If you need an example source code, init a new project (you’ll need `git`, `python` and `pip`, `pipx` or `uv`):

```bash
pip install otree
otree startproject oTreeExample

# You can also use pipx
pipx otree startproject oTreeExample

# Or uv
uvx otree startproject oTreeExample
```

## Create a Python application

You can create an application in the [Console](https://console.clever-cloud.com) or through [Clever Tools](https://github.com/CleverCloud/clever-tools/):

```bash
# Install Clever Tools if you don't have it yet
# You can also use your package manager: https://www.clever-cloud.com/developers/doc/cli/install/
npm i -g clever-tools
clever login

cd oTreeExample
clever create -t python
```

To deploy on Clever Cloud, your local folder need to be a git repository (if not, `git init`).

## Deploy oTree

oTree uses de SQLite database by default, but we recommend using a PostgreSQL database for production deployments. You can create it and link it to your Python application in the [Console](https://console.clever-cloud.com) or through [Clever Tools](https://github.com/CleverCloud/clever-tools/):

```bash
# Here we use a XXS Small plan, but you can choose the one fitting your needs
clever addon create postgresql-addon --plan xxs_sml --link oTreeExample oTreePg
```

### Configure the application

Set the following environment variables:

```bash
clever env set OTREE_PRODUCTION "1"

# Ask a password for the admin interface (user: admin), use STUDY for no login
clever env set OTREE_AUTH_LEVEL "DEMO"

# Automatically generate a random password, or use your own
clever env set OTREE_ADMIN_PASSWORD $(openssl rand -base64 32)

# We use a script to bind $DATABASE_URL to the PostgreSQL add-on before starting the server
clever env set clever env set CC_RUN_COMMAND "bash run.sh"
```

In the `run.sh`, you'll only need:

```bash
#!/bin/bash

export DATABASE_URL=${POSTGRESQL_ADDON_URI}
otree prodserver 9000
```

### Deploy the Python application

Now you can deploy your application:

```bash
git add .
git commit -m "First deploy"
clever deploy
```

You can display your website’s URL or add a custom domain to it (you’ll need to configure DNS):

```bash
clever domain
clever domain add your.website.tld
```

