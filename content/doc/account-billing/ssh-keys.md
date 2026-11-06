---
type: docs
linkTitle: SSH Keys
title: SSH Keys
description: Configure and manage SSH keys for secure access to your Clever Cloud applications and streamlined deployment workflows
keywords:
- ssh keys
- git deployment
- secure access
- ssh authentication
- clever cloud ssh
- public key
aliases:
- /account/ssh-keys-management
- /doc/account/ssh-keys
- /doc/account/ssh-keys-management
- /doc/account/ssh-keys-managment
- /doc/getting-started/ssh-keys
- /doc/ssh-keys
---

You need to add a SSH key to your Clever Cloud's account to deploy via Git.
SSH keys are used to establish a secure connection between your computer and Clever Cloud. A user can have multiple SSH keys.

> [!NOTE] One account per key
> Clever Cloud identifies your account from your SSH key when you deploy with Git or connect to an instance. A key can then belong to only one account. If several accounts use the same key, the Console displays a warning.

## How to add your SSH key on Clever Cloud?

{{% steps %}}

### Generate the key

In your Terminal, enter the following bash line:

```bash
ssh-keygen -t ed25519 -C "your_email@youremail.com"
```

This command creates a new SSH key using the provided email, so that the owner of the key can be identified.

### Save the key

