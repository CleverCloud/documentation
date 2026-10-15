---
title: "Clever Tools 5.2: KV command generally available and drains filtered by type"
date: 2026-10-15
description: Clever Tools 5.2 makes the clever kv command generally available, filters drains by type and accepts now as a date in logs commands
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

[Clever Tools 5.2.0](https://github.com/CleverCloud/clever-tools/releases/tag/5.2.0) is available. The `clever kv` command leaves the experimental features, `clever drain` lists drains by type, and date options accept `now`.

## KV command generally available

You no longer need `clever features enable kv` to send commands to your [Materia KV](/doc/deploy/databases/materia-kv/) and Redis® add-ons. List replies now print one element per line, and Clever Tools refuses the commands a single connection can't serve, such as `SUBSCRIBE`, before connecting:

```bash
clever kv session-cache SET session-status active
clever kv session-cache HGETALL session-details
```

`clever kv` now relies on node-redis instead of ioredis, which changes some outputs compared to Clever Tools 5.1:

- Replies no longer depend on the case of the command: `hgetall` and `HGETALL` both print the flat list of fields and values sent by the server.
- `ZRANGE ... WITHSCORES` prints `[member, score]` pairs with numeric scores. An infinite score prints `Infinity`, or `null` with `--format json`.
- Integers outside the safe range of JavaScript may be rounded. Clever Tools prints a warning on the standard error output for an integer reply, but doesn't check integers nested in a list.
- A write is never sent twice: if the connection drops, the command fails, so check whether it landed before you retry.
- Clever Tools no longer adds the arguments you sent to its errors, although a server error message can still contain them. With `CLEVER_VERBOSE`, the debug messages of `clever kv` show the command name, never its arguments or replies.

## Filter drains by type

`clever drain` shows the recipient type of each drain in a new `Type` column. Add `--type` to only list the drains of a given type, such as `datadog`, `raw-http` or `syslog-tcp`:

```bash
clever drain --type datadog
clever drain --addon postgresql_xxxxxxxx --type raw-http -F json
```

## Other changes

The `--after` and `--before` options of `clever logs`, `clever accesslogs` and `clever instances`, and their `--since` and `--until` aliases, now accept `now` as a value. `clever drain` displays the application ID or name instead of `[object Object]` when it has no drain.

`clever deploy` shows the pushed reference next to the local commit instead of the remote one, which is always `master` on Clever Cloud. An unknown or ambiguous commit or reference now produces the same clear error with both Git backends, whatever the language of your `git`. Kubernetes commands recognize the new UUID-based IDs of clusters and node groups, and operator commands rely on the API to report a rolling version tag as up to date.

## How to upgrade

To upgrade Clever Tools, follow the [update guide](/doc/manage/cli/install/update/) for the installation method you use. For example with `npm`:

```bash
npm install -g clever-tools
clever version
```

- [Learn more about KV stores with Clever Tools](/doc/manage/cli/kv-stores/)
- [Learn more about logs drains](/doc/manage/cli/logs-drains/)
