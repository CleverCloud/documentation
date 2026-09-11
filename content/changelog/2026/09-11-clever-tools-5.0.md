---
title: "Clever Tools 5.0: Node.js 24, system Git by default and Splunk drains"
date: 2026-09-11
description: Clever Tools 5.0 moves to Node.js 24, deploys with your system Git by default, forwards logs to Splunk, displays TCP and SSH access logs and honors proxy settings
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

[Clever Tools 5.0.0](https://github.com/CleverCloud/clever-tools/releases/tag/5.0.0) is available. It's a new major version: the npm package now requires Node.js 24, and Git operations rely on the `git` installed on your system by default. This release also forwards logs to Splunk, displays TCP and SSH access logs, and honors proxy environment variables.

## Node.js 24

Clever Tools now runs on Node.js 24, the current Active LTS. If you install the package with npm, pnpm or Yarn, upgrade Node.js to version 24 or later first. Standalone binaries embed their own Node.js runtime, so this change doesn't affect them.

## System Git by default

Clever Tools used a pure JavaScript Git implementation to deploy your applications. It only supports HTTP, slows down on repositories with rewritten history, times out on large pushes and can't deploy from a linked worktree. The `system-git` feature, which uses the `git` available in your `PATH` instead, is now stable and enabled by default.

If `git` isn't installed on your system, or if you face an issue with this backend, fall back to the previous implementation:

```bash
clever features disable system-git
```

In the latter case, [open an issue on the Clever Tools repository](https://github.com/CleverCloud/clever-tools/issues) with the command you ran and its output, so the team can fix it.

## Splunk drains and per-type drain commands

You can now forward logs of an application or an add-on to a [Splunk HTTP Event Collector](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector) (HEC). The `--index` and `--sourcetype` options are optional: without them, the values bound to your HEC token apply. As self-hosted Splunk instances ship a self-signed certificate on port `8088` by default, add `--tls-verification trustful` if you didn't replace it:

```bash
clever drain create splunk https://splunk.example.com:8088/services/collector/event --hec-token "$SPLUNK_HEC_TOKEN"
clever drain create splunk https://splunk.example.com:8088/services/collector/event --hec-token "$SPLUNK_HEC_TOKEN" --tls-verification trustful
```

`clever drain create` now exposes one subcommand per drain type. Valid commands keep the same syntax, but the help of each type only lists the options it supports, and a wrong option fails before any API call instead of being silently ignored.

## TCP and SSH access logs

`clever accesslogs` used to skip every access log without an HTTP section. It now displays TCP redirections and SSH connections too, with their transport in a new column. HTTP methods and paths also get their own columns, so paths stay aligned whatever the method length. The CLF output format remains dedicated to HTTP access logs.

## Proxy support

Clever Tools now honors the `http_proxy` and `https_proxy` environment variables, like `curl` or `kubectl` do, and `no_proxy` to exclude hosts. When none of them is set, requests go out directly as before:

```bash
export https_proxy="http://proxy.internal:3128"
clever status
```

## Other changes

`clever ssh` no longer falls back to password authentication, so a missing or unregistered key fails immediately, and its `--identity-file` option now presents the requested key. When `clever login` can't open a browser, for example on a headless Linux system, it prints a warning instead of crashing and waits for you to open the displayed URL.

Clever Tools now notifies you when a new version is available, even in standalone binaries. On Arch Linux, Clever Cloud now maintains the [`clever-tools`](https://aur.archlinux.org/packages/clever-tools/) AUR package, which installs the npm package, alongside [`clever-tools-bin`](https://aur.archlinux.org/packages/clever-tools-bin/) and its standalone binary.

## How to upgrade

To upgrade Clever Tools, follow the [new update guide](/doc/manage/cli/install/update/) for the installation method you use. For example with `npm`, once Node.js 24 is installed:

```bash
npm install -g clever-tools
clever version
```
