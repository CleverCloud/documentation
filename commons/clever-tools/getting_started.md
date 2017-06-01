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

Clever Tools is packaged and distributed through [npm](https://npmjs.com).
You need nodeJS, npm and openssl headers (openssl-dev on ubuntu / debian)
installed on your system.

To install Clever Tools for your user only, run

    npm install -g clever-tools

To install Clever Tools system-wide, run

    sudo npm install -g clever-tools

### Installing auto-completion

Clever Tools comes with a powerful auto-completion support. Make sure to
enable it for a better experience.

    sudo install-clever-completion

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
