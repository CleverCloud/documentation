---
type: docs
title: Elixir
shortdesc: Elixir is a functional, concurrent, general-purpose programming language that runs on the Erlang virtual machine…
tags:
- deploy
keywords:
- elixir
- phoenix
- erlang
str_replace_dict:
  "@application-type@": "Elixir"
type: docs
aliases:
- /doc/deploy/application/elixir
- /doc/deploy/application/elixir/elixir
- /doc/getting-started/by-language/elixir/
- /doc/partials/language-specific-deploy/elixir
---

## Overview

Clever Cloud supports Elixir based applications.

{{< content "create-application" >}}

{{< content "set-env-vars" >}}

## Configure your Elixir application

### Mandatory configuration

Get your Elixir version in your console with `$ elixir -v` and set the environment variable `CC_ELIXIR_VERSION` to its value. Available versions as of today are the following:

{{< runtimes_versions elixir >}}

#### Compatibility between Elixir and Erlang/OTP

- Each version of Elixir uses the most recent compatible version of Erlang, based on the compatibility table provided in the [official Elixir documentation](https://hexdocs.pm/elixir/compatibility-and-deprecations.html#between-elixir-and-erlang-otp).

#### If you deploy a Phoenix application

- Edit the file `config/prod.secret.exs` to replace `System.get_env("DATABASE_URL")` with `System.get_env("POSTGRESQL_ADDON_URI")`.
- Generate a secret token with `$ mix phx.gen.secret`.
- set environment variable **SECRET_KEY_BASE** to the value obtained with `$ mix phx.gen.secret` previously
- set environment variable **CC_PHOENIX_RUN_ECTO_MIGRATE** to `true` if you need to trigger the command `$ mix ecto.migrate`

## Build, deployment phases and custom configuration

Once you push your code to Clever Cloud, the following commands are run:

```bash
mix deps.get
mix deps.compile
npm install
```

These commands will compile your dependencies at the root of your project folder.
If you want to use another folder for `npm install`, specify it via the environment variable **CC_PHOENIX_ASSETS_DIR**.
To change the folder for the entire build / run process, you should use **APP_FOLDER** environment variable.

Then `mix compile` is run. If you want to override this behavior, you can set the environment variable **CC_MIX_BUILD_GOAL** to the value you desire.

At this point, there is the command `npm run deploy`.

Then `mix phx.digest` is run. You can override this one with the variable **CC_PHOENIX_DIGEST_GOAL**.

Finally, `mix phx.server` is invoked, and as always, you can override this behavior, either with **CC_RUN_COMMAND** where you have to specify the full command, or **CC_PHOENIX_SERVER_GOAL** where it will be a mix task by default.

Note: If you need to specify the timezone of your application, you can do it with the variable **TZ** set to the usual timezone format, for instance `Europe/Paris`.

 {{< content "deploy-git" >}}

 {{< content "link-addon" >}}

{{< content "more-config" >}}
