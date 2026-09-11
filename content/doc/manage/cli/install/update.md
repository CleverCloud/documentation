---
type: docs
weight: 1
linkTitle: Update Clever Tools
title: Update Clever Tools
description: Update Clever Tools CLI to its latest version with npm, pnpm, Bun, Yarn, AUR, rpm, deb, Homebrew, WinGet, Docker, Nix or standalone binaries
keywords:
- update
- upgrade
- clever-tools
- cli
- version
---

Clever Tools notifies you when a new version is available. The command to update it depends on how you installed it. If you're not sure, see [how to install Clever Tools](/doc/manage/cli/install/). Once updated, check the installed version:

```bash
clever version
```

## Node.js

The npm package requires Node.js 24 or later, upgrade Node.js first if needed.

### npm

```bash
npm install -g clever-tools
```

### pnpm

```bash
pnpm add -g clever-tools
```

### Bun

```bash
bun add -g clever-tools
```

### Yarn

```bash
yarn global add clever-tools
```

## GNU/Linux

### Arch Linux (AUR)

With an AUR helper like `yay`, update the package you installed. For [`clever-tools`](https://aur.archlinux.org/packages/clever-tools/), the Node.js flavor, run:

```bash
yay -S clever-tools
```

For [`clever-tools-bin`](https://aur.archlinux.org/packages/clever-tools-bin/), the self-contained binary, run:

```bash
yay -S clever-tools-bin
```

### CentOS/Fedora (.rpm)

```bash
yum update clever-tools
```

### Debian/Ubuntu (.deb)

```bash
apt update
apt install --only-upgrade clever-tools
```

### Exherbo

```bash
cave sync
cave resolve clever-tools-bin -zx
```

### Other distributions (.tar.gz)

Download the latest archive again and replace the binary in your `PATH`:

```bash
curl -O https://clever-tools.clever-cloud.com/releases/latest/clever-tools-latest_linux.tar.gz
tar xvzf clever-tools-latest_linux.tar.gz
cp clever-tools-latest_linux/clever ~/.local/bin/
```

## macOS

### Homebrew

```bash
brew upgrade CleverCloud/homebrew-tap/clever-tools
```

### Binary (.tar.gz)

Download the latest archive again and replace the binary in your `PATH`:

```bash
curl -O https://clever-tools.clever-cloud.com/releases/latest/clever-tools-latest_macos.tar.gz
tar xvzf clever-tools-latest_macos.tar.gz
cp clever-tools-latest_macos/clever ~/.local/bin/
```

## Windows

### WinGet

```PowerShell
winget upgrade CleverTools
```

### Binary (.zip)

Download the latest archive again and replace the binary in your `PATH`:

```PowerShell
Invoke-WebRequest https://clever-tools.clever-cloud.com/releases/latest/clever-tools-latest_win.zip -OutFile clever-tools-latest_win.zip
Expand-Archive .\clever-tools-latest_win.zip -DestinationPath . -Force
```

## Docker

Pull the image again to get the latest tag:

```bash
docker pull clevercloud/clever-tools
```

## Nix package manager

Update your channel or flake input, then upgrade the package as usual for your setup. See [the Clever Tools package on NixOS Search](https://search.nixos.org/packages?channel=unstable&show=clever-tools&from=0&size=50&sort=relevance&type=packages&query=clever-tools).
