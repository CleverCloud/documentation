---
title: "Clever Tools 5.1.1: more reliable SSH commands"
date: 2026-10-08
description: Clever Tools 5.1.1 runs SSH commands in a predictable shell, reports why an SSH session fails and fixes drains, SSH keys and tokens commands
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

[Clever Tools 5.1.1](https://github.com/CleverCloud/clever-tools/releases/tag/5.1.1) is available. This patch release makes `clever ssh --command` more reliable in scripts and CI jobs, following the `--instance` option introduced in [Clever Tools 5.1](/changelog/2026/10-02-clever-tools-5.1/), and fixes several commands.

`clever ssh --command` now runs your command in `bash` when the instance provides it, and in `/bin/sh` otherwise, instead of the shell set in `$SHELL`, which may be unset or wrong in Docker containers. When the SSH session ends before the command runs, for example after an authentication failure, Clever Tools now displays the reason instead of exiting silently with an error code. The output no longer gets truncated when you pipe it, and multi-byte characters stay intact:

```bash
clever ssh --instance any --command "uname -a" | tee instance.txt
```

`clever drain` and `clever drain get` no longer crash when the API can't provide the backlog statistics of a drain, for example for a disabled one. `clever ssh-keys add` reports an error instead of a success when the API rejects the key, and `clever tokens create` shows the invalid credentials hints instead of a misleading login error. Finally, `--no-color` and non-interactive outputs now disable colors even when `FORCE_COLOR` is set in your environment.

To upgrade Clever Tools, follow the [update guide](/doc/manage/cli/install/update/) for the installation method you use. For example with `npm`:

```bash
npm install -g clever-tools
clever version
```

- [Learn more about SSH access with Clever Tools](/doc/manage/cli/applications/deployment-lifecycle/#ssh)
