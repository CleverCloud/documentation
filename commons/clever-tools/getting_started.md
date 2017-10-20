---
title: Getting started with Clever Cloud CLI
position: 1
shortdesc: Installing and using the Clever Cloud CLI tool
tags:
- cli-setup
keywords:
- cli
- clever-tools
---

# Clever Cloud CLI overview

In addition to the Clever Cloud console, you can manage your addons and
applications from the command line with Clever Tools.

## Installing Clever Tools

Clever Tools is available on Windows, GNU/Linux and MacOS.

### MacOS

Clever Tools is packaged using [homebrew](https://brew.sh):

    brew install CleverCloud/tap/clever-tools

If you don't want to use `brew`, a pre-compiled version is available: [clever-tools-0.9.0_macos.tar.gz](https://clever-tools.cellar.services.clever-cloud.com/releases/0.9.0/clever-tools-0.9.0_macos.tar.gz).
You need to put both files (`clever` and `nodegit.node`) in your `PATH` to use the application.

#### Autocompletion

Clever Tools comes with a comprehensive auto-completion system. The brew package installs it automatically (for `bash` and `zsh`). Make sure `bash-completions` or `zsh-completions` are properly set up.

    # In ~/.bash_profile
    . /usr/local/etc/bash_completion

    # In ~/.zshrc
    fpath=(/usr/local/share/zsh-completions $fpath)

### Windows

Clever Tools is packaged using [chocolatey](https://chocolatey.org):

    choco install clever-tools

If you don't want to use `chocolatey`, a pre-compiled version is available: [clever-tools-0.9.0_windows.zip](https://clever-tools.cellar.services.clever-cloud.com/releases/0.9.0/clever-tools-0.9.0_windows.zip).
You need to add both files (`clever.exe` and `nodegit.node`) to your `PATH` to use the application.

### GNU/Linux

A pre-compiled version is available: [clever-tools-0.9.3_linux.tar.gz](https://clever-tools.cellar.services.clever-cloud.com/releases/0.9.3/clever-tools-0.9.3_linux.tar.gz).
You need to add both files (`clever` and `nodegit.node`) to your `PATH` to use the application.

#### Autocompletion

Clever Tools comes with a comprehensive auto-completion system.

    # for bash
    clever --bash-autocomplete-script $(which clever) | sudo tee /usr/share/bash-completion/completions/clever

    # for zsh
    clever --zsh-autocomplete-script $(which clever) | sudo tee /usr/share/zsh/site-functions

#### In case of `libcurl` version mismatch

On some distributions (eg. archlinux), a `libcurl` version mismatch between the system default and the expected version can happen. If you see `Error: /usr/lib/libcurl.so.4: version 'CURL_OPENSSL_3' not found (required by /usr/bin/nodegit.node)` in the logs, you can fix the issue by using a compatible libcurl version:

    # install libcurl-compat
    pacman -S libcurl-compat # on archlinux

    # add an alias to start clever tools with a compatible libcurl version
    alias clever='LD_PRELOAD=libcurl.so.3 clever'

### Manual installation (advanced)

Clever Tools is built with [npm](https://npmjs.org). If you wish to install it from `npm`, you can run `npm install -g clever-tools`. You can also install it [from source](https://github.com/CleverCloud/clever-tools).

## Linking your account

Once you have installed Clever Tools, the next step is to link your account:

    clever login

This will open a login page in your browser, and will give you identification
tokens. Copy them and paste them in the `clever login` prompt.

## Linking an existing application

If you have an already existing application, you can start managing it with
Clever Tools.

    # First, go to your local repository
    cd /path/to/your/application

    # Then, link it to the Clever Cloud application
    clever link <app_id>

    # You can also use the application name (make sure to specify the
    # organization name if your application is in an organization.
    clever link --org <org_name> <app_name>

    # Unlink an application
    clever unlink <app_id>

<div class="panel panel-warning">
  <div class="panel-heading">
     <h4>Notes on `.clever.json`</h4>
  </div>
  <div class="panel-body">
    <div>
      Once you have linked an application, clever-tools will create a Json configuration file named `.clever.json` at the root of the directory.
    </div>
    <div>This file can be commited safely, others team members working on this repository will not have to link the application again.</div>
    <div>This configuration file contains the AppID, so keep this in mind if you publish it on a public repository.</div>
  </div>
</div>
<br>
## Deploying new code

After having written new code, you can deploy it to Clever Cloud

    # Will git push your code to Clever Cloud and display logs
    clever deploy

    # Will open your application
    clever open
