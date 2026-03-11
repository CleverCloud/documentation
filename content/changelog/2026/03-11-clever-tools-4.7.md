---
title: "Clever Tools 4.7: SSH remote commands, improved drains and backup downloads"
date: 2026-03-11
description: Clever Tools 4.7 adds remote command execution over SSH, interactive instance selection, improved drain monitoring and more reliable database backup downloads
tags:
  - clever-tools
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonniere
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
excludeSearch: true
---

[Clever Tools 4.7.0](https://github.com/CleverCloud/clever-tools/releases/tag/4.7.0) is available. This release enhances SSH with remote command execution and interactive instance selection, improves drain monitoring and fixes database backup downloads.

## SSH remote command execution

You can now execute a single command on a running instance with the new `--command` (or `-c`) option. The command runs in a login shell and exits immediately, making it convenient for quick diagnostics, scripting or automation.

```bash
# List application files
clever ssh -c 'ls -lah $APP_HOME'

# Inspect application environment variables
clever ssh -c "env | sort"

# Read application logs
clever ssh -c "journalctl -u bas-deploy.service --no-pager -n 50"
```

This also enables AI coding assistants (Claude Code, Codex, Cursor, OpenCode...) to inspect the state of a running instance, analyse configuration files, check logs or troubleshoot issues on your behalf.

## Interactive instance selection

When multiple instances are running, `clever ssh` now displays an interactive selection prompt instead of a numbered list. This provides a more intuitive experience when choosing which instance to connect to.

```bash
clever ssh
> ? Select an instance:
> ❯ Sleepy Ponita - Instance 0 - UP (11281f38-...)
>   Tense Caterpie - Instance 1 - UP (b10d19d9-...)
```

## Improved drain monitoring

The `clever drain` and `clever drain get` commands now display message rates and throughput with dynamic units (messages/hour, messages/minute, messages/second, KiB/second, MiB/second) that adapt to the actual values. Retry information is also shown, including attempt count, last and next attempt timestamps, helping you troubleshoot delivery issues more effectively.

## Bug fixes

- **Database backup downloads** now use Node.js stream pipelines, fixing backpressure issues that could cause incomplete downloads on large backups.
- **Detached HEAD deployments** are now handled correctly when using the system Git feature, fixing failures that occurred when deploying from a detached HEAD state.

## How to upgrade

To upgrade Clever Tools, [use your favourite package manager](/doc/cli/install/). For example with `npm`:

```
npm update -g clever-tools
clever version
```
