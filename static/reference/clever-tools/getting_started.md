---
type: docs
title: Getting started with Clever Cloud CLI
position: 1
shortdesc: Installing and using the Clever Cloud CLI tool
tags:
- cli
- reference
keywords:
- clever-tools
- get started
---

In addition to the Clever Cloud console, you can manage your addons and applications from the command line with Clever Tools.

## Installing Clever Tools

The clever-tools CLI can be installed through many different channels depending on your system setup.

### Via npm

If you already have node/npm on your system, you can run:

```shell
npm install -g clever-tools
```

If you want to install our latest beta release, you can run:

```shell
npm install -g clever-tools@beta
```

### On GNU/Linux

#### Debian/Ubuntu (.deb)

{{< callout type="warning" >}}
We recently moved from Bintray to a self-hosted Nexus repository available at <https://nexus.clever-cloud.com>.
If you were using Bintray to install our `.deb` packages, you will need to edit your `/etc/apt/sources.list` and remove the old entry with `https://dl.bintray.com/clevercloud/deb` before going further.
{{< /callout >}}

If you are using a GNU/Linux distribution that uses `.deb` packages like Debian or Ubuntu, you can run:

```sh
curl -fsSL https://clever-tools.clever-cloud.com/gpg/cc-nexus-deb.public.gpg.key | gpg --dearmor -o /usr/share/keyrings/cc-nexus-deb.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/cc-nexus-deb.gpg] https://nexus.clever-cloud.com/repository/deb stable main" | tee -a /etc/apt/sources.list
apt-get update
apt-get install clever-tools
```

NOTES:

* The `.deb` packages are hosted on Clever Cloud's public Nexus instance available at [https://nexus.clever-cloud.com](https://nexus.clever-cloud.com).
* Our PGP key is required to trust the repository.
* If you want access to the beta channel, you can use this in your `sources.list`:

```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/cc-nexus-deb.gpg] https://nexus.clever-cloud.com/repository/deb-beta beta main" | tee -a /etc/apt/sources.list
```

#### CentOS/Fedora (.rpm)

{{< callout type="warning" >}}
We recently moved from Bintray to a self-hosted Nexus repository available at <https://nexus.clever-cloud.com>.
If you were using Bintray to install our `.rpm` packages, you will need to remove the old `/etc/yum.repos.d/bintray-clevercloud-rpm.repo` before going further.
{{< /callout >}}

If you are using a GNU/Linux distribution that uses `.rpm` packages like CentOS or Fedora, you can run:

```sh
curl -s https://clever-tools.clever-cloud.com/repos/cc-nexus-rpm.repo > /etc/yum.repos.d/cc-nexus-rpm.repo
yum update
yum install clever-tools
```

NOTES:

* The `.rpm` packages are hosted on Clever Cloud's public Nexus instance available at [https://nexus.clever-cloud.com](https://nexus.clever-cloud.com).
* If you want access to the beta channel, you will need to edit `/etc/yum.repos.d/cc-nexus-rpm.repo` and set `enabled=1` for the `[clever-tools-beta]`.

#### Arch Linux

