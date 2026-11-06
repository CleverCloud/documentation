---
type: docs
linkTitle: File System Buckets
title: File System Buckets
description: Mount a persistent network file system in your Clever Cloud applications, shared by their instances and reachable over FTP and SFTP
keywords:
- file system buckets
- persistent storage
- NFS
- file storage
- filesystem
- buckets
- network storage
- file sharing
- sftp
aliases:
- /addons/fs_buckets
- /deploy/addon/fs-bucket
- /doc/addons/fs-bucket
- /doc/addons/fs_buckets
- /doc/administrate/fs-bucket
- /doc/databases-and-services/fs-buckets
- /doc/deploy/addon/fs-bucket
- /doc/fs-bucket
- /doc/storage/fs-bucket
- /doc/storage/fsbucket
---

Each deployment on Clever Cloud starts new instances and deletes the previous ones. The files your application writes on their local disk, such as user uploads, disappear with them. A File System Bucket (FS Bucket) is a network file system that keeps these files. You mount it in a folder of your application, and all its instances share the same content, from one deployment to the next.

FS Buckets suit applications that expect a file system, such as a content management system storing its media. For a new project, prefer [Cellar](/doc/deploy/storage/cellar/), the S3-compatible object storage of Clever Cloud.

## Create an FS Bucket

