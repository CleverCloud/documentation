---
type: docs
title: SSH access
weight: 5
shortdesc: SSH access to running instances
tags:
- cli
- reference
keywords:
- ssh
- shell
- console
aliases:
- /doc/administrate/clever-tools/ssh-access
draft: true
---

While direct SSH access to instances is not recommended in an [immutable infrastructure](https://boxfuse.com/blog/no-ssh.html) setup, it can be useful for debugging purposes. Clever Cloud allows you to connect to running instances via SSH.

{{< callout type="warning" >}}
Clever Cloud instances are to be seen as *read-only* resources. Any change made on an instance **will not be persisted**. You can use SSH access for quick tests, but if you want to persist changes, you need to commit them in your repository. Changes made on instances are not kept across deployments.
{{< /callout >}}

{{< callout type="info" >}}
SSH on docker instances will attach to the running container. You must have `/bin/bash` installed (usually from the `bash` package) otherwise attaching to the container will fail.
{{< /callout >}}

## Requirements

You need to have the Clever Tools CLI installed locally.

[//]: # (ref "/doc/quickstartclever-tools-intro")

### Make sure you have a properly configured SSH key

To use SSH access, you need to have an SSH key properly configured in your Clever Cloud account. Please refer to [the SSH keys section of the documentation]({{< ref "doc/account/ssh-keys-management" >}}) to know how to set up your SSH keys.

## Accessing your machine with Clever Tools CLI

In order to access the machine via SSH using the Clever Tools CLI

[//]: # (ref "/doc/quickstartclever-tools-intro)

you need to have an application running on Clever Cloud and have linked it with your local repository using the Clever Tools CLI with `clever link --org <your_application's_organisation_id> <your_application_id>`

### Accessing your machine

You can access running instances of a linked application with `$ clever ssh` in the linked application's repository locally.

```shell
$ clever ssh
> Opening an ssh shell
> bas@67fbf787-3518-47bb-abd9-2c2575844edd ~ $
```

If multiple instances are running, you will be asked which one to use:

```shell
$ clever ssh
> 1) Sleepy Ponita - Instance 0 - UP (11281f38-31ff-43a7-8595-a2d82630c32b)
> 2) Tense Caterpie - Instance 1 - UP (b10d19d9-5238-408b-b038-3e32c7a301c2)
> Your choice: 1
> Opening an ssh shell
> bas@11281f38-31ff-43a7-8595-a2d82630c32b ~ $
```

You are now connected to the machine.

### Note for Windows users

`$ clever ssh` command will fail on PowerShell or cmd.exe if there is no `ssh.exe` in your path.
The most straightforward solution is to start `$ clever ssh` from `git-bash` but you can also add `ssh.exe` in your path..

## Access your application's folder

No matter wich way you've decided to use to SSH to the machine, your application's folder is located at: `/home/bas/<app_id>`.

## Show your application's logs

If you want to show your application's logs while you debug:

```shell
journalctl -efa -u bas-deploy.service
```

You can also use `journalctl` [with other options](https://www.commandlinux.com/man-page/man1/journalctl.1.html) if you need to.
