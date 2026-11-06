---
title: "Clever Tools 5.4: faster startup and commands run from the application folder"
date: 2026-11-05
description: Clever Tools 5.4 starts faster, from npm and from standalone binaries, and runs clever ssh commands from the application folder with --app-home
tags:
  - clever-tools
  - cli
authors:
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Clever Tools 5.4.0](https://github.com/CleverCloud/clever-tools/releases/tag/5.4.0) is available. It reduces the commands startup time, and `clever ssh --command` can run from your application's folder.

## Faster startup

Clever Tools now loads several heavy dependencies only when a command needs them. The Redis® client only loads when `clever kv` sends a command, the HTTP proxy support only when you configure a proxy, and the JavaScript Git backend only when it runs. The update notifier relies on a lighter library, and a faster bundler now builds the standalone binaries.

Installed with npm, Clever Tools also enables the Node.js compile cache. Node.js stores the compiled code of Clever Tools in the cache folder of your user, such as `~/.cache/clever-cloud/compile-cache`, and reuses it on the next runs. The first run after an installation or a Node.js upgrade fills this cache, so it's slightly slower.

In the [benchmarks of these changes](https://github.com/CleverCloud/clever-tools/pull/1290), run on Linux with a filled cache, `clever addon list --help` went from about 310 ms to 175 ms with npm. With a standalone binary, it went from about 105 ms to 75 ms, a figure measured in a separate session after the switch to the new bundler.

## Run commands from the application folder

`clever ssh --command` runs from `/home/bas`. Add `--app-home` to run the command from the folder of your application, `$APP_HOME`, without a `cd` at its start. If `$APP_HOME` isn't set or the instance can't enter it, the command doesn't run and `clever ssh` fails:

```bash
clever ssh --instance any --app-home -c 'ls -la'
clever ssh --instance any --app-home -c 'php artisan migrate:status'
```

`--app-home` requires `--command`, and isn't available for Docker applications, whose sessions already open in the working directory of the image.

## Other changes

The update notifier still honors `--no-update-notifier`, `NO_UPDATE_NOTIFIER` and `CI`, and checks for a new version at most once a day. It now queries `registry.npmjs.org`, whatever the registry of your npm configuration. As before, standalone binaries don't show it: update them through your package manager or installer.

## How to upgrade

To upgrade Clever Tools, follow the [update guide](/doc/tools/cli/install/update/) for the installation method you use. For example with `npm`:

```bash
npm install -g clever-tools
clever version
```

- [Learn more about SSH access](/doc/develop/ssh-access/)
- [Learn more about Clever Tools](/doc/tools/cli/)
