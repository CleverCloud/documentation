---
type: docs
title: SSH access to running instances
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

{{< callout type="warning" >}}
    <p>
    Clever Cloud instances are to be seen as <i>read-only</i> resources. Any change made on an instance <b>will not be persisted</b>. You can use SSH access for quick tests, but if you want to persist changes, you need to commit them in your repository. Changes made on instances are not kept across deployments.
    </p>
{{< /callout >}}

{{< callout type="warning">}}
    <p>
    For security reasons, you can't connect on the instance that hosts your Docker application.<br/>
    Instead, if `bash` is installed in your Docker application, you will be able to connect directly inside your container.<br/>
    Contact the support if you need help to debug your Docker applications.
    </p>
{{< /callout >}}


## Requirements

You need to have at least one of the following installed locally:
* the Clever Tools CLI

[//]: # (ref "doc/getting-started/clever-tools-intro.md)

* an SSH client (e.g [putty](https://putty.org/) for windows users)

### Make sure you have a properly configured SSH key

To use SSH access, you need to have a SSH key properly configured in your Clever Cloud account. Please refer to [the SSH keys section of the documentation]({{< ref "doc/account/ssh-keys-managment.md" >}}) to know how to set up your SSH keys.

## Using Clever Tools CLI

In order to access the machine via SSH using the Clever Tools CLI

[//]: # (ref "doc/getting-started/clever-tools-intro.md)

you need to have an application running on Clever Cloud and have linked it with your local repository using the Clever Tools CLI with `clever link --org <your_application's_organization_id> <your_application_id>`

### Accessing your machine

You can access running instances of a linked application with `$ clever ssh` in the linked application's repository locally.

    $ clever ssh
    > Opening an ssh shell
    > bas@67fbf787-3518-47bb-abd9-2c2575844edd ~ $

If multiple instances are running, you will be asked which one to use:

    $ clever ssh
    > 1) Sleepy Ponita - Instance 0 - UP (11281f38-31ff-43a7-8595-a2d82630c32b)
    > 2) Tense Caterpie - Instance 1 - UP (b10d19d9-5238-408b-b038-3e32c7a301c2)
    > Your choice: 1
    > Opening an ssh shell
    > bas@11281f38-31ff-43a7-8595-a2d82630c32b ~ $
    
You are now connected to the machine.

### Note for Windows users
`$ clever ssh` command will fail on PowerShell or cmd.exe if there is no `ssh.exe` in your path. 
The most straightforward solution is to start `$ clever ssh` from `git-bash` but you can also add `ssh.exe` in your path..

## Using an SSH client

You can connect using only your ssh client:

    ssh -t ssh@sshgateway-clevercloud-customers.services.clever-cloud.com <app_id>

You can omit the application ID. In that case, you will be prompted to choose an organization and an application.

You can validate connection to remote server with this fingerprint :

    ED25519 key fingerprint is SHA256:lys1oC3plDGyAsWD7Yd5fJVKQUV/Pbn/M5KI5GyAj5s.
    RSA     key fingerprint is SHA256:0odQb8NQPKYNCme2Nf3Xrz3Bc9kmrDK6eSJGIzj9aEA.

{{< callout type="warning" >}}
    <p>
        The <code>-t</code> flag, it is mandatory for the ssh connection to work properly.
        If your terminal hangs and you see <code>pseudo-terminal will not be allocated because stdin is not a terminal</code>, it's likely you've forgotten the <code>-t</code> flag.
    </p>
{{< /callout >}}


## Access your application's folder

No matter wich way you've decided to use to SSH to the machine, your application's folder is located at: `/home/bas/<app_id>`.

## Show your application's logs

If you want to show your application's logs while you debug:

    journalctl -efa -u bas-deploy.service

You can also use `journalctl` [with other options](https://www.commandlinux.com/man-page/man1/journalctl.1.html) if you need to.
