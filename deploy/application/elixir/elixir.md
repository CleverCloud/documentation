---
title: Deploy Elixir applications
shortdesc: Elixir is a functional, concurrent, general-purpose programming language that runs on the Erlang virtual machine…
tags:
- deploy
keywords:
- elixir
- phoenix
- erlang
str_replace_dict:
  "@application-type@": "Elixir"
---

## Overview

Clever Cloud supports Elixir based applications.

{{< readfile "/content/partials/create-application.md" >}}

You must select **PostgreSQL** add-on for a Phoenix application.

{{< readfile "/content/partials/set-env-vars.md" >}}

{{< readfile "/content/partials/language-specific-deploy/elixir.md" >}}

{{< readfile "/content/partials/deploy-git.md" >}}

{{< readfile "/content/partials/link-addon.md" >}}

## Build, deployment phases and custom configuration

Once you push your code to the Clever Cloud remote provided, the following commands are run:
```
$ mix deps.get
$ mix deps.compile
$ npm install
```
These commands will compile your dependencies at the root of your project folder. 
If you want to use another folder for `npm install`, specify it via the environment variable **CC_PHOENIX_ASSETS_DIR**.
To change the folder for the entire build / run process, you should use **APP_FOLDER** environment variable.

Then `$ mix compile` is run. If you want to override this behavior, you can set the environment variable **CC_MIX_BUILD_GOAL** to the value you desire.

At this point, there is the command `$ npm run deploy`.

Then `$ mix phx.digest` is run. You can override this one with the variable **CC_PHOENIX_DIGEST_GOAL**.

Finally, `$ mix phx.server` is invoked, and as always, you can override this behavior, either with **CC_RUN_COMMAND** where you have to specify the full command, or **CC_PHOENIX_SERVER_GOAL** where it will be a mix task by default.

Note: If you need to specify the timezone of your application, you can do it with the variable **TZ** set to the usual timezone format, for instance `Europe/Paris`.

{{< readfile "/content/partials/more-config.md" >}}