When prompted in which file you want to save the key, just press enter.
If it says that the file already exists, enter `n` for `no`.
Type `ls`, verify the presence of the file and jump to [Add your SSH key on Clever Cloud](#add-a-public-ssh-key-on-clever-cloud).

### Enter a passphrase

When asked, enter a passphrase:

```bash
Generating public/private ed25519 key pair.
Enter file in which to save the key (/your_home_path/.ssh/id_ed25519):
# Now you should enter a passphrase.
Enter passphrase (empty for no passphrase): [Type a passphrase]
Enter same passphrase again: [Type passphrase again]
```

Which should give you something like this:

```bash
Your identification has been saved in /your_home_path/.ssh/id_ed25519.
Your public key has been saved in /your_home_path/.ssh/id_ed25519.pub.
The key fingerprint is:
01:0e:e5:2d:ab:98:d6:17:a1:6d:f0:68:9f:d0:a2:db your_email@youremail.com
```

{{% /steps %}}

## Add a FIDO/U2F SSH key

Since [OpenSSH 8.2](https://www.openssh.com/txt/release-8.2 ), generated keys can require a security device compatible with the FIDO/U2F standards (such as Nitrokeys, Solokeys or Yubikeys) to complete the authentication process. To generate such key, plug the device to your machine and enter this command:

```bash
ssh-keygen -t ed25519-sk -C "your_email@youremail.com"
```

Under macOS, you may need to install [Homebrew](https://brew.sh/), an OpenSSH version including full FIDO/U2F support, and use [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) key format:

```bash
brew install openssh
ssh-keygen -t ecdsa-sk -C "your_email@youremail.com"
```

> [!TIP] Security device options
> Add options for your security device with `-O`, such as `-O resident`. The [ssh-keygen manual](https://man.openbsd.org/ssh-keygen#FIDO_AUTHENTICATOR) lists them.

## Checking of existing SSH keys

### GitHub account and SSH key on Clever Cloud

If your account is linked to GitHub, a panel with your GitHub SSH keys will appear in the "SSH Keys" tab.
You can add any key already present in your GitHub account by clicking on the import button next to it.

### Finding SSH key locally

You may already have an SSH key and so do not need to generate a new one. To check if you have one, follow these steps:

{{< tabs >}}

{{< tab name="Linux and macOS" icon="simple:linux" >}}

1. Whether you use macOS or Linux, open your Terminal application.
2. Run `cd ~/.ssh/` in your Terminal.
3. If the folder exists, run `ls` and check if a pair of key exists : *id_ed25519* and *id_ed25519.pub*.
Using *id_rsa* and *id_rsa.pub* is fine too. The recommendation here is to consider using *ed25519* instead.
Smaller to copy and way stronger than 2048-bit RSA keys.
If you can find them, you do not need to generate a new one, simply go to the following
"Add your key on Clever Cloud" part!

{{< /tab >}}

{{< tab name="Windows" icon="windows" >}}1. If you don't have it, download [Git for Windows](https://git-for-windows.GitHub.io/) and install it.
2. Run **Git Bash** (from the *Start Menu* or from the *Explorer* with the contextual menu (right click)).
3. Run `cd ~/.ssh/` in your Terminal.
4. If the folder exists, run `ls` and check if a pair of key exists : *id_ed25519* and *id_ed25519.pub* or *id_rsa* and *id_rsa.pub*. We would recommend using *ed25519* keys. Smaller to copy and way stronger than 2048-bit RSA keys. If you can find them, you do not need to generate a new one, simply go to the following "Add your key on Clever Cloud" part!
{{< /tab >}}

{{< /tabs >}}

## Add a public SSH key on Clever Cloud

### From the Console

To declare your **public SSH Key** on Clever Cloud, in the [Console](https://console.clever-cloud.com)'s left navigation bar, go in "Profile" and in the "SSH Keys" tab.

Add the key by entering a name and the public SSH key. The key is the entire contents of the **id_[ed25519/rsa].pub** file including the `id_ed25519/ssh-rsa` part and your email.

If you see "*access denied*" or "*password:*" when you [push on Clever Cloud](/doc/getting-started/#choose-how-to-deploy), your SSH keys may be invalid or not available on Clever Cloud. Check that your SSH key is present and valid in your profile.

### From Clever Tools {#through-cc-api-or-clever-curl}

With [Clever Tools](/doc/tools/cli/) installed and authenticated, add your public key to your account:

```bash
clever ssh-keys add workstation ~/.ssh/id_ed25519.pub
```

Use the `.pub` file. The command registers its contents under the name `workstation`. Run `clever ssh-keys` to list the keys registered to your account.

## Use a private SSH key in an application

To let an application fetch private dependencies over SSH, configure its [private SSH key](/doc/manage/#private-ssh-key). This key authenticates outgoing connections from the application; it doesn't grant access to your Clever Cloud account.

## Check your SSH configuration

To check if your SSH key is correctly configured, you can try to run:

```bash
ssh git@push.clever-cloud.com
```

The first time, you may have to type "yes" to continue.

If you see:

```text
git@push-par-clevercloud-customers.services.clever-cloud.com: Permission denied (publickey).
fatal: Could not read from remote repository.
Please make sure you have the correct access rights
and the repository exists.
```

This error can occur when your SSH agent has not be configured to use your SSH key.

Most of the time, it is due to the presence of multiple SSH keys generated by 3rd party software, like GitHub for macOS.
To fix this you will need to configure your SSH agent.

## Configure your SSH agent

Add these entries to `~/.ssh/config` to select a key for Git deployments and for [SSH access to instances](/doc/develop/ssh-access/). Replace the identity file path with the private key that matches a public key registered to your account:

```sshconfig {filename="~/.ssh/config"}
Host push-*.services.clever-cloud.com
  User git
  IdentityFile ~/.ssh/id_ed25519_clevercloud
  IdentitiesOnly yes

Host sshgateway-clevercloud-customers.services.clever-cloud.com
  User ssh
  IdentityFile ~/.ssh/id_ed25519_clevercloud
  IdentitiesOnly yes
```

These entries configure the SSH client. They select the identities offered for each host; they don't add a key to your SSH agent.

To learn more about SSH keys, read the [Git documentation](https://git-scm.com/book/en/Git-on-the-Server-Generating-Your-SSH-Public-Key). For help with your account, contact [Clever Cloud Support](https://console.clever-cloud.com/ticket-center-choice).