If you are using Arch Linux, the packages can be installed from AUR with this repo: [clever-tools-bin](https://aur.archlinux.org/packages/clever-tools-bin/).
If you don't know how to use this, you can run:

```sh
git clone https://aur.archlinux.org/clever-tools-bin.git clever-tools
cd clever-tools
makepkg -si
```

NOTES:

* If you want access to the beta channel, you can use this repo [clever-tools-bin-beta](https://aur.archlinux.org/packages/clever-tools-bin-beta/).

#### Exherbo

If you are using Exherbo, you can run:

```sh
cave resolve repository/CleverCloud -zx1
cave resolve clever-tools-bin -zx
```

#### Other distributions (.tar.gz)

If you are using another GNU/Linux distribution, you can download a `.tar.gz` archive and extract the binary in your `PATH`:

```sh
curl -O https://clever-tools.clever-cloud.com/releases/latest/clever-tools-latest_linux.tar.gz
tar xvzf clever-tools-latest_linux.tar.gz
cp clever-tools-latest_linux/clever ~/.local/bin/
```

NOTES:

* The packages are available on Clever Cloud's Cellar bucket: [clever-tools-latest_linux.tar.gz](https://clever-tools.clever-cloud.com/releases/latest/clever-tools-latest_linux.tar.gz).
* You can also retrieve any release (including beta) on this Cellar bucket by replacing `latest` (path and filename) with the version number you need.

### On macOS

#### Using homebrew

If you are using macOS and you have [homebrew](https://brew.sh) installed, you can run:

```sh
brew install CleverCloud/homebrew-tap/clever-tools
```

NOTES:

* If you want access to the beta channel, you can use `CleverCloud/homebrew-tap-beta/clever-tools` instead.

#### Using the `.tar.gz` archive

If you are using macOS, but you don't have [homebrew](https://brew.sh) installed, you can download a `.tar.gz` archive and extract the binary in your `PATH`:

```sh
curl -O https://clever-tools.clever-cloud.com/releases/latest/clever-tools-latest_macos.tar.gz
tar xvzf clever-tools-latest_macos.tar.gz
cp clever-tools-latest_macos/clever ~/.local/bin/
```

NOTES:

* The packages are available on Clever Cloud's Cellar bucket: [clever-tools-latest_macos.tar.gz](https://clever-tools.clever-cloud.com/releases/latest/clever-tools-latest_macos.tar.gz).
* You can also retrieve any release (including beta) on this Cellar bucket by replacing `latest` (path and filename) with the version number you need.

### On Windows

#### Using chocolatey

{{< callout type="warning" >}}
We recently moved from Bintray to a self-hosted Nexus repository available at <ahttps://nexus.clever-cloud.com>.
If you were using Bintray to install our `.nupkg` packages, you will need to remove the old source.
{{< /callout >}}

If you are using Windows and you have [chocolatey](https://chocolatey.org) installed, you can run:

```bash
choco sources add -n=clevercloud -s='https://nexus.clever-cloud.com/repository/nupkg/'
choco install clever-tools
```

NOTES:

* If you want access to the beta channel, you can use `choco sources add -n=clevercloud -s='https://nexus.clever-cloud.com/repository/nupkg-beta/'` instead.

#### Using the `.zip` archive

If you are using Windows, but you don't have [chocolatey](https://chocolatey.org) installed, you can download a `.zip` archive and extract the binary in your `PATH`.

NOTES:

* The packages are available on Clever Cloud's Cellar bucket: [clever-tools-latest_win.tar.gz](https://clever-tools.clever-cloud.com/releases/latest/clever-tools-latest_win.zip).
* You can also retrieve any release (including beta) on this Cellar bucket by replacing `latest` (path and filename) with the version number you need.

### Via Docker

If you are using docker, you can use the image provided [here](https://hub.docker.com/r/clevercloud/clever-tools/).

```sh
docker pull clevercloud/clever-tools
docker run --rm clever-tools <command>
```

#### Dockerfile

In your `Dockerfile` you can copy the clever-tools CLI from the image itself with a simple one liner:

```Dockerfile
COPY --from=clevercloud/clever-tools /bin/clever /usr/local/bin/clever
```

### Via Nix

If you are using Nix, you will find a Nix derivation on Fretlink's GitHub repository: <https://github.com/fretlink/clever-tools-nix>

## Enabling autocompletion

The clever-tools CLI comes with a comprehensive auto-completion system.
Some installation methods like `.deb` packages, `.rpm` packages or brew will try to enable it automatically.
If it does not work, try this for bash:

```bash
clever --bash-autocomplete-script $(which clever) | sudo tee /usr/share/bash-completion/completions/clever
```

or this for zsh:

```bash
clever --zsh-autocomplete-script $(which clever) | sudo tee /usr/share/zsh/site-functions
```

## Linking your account

To use `clever-tools`, you have to login.

```sh
clever login
```

It will open the Web console in your browser and reuse your existing session if you're already logged in.

`clever login` tries to open a browser through `xdg-open` on GNU/Linux systems (and in bash for windows).
Make sure you have `xdg-utils` available as well as a default browser set (or you can copy and paste the URL displayed in the console.

## Linking an existing application

If you have an already existing application, you can start managing it with
Clever Tools.

```sh
# First, go to your local repository
cd /path/to/your/application

# Then, link it to the Clever Cloud application
clever link <app_id>

# You can also use the application name (make sure to specify the
# organisation name if your application is in an organisation.
clever link --org <org_name> <app_name>

# Unlink an application
clever unlink <app_id>
```

{{< callout type="info" >}}
Once you have linked an application, clever-tools will create a Json configuration file named `.clever.json` at the root of the directory.
This file can be commited safely, others team members working on this repository will not have to link the application again.
This configuration file contains the AppID, so keep this in mind if you publish it on a public repository.
{{< /callout >}}

## Deploying new code

After having written new code, you can deploy it to Clever Cloud

```sh
# Will git push your code to Clever Cloud and display logs
clever deploy

# Will open your application
clever open
```
