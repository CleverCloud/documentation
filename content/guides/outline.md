---
type: docs
linkTitle: Outline
title: Outline Knowledge Base on Clever Cloud
description: Deploy Outline team knowledge base and wiki on Clever Cloud with detailed tutorials and best practices
keywords:
- outline
- knowledge base
- wiki
- collaborative
- Node.js
- postgresql
aliases:
- /outline
---

[Outline](https://getoutline.com) is an open source team knowledge base and wiki that helps teams organize, share, and collaborate on documentation. It offers a clean, fast interface with powerful features for creating and maintaining company knowledge. This guide explains how to configure Outline from source, using the Clever Cloud Console. For an alternative using [Clever Tools](/doc/cli) there is a complete example in [this repository](https://github.com/CleverCloud/outline-example).

## How to Configure and Deploy Outline on Clever Cloud

{{% steps %}}

### Initialize repository and download Outline

Create a new `outline` folder for Outline and, inside it, initialize a Git repository with `git init`.

Download the latest release of Outline from [https://github.com/outline/outline/releases](GitHub) and expand it in `outline` folder.

### Create a Node application

On Clever Cloud Console, click **Create** > **An application** and choose a [Node.js](/developers/doc/applications/nodejs) application with Git deployment.

Select at least an `S` plan. Smaller instances can make the build to fail.

### Create a PostgreSQL add-on

On Clever Cloud Console, click **Create** > **An add-on** and choose a [PostgreSQL](/developers/doc/addons/postgresql/) add-on.

Select at least an `XSS` plan.

Link the add-on to the application previously created.

### Create a Redis add-on

On Clever Cloud Console, click **Create** > **An add-on** and choose a [Redis](/developers/doc/addons/redis/) add-on.

Link the add-on to the application previously created.

### Create a Cellar S3 Object Storage add-on

On Clever Cloud Console, click **Create** > **An add-on** and choose a [Cellar S3 Object Storage](/developers/doc/addons/cellar/) add-on.

Link the add-on to the application previously created.

### Set Up Domain

Outline needs an URL declared in variables to work properly. You can set it up in **Domains names**, from your application menu. If you don't have a domain name yet, you can use a `cleverapp.io` subdomain provided by Clever Cloud for test purposes.

### Generate a <secret_key> and an <utils_secret>

Using for example [OpenSSL](https://openssl-library.org/).

In a Linux/Mac shell:

```bash
SECRET_KEY=$( openssl rand -hex 32 )
UTILS_SECRET=$( openssl rand -hex 32 )
echo "<secret_key>: $SECRET_KEY \n<utils_secret>: $UTILS_SECRET"
```

### Choose a S3 bucket name

As explained in the [Cellar S3 doc](https://www.clever.cloud/developers/doc/addons/cellar/), Buckets' names are global for every region. You can’t give the same name to two different buckets in the same region, because the URL already exists in the Cellar cluster on this region.

Unless you have a better option, use the Outline domain as bucket name.

### Configure environment variables

In the Clever Cloud Console, go to the Outline Node.js application you've created and, in the **Environment variables** section, inject the following environment variables into the application:

```env
URL="<outline_domain>"
NODE_ENV="production"
PORT="8080"
CC_NODE_DEV_DEPENDENCIES="install"
CC_POST_BUILD_HOOK="NODE_ENV=production && yarn build"
WEB_CONCURRENCY="2"
DEFAULT_LANGUAGE="en_US"
SECRET_KEY="<secret_key>
UTILS_SECRET="<utils_secret>"
```

Now inject the add-ons credentials:

```env
DATABASE_URL "<POSTGRESQL_ADDON_URI value>"
REDIS_URL "<REDIS_URL value>"
FILE_STORAGE="s3"
AWS_S3_UPLOAD_BUCKET_URL="https://<CELLAR_ADDON_HOST value>"
AWS_S3_UPLOAD_BUCKET_NAME=<bucket_name>
AWS_ACCESS_KEY_ID="<CELLAR_ADDON_KEY_ID value>"
AWS_SECRET_ACCESS_KEY="<CELLAR_ADDON_KEY_SECRET value>"
AWS_S3_FORCE_PATH_STYLE="true"
AWS_S3_ACL="private"
AWS_REGION="us"
```

### Setting the S3 policies

For Outline to use Cellar S3 as storage for its content files, you need to configure specific S3 bucket policies. These policies ensure that Outline can properly read, write, and manage files in your Cellar bucket.

Unless you have a better option, use [s3cmd](https://s3tools.org/s3cmd) to apply these policies to your bucket. Here are the required policies:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadForGetBucketObjects",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::$BUCKET/*"]
    }
  ]
}
```

First, configure s3cmd with your Cellar credentials:

```bash
s3cmd --configure
```

When prompted, use the following values:
- Access Key: Your `CELLAR_ADDON_KEY_ID`
- Secret Key: Your `CELLAR_ADDON_KEY_SECRET`
- Default Region: `us-east-1`
- S3 Endpoint: Your `CELLAR_ADDON_HOST`
- DNS-style bucket: Yes

Then apply the policy using s3cmd:

```bash
s3cmd setpolicy policy.json s3://<bucket_name>
```

You also need to configure CORS (Cross-Origin Resource Sharing) for your bucket. Create a `cors.xml` file with the following configuration:

```xml
<CORSConfiguration>
  <CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>DELETE</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
    <ExposeHeader>ETag</ExposeHeader>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
  </CORSRule>
</CORSConfiguration>
```

Apply the CORS configuration using s3cmd:

```bash
s3cmd setcors cors.xml s3://<bucket_name>
```

### Configure Authentication

<!-- vale off -->
At least **one of either** Google, Slack, Discord, or Microsoft is required for a working installation or you'll have no sign-in options.
<!-- vale on -->

Choose one or more of the following authentication providers and add the corresponding environment variables to your Clever Cloud application:

#### Google OAuth

```env
GOOGLE_CLIENT_ID="<your_google_client_id>"
GOOGLE_CLIENT_SECRET="<your_google_client_secret>"
```

#### Slack OAuth

```env
SLACK_CLIENT_ID="<your_slack_client_id>"
SLACK_CLIENT_SECRET="<your_slack_client_secret>"
```

#### Discord OAuth

```env
DISCORD_CLIENT_ID="<your_discord_client_id>"
DISCORD_CLIENT_SECRET="<your_discord_client_secret>"
```

#### Microsoft OAuth

```env
AZURE_CLIENT_ID="<your_azure_client_id>"
AZURE_CLIENT_SECRET="<your_azure_client_secret>"
```

### Deploy

Get the remote in your application menu > **Information** > **Deployment URL** and add it to Git with `git remote add clever <clever-remote-url>`. Then, push your code with `git push clever -u master`

💡 If you get a reference error when pushing, try this: `git push clever main:master`.

{{% /steps %}}


## 🎓 Further Help

{{< cards >}}
  {{< card link="/developers/doc/applications/nodejs" title="Node.js" subtitle="Deploy a Node.js application on Clever Cloud" icon="node" >}}
  {{< card link="/developers/doc/addons/cellar" title="Cellar S3 Object Storage" subtitle="Object Storage for your apps" icon="fsbucket" >}}
  {{< card link="/developers/doc/addons/postgresql" title="PostgreSQL" icon="mysql" subtitle="Your self-hosted managed relational database" >}}
  {{< card link="https://docs.getoutline.com/s/hosting/doc/from-source-BlBxrNzMIP" title="Installing Outline from source" subtitle="Check Outline installation guide" icon="outline" >}}
{{< /cards >}}
