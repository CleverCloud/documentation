---
type: docs
title: SSH access to running instances
linkTitle: SSH access
shortdesc: How to SSH access running instances on Clever Cloud
tags:
- administrate
keywords:
- ssh
- cli
- clever-tools
- putty
type: docs
---

## Overview

Clever Cloud allows you to connect to running instances via SSH.

While direct SSH access to instances is not recommended in an [immutable infrastructure](https://boxfuse.com/blog/no-ssh.html) setup, it can be useful for debugging purposes.

## Purpose

Clever Cloud instances are to be seen as _read-only_ resources. Any change made on an instance **will not be persisted**. You can use SSH access for quick tests, but if you want to persist changes, you need to commit them in your repository. Changes made on instances are not kept across deployments.

{{< callout type="warning">}}
For security reasons, you can't connect on the instance that hosts your Docker application. Instead, if `bash` is installed in your Docker application, you will be able to connect directly inside your container. Contact the support if you need help to debug your Docker applications.
{{< /callout >}}

## Requirements

You need to have at least one of the following installed locally:

* the [Clever Tools CLI](../../cli)
* an SSH client (e.g [putty](https://putty.org/) for windows users)

### Make sure you have a properly configured SSH key

To use SSH access, you need to have a SSH key properly configured in your Clever Cloud account. Please refer to [the SSH keys section of the documentation](../../account/ssh-keys-management) to know how to set up your SSH keys.

## Using Clever Tools CLI

In order to access the machine via SSH using the Clever Tools CLI
you need to have an application running on Clever Cloud and have linked it with your local repository using the Clever Tools CLI with `clever link --org <your_application's_organisation_id> <your_application_id>`

### Accessing your machine

You can access running instances of a linked application with `$ clever ssh` in the linked application's repository locally.

```shell
clever ssh
> Opening an ssh shell
> bas@67fbf787-3518-47bb-abd9-2c2575844edd ~ $
```

If multiple instances are running, you will be asked which one to use:

```shell
clever ssh
> 1) Sleepy Ponita - Instance 0 - UP (11281f38-31ff-43a7-8595-a2d82630c32b)
> 2) Tense Caterpie - Instance 1 - UP (b10d19d9-5238-408b-b038-3e32c7a301c2)
> Your choice: 1
> Opening an ssh shell
> bas@11281f38-31ff-43a7-8595-a2d82630c32b ~ $

You are now connected to the machine.
```

### Note for Windows users

`$ clever ssh` command will fail on PowerShell or cmd.exe if there is no `ssh.exe` in your path. The most straightforward solution is to start `$ clever ssh` from `git-bash` but you can also add `ssh.exe` in your path..

## Using an SSH client

You can connect using only your ssh client:

```shell
ssh -t ssh@sshgateway-clevercloud-customers.services.clever-cloud.com <app_id>
````

You can omit the application ID. In that case, you will be prompted to choose an organisation and an application.

You can validate connection to remote server with this fingerprint :

```shell
ED25519 key fingerprint is SHA256:lys1oC3plDGyAsWD7Yd5fJVKQUV/Pbn/M5KI5GyAj5s.
RSA     key fingerprint is SHA256:0odQb8NQPKYNCme2Nf3Xrz3Bc9kmrDK6eSJGIzj9aEA.
```

{{< callout type="warning" >}}
The `-t` flag is mandatory for the ssh connection to work properly. If your terminal hangs and you see `pseudo-terminal will not be allocated because stdin is not a terminal`, it's likely you've forgotten the `-t` flag.
{{< /callout >}}

## Access your application's folder

No matter which way you've decided to use to SSH to the machine, your application's folder is located at: `/home/bas/<app_id>`.

## Show your application's logs

If you want to show your application's logs while you debug:

```shell
journalctl -efa -u bas-deploy.service
```

You can also use `journalctl` [with other options](https://www.commandlinux.com/man-page/man1/journalctl.1.html) if you need to.

## Troubleshooting

A commonly encountered issue when using `clever ssh` is:
```
Error: Failed to choose instance: 'Error while running choice script: Error: This application has no instances you can ssh to'
```

First, make sure your application is running, otherwise there is no instance to connect to.

If your application is up, this means you aren't allowed to access the organisation or application. This might be due to permission issue.
If you're supposed to have access to the application, this is likely due to a key management issue. To fix it:
* make sure you've added your public key on your Clever Cloud profile. You can refer to our documentation to [add your SSH key on Clever Cloud](../../account/ssh-keys-management#add-a-public-ssh-key-on-clever-cloud)
* make sure your SSH agent is using the proper private key

A useful command for debugging is:
```
ssh -t ssh@sshgateway-clevercloud-customers.services.clever-cloud.com -v
```

This command shows information about your SSH connection attempt, such as the key, and the organisation your key is linked to.

If you don't see your SSH key listed, you must [add it to your SSH agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent).
If your key is present but not resolved as the first one in the list, you can [force the use of a specific key](../../account/ssh-keys-management/#configure-your-ssh-agent)