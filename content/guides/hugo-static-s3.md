---
type: docs
linkTitle: Hugo + Cellar
title: Use Hugo with Cellar object storage
description: Deploy a Hugo website with the Static runtime and use Cellar to publish generated assets or build artifacts
keywords:
- cellar
- hugo
- object storage
- static website
---

[Hugo](https://gohugo.io/) generates static files that can be deployed with Clever Cloud's [Static runtime](/guides/hugo/). [Cellar](/doc/addons/cellar/) is S3-compatible object storage and is useful for publishing individual assets or keeping generated build artifacts.

> [!IMPORTANT]
> Cellar does not implement S3 website-hosting behavior. A request to a bucket root returns an object listing instead of `index.html`, directory URLs do not resolve their index document and S3 website configuration requests are not supported. Use the Static runtime when visitors need to navigate a Hugo website.

## Deploy the website

Follow the [Hugo deployment guide](/guides/hugo/) to create a Static application. The runtime builds the site, serves index documents and clean URLs, provides TLS and lets you add a custom domain.

## Publish generated files to Cellar

To expose individual generated objects through Cellar, create a [Cellar add-on and bucket](/doc/addons/cellar/#creating-a-bucket), install [s3cmd](https://s3tools.org/s3cmd) or another S3-compatible client, then download the add-on's configuration file from the Console.

Build the site and synchronize its generated files:

```bash
hugo
s3cmd -c path/to/s3cfg.txt sync --delete-removed public/ s3://BUCKET_NAME/
```

Objects are private by default. Follow the [public bucket policy instructions](/doc/addons/cellar/#public-bucket-policy) only for a bucket whose entire published content can be read publicly.

A public object is available at its complete key, for example:

```text
https://BUCKET_NAME.CELLAR_HOST/images/logo.svg
```

Uploading `public/index.html` does not make the bucket root serve that file. Likewise, `public/posts/example/index.html` remains available only through its complete object key and not through `/posts/example/`. These limits make Cellar suitable for assets and archives, not as the origin for a normal Hugo website.

## Learn more

- [Deploy Hugo](/guides/hugo/) — Build and serve a Hugo website with the Static runtime
- [Cellar object storage](/doc/addons/cellar/) — Create buckets, configure clients and manage object access
- [Hugo deployment](https://gohugo.io/host-and-deploy/deploy-with-hugo-deploy/) — Review Hugo's native deployment targets
