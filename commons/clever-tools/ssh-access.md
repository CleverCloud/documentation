---
title: SSH access
shortdesc: SSH access to running instances
tags:
- cli-setup
- apps
keywords:
- ssh
- shell
- console
---
# SSH access

While direct SSH access to instances is not recommended in an [immutable infrastructure](https://boxfuse.com/blog/no-ssh.html) setup, it can be useful for debugging purposes. Clever Cloud allows you to connect to running instances via SSH.

<div class="panel panel-warning">
  <div class="panel-heading">
    <h4 class="panel-title">SSH access is meant only for debugging purposes</h4>
  </div>
  <div class="panel-body">
    <p>
    Clever Cloud instances are to be seen as <i>read-only</i> resources. Any change made on an instance <b>will not be persisted</b>. You can use SSH access for quick tests, but if you want to persist changes, you need to commit them in your repository. Changes made on instances are not kept across deployments.
    </p>
  </div>
</div>

<div class="panel panel-warning">
  <div class="panel-heading">
    <h4 class="panel-title">SSH access is disabled on Docker instances</h4>
  </div>
  <div class="panel-body">
    <p>
    For security reasons, SSH access is disabled for Docker applications. Contact the support if you need help to debug your Docker applications.
    </p>
  </div>
</div>

## Make sure you have a properly configured SSH key

To use SSH access, you need to have a SSH key properly configured in your Clever Cloud account.

## Using clever-tools, with a linked application

You can access running instances of a linked application with `clever ssh`.

    clever ssh
    > Opening an ssh shell
    > bas@67fbf787-3518-47bb-abd9-2c2575844edd ~ $

If multiple instances are running, you will be asked which one to use:

    clever ssh
    > 1) Sleepy Ponita - Instance 0 - UP (11281f38-31ff-43a7-8595-a2d82630c32b)
    > 2) Tense Caterpie - Instance 1 - UP (b10d19d9-5238-408b-b038-3e32c7a301c2)
    > Your choice: 1
    > Opening an ssh shell
    > bas@11281f38-31ff-43a7-8595-a2d82630c32b ~ $
    
### For Windows users
`clever ssh` command will fail on PowerShell or cmd.exe if there is no ssh.exe in your path, which is true for most users. To be able to overcome this problem, the most straightforward solution is to start "clever ssh" from "git-bash".

## Without clever-tools

Alternatively, you can connect using only your ssh client:

    ssh -t ssh@sshgateway-clevercloud-customers.services.clever-cloud.com <app_id>

<div class="panel panel-warning">
  <div class="panel-heading">
    <h4 class="panel-title">Don't forget the <code>-t</code> flag</h4>
  </div>
  <div class="panel-body">
    <p>
        Don't forget the <code>-t</code> flag, it is mandatory for the ssh connection to work properly.
        If your terminal hangs and you see <code>pseudo-terminal will not be allocated because stdin is not a terminal</code>, it's likely you've forgotten the <code>-t</code> flag.
    </p>
  </div>
</div>

You can omit the application ID. In that case, you will be asked to choose an organization and an application.

## Access your application's folder

Your application's folder is located at: `/home/bas/<app_id>`

## Show your application's logs

If you want to show your application's logs while you debug:

    journalctl -efa -u bas-deploy.service

You can also use `journalctl` with other options if you need it
