---
type: docs
linkTitle: oTree
title: Deploy an oTree application
description: Configure and deploy oTree with PostgreSQL on Clever Cloud
keywords:
- otree
- python
- multiplayer games
- survey platform
- postgresql
---

{{< hextra/hero-subtitle >}}
  Deploy multiplayer experiments and surveys with oTree and PostgreSQL
{{< /hextra/hero-subtitle >}}

[oTree](https://www.otree.org/) is a Python framework for multiplayer experiments, behavioural research and surveys. This guide creates a current oTree project, stores its data in PostgreSQL and runs its production server on Clever Cloud.

## Prerequisites

- A [Clever Cloud account](https://console.clever-cloud.com)
- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Clever Tools](/doc/cli), installed and connected to your account

## Create an oTree project

Generate a project with the latest oTree release and move into its directory. The command asks whether you want to include the sample games:

```bash
uvx otree startproject oTreeExample
cd oTreeExample
```

The generated `requirements.txt` declares oTree and its PostgreSQL driver. Initialise the Git repository, then create a Python application with a local alias:

```bash
git init
clever create -t python -a myOTreeApp
```

Clever Tools targets your personal organisation by default. To use another organisation, add `--org ORGANISATION` or `-o ORGANISATION` when you create or link the application.

You can display your application’s URL or add a custom domain. A custom domain also requires DNS configuration:

```bash
clever domain
clever domain add your.website.tld
```

## Create the PostgreSQL database

Create a PostgreSQL add-on and link it to the application:

```bash
clever addon create postgresql-addon myOTreeDb -p xxs_sml -l myOTreeApp
```

oTree expects its connection string in `DATABASE_URL`, while a linked Clever Cloud PostgreSQL add-on provides `POSTGRESQL_ADDON_URI`. Add a `run.sh` file at the project root to map the variable before starting oTree on the Python runtime’s backend port:

```bash {filename="run.sh"}
#!/bin/bash

export DATABASE_URL="${POSTGRESQL_ADDON_URI}"
otree prodserver 9000
```

## Configure oTree

Enable production mode, protect the administration interface and configure the startup script:

```bash
clever env set OTREE_PRODUCTION 1
clever env set OTREE_AUTH_LEVEL DEMO
clever env set OTREE_ADMIN_PASSWORD "$(openssl rand -base64 32)"
clever env set CC_RUN_COMMAND "bash run.sh"
```

`DEMO` leaves public demonstrations accessible while protecting the administration interface. Use `STUDY` when participants must only access experiments through links you provide. The default administrator username is `admin`; replace the generated password with a value you can store securely if you need to log in.

## Deploy the application

Commit the project and deploy it:

```bash
git add .
git commit -m "First deploy"

clever deploy
clever open
```

The oTree home page redirects to the public demo list when you included sample games. PostgreSQL preserves sessions, participant data and configuration across restarts and deployments.

## Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/python/" title="Python runtime" subtitle="Configure Python applications" icon="python" >}}
  {{< card link="/developers/doc/addons/postgresql/" title="PostgreSQL" subtitle="Manage a PostgreSQL add-on" icon="circle-stack" >}}
  <!-- markdownlint-disable-next-line MD034 -->
  {{< card link="https://otree.readthedocs.io/en/latest/" title="oTree documentation" subtitle="Build experiments, games and surveys" icon="django" >}}
{{< /cards >}}
