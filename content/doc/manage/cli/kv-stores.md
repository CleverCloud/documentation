---
type: docs
linkTitle: KV stores
title: KV stores
description: Manage Materia KV and Redis key-value stores directly from Clever Tools CLI with commands for data operations and configuration
keywords:
- kv-stores
- materia-kv
- redis
- cli
- key-value
- database
- serverless
aliases:
- /doc/cli/kv-stores
- /doc/kv-stores
---

You can use Clever Tools to send Redis protocol commands to [Materia KV](/doc/deploy/databases/materia-kv/) and Redis® add-ons. Create a Materia KV add-on, then enable the experimental `kv` command:

```bash
clever addon create kv session-cache
clever features enable kv
clever kv session-cache PING
clever kv session-cache PING Hello
```

The first `PING` returns `PONG`; the second returns `Hello`. Clever Tools connects using the add-on's `REDIS_URL` environment variable. You can identify the add-on by its name, add-on ID or real ID. Use an ID when several add-ons share the same name.

To limit the lookup to an organisation, add `--org` (or `-o`):

```bash
clever kv session-cache PING --org platform-team
```

## Commands

You can send any Redis protocol command supported by your add-on. For example, store and retrieve a value, increment a counter, or set a key that expires after 120 seconds:

```bash
clever kv session-cache SET session-status active
clever kv session-cache GET session-status
clever kv session-cache INCR session-count
clever kv session-cache SET session-status active EX 120
clever kv session-cache TTL session-status
```

Use `COMMAND` to inspect the commands supported by the add-on:

```bash
clever kv session-cache COMMAND
```

To query a stored JSON string with `jq`, pass the value directly to it:

```bash
clever kv session-cache SET session-details '{"status": "active"}'
clever kv session-cache GET session-details | jq .status
```

Use `--format json` (or `-F json`) to encode the command result as JSON. This is useful for responses containing arrays, such as `SCAN`:

```bash
clever kv session-cache SCAN 0 -F json | jq '.[1]'
```

`SCAN` returns a cursor and a batch of keys. Repeat it with the returned cursor until the cursor is `0` to complete the iteration.
