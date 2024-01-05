---
type: docs
title: SSH Keys
weight: 6
description: Secure your PaaS deployments with SSH key management on Clever Cloud. Learn how to generate, add, and manage SSH keys for secure access to your services.
tags:
- account-setup
keywords:
- git
- deploy
- deployment
- push
- ssh
- sshkeys
- private ssh
aliases:
- /doc/getting-started/ssh-keys
---

You need to add a SSH key to your Clever Cloud's account to deploy via Git.
SSH keys are used to establish a secure connection between your computer and Clever Cloud. A user can have multiple SSH keys.

{{< callout type="warning">}}
  Accounts cannot share the same SSH key. A SSH key is used to identify the actions made by a user and must be
  associated with only one account. If a key is used by more than one account, a warning will be displayed in the console.
{{< /callout >}}

## How to add a SSH key on Clever Cloud?
### Generate a classic SSH key
In your terminal, enter the following command:

```bash
ssh-keygen -t ed25519 -C "your_email@youremail.com"
```
It creates a new SSH key using the provided email, so that the owner of the key can be identified.

### Generate a FIDO/U2F SSH key
Since [OpenSSH 8.2](https://www.openssh.com/txt/release-8.2 ), generated keys can require a security device compatible with the FIDO/U2F standards (such as Nitrokeys, Solokeys or Yubikeys) to complete the authentication process. To generate such key, plug the device to your machine and enter this command:

```bash
ssh-keygen -t ed25519-sk -C "your_email@youremail.com"
```

Under macOS, you may need to install [Homebrew](https://brew.sh/), an OpenSSH version including full FIDO/U2F support, and use [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) key format:

```bash
brew install openssh
ssh-keygen -t ecdsa-sk -C "your_email@youremail.com"
```

{{< callout type="info" >}}
  You can use options related to security devices adding them with the `-O` argument (for example `-O resident`). They're detailed [here](https://man.openbsd.org/ssh-keygen#FIDO_AUTHENTICATOR).
{{< /callout >}}

### Choose the location of the key and a passphrase
When prompted in which file you want to save the key, just press enter. If it says that the file already exists, enter `n` for `no`. Type `ls`, verify the presence of the file and jump to [Add your SSH key on Clever Cloud](#AddYourSSHKeysOnCleverCloud). When asked, enter a passphrase:

  ```bash
  Generating public/private ed25519 key pair.
  Enter file in which to save the key (/your_home_path/.ssh/id_ed25519):
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

## I maybe have SSH keys, I want to check

### GitHub account and SSH key on Clever Cloud

If your account is linked to GitHub, a panel with your GitHub SSH keys will appear in the "SSH Keys" tab.
You can add any key already present in your GitHub account by clicking on the import button next to it.

### Find your SSH key

You may already have an SSH key and so do not need to generate a new one. To check if you have one, follow these steps:

#### Linux and macOS

1. Whether you use macOS or Linux, open your Terminal application.
2. Run `cd ~/.ssh/` in your Terminal.
3. If the folder exists, run `ls` and check if a pair of key exists : *id_ed25519* and *id_ed25519.pub*.
   Using *id_rsa* and *id_rsa.pub* is fine too. We are just advocating the use of *ed25519*.
   Smaller to copy and way stronger than 2048-bit RSA keys.
   If you can find them, you do not need to generate a new one, simply go to the following
   "Add your key on Clever Cloud" part!

<br/>

#### Windows

1. If you don't have it, download [Git for Windows](https://git-for-windows.GitHub.io/) and install it.
2. Run **Git Bash** (from the *Start Menu* or from the *Explorer* with the contextual menu (right click)).
3. Run `cd ~/.ssh/` in your Terminal.
4. If the folder exists, run `ls` and check if a pair of key exists : *id_ed25519* and *id_ed25519.pub* or *id_rsa* and *id_rsa.pub*. We would recommend using *ed25519* keys. Smaller to copy and way stronger than 2048-bit RSA keys. If you can find them, you do not need to generate a new one, simply go to the following "Add your key on Clever Cloud" part!

## Specific SSH key for Clever Cloud

If you want to use a specific key for Clever Cloud, you can set it in your SSH config by adding this :
```
Host *.clever-cloud.com 
   IdentityFile ~/.ssh/clevercloud
```

## Add a public SSH key on Clever Cloud

### From the Console
To declare your **public SSH Key** on Clever Cloud, in the [Console](https://console.clever-cloud.com)'s left navigation bar, go in "Profile" and in the "SSH Keys" tab.

Add the key by entering a name and the public SSH key. The key is the entire contents of the **id_[ed25519/rsa].pub** file including the `id_ed25519/ssh-rsa` part and your email.

{{< callout type="warning">}}
<p>Your public SSH key must be associated with only one account.</p>
{{< /callout >}}

If you see "*access denied*" or "*password:*" when you [push on Clever Cloud](https://www.clever-cloud.com/doc/clever-cloud-overview/add-application/#git-deployment), your SSH keys may be invalid or not available on Clever Cloud. Please check that you SSH key is present and valid in your profile.

### Through CC API or Clever cURL
You can also add a **public SSH key** from the command line with a simple cURL request to [our API](../openapi). The simpler way to do that is to use our CLI, [Clever Tools](https://github.com/CleverCloud/clever-tools), and its `clever curl` command once logged in:   
```
clever curl -X PUT -H "Content-Type: application/json" --data "\"$(cat ~/.ssh/yourkey.pub)\"" https://api.clever-cloud.com/v2/self/keys/newkeyname
```

## Use a private SSH key in an application
If you want to clone a repository from a private repository, you can add a [private SSH key]({{< ref "doc/reference/common-configuration.md##private-ssh-key" >}}) to an application by creating a folder clevercloud at the root of your application and creating the file `clevercloud/ssh.json` with the following content:
```
{
    "privateKeyFile": "path/to/file"
}
```
Of course you need to provide a valid path to a file that contains a valid key and that you will push on the Clever Cloud git remote.

## Check your SSH configuration

To check if your SSH key is correctly configured, you can try to run:

```bash
    ssh git@push.clever-cloud.com
```

The first time, you may have to type "yes" to continue.

If you see 
```
> git@push-par-clevercloud-customers.services.clever-cloud.com: Permission denied (publickey).
>
> fatal: Could not read from remote repository.
>
> Please make sure you have the correct access rights
> and the repository exists.
```
This error can occur when your SSH agent has not be configured to use your SSH key.

Most of the time, it is due to the presence of multiple SSH keys generated by 3rd party software, like GitHub for macOS.
To fix this you will need to configure your SSH agent.

## Configure your SSH agent

You can add those lines into your `~/.ssh/config` file. It tells your SSH agent which key to pick for a given hostname.
Please update your Clever Cloud SSH key path accordingly.

```bash
# config for Clever Cloud specific key (Paris zone)
Host push-par-clevercloud-customers.services.clever-cloud.com
  Hostname push-par-clevercloud-customers.services.clever-cloud.com
  User git
  IdentityFile ~/.ssh/id_ed25519_clevercloud

# config for Clever Cloud specific key (Roubaix zone)
Host push-rbx-clevercloud-customers.services.clever-cloud.com
  Hostname push-rbx-clevercloud-customers.services.clever-cloud.com
  User git
  IdentityFile ~/.ssh/id_ed25519_clevercloud

# config for Clever Cloud specific key (Warsaw zone)
Host push-wsw-clevercloud-customers.services.clever-cloud.com
  Hostname push-wsw-clevercloud-customers.services.clever-cloud.com
  User git
  IdentityFile ~/.ssh/id_ed25519_clevercloud

# config for Clever Cloud specific key (Montreal zone)
Host push-mtl-clevercloud-customers.services.clever-cloud.com
  Hostname push-mtl-clevercloud-customers.services.clever-cloud.com
  User git
  IdentityFile ~/.ssh/id_ed25519_clevercloud

# config for Clever Cloud specific key (Singapore zone)
Host push-sgp-clevercloud-customers.services.clever-cloud.com
  Hostname push-sgp-clevercloud-customers.services.clever-cloud.com
  User git
  IdentityFile ~/.ssh/id_ed25519_clevercloud

# config for Clever Cloud specific key (Sydney zone)
Host push-syd-clevercloud-customers.services.clever-cloud.com
  Hostname push-syd-clevercloud-customers.services.clever-cloud.com
  User git
  IdentityFile ~/.ssh/id_ed25519_clevercloud
```

<i class="icon-question-sign"></i> **Need help about SSH keys?**  
Contact us at <support@clever-cloud.com> or you can [read more about SSH Keys](https://git-scm.com/book/en/Git-on-the-Server-Generating-Your-SSH-Public-Key).

