---
type: docs
linkTitle: Services Dependencies
title: Services Dependencies
description: Configure and manage service dependencies using Clever Tools CLI including linking applications and managing environment connections
keywords:
- services
- dependencies
- linking
- cli
- environment
- configuration
aliases:
- /doc/cli/services-depedencies
---

On Clever Cloud, applications can expose configuration to share environment variables with other services within the same account/organisation. Add-ons expose their configuration by default. Thus, when they're linked to an application, they automatically share credentials or important variables needed to configure and use them. Following commands help you with that.

Each can target a specific application, adding `--app APP_ID_OR_NAME` or a local alias (`--alias`, `-a`).

## published-config

To list exposed configuration, use:

```console
clever published-config
clever published-config -F json
clever published-config --format shell
```

To configure exposed configuration, use:

```console
clever published-config set SERVICE_URL https://payments-api.cleverapps.io
clever published-config rm SERVICE_URL
```

Use `set` to add or update a variable, `rm` to remove one, and `import` to replace the entire published configuration from standard input. Create a file containing `NAME=value` entries before importing it:

```console
printf '%s\n' 'SERVICE_URL=https://payments-api.cleverapps.io' > service.config
clever published-config import < service.config
```

For JSON input, add `--json`:

```bash
printf '%s\n' '[{"name":"SERVICE_URL","value":"https://payments-api.cleverapps.io"}]' | clever published-config import --json
```

## service

To list services dependencies, use:

```console
clever service
clever service --format json
```

Use `--only-apps` or `--only-addons` to filter dependencies. These options are mutually exclusive. Add `--show-all` to include services available for linking:

```bash
clever service --only-apps
clever service --only-addons --show-all
```

To add or remove a dependency, provide its ID or unambiguous name:

```bash
clever service link-app payments-api
clever service unlink-app payments-api
clever service link-addon session-cache
clever service unlink-addon session-cache
```
