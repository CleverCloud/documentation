---
title: Clever Tools commands in more Console pages
description: The domain names, environment variables, TCP redirections, and add-on backups pages of the Console now show the matching Clever Tools commands, filled with the ID of your application or add-on
date: 2025-07-08
tags:
  - console
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

With the [new API tokens page](/changelog/2025/06-05-api-tokens-console-tips/), we introduced tips showing how to do the same task from the command line. They now reach more pages of the [Clever Cloud Console](https://console.clever-cloud.com): domain names, environment variables, TCP redirections, and add-on backups.

Open the `Command line` panel at the bottom of these blocks. It lists the matching [Clever Tools](/doc/tools/cli/) commands, filled with the ID of the current application or add-on, and links to the documentation. Copy them to script what you did in the Console or to automate it in a CI/CD pipeline. For example, with `app_xxxxxxxx` and `addon_xxxxxxxx` standing for the IDs the Console fills in:

```bash
clever domain diag --app app_xxxxxxxx
clever env --app app_xxxxxxxx -F shell
clever tcp-redirs add --namespace default --app app_xxxxxxxx
clever database backups addon_xxxxxxxx
```

- [Learn more about Clever Tools](/doc/tools/cli/)
- [Manage the configuration of your applications from Clever Tools](/doc/tools/cli/applications/configuration/)
- [Manage your add-ons and their backups from Clever Tools](/doc/tools/cli/addons/)
