You need to add a SSH key to your Clever Cloud's account to deploy via Git.
SSH keys are used to establish a secure connection between your computer and Clever Cloud. A user can have multiple SSH keys.

## I need to create my SSH key

1. In your Terminal, enter the following bash line:

    ```bash
    ssh-keygen -t ed25519 -C "your_email@youremail.com"
    ```

    This command creates a new ssh key using the provided email, so that the owner of the key can be identified.

2. When prompted in which file you want to save the key, just press enter.
    If it says that the file already exists, enter `n` for `no`. Type `ls`, verify the presence of the file and jump to [Add your SSH key on Clever Cloud](#AddYourSSHKeysOnCleverCloud).

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

## I created my account with GitHub

If your account is linked to GitHub, a panel with your GitHub SSH keys will appear in the "SSH Keys" tab.
You can add any key already present in your GitHub account by clicking on the import button next to it.

## Add your SSH key on Clever Cloud

### Public SSH Key

To declare your **public SSH Key** on Clever Cloud, in the left navigation bar, go in "Profile" and in the "SSH Keys" tab, add the key by entering a name and the public SSH key. The key is the entire content of the **id_[ed25519/rsa].pub** file including the `id_ed25519/ssh-rsa` part and your email.

### Private SSH Key

If you want to clone a repository from a private repository, you can add a [Private SSH Key]({{< ref "doc/reference/common-configuration.md#private-ssh-key" >}}) to an application by creating a folder clevercloud at the root of your application and creating the file `clevercloud/ssh.json` with the following content:

```json
{
    "privateKeyFile": "path/to/file"
}
```

Of course you need to provide a valid path to a file that contains a valid key and that you will push on the Clever Cloud git remote.

If you have trouble configuring this key you can refer to [this extended documentation](/getting-started/ssh-keys/)