In the [Console](https://console.clever-cloud.com), create the add-on in the region of your application, then link it to the application. With [Clever Tools](/doc/tools/cli/), from a folder linked to your application, set its alias with `--link`:

```bash
clever addon create fs-bucket my-bucket --region par --link my-app
```

Linking the add-on to an application adds these environment variables to it:

- `BUCKET_HOST`: the host of the bucket, such as `bucket-<uuid>-fsbucket.services.clever-cloud.com`
- `BUCKET_FTP_USERNAME` and `BUCKET_FTP_PASSWORD`: the credentials to [access the files](#access-your-files) over FTP or SFTP

Linking doesn't mount the bucket: set `CC_FS_BUCKET` for that.

## Mount the bucket in your application

Set `CC_FS_BUCKET` to the folder to mount, followed by the host of the bucket: replace `bucket-<uuid>-fsbucket.services.clever-cloud.com` with the value of `BUCKET_HOST`. Then restart the application, so that its new instances mount the bucket:

```bash
clever env set CC_FS_BUCKET "/uploads:bucket-<uuid>-fsbucket.services.clever-cloud.com"
clever restart
```

The path is relative to the root of your application: `/uploads` stands for `/home/bas/<app_id>/uploads`. If this folder exists in your repository, it must be empty, otherwise the deployment fails. The mount happens before the build, so [build hooks](/doc/develop/common-configuration/build-hooks/) can read and write the files of the bucket.

To mount several buckets, add a number to the name of the variable. Each folder can only hold one bucket:

```bash
clever env set CC_FS_BUCKET "/uploads:bucket-<uuid>-fsbucket.services.clever-cloud.com"
clever env set CC_FS_BUCKET_1 "/exports:bucket-<other-uuid>-fsbucket.services.clever-cloud.com:async"
```

By default, each write waits for the bucket server to receive it. Add `:async` at the end of the value to mount a bucket in asynchronous mode. Writes can be faster, but a network issue can then lose or corrupt the files your application is writing.

## Access your files

Your application reads and writes the files in the mounted folder. For an absolute path, start from the `APP_HOME` [environment variable](/doc/develop/common-configuration/environment-variables/).

The **Dashboard** of the add-on in the [Console](https://console.clever-cloud.com) shows the files of the bucket. From your computer, connect with an FTP or SFTP client to the host in `BUCKET_HOST`, with `BUCKET_FTP_USERNAME` and `BUCKET_FTP_PASSWORD`:

- SFTP on port `22`
- FTP on port `21`, or FTP over TLS (FTPS) through `AUTH TLS` if your client supports it

The SFTP server presents one of these host keys:

| Algorithm | Key size | Fingerprint                                          |
| --------- | -------- | ---------------------------------------------------- |
| ED25519   | 256      | `SHA256:+ku6hhQb1O3OVzkZa2B+htPD+P+5K/X6QQYWXym/4Zo` |
| ED25519   | 256      | `SHA256:8tZzRvA3Fh9poG7g1bu8m0LQS819UBh7AYcEXJYiPqw` |
| ED25519   | 256      | `SHA256:HHGCP5cf0jQbQrIRXjiC9aYJGNQ+L9ijOmJUueLp+9A` |
| ED25519   | 256      | `SHA256:Hyt6ox+v2Lrvdfl29jwe1/dBq9zh2fmq2DO6rqurl7o` |
| ED25519   | 256      | `SHA256:drShQbl3Ox+sYYYP+urOCtuMiJFh7k1kECdvZ4hMuAE` |
| ED25519   | 256      | `SHA256:h1oUNRkYaIycchUsyAXPQHnu6MtTF2YUEYuisu+vnOE` |
| RSA       | 4096     | `SHA256:+550bmBCNAHscjOmKrdweueVUz2E6h1KzmSV+0c0U7w` |
| RSA       | 4096     | `SHA256:1O7d6cdmqj42Dw4nX90Y+6zIFTUI+aIwD0SLMQuj0ko` |
| RSA       | 4096     | `SHA256:AkHQnQXJ1lFEtliLHl8hlG7NiIZZgVn/uuRMCZJOKJk` |
| RSA       | 4096     | `SHA256:Atxhx7U0MOuZC7e4vs1tpyTJmNttB7d4+HNC5hiavFo` |
| RSA       | 4096     | `SHA256:Bla7GeL6hggg+rf6iDlKMrzIhxEBYB3VL7Q6PYGJYt4` |
| RSA       | 4096     | `SHA256:H5ZhQ/5JdMPSG49ojUNEhwSuRD663mnIJb/YDFFntyk` |
| RSA       | 4096     | `SHA256:TZr6eFrzoJmn4RS55Tb6yTd+WV9lTGtW0q+uLVbI7IE` |
| RSA       | 4096     | `SHA256:ZYFb1AsB+q++NRf7yW8E5rNOfxTRwjpJt6hqFP/NBNs` |
| RSA       | 4096     | `SHA256:d+nTyowvYtcxF28mCUu1ilqPJuLMExGyJ16Sv/pvoVY` |
| RSA       | 4096     | `SHA256:flpv4s3VxOrQFc/IG+BpR1s9dgDvR07A6zunNqO4Co0` |
| RSA       | 4096     | `SHA256:hvZN8rgSG82weLOeMTXdh1VwhjuRv+MJNnUt/X9R39g` |
| RSA       | 4096     | `SHA256:ls20B8C6Jdqx7RPQAjzVX7KmnrHizJum2sEvNhMcl60` |
| RSA       | 4096     | `SHA256:u1AzFc2AdFmlPRdNIZsn0sQJ/CKbfC2ZmXnQfabPek4` |
| RSA       | 4096     | `SHA256:wUPBX3X5gALgxXqD+IwG5qPRb0jbiOZ8/U1BOZeNhtk` |
| RSA       | 4096     | `SHA256:yRHC/tAlBpHLlRZ5rwbZ1z+159Bj3yg0VxHf+hXINLg` |
| RSA       | 4096     | `SHA256:yhn79aqxOGQZ+LXdN1/vIY+jwRIbBamlVT1+HdFoA6o` |

Each bucket has a single account, managed by Clever Cloud, without custom SSH keys. For several users or SSH keys, deploy [SFTPGo](/guides/sftpgo/) instead.

With [Terraform](/doc/tools/terraform/), the `clevercloud_fsbucket_upload` action pushes local files or the content of a URL to a bucket.

## Limits

FS Buckets favor compatibility over performance. They don't suit applications with intensive disk access, such as a cache. Other limits apply:

- Docker applications can't mount FS Buckets
- An application can only mount the buckets of its region
- FS Buckets aren't available in the Health Data Hosting (HDS) regions
- File locks only apply within an instance. Don't store a SQLite database, or other files that rely on locks, in a bucket several instances use
- Clever Cloud backs up FS Buckets every 24 hours, and keeps these backups for 72 hours

> [!NOTE] PHP applications include a default FS Bucket for sessions
> To deploy a PHP application in an HDS region, set [`CC_PHP_DISABLE_APP_BUCKET=true`](/doc/deploy/applications/php/sessions-emails/#speed-up-or-disable-the-session-fs-bucket). Store the sessions in Redis instead.

## Monitor your storage usage

Clever Cloud records the size of each bucket every hour in Warp 10, as the `fsbucket.storage` metric, in bytes. The read token of the **Metrics** tab of an application doesn't include this metric: generate a token with the FS Bucket scope.

- [Generate the token and query the FS Bucket storage metric](/doc/develop/observability/metrics#fs-bucket)
