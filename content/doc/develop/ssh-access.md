---
type: docs
linkTitle: SSH access
title: SSH access to running instances
description: Open a shell or run a command on the running instances of your Clever Cloud applications with Clever Tools or an SSH client, and debug failed deployments
keywords:
- ssh
- clever ssh
- ssh gateway
- debugging
- remote command
aliases:
- /doc/admin-console/ssh-keys
- /doc/administrate/ssh-clever-tools
- /doc/common-configuration/ssh-access
- /doc/develop/ssh
- /doc/doc/admin-console/ssh-keys
- /doc/find-help/ssh-access
- /doc/reference/clever-tools/ssh-access
- /doc/ssh-access
- /doc/tutorials/ssh_keys
---

To debug an application, open a shell on one of its running instances, or run a single command there, through the Clever Cloud SSH gateway. [Instances are immutable](/doc/develop/best-practices/immutable-infrastructure/): what you change on the disk of an instance disappears when a deployment or a scaling operation replaces it. Fix your code or your environment variables, then redeploy. Data you write to a database or an FS Bucket persists as usual.

## Before you start

You need:

- An OpenSSH client, with the `ssh` command in your `PATH`. macOS and most Linux distributions include one, and Windows provides it as the [OpenSSH Client](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse) feature. `clever ssh` runs this command too.
- A public SSH key [registered on your Clever Cloud account](/doc/account-billing/ssh-keys/). The gateway identifies your account from this key, and gives you access to the applications this account can reach.
- [Clever Tools](/doc/tools/cli/), logged in, to use `clever ssh`

## Connect with Clever Tools

From a folder linked to your application, `clever ssh` opens a shell on its instance. From anywhere else, set the application with `--app`, followed by its ID, or by its name if no other application shares it:

```bash
clever ssh
clever ssh --app my-api
```

