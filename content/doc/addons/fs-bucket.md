---
type: docs
linkTitle: File System Buckets
title: File System Buckets
description: Configure FS Bucket add-on service for persistent file storage and data management across your Clever Cloud applications
keywords:
- file system buckets
- persistent storage
- NFS
- file storage
- data management
- filesystem
- buckets
- network storage
- file sharing
aliases:
- /addons/fs_buckets
- /deploy/addon/fs-bucket
- /doc/addons/fs_buckets
- /doc/databases-and-services/fs-buckets
- /doc/deploy/addon/fs-bucket
- /doc/fs-bucket
---

When you deploy an application on Clever Cloud, like most PaaS, a new virtual machine is created, the previous one is deleted. If your application generates data, for example if you let users upload pictures and you don't store it on databases or object storage, you will lose anything on the local disk after a rebuild or a restart.

Immutable infrastructure doesn't allow you to keep generated data files between deployments. To avoid this, you need **a persistent file system**. This is why we created File System Buckets, a network-based storage solution to retrieve data from a deployment to another.

## Known Limitations

FS Buckets are provided for application needing file-system backward compatibility, but there are not optimized for high-performance applications, especially those relying on caching. There are also some availability and features limitations:

- FS Buckets are not available for Docker applications
- FS Buckets can't be mounted across different regions
- FS Buckets are note available in Health Data Hosting (HDS) Zone
- Clever Cloud provides automated backups every 24 hours, with only 72 hours of retention for FS Buckets (7 days for databases)

> [!NOTE] PHP applications includes a default FS Bucket for session storage
> To deploy a PHP application on an HDS region, set [`CC_PHP_DISABLE_APP_BUCKET=true`](/doc/applications/php/#speed-up-or-disable-the-session-fs-bucket). Consider using Redis to manage PHP sessions.

## Configuring your application

Buckets are configured using environment variables. Add the following to your application :

```text
CC_FS_BUCKET=/some/empty/folder:bucket-xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx-fsbucket.services.clever-cloud.com[:async]
```

Don't forget to replace the path of the mounted folder and the fs-bucket host with the targeted folder path (make sure the folder does not exists in your application) and your fs-bucket host.

The mounted root directory is relative to the application directory. So `/my-directory` will be mounted in `/home/bas/<app_id>/my-directory/`.

Optionnally, you can add `:async` to the end of the environment variable.
This will make Clever Cloud mount the FS Bucket with the `async` option.
It will make the FS Bucket faster (sometimes up to 3 times faster), but in case of a network issue it may cause file
corruption.

You can setup multiple buckets by appending a number at the end of the environment variable's name.

```text
CC_FS_BUCKET=/some/empty/folder:fs_bucket_host
CC_FS_BUCKET_1=/some/otherempty/folder:fs_bucket_other_host:async
```

Note that the `async` parameter can be set per bucket.

## Configuring your application with buckets.json (@deprecated)

{{< callout emoji="🧹" >}}
**This method is deprecated**
This method is deprecated, we strongly recommend that you use environment variables.
If you want to switch from this method to the environment variables, you need to remove the `buckets.json` file. Otherwise, the environment variables will be ignored.
Also, this method does not support the `async` parameter.
{{< /callout >}}

To configure your application to use buckets, use the
`clevercloud/buckets.json` file.
The `clevercloud` folder must be located at the root of your application.
The `buckets.json` file must contain the following structure:

```javascript
[
  {
    "bucket" : "bucketId",
    "folder" : "/myFolder",
    "apps"   : ["app_id"]

  },
  {
    "bucket_host" : "bucket-01234567-0123-0123-0123-012345678987-fsbucket.services.clever-cloud.com",
    "folder" : "/myotherFolder",
    "apps"   : ["app_id_2"]
  }
]
```

{{< callout type="info" >}}
You can find a pre-filled json object to copy in the dashboard of your FSBucket add-on, in the "Dashboard configuration" tab
{{< /callout >}}

It's a json array containing objects with at least two fields:

Usage    | Field        | Description
---------|--------------|--------------------------------------------------------------
Required | bucket       | The bucket id you can find in the console. It begins with `bucket_`. This is for "old-style" buckets (created before the 7 December 2015)
Required | bucket_host  | The bucket host you can find in the console. It begins with `bucket-` and ends with `services.clever-cloud.com`. This is for "new-style" buckets.
Required | folder       | The folder you want the bucket to be mounted in. Should start with `/`. Using the example *myFolder*, you can access your bucket via the *myFolder* folder at the root of your application (which absolute path is available in the `APP_HOME` environment variable)
Optional | apps         | Whitelist of the applications allowed to mount this bucket. It's helpful if you need to deploy a *preprod* app and a *prod* app using the exact same codebase but different buckets

The folder must not exist in your repository (or it needs to be empty). Otherwise, the mount of your bucket will be ignored.
You can mount the same bucket in different folders, but they will share the same content, so it's not the solution. You should prefer to mount the bucket in only one folder and then manage multiple subfolders in it.

{{< callout type="warning" >}}
You cannot mount two buckets in the same folder for the same app. If you put the same "folder" value for two entries in your environment variables or the *buckets.json* array, **make sure** that the "apps" fields make the two buckets mutually exclusive upon deployment!
{{< /callout >}}

## Accessing your data inside the FS Bucket

### From your application

Your bucket is mounted at the configured path, starting from your application's
root folder.

If you want to use an absolute path, you can use the `APP_HOME` environment
variable, see [special environment variables](/doc/develop/env-variables#special-environment-variables)

### From the add-on dashboard

The **File explorer** tab of the **add-on dashboard** gives you access to your files
in the FS bucket.

### From your favorite SFTP client

The **Add-on information** tab of your FS Bucket in [Clever Cloud Console](https://console.clever-cloud.com) displays information you need to connect using SSH File Transfer Protocol (SFTP). You can use the following SSH public keys to ensure the connection is authentic and trusted:

| Algorithm | Key size | Fingerprint                                        |
|-----------|----------|----------------------------------------------------|
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

### From your favorite FTP client

The **Add-on information** tab of your FS Bucket add-on displays the information
you need to connect to your bucket using FTP.
