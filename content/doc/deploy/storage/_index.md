---
type: docs
linkTitle: Storage
title: Storage
description: Keep the files of your applications across deployments on Clever Cloud, with Cellar object storage or an FS Bucket file system, and choose between them
keywords:
- storage
- object storage
- s3
- file system
- buckets
aliases:
- /addons/cellar-vs-fsbuckets
- /doc/best-practices/cloud-storage
- /doc/develop/best-practices/cloud-storage
- /doc/develop/cloud-storage
- /doc/storage
---

Each deployment starts new instances: the files an application writes on its local disk disappear with the previous ones. To keep them across deployments, and share them between instances, store them in one of these add-ons.

{{< cards cols="2" >}}
  {{< card link="/developers/doc/deploy/storage/cellar" title="Cellar" subtitle="S3-compatible object storage" icon="cellar" >}}
  {{< card link="/developers/doc/deploy/storage/fs-bucket" title="FS Bucket" subtitle="Persistent file system for applications" icon="fsbucket" >}}
{{< /cards >}}

## Choose between Cellar and FS Bucket

For a new project, use Cellar. Your application reads and writes objects over HTTPS, with any S3 client or SDK, and doesn't depend on the instance it runs on. It can also hand out [temporary signed URLs](/doc/deploy/storage/cellar/#uploading-objects-with-presigned-urls-and-checksum-validation), so that browsers upload or download files directly, without going through your application. Cellar also [hosts static websites](/doc/deploy/storage/cellar/#static-hosting), and keeps former versions of your files when you enable [versioning](/doc/deploy/storage/cellar/#versioning).

Use an FS Bucket for software that writes to its disk and that you can't change, such as a content management system storing its media. Your application sees a folder, mounted over the network and shared by all its instances, so its code doesn't change. This compatibility comes with [limits](/doc/deploy/storage/fs-bucket/#limits): Docker applications can't mount an FS Bucket, an application only mounts the buckets of its region, and file locks only apply within an instance. Don't store a SQLite database in a bucket that several instances use.

## Create a storage add-on

In the [Console](https://console.clever-cloud.com/), select **Create** at the top of the sidebar, then **Add-on**, and pick Cellar or FS Bucket. Choose its region, its name, and the applications to link it to. With [Clever Tools](/doc/tools/cli/addons/), from a folder linked to your application, create one of them and link it with the alias of the application:

```bash
clever addon create cellar-addon my-storage --link my-app
clever addon create fs-bucket my-bucket --region par --link my-app
```

Linking Cellar gives the application its credentials in `CELLAR_ADDON_HOST`, `CELLAR_ADDON_KEY_ID`, and `CELLAR_ADDON_KEY_SECRET`: then [create a bucket](/doc/deploy/storage/cellar/#creating-a-bucket) for your files. Linking an FS Bucket gives its host and FTP credentials, but doesn't mount it: [mount it](/doc/deploy/storage/fs-bucket/#mount-the-bucket-in-your-application) with `CC_FS_BUCKET`.

## Delete a storage add-on

Select **Delete the add-on** in the danger zone of the **Dashboard** of the add-on, or **Remove add-on** in its **Information** menu. With Clever Tools:

```bash
clever addon delete my-storage
```
