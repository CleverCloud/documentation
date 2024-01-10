---
type: docs
title: Configuration on all instances
position: 5
shortdesc: Learn how to do some basic setup configuration to get started
tags:
- reference
- dashboard-setup
keywords:
- common
- configuration
- hooks
type: docs
---

Each instance type (php,java,python,go,ruby…) has its own configuration. However, some of
these configuration items can be applied to any instance.

## Private SSH Key

If your company manages its own artifacts in a private repository (like, you
can only access them via git+ssh or sftp), and you need a private key to
connect to the server, you can either set it in an environment variable or
commit it in your application's Clever Cloud repository.

That key will be installed in `~/.ssh/` before the start of the build. So the
dependency manager will use it to fetch libs only accessible by ssh.

{{< callout type="info" >}}
  Please provide a key without pass phrase, or the system will be unable to unlock it
{{< /callout >}}

### Environment variable

Set your key as the value of the `CC_SSH_PRIVATE_KEY` variable. If you want it
to be saved to a specific file, you can set the `CC_SSH_PRIVATE_KEY_FILE`
variable.

### Committed file

First, you need to add the file `clevercloud/ssh.json`, its content is pretty straight-forward:

```json
{
    "privateKeyFile": "path/to/file"
}
```

The `privateKeyFile` field must be a path to an SSH private key. The path must be relative to the root of your repository.

For example, if your private key file is in the `clevercloud` folder and is named `my_key`, the `privateKeyFile` field will be `"clevercloud/my_key"`.

## Hooks

You can run specific tasks during the deployment of your application.

Please refer to the [hooks documentation]({{< ref "doc/develop/build-hooks.md" >}}) to learn more about them.

## Workers

You can run background tasks running in parallel of your application.

Please refer to the [workers documentation]({{< ref "doc/develop/workers.md" >}}) to learn more about them.
