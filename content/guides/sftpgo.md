---
type: docs
linkTitle: SFTPGo
title: SFTPGo
description: Deploy SFTPGo on Clever Cloud with Docker to set up a custom SFTP server with user management and Cellar S3 storage backend
keywords:
- sftpgo
- sftp
- ftp
- file transfer
- docker
- cellar
- s3 storage
- file management
- webdav
aliases:
- /sftpgo
---

{{< hextra/hero-subtitle >}}
  SFTPGo is a modern, open-source SFTP server with multi-user management, a web interface and S3-compatible storage backends like Cellar.
{{< /hextra/hero-subtitle >}}

## Overview

Clever Cloud provides built-in SFTP access to [FS Buckets](/doc/addons/fs-buckets/), but if you need advanced user management, fine-grained access control, or want to expose files stored in [Cellar](/doc/addons/cellar/) over SFTP, you can deploy SFTPGo as a Docker application.

> [!WARNING] Only the SFTP protocol works out of the box on Clever Cloud
> FTP (non-encrypted) requires a dedicated TCP port range. Contact [Clever Cloud support](https://console.clever-cloud.com/ticket/center) to enable it.

## Requirements

You need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and a [Clever Cloud account](https://console.clever-cloud.com).

## Create and configure resources on Clever Cloud

1. Create a **Docker** application (XS size or above) from the [Console](https://console.clever-cloud.com)
2. Create a **PostgreSQL** add-on (version 15, XXS Small Space) and link it to your application
3. Create a **Cellar** add-on for S3-compatible object storage and link it to your application
4. Enable **TCP redirection** on your Docker application from the Console

## Prepare the project

Initialize a Git repository with a minimal **Dockerfile**:

```bash
mkdir my-sftpgo && cd my-sftpgo
git init
```

Create a **Dockerfile** at the root of the project

```bash
FROM drakkan/sftpgo:latest
```

## Set environment variables

Add the following environment variables to your Docker application in the console. Replace placeholder values with the credentials provided by Clever Cloud for your PostgreSQL add-on:

```bash
CC_DOCKER_EXPOSED_TCP_PORT="2022"
SFTPGO_DATA_PROVIDER__DRIVER="postgresql"
SFTPGO_DATA_PROVIDER__HOST="<pg_host>"
SFTPGO_DATA_PROVIDER__NAME="<pg_dbname>"
SFTPGO_DATA_PROVIDER__PASSWORD="<pg_password>"
SFTPGO_DATA_PROVIDER__PORT="<pg_port>"
SFTPGO_DATA_PROVIDER__USERNAME="<pg_user>"
```

## Deploy

First, commit and push your code:

```bash
git add .
git commit -m "Deploy SFTPGo"
clever link <your-app-id>
clever deploy
```

Or using a Git remote:

```bash
git remote add clever <your-clever-git-url>
git push clever master

```

## Initialize SFTPGo

1. Open your application URL in a browser
2. Follow the setup wizard to create an **admin account**

## Connect Cellar as a storage backend

In the SFTPGo web admin interface, create a new user with an **S3-compatible** filesystem:

| Setting | Value |
|---------|-------|
| Bucket | Your Cellar bucket name |
| Region | FR |
| Access Key | Your Cellar Key ID |
| Access Secret | Your Cellar Key Secret |
| Endpoint | https://cellar-c2.services.clever-cloud.com |


## Connect with an SFTP client

Use any SFTP client (such as FileZilla, Cyberduck, or the sftp CLI) with:

- Host: shown in the TCP redirection tab of your application in the console
- Port: shown in the TCP redirection tab
- Username & Password: your SFTPGo admin credentials

## 🎓 Learn more

{{< cards >}}
  {{< card link="/developers/doc/applications/docker" title="Deploy a Docker application" subtitle="How to configure your Docker app" icon="docker" >}}
  {{< card link="/developers/doc/addons/cellar" title="Cellar Object Storage" subtitle="S3-compatible storage on Clever Cloud" icon="database" >}}
  {{< card link="/developers/doc/addons/fs-bucket" title="FS Buckets" subtitle="Built-in persistent file storage with SFTP access" icon="database" >}}
  {{< card link="https://docs.sftpgo.com/" title="SFTPGo Documentation" subtitle="Official SFTPGo documentation" icon="book-open" >}}
{{< /cards >}}
