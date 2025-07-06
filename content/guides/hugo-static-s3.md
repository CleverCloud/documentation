---
title: Hugo + Cellar
description: Build your website with Hugo and deploy it through Cellar, a S3-compatible object storage
tags:
- guides
keywords:

type: "docs"
comments: false
draft: false
---

When creating a static website, it's possible to host it using a runtime.
You can also use Cellar, a S3-compatible object storage. This hosting method saves time on configuration and application management, and is fast.

To do so, you need:

- a [Clever Cloud account](../../doc/quickstart/)
- [Hugo](https://gohugo.io/) on your machine
- to have [created your website](https://gohugo.io/getting-started/quick-start/) files with Hugo
- a Cellar add-on; if you have never created an add-on, you can follow [this guide](../../doc/quickstart/#create-your-first-add-on)

## Bucket creation and management

To create a bucket:

- Follow the [bucket creation instructions](../../doc/addons/cellar/#creating-a-bucket),
- or use third party software like [s3cmd](https://s3tools.org/s3cmd).

{{< callout type="warning" >}}
  Your bucket name must match the domain name you want to use. If your domain name is `my-static-website.com`, your bucket name must be : `my-static-website.com`.
{{< /callout >}}

To use a custom domain, for example `cdn.example.com`, you need to create a bucket named exactly like your domain:

```bash
s3cmd --host-bucket=cellar-c2.services.clever-cloud.com mb s3://cdn.example.com
```

Then, create a CNAME record on your domain pointing to `cellar-c2.services.clever-cloud.com.`.

## Public access policy

By default, your bucket is only visible and manageable an authenticated user.
To make your bucket publicly accessible, you have to apply a policy to the bucket

{{< callout type="warning" >}}
  This makes all of your bucket's objects publicly readable. Be careful that there aren't objects you don't want publicly exposed.
{{< /callout >}}

To set your bucket as public, you have to apply the following policy which you can save in a file named `policy.json`:

```json{filename="policy.json"}
{
  "Id": "Policy1587216857769",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1587216727444",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::<bucket-name>/*",
      "Principal": "*"
    }
  ]
}
```

Replace the `<bucket-name>` with your bucket name in the policy file. Don't change the `Version` field to the current date, keep it as is.

Now, you can set the policy to your bucket using s3cmd:

```bash
s3cmd setpolicy ./policy.json s3://<bucket-name>
```

If you encounter errors, you might need to specify the [configuration file path](#download-the-configuration-file):

```bash
s3cmd setpolicy ./policy.json -c path/to/s3cfg.txt s3://<bucket-name>
```

All of your objects should now be publicly accessible.
If needed, you can delete this policy by using:

```bash
s3cmd delpolicy s3://<bucket-name>
```

The original ACL should apply to all of your objects after that.

## Hugo configuration for Cellar

Hugo doesn’t know by default the path to your bucket in your Cellar. You have to add a few things to guide the deployment process.

In the folder of your website, you’ll find Hugo’s configuration file:

- `hugo.toml`
- `hugo.yaml`
- `hugo.json`

Open it, then add the following (according to the programing language):

{{< tabs items="JSON,YAML,TOML" >}}

  {{< tab >}}**JSON**

```json {filename="hugo.json"}
  {
    "deployment": {
      "targets": [
        {
          "name": "(a name for your own reference)",
          "URL": "s3://<BUCKET_NAME>?endpoint=https://<CELLAR_HOST>&region=fr-par"
        }
      ]
    }
  }
    ```


{{< /tab >}}

  {{< tab >}}**YAML**

  ```json {filename="hugo.yaml"}
  deployment:
  targets:
    - name: "(a name for your own reference)"
    - URL: "s3://<BUCKET_NAME>?endpoint=https://<CELLAR_HOST>&region=fr-par"
    ```

  {{< /tab >}}


  {{< tab >}}**TOML**
```json {filename="hugo.toml"}
[deployment]
[[deployment.targets]]
name: "(a name for your own reference)"
URL: "s3://<BUCKET_NAME>?endpoint=https://<CELLAR_HOST>&region=fr-par"
    ```

{{< /tab >}}

{{< /tabs >}}

- The deployment name is arbitrary and for your own reference: “production”, “test”, anything you’d like.
- The cellar host address can found on your Clever Cloud console: select your Cellar and you’ll have the “Host” field. The address looks like: `cellar-c2.services.clever-cloud.com`

Save your configuration file: Hugo now knows where to send file when deploying.



To deploy, proceed as usual: `hugo` to build the website locally, then `hugo deploy` to push files through Cellar.
If all the steps have been correctly completed, you are now able to access your website with:
 `https://<BUCKET_NAME>.<CELLAR_HOST>`


Is's possible to encounter an error where the website warns the user with a "not secure" message.
This happens when the SSL certificate was not properly generated.
You can manually generate one certificate by creating an application, then adding the domain name from the "domain" tab.
The certification propagation takes about 10-15mn.

If you still encounter an issue at this point, please contact our support team.




