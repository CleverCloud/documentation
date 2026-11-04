---
type: docs
weight: 63
linkTitle: Configure applications
title: Configure applications
description: Configure common settings across all instance types including SSH keys, build hooks, and shared deployment configurations
keywords:
- configuration
- instances
- ssh-keys
- build-hooks
- deployment
- settings
aliases:
- /doc/clever-cloud-overview/common-application-configuration
- /doc/common-configuration
- /doc/clever-cloud-overview/common-application-configuration/
- /doc/reference/common-configuration
---

Each instance type (php,java,python,go,ruby…) has its own configuration. However, some of
these configuration items can be applied to any instance.

## Private SSH Key

To fetch private dependencies over SSH, provide a private key for your application.
Clever Cloud installs it in `~/.ssh/` before the build. Register its public key
with the service that hosts the dependencies. This key is separate from the
[public keys on your Clever Cloud account](/doc/account-billing/ssh-keys/),
which authenticate your Git deployments and access to instances.

Use a key without a passphrase: the deployment can't unlock it interactively.

Set `CC_SSH_PRIVATE_KEY` to the complete private key, including its header,
footer, and line breaks, in your application's environment variables. This
keeps the key out of version control. With Clever Tools, write `--` before
the key, otherwise Clever Tools reads its `-----BEGIN` line as an option:

```bash
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519_dependencies
clever env set CC_SSH_PRIVATE_KEY -- "$(cat ~/.ssh/id_ed25519_dependencies)"
```

Clever Cloud saves the key as `~/.ssh/id_ed25519` by default. To change its
name, set `CC_SSH_PRIVATE_KEY_FILE` to a file name, such as `dependencies_key`.
This value is a file name within `~/.ssh/`, not a path, and can't contain `/`.

## Hooks

You can run specific tasks during the deployment of your application.

Please refer to the [hooks documentation](/doc/develop/common-configuration/build-hooks) to learn more about them.

## Workers

You can run background tasks running in parallel of your application.

Please refer to the [workers documentation](/doc/develop/common-configuration/workers) to learn more about them.
