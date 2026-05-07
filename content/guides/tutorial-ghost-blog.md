---
type: docs
title: Ghost Blog
description: This article shows you how to deploy a Ghost blog on Clever Cloud.
tags:
- deploy
keywords:
- node.js
- ghost
---

## Overview

[Ghost](https://ghost.org) is a modern, open-source publishing platform ideal for bloggers and content creators. This guide will walk you through the process of deploying a Ghost blog on Clever Cloud using Node.js.

### Prerequisites

- **Node.js 20**
- **MySQL**
- **Cellar S3**
- **Ghost-CLI**
- **Clever Tools CLI** ([documentation](https://www.clever-cloud.com/developers/doc/cli/))
- **Git**

## Installation and Configuration

### Initialize Your Project

Create a project folder and install Ghost locally:

```sh
# Create the project file
mkdir myblog && cd myblog
# Install Ghost-CLI
npm install -g ghost-cli@latest
nvm use 20 #to use node 20
# Install Ghost
ghost install local
ghost stop
```

Remove the default theme and add custom theme submodules:

```sh
rm -r content/themes/casper
cp -r current/content/themes/casper/ content/themes/
git init
cd content/themes/
git submodule add https://github.com/curiositry/mnml-ghost-theme
git submodule add https://github.com/zutrinken/attila/
wget https://github.com/TryGhost/Source/archive/refs/tags/<last-version>.zip -O source.zip #check and use the lastest version https://github.com/TryGhost/Source/releases
rm -R source
unzip source.zip -d temp
mkdir source
mv temp/*/* source/
rm -R temp source.zip
```

Add the S3 module:

```sh
npm install ghost-storage-adapter-s3
mkdir -p ./content/adapters/storage
cp -r ./node_modules/ghost-storage-adapter-s3 ./content/adapters/storage/s3
```

### Create and Configure Node Application and MySQL

Use the [Clever Tools CLI](/developers/doc/cli/install):

Create the Node.js app and a MySQL add-on on Clever Cloud:

```sh
# Create the Node.js app
clever create --type node myblog

# Create MySQL add-on
clever addon create mysql-addon --plan s_sml myblogsql
clever service link-addon myblogsql
```

The Ghost configuration file can't use direct environment variables. Set the following environment variables to connect your app to the database:

```sh
clever env set database__connection__host <ADDON_HOST>
clever env set database__connection__user <ADDON_USER>
clever env set database__connection__password <ADDON_PASSWORD>
clever env set database__connection__database <ADDON_DATABASE>
clever env set database__connection__port <ADDON_PORT>
clever env set url https://<domain_URL_blog>
```

### Install and Configure Cellar S3 

Create the Cellar S3 add-on on Clever Cloud:

```sh
# Create and link Cellar add-on
clever addon create cellar-addon --plan s_sml <cellar-app>
clever service link-addon <cellar-app>
```

In your Cellar S3 add-on console, create a bucket for your blog.

Add the environment variables to configure Ghost with Cellar:

```sh
clever env set storage__s3__accessKeyId <CELLAR_ACCESS_KEY>
clever env set storage__s3__secretAccessKey <CELLAR_SECRET_KEY>
clever ens set storage__s3__assetHost <CELLAR_ADDON_HOST>
clever env set storage__s3__bucket <your-bucket>
clever env set storage__s3__region fr
```

Make sure to configure public read access in your Cellar bucket:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::<bucket>"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:PutObjectVersionAcl",
                "s3:DeleteObject",
                "s3:PutObjectAcl"
            ],
            "Resource": "arn:aws:s3:::<bucket>/*"
        },
        {
            "Sid": "PublicReadAccess",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<bucket>/*",
            "Principal": "*"
        }
    ]
}
```

### Create a Pre-Run Hook

In the root folder of your project, create the file `.clevercloud-pre-run-hook.sh`:

```sh
#!/bin/sh
npm install -g ghost-cli 
mkdir ghost 
cd ghost
ghost install local 
ghost stop
cp ../config.production.json .
npm install ghost-storage-adapter-s3
mkdir -p ./content/adapters/storage
cp -r ../content/adapters/storage/s3 content/adapters/storage/s3
rm -R content/themes/source
cp -r ../content/themes/source content/themes/
```

Grant execution permissions to the script:

```sh
sudo chmod +x clevercloud.sh
```

### Configure Ghost

Create the file `config.production.json` in the root folder of your project:

```json
{
  "url": "https://<your-url-app>/",
  "server": {
    "port": 8080,
    "host": "0.0.0.0"
  },
  "database": {
    "client": "mysql"
  },
  "storage": {
    "active": "s3"
  },
  "mail": {
    "transport": "SMTP"
  },
  "process": "local",
  "logging": {
    "level": "debug",
    "transports": ["stdout"]
  },
  "paths": {
    "contentPath": "../../../content/"
  }
}
```

### Create `package.json` and `.gitignore`

Create the file `package.json`:

```json
{
    "name": "ghost",
    "version": "0.1.0",
    "description": "",
    "scripts": {
        "start": "ghost run --dir ghost"
    },
    "devDependencies": {},
    "dependencies": {}
}
```

Create the file `.gitignore`:

```
.ghost-cli
config.development.json
current
versions
node_modules
```

### Set Other Environment Variables for Your Application

Before deploying your application on Clever Cloud, make sure to set the following environment variables:

```sh
clever env set CC_NODE_BUILD_TOOL yarn2
clever env set CC_NODE_VERSION 20
clever env set CC_PRE_RUN_HOOK "./.clevercloud-pre-run-build.sh"
clever env set NODE_ENV production
```

#### Optional: Configure Email Service

Ghost allows you to configure an SMTP service for sending emails (such as invitations, password resets, etc.). You can set it up using the following environment variables:

```sh
clever env set mail__from "your-email@example.com"
clever env set mail__options__service "your-mail-service" # e.g. Mailgun, Gmail, etc.
clever env set mail__options__host "smtp.yourmail.com"
clever env set mail__options__port "587"
clever env set mail__options__secureConnection "false"
clever env set mail__options__auth__user "your-smtp-username"
clever env set mail__options__auth__pass "your-smtp-password"
```

> 💡 > [!NOTE] Setup email service
> These environment variables allow Ghost to connect to your email service automatically, see the [official Ghost SMTP configuration docs](https://ghost.org/docs/config/#mail) for more information.

## Deploy on Clever Cloud

Initialize git, add files, and push:

```sh
git add clevercloud.sh package.json config.production.json content
git commit -m "Initial commit"
git remote add clever <CLEVER_GIT_URL>
git push clever <branch>:master
```

## More Information

For a small blog, you can use the XS or S Node.js plan.