The session opens as the `bas` user, in `/home/bas`, with your environment variables loaded. The files of your application are in `$APP_HOME`, that is `/home/bas/<app_id>`. [Docker applications](#docker-applications) work differently.

When several instances run, Clever Tools asks which one to connect to. In a script, without an interactive terminal, it lists them and fails instead. To choose upfront, set `--instance` to an instance number, an instance ID, or `any`:

```bash
clever ssh --instance 1
clever ssh --instance any
```

During a deployment, the instance going away and the one replacing it share the same number: Clever Tools then prefers an `UP` instance, the most recent first. A number never selects a build instance, and `any` only selects one when no other instance runs. To reach a specific instance, such as a build instance during a deployment, use its ID. `clever instances` lists them, with `build` in the `#` column of build instances:

```bash
clever instances
clever ssh --instance 9274818a-6247-46fb-adec-d9c0f190dcdd
```

Clever Tools uses your OpenSSH configuration and agent to choose the key. If they offer the key of another account, set the private key that matches a key of your account with `--identity-file`, or `-i`. Clever Tools then ignores the other keys of your agent, while the `IdentityFile` entries of your SSH configuration still apply:

```bash
clever ssh --identity-file ~/.ssh/id_ed25519_clevercloud
```

## Run a command

`--command`, or `-c`, runs one command on the instance and exits. Its output goes to your terminal, and `clever ssh` exits with the exit code of the command. You can then use it in scripts, or let an [AI agent](/doc/ai-llms/) inspect an instance. The command runs in a `bash` login shell, or `/bin/sh` if the instance has no `bash`, from `/home/bas` with your environment variables loaded:

```bash
clever ssh --instance any -c 'ls -la $APP_HOME'
clever ssh --instance any -c 'node --version'
```

Write the command between single quotes, so `$APP_HOME` and other variables expand on the instance and not on your computer. `clever ssh` doesn't forward your local standard input to the command, so you can't pipe a local file to it.

Add `--app-home` to run the command from the folder of your application, `$APP_HOME`, instead of `/home/bas`. If `$APP_HOME` isn't set or the instance can't enter it, the command doesn't run and `clever ssh` fails. `--app-home` isn't available for [Docker applications](#docker-applications):

```bash
clever ssh --instance any --app-home -c 'ls -la'
```

## Inspect an instance

The output of your application on an instance is in its journal. To read its last lines from your computer:

```bash
clever ssh --instance any -c 'journalctl -u bas-deploy.service --no-pager -n 50'
```

To follow it from an interactive session on the instance:

```bash
journalctl -efa -u bas-deploy.service
```

This journal only holds what this instance wrote since it started. To read the logs of all instances, including the ones a deployment removed, use [the logs of your application](/doc/observability/logs/).

### Debug a failed deployment

When a deployment fails, Clever Cloud removes its instance. To keep it for up to one hour, set `CC_TROUBLESHOOT` to `true`, then redeploy:

```bash
clever env set CC_TROUBLESHOOT true
clever restart
```

When the deployment fails, its logs show `Deploy failed in troubleshoot mode, keeping the instance up for closer inspection`. The deployment then stays in progress, and `clever deploy` or `clever restart` keeps waiting: run the next commands from another terminal.

The kept instance shows as `DEPLOYING` in `clever instances`. Connect to it by its ID: if a previous deployment still runs, its `UP` instances share its number, and `--instance any` prefers them:

```bash
clever instances
clever ssh --instance 3df3355e-6555-4d68-aa6f-a8f04c2734ac
```

A failure in the first steps of the deployment doesn't keep the instance. Once you're done, end the deployment with `clever cancel-deploy`, or push a fix. With the **Cancel ongoing deployment on new push** option, the new deployment cancels it. Then remove the variable with `clever env rm CC_TROUBLESHOOT`.

## Connect with an SSH client

Without Clever Tools, connect to the gateway with `ssh`. It lists the organisations your account can reach, then their applications, and asks you to choose one by its number:

```bash
ssh -t ssh@sshgateway-clevercloud-customers.services.clever-cloud.com
```

An application ID or an instance ID after the address skips these questions. With an application ID, the gateway still asks which instance to connect to if several run:

```bash
ssh -t ssh@sshgateway-clevercloud-customers.services.clever-cloud.com app_7d3f0c2e-5b1a-4c8e-9f2d-6a4b8e1c3f90
```

`-t` opens an interactive terminal. To run commands from a script, prefer `clever ssh --command`.

On your first connection, check that the gateway presents one of these fingerprints:

```text
ED25519 key fingerprint is SHA256:lys1oC3plDGyAsWD7Yd5fJVKQUV/Pbn/M5KI5GyAj5s.
RSA key fingerprint is SHA256:0odQb8NQPKYNCme2Nf3Xrz3Bc9kmrDK6eSJGIzj9aEA.
```

To choose the key `ssh` offers to the gateway, add a `Host` entry to your SSH configuration, as the [SSH keys page shows](/doc/account-billing/ssh-keys/#configure-your-ssh-agent). The gateway doesn't allow port forwarding: a tunnel opened with `-L` fails with `administratively prohibited`.

## Docker applications

In a Docker application, the SSH session opens a `bash` shell inside the container, in the working directory of the image, with your environment variables set. The image must include `bash`: otherwise the connection fails with `exec: "bash": executable file not found in $PATH`.

`clever ssh --command` doesn't work with Docker applications: it fails with `cannot attach stdin to a TTY-enabled container`. Open an interactive session instead. The `bas-deploy.service` journal and the `/home/bas` folder of other runtimes don't apply inside a container.

## Troubleshooting

Start from the message you get:

| Message                                                                  | Possible causes and fixes                                                                                                                                                                                                   |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Multiple instances are running, pick one with --instance`               | Several instances run and the terminal isn't interactive. Set `--instance`                                                                                                                                                  |
| `No running instances found for this application`                        | The application doesn't run. Check its state with `clever status`, then start or deploy it                                                                                                                                  |
| `Permission denied (publickey…)`                                         | `ssh` offered no key registered on a Clever Cloud account: the key file is missing, isn't loaded in your agent, or [isn't on your account](/doc/account-billing/ssh-keys/)                                                  |
| `The specified instance does not exist` or `no instances you can ssh to` | The ID is wrong or no longer exists, after a redeployment for example, or the key `ssh` offered belongs to an account that can't reach this application. Check the ID with `clever instances`, then the account of your key |

To check which account your key identifies, connect to the gateway without any ID:

```bash
ssh -t ssh@sshgateway-clevercloud-customers.services.clever-cloud.com
```

It lists the organisations of the account your key belongs to. If they aren't the expected ones, your agent offered the key of another account. Select the right one with `--identity-file` for `clever ssh`, or with a `Host` entry in your SSH configuration. If they're the expected ones but the application doesn't appear, ask an administrator of its organisation for access.

To check another key with `ssh`, add `-i` with `-o IdentitiesOnly=yes`, otherwise `ssh` still offers the keys of your agent first:

```bash
ssh -t -i ~/.ssh/id_ed25519_clevercloud -o IdentitiesOnly=yes ssh@sshgateway-clevercloud-customers.services.clever-cloud.com
```
