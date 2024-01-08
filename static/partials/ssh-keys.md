You need to add a SSH key to your Clever Cloud's account to deploy via Git.
SSH keys are used to establish a secure connection between your computer and Clever Cloud. A user can have multiple SSH keys.

{{< callout type="warning" >}}
Accounts cannot share the same SSH key. A SSH key is used to identify the actions made by a user and must be associated with only one account.<br/>
If a key is used by more than one account, a warning will be displayed in the console.
{{< /callout >}}

## How to add your SSH key on Clever Cloud?

### I don't have any, I want to create an SSH key

1. In your Terminal, enter the following bash line:

    ```bash
    ssh-keygen -t ed25519 -C "your_email@youremail.com"
    ```

    This command creates a new ssh key using the provided email, so that the owner of the key can be identified.

2. When prompted in which file you want to save the key, just press enter.
    If it says that the file already exists, enter `n` for `no`. Type `ls`, verify the presence of the file and jump to [Add your SSH key on Clever Cloud](#add-your-ssh-key-on-clever-cloud).

3. When asked, enter a passphrase:

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

## I maybe have SSH keys, I want to check

### GitHub account and SSH key on Clever Cloud

If your account is linked to GitHub, a panel with your GitHub SSH keys will appear in the "SSH Keys" tab.
You can add any key already present in your GitHub account by clicking on the import button next to it.

### Find your SSH key

You may already have an SSH key and so do not need to generate a new one. To check if you have one, follow these steps:

#### Linux and Mac

1. Whether you use Mac or Linux, open your Terminal application.
2. Run `cd ~/.ssh/` in your Terminal.
3. If the folder exists, run `ls` and check if a pair of key exists : `id_ed25519` and `id_ed25519.pub`.

Using `id_rsa` and `id_rsa.pub` is fine too. We are just advocating the use of **ed25519**.

It is smaller to copy and way stronger than 2048-bit RSA keys.

If you can find them, you do not need to generate a new one, simply go to the following "Add your key on Clever Cloud" part!

#### Windows

1. If you don't have it, download [Git for Windows](https://git-for-windows.GitHub.io/) and install it.
2. Run **Git Bash** (from the *Start Menu* or from the *Explorer* with the contextual menu (right click)).
3. Run `cd ~/.ssh/` in your Terminal.
4. If the folder exists, run `ls` and check if a pair of key exists : `id_ed25519` and `id_ed25519.pub`.

Using `id_rsa` and `id_rsa.pub` is fine too. We are just advocating the use of **ed25519**.

It is smaller to copy and way stronger than 2048-bit RSA keys.

If you can find them, you do not need to generate a new one, simply go to the following "Add your key on Clever Cloud" part!

## Specific SSH key for Clever Cloud

If you want to use a specific key for Clever Cloud, you can set it in your SSH config by adding this:

```shell
Host *.clever-cloud.com 
  IdentityFile ~/.ssh/clevercloud
```

## Add your SSH key on Clever Cloud

### Public SSH Key

To declare your **public SSH Key** on Clever Cloud, in the left navigation bar, go in "Profile" and in the "SSH Keys" tab.

Add the key by entering a name and the public SSH key. The key is the entire contents of the **id_[ed25519/rsa].pub** file including the `id_ed25519/ssh-rsa` part and your email.

{{< callout type="warning" >}}
Your public SSH key must be associated with only one account.
{{< /callout >}}

If you see "*access denied*" or "*password:*" when you [push on Clever Cloud](https://www.clever-cloud.com/doc/clever-cloud-overview/add-application/#git-deployment), your SSH Keys may be invalid or not available on Clever Cloud. Please check that you SSH Key is present and valid in your profile.

## Private SSH Key

If your company manages its own artifacts in a private repository (like, you
can only access them via git+ssh or sftp), and you need a private key to
connect to the server, you can either set it in an environment variable or
commit it in your application's Clever Cloud repository.

That key will be installed in `~/.ssh/` before the start of the build. So the
dependency manager will use it to fetch libs only accessible by ssh.

NB: Please provide a key without pass phrase, or the system will be unable to unlock it

### Environment variable

Set your key as the value of the `CC_SSH_PRIVATE_KEY` variable. If you want it
to be saved to a specific file, you can set the `CC_SSH_PRIVATE_KEY_FILE`
variable.

### Committed file

First, you need to add the file `clevercloud/ssh.json`, its content is pretty straight-forward:

```javascript
{
  "privateKeyFile": "path/to/file"
}
```

The `privateKeyFile` field must be a path to a SSH private key. The path must be relative to the root of your repository. e.g. if your private key file is in the `clevercloud` folder and is named `my_key`, the `privateKeyFile` field will be `"clevercloud/my_key"`.

## Check your ssh configuration

To check if your ssh key is correctly configured, you can try to run:

```bash
ssh git@push.clever-cloud.com
```

The first time, you may have to type "yes" to continue.

If you see:

```shell
> git@push-par-clevercloud-customers.services.clever-cloud.com: Permission denied (publickey).
>
> fatal: Could not read from remote repository.
>
> Please make sure you have the correct access rights
> and the repository exists.
```

This error can occur when your SSH agent has not be configured to use your SSH key.

Most of the time, it is due to the presence of multiple SSH keys generated by 3rd party software, like GitHub for Mac.
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

{{< callout emoji="❔" >}}
**Need h elp about SSH keys?**  
Contact us at <support@clever-cloud.com> or you can [read more about SSH Keys](https://git-scm.com/book/en/Git-on-the-Server-Generating-Your-SSH-Public-Key).
{{< /callout >}}
