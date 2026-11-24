---
type: docs
title: Cellar, S3-compatible object storage
linkTitle: Cellar Object Storage
description: Store the files of your applications in Cellar, the S3-compatible object storage of Clever Cloud, and control their access, versions, retention, and encryption
keywords:
- S3
- amazon
- Storage
- file
- files
- s3cmd
- aws
- encryption
- SSE-C
- object lock
- presigned URL
aliases:
- /addons/cellar
- /deploy/addon/cellar
- /doc/addons/cellar
- /doc/cellar
- /doc/cellar/faq
- /doc/deploy/addon/cellar
- /doc/addon/cellar/
- /doc/deploy/addons/cellar/
- /doc/deploy/databases/cellar/
- /doc/storage/cellar
---

Cellar is the object storage of Clever Cloud. It keeps the files of your applications, such as user uploads, exports, or backups, out of their instances, so they survive each deployment. Cellar speaks the S3 protocol of Amazon Web Services (AWS). Use it with the S3 SDK of your language, or with S3 clients such as s3cmd, the AWS CLI, the RustFS CLI, or rclone.

A Cellar add-on is serverless: you don't choose a size, and you pay for the data you store and the outbound traffic. It holds buckets, which hold your files as objects. Create it in the `par` region, or in `parhds` to store [health data](/doc/manage/regions/#health-data-hosting).

Cellar serves objects over HTTPS, but doesn't host websites: to serve a static website, deploy it with the [Static](/doc/deploy/applications/static/) runtime. For an application that expects a file system, mount an [FS Bucket](/doc/deploy/storage/fs-bucket/) instead.

## Create a Cellar add-on

In the [Console](https://console.clever-cloud.com), select **Create** in the sidebar, then **Add-on**, and pick Cellar. Choose its region, its name, and the applications to link it to. With [Clever Tools](/doc/tools/cli/), from a folder linked to your application, set its alias with `--link`:

```bash
clever addon create cellar-addon my-storage --region par --link my-app
```

Linking the add-on to an application adds these environment variables to it:

- `CELLAR_ADDON_HOST`: the host of Cellar, such as `cellar-c2.services.clever-cloud.com`, without `https://`
- `CELLAR_ADDON_KEY_ID` and `CELLAR_ADDON_KEY_SECRET`: the access key of the add-on, which grants full access to all its buckets

The **Add-on dashboard** of the Console shows these credentials, and offers a pre-filled `s3cfg` configuration file for s3cmd. Its **Information** panel shows the number of buckets and objects, the storage used, and the traffic of the last 30 days.

### Renew the secret

If your secret leaks, select **Renew secret** in the **Add-on dashboard**. The key ID stays the same, but the old secret and its presigned URLs stop working at once. Clever Cloud updates `CELLAR_ADDON_KEY_SECRET` in the linked applications: restart them, then update your other clients.

## Create a bucket

A new Cellar add-on has no bucket. Bucket names are unique among all the add-ons of a region: if another add-on uses a name, you can't create a bucket with it. Names hold 3 to 63 characters: lowercase letters, numbers, hyphens, and dots, without underscores.

In the Console, open the [Cellar Explorer](#manage-your-files-in-the-console) tab of the add-on, and select **Create bucket**. With an S3 client, once you [configure it](#configure-an-s3-client):

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  ```bash
  s3cmd mb s3://my-bucket
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  ```bash
  aws s3 mb s3://my-bucket
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  ```bash
  rc bucket create cellar/my-bucket
  ```

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  ```bash
  rclone mkdir cellar:my-bucket
  ```

  {{< /tab >}}

{{< /tabs >}}

Objects are private: only the add-on credentials can read them. To serve some of them publicly, see [Control access](#control-access).

## Manage your files in the Console

The **Cellar Explorer** tab of the add-on, in the [Console](https://console.clever-cloud.com), lists its buckets with their number of objects, size, and last update. Open a bucket to browse and filter its objects, and see the content type, size, and date of each one. From this tab, you can:

- Create a bucket, without versioning
- Create a directory, which Cellar keeps once you upload an object to it
- Delete a bucket once it's empty
- Upload, download, or delete objects

The details of a bucket show whether its versioning is on. To change it, or to set policies, CORS, or Object Lock, use an [S3 client](#configure-an-s3-client).

> [!NOTE] The Cellar Explorer is in beta
> Its features and interface can still change.

- [Share your feedback on the Cellar Explorer](https://github.com/CleverCloud/Community/discussions/155)

## Configure an S3 client

Cellar works with S3 clients that let you set a custom endpoint: use `https://` and the value of `CELLAR_ADDON_HOST`, such as `https://cellar-c2.services.clever-cloud.com`. The s3cmd commands for S3 websites and CloudFront, `ws-*` and `cf*`, don't work with Cellar.

S3 clients also ask for a region, which Cellar ignores: your data stays in the region of the add-on, such as Paris for `par`. Set `us-east-1`: the AWS CLI and the Node.js SDK send any other value as the location of the buckets they create, which Cellar refuses.

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  Install [s3cmd](https://s3tools.org/s3cmd). In the **Add-on dashboard** of the Console, select **Download a pre-filled s3cfg file**, and save it as `~/.s3cfg`. To use another location, add `-c path/to/s3cfg` to each command. List your buckets to check the configuration:

  ```bash
  s3cmd ls
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  Install the [AWS CLI](https://aws.amazon.com/cli/), then add a `cellar` profile to `~/.aws/config`. Replace the endpoint with the value of `CELLAR_ADDON_HOST`. Recent versions of the AWS CLI add checksums that Cellar rejects: the last two lines turn them off.

  ```ini {filename="~/.aws/config"}
  [profile cellar]
  region = us-east-1
  endpoint_url = https://cellar-c2.services.clever-cloud.com
  request_checksum_calculation = when_required
  response_checksum_validation = when_required
  ```

  Store the credentials of the add-on in this profile, then select it for the session:

  ```bash
  aws configure set aws_access_key_id "$CELLAR_ADDON_KEY_ID" --profile cellar
  aws configure set aws_secret_access_key "$CELLAR_ADDON_KEY_SECRET" --profile cellar
  export AWS_PROFILE=cellar
  aws s3 ls
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  Install `rc`, the [RustFS CLI](https://github.com/rustfs/cli), with `brew install rustfs/tap/rc` or `cargo install rustfs-cli`, then create a `cellar` alias:

  ```bash
  rc alias set cellar "https://$CELLAR_ADDON_HOST" "$CELLAR_ADDON_KEY_ID" "$CELLAR_ADDON_KEY_SECRET"
  rc bucket list cellar
  ```

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  Install [rclone](https://rclone.org), which lists Cellar among its S3 providers. Then create a `cellar` remote with the credentials of the add-on:

  ```bash
  rclone config create cellar s3 \
    provider=Cellar \
    access_key_id="$CELLAR_ADDON_KEY_ID" \
    secret_access_key="$CELLAR_ADDON_KEY_SECRET" \
    endpoint="https://$CELLAR_ADDON_HOST"
  rclone lsd cellar:
  ```

  {{< /tab >}}

{{< /tabs >}}

### Desktop clients

These graphical clients, among others, let you set the endpoint of Cellar:

- [Cyberduck](https://cyberduck.io)
- [Filestash](https://www.filestash.app/)
- [Rclone Web GUI](https://rclone.org/gui/)
- [S3 Browser](https://s3browser.com/)
- [S3 Explorer](https://s3explorer.accessdevops.com/)
- [WinSCP](https://winscp.net)

## Upload and synchronize files

Synchronizing a folder uploads its new and changed files to a bucket, such as exports or media files. Preview the changes with a dry run first:

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  `put` uploads files. `sync` uploads the new files of a folder, and those whose size or checksum changed. `--delete-removed` deletes the others:

  ```bash
  s3cmd put image.jpg s3://my-bucket/images/image.jpg
  s3cmd sync --dry-run --delete-removed ./public/ s3://my-bucket/
  s3cmd sync --delete-removed ./public/ s3://my-bucket/
  s3cmd ls s3://my-bucket/images/
  ```

  s3cmd guesses the content type of each file, which browsers need to display it. Its guess can return `text/plain` for HTML or CSS files: add `--no-mime-magic` to guess from the extension of the file, or `-m text/html` to set the type yourself.

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  `cp` uploads files, and `sync` uploads the new and changed files of a folder. `--delete` also deletes the files the folder no longer holds:

  ```bash
  aws s3 cp image.jpg s3://my-bucket/images/image.jpg
  aws s3 sync --dryrun --delete ./public s3://my-bucket/
  aws s3 sync --delete ./public s3://my-bucket/
  aws s3 ls --recursive s3://my-bucket/images/
  ```

  The AWS CLI sets the content type of each file from its extension.

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  `put` uploads files, and `mirror` uploads the files of a folder that the bucket doesn't hold. Add `--overwrite` to also upload the changed files, and `--remove` to delete the files the folder no longer holds:

  ```bash
  rc put image.jpg cellar/my-bucket/images/image.jpg
  rc mirror --dry-run --overwrite --remove ./public cellar/my-bucket
  rc mirror --overwrite --remove ./public cellar/my-bucket
  rc object list --recursive cellar/my-bucket/images
  ```

  The RustFS CLI sets the content type of each file from its extension.

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  `copy` uploads the new and changed files of a folder to the [`cellar` remote](#configure-an-s3-client). `sync` also deletes the files the folder no longer holds:

  ```bash
  rclone copy ./public cellar:my-bucket
  rclone sync --dry-run ./public cellar:my-bucket
  rclone sync ./public cellar:my-bucket
  rclone ls cellar:my-bucket
  ```

  rclone sets the content type of each file from its extension.

  {{< /tab >}}

{{< /tabs >}}

## Use Cellar from your application

Use the S3 SDK of your language, with `https://` and the value of `CELLAR_ADDON_HOST` as endpoint, and the [`us-east-1`](#configure-an-s3-client) region, which Cellar ignores. Recent AWS SDKs add checksums that Cellar rejects: set the checksum options to `when_required`, except with Ruby.

{{< tabs >}}

  {{< tab name="Bun" icon="simple:bun" >}}

  [Bun](https://bun.sh) includes an [S3 client](https://bun.sh/docs/api/s3), without any dependency:

  ```typescript
  import { S3Client } from "bun";

  const cellar = new S3Client({
    accessKeyId: process.env.CELLAR_ADDON_KEY_ID,
    secretAccessKey: process.env.CELLAR_ADDON_KEY_SECRET,
    endpoint: `https://${process.env.CELLAR_ADDON_HOST}`,
    bucket: "my-bucket",
  });

  await cellar.write("hello.txt", "Hello from Cellar!");
  const text = await cellar.file("hello.txt").text();
  await cellar.delete("hello.txt");
  ```

  Bun also reads `s3://` URLs with `fetch` and `Bun.file()`. Set `S3_ACCESS_KEY_ID`, `S3_SECRET_ACCESS_KEY`, and `S3_ENDPOINT` to the credentials and the endpoint of Cellar, then read your objects by their URL, without any client:

  ```typescript
  const response = await fetch("s3://my-bucket/hello.txt");
  const content = await response.text();
  ```

  Bun sends its uploads without any checksum, so Cellar can't check their integrity.

  {{< /tab >}}

  {{< tab name="Node.js" icon="simple:nodedotjs" >}}

  Install the [AWS SDK for JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/) v3:

  ```bash
  npm install @aws-sdk/client-s3
  ```

  Without the checksum options, uploads from a stream fail with a `MissingContentLength` error:

  ```javascript
  import { S3Client, PutObjectCommand, ListBucketsCommand } from "@aws-sdk/client-s3";

  const s3 = new S3Client({
    endpoint: `https://${process.env.CELLAR_ADDON_HOST}`,
    region: "us-east-1",
    credentials: {
      accessKeyId: process.env.CELLAR_ADDON_KEY_ID,
      secretAccessKey: process.env.CELLAR_ADDON_KEY_SECRET,
    },
    requestChecksumCalculation: "WHEN_REQUIRED",
    responseChecksumValidation: "WHEN_REQUIRED",
  });

  const { Buckets } = await s3.send(new ListBucketsCommand({}));
  console.log(Buckets);

  await s3.send(new PutObjectCommand({ Bucket: "my-bucket", Key: "hello.txt", Body: "Hello from Cellar!" }));
  ```

  {{< /tab >}}

  {{< tab name="Java" icon="java" >}}

  Add the S3 module of the [AWS SDK for Java](https://github.com/aws/aws-sdk-java-v2) 2.x. With Maven, use the latest version of this dependency:

  ```xml
  <dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>s3</artifactId>
    <version>2.59.8</version>
  </dependency>
  ```

  Without the checksum options, uploads fail with a `400` error. This class uploads a file, then lists the objects of each bucket:

  ```java
  import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
  import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
  import software.amazon.awssdk.core.checksums.RequestChecksumCalculation;
  import software.amazon.awssdk.core.checksums.ResponseChecksumValidation;
  import software.amazon.awssdk.core.sync.RequestBody;
  import software.amazon.awssdk.regions.Region;
  import software.amazon.awssdk.services.s3.S3Client;
  import software.amazon.awssdk.services.s3.model.ListObjectsV2Request;

  import java.net.URI;

  public class CellarDemo {

      public static void main(String[] args) throws Exception {
          var credentials = StaticCredentialsProvider.create(AwsBasicCredentials.create(
              System.getenv("CELLAR_ADDON_KEY_ID"),
              System.getenv("CELLAR_ADDON_KEY_SECRET")
          ));

          try (S3Client s3 = S3Client.builder()
                  .endpointOverride(URI.create("https://" + System.getenv("CELLAR_ADDON_HOST")))
                  .region(Region.US_EAST_1)
                  .credentialsProvider(credentials)
                  .requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)
                  .responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)
                  .build()) {
              s3.putObject(request -> request.bucket("my-bucket").key("hello.txt"), RequestBody.fromString("Hello from Cellar!"));

              s3.listBuckets().buckets().forEach(bucket -> {
                  var request = ListObjectsV2Request.builder().bucket(bucket.name()).build();
                  s3.listObjectsV2(request).contents().forEach(object -> System.out.println(bucket.name() + "/" + object.key()));
              });
          }
      }
  }
  ```

  The [AWS code examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3) show other uses of the SDK.

  {{< /tab >}}

  {{< tab name="Python" icon="simple:python" >}}

  Install [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), the AWS SDK for Python. Without the checksum options, uploads fail with a `MissingContentLength` error:

  ```python
  import os

  import boto3
  from botocore.config import Config

  s3 = boto3.client(
      "s3",
      region_name="us-east-1",
      endpoint_url=f"https://{os.environ['CELLAR_ADDON_HOST']}",
      aws_access_key_id=os.environ["CELLAR_ADDON_KEY_ID"],
      aws_secret_access_key=os.environ["CELLAR_ADDON_KEY_SECRET"],
      config=Config(
          signature_version="s3v4",
          request_checksum_calculation="when_required",
          response_checksum_validation="when_required",
      ),
  )

  print(s3.list_buckets()["Buckets"])

  s3.upload_file("report.pdf", "my-bucket", "reports/report.pdf")
  ```

  {{< /tab >}}

  {{< tab name="Ruby" icon="ruby" >}}

  Add the `aws-sdk-s3` gem to your `Gemfile`, then create a client:

  ```ruby
  require "aws-sdk-s3"

  s3 = Aws::S3::Client.new(
    endpoint: "https://#{ENV.fetch('CELLAR_ADDON_HOST')}",
    region: "us-east-1",
    access_key_id: ENV.fetch("CELLAR_ADDON_KEY_ID"),
    secret_access_key: ENV.fetch("CELLAR_ADDON_KEY_SECRET"),
  )

  s3.put_object(bucket: "my-bucket", key: "reports/report.pdf", body: File.open("report.pdf"))
  ```

  [Active Storage](https://guides.rubyonrails.org/active_storage_overview.html), the file storage of Ruby on Rails, uses Cellar as an S3 service. Declare Cellar:

  ```yaml {filename="config/storage.yml"}
  cellar:
    service: S3
    access_key_id: <%= ENV.fetch("CELLAR_ADDON_KEY_ID") %>
    secret_access_key: <%= ENV.fetch("CELLAR_ADDON_KEY_SECRET") %>
    endpoint: https://<%= ENV.fetch("CELLAR_ADDON_HOST") %>
    region: us-east-1
    bucket: my-bucket
  ```

  Then select this service for production:

  ```ruby {filename="config/environments/production.rb"}
  config.active_storage.service = :cellar
  ```

  {{< /tab >}}

  {{< tab name="Rust" icon="simple:rust" >}}

  Add the [AWS SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_s3_code_examples.html) and Tokio to your project:

  ```bash
  cargo add aws-sdk-s3 --features behavior-version-latest
  cargo add tokio --features full
  ```

  Without the checksum options, uploads fail with an `XAmzContentSHA256Mismatch` error:

  ```rust
  use std::env;

  use aws_sdk_s3::{
      config::{Builder, Credentials, Region, RequestChecksumCalculation, ResponseChecksumValidation},
      primitives::ByteStream,
      Client,
  };

  #[tokio::main]
  async fn main() -> Result<(), Box<dyn std::error::Error>> {
      let credentials = Credentials::new(
          env::var("CELLAR_ADDON_KEY_ID")?,
          env::var("CELLAR_ADDON_KEY_SECRET")?,
          None,
          None,
          "cellar",
      );
      let config = Builder::new()
          .endpoint_url(format!("https://{}", env::var("CELLAR_ADDON_HOST")?))
          .region(Region::new("us-east-1"))
          .credentials_provider(credentials)
          .request_checksum_calculation(RequestChecksumCalculation::WhenRequired)
          .response_checksum_validation(ResponseChecksumValidation::WhenRequired)
          .build();
      let s3 = Client::from_conf(config);

      s3.put_object()
          .bucket("my-bucket")
          .key("reports/report.pdf")
          .body(ByteStream::from_path("report.pdf").await?)
          .send()
          .await?;

      let object = s3.get_object().bucket("my-bucket").key("reports/report.pdf").send().await?;
      let content = object.body.collect().await?.into_bytes();
      println!("{} bytes", content.len());
      Ok(())
  }
  ```

  {{< /tab >}}

  {{< tab name="V" icon="simple:v" >}}

  The [`net.s3` module](https://modules.vlang.io/net.s3.html) of the V standard library reads the variables of Cellar, after the `S3_` and `AWS_` variables if your application sets them. Set the bucket in the client, or in `S3_BUCKET`:

  ```v
  import net.s3

  fn main() {
      c := s3.new_client(s3.Credentials{
          ...s3.Credentials.from_env()
          bucket: 'my-bucket'
      })

      c.put('hello.txt', 'Hello from Cellar!'.bytes(), content_type: 'text/plain')!
      println(c.get_string('hello.txt')!)

      res := c.list()!
      for object in res.objects {
          println('${object.key} ${object.size}')
      }
      c.delete('hello.txt')!
  }
  ```

  Add `hash_payload: true` to `put` to sign the SHA-256 checksum of the content: Cellar then rejects a content that doesn't match it.

  {{< /tab >}}

{{< /tabs >}}

### Use Cellar in the scripts of your application

Scripts such as [hooks](/doc/manage/build-hooks/) or [scheduled tasks](/doc/manage/cron/) use the add-on without any configuration file. A scheduled task needs a login shell to get these variables and tools: start its script with `#!/bin/bash -l`, as [Load your environment variables](/doc/manage/cron/#load-your-environment-variables) details. Clever Cloud instances, except Docker ones, include s3cmd, Bun, and V. They install the other clients with mise or uv at the first use: replace `latest` with a version in production.

These commands upload a backup from a Bash script, with the variables of the add-on:

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  ```bash
  s3cmd --access_key="$CELLAR_ADDON_KEY_ID" --secret_key="$CELLAR_ADDON_KEY_SECRET" \
    --host="$CELLAR_ADDON_HOST" --host-bucket="%(bucket)s.$CELLAR_ADDON_HOST" \
    put backup.tar.gz s3://my-bucket/backups/backup.tar.gz
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  ```bash
  export AWS_ACCESS_KEY_ID="$CELLAR_ADDON_KEY_ID" AWS_SECRET_ACCESS_KEY="$CELLAR_ADDON_KEY_SECRET"
  export AWS_ENDPOINT_URL="https://$CELLAR_ADDON_HOST" AWS_DEFAULT_REGION=us-east-1
  export AWS_REQUEST_CHECKSUM_CALCULATION=when_required AWS_RESPONSE_CHECKSUM_VALIDATION=when_required

  uvx --from awscli aws s3 cp backup.tar.gz s3://my-bucket/backups/backup.tar.gz
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  ```bash
  mise x github:rustfs/cli@latest -- rc alias set cellar "https://$CELLAR_ADDON_HOST" "$CELLAR_ADDON_KEY_ID" "$CELLAR_ADDON_KEY_SECRET"
  mise x github:rustfs/cli@latest -- rc put backup.tar.gz cellar/my-bucket/backups/backup.tar.gz
  ```

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  rclone reads the configuration of a remote from variables:

  ```bash
  export RCLONE_CONFIG_CELLAR_TYPE=s3 RCLONE_CONFIG_CELLAR_PROVIDER=Cellar
  export RCLONE_CONFIG_CELLAR_ACCESS_KEY_ID="$CELLAR_ADDON_KEY_ID"
  export RCLONE_CONFIG_CELLAR_SECRET_ACCESS_KEY="$CELLAR_ADDON_KEY_SECRET"
  export RCLONE_CONFIG_CELLAR_ENDPOINT="https://$CELLAR_ADDON_HOST"

  mise x rclone@latest -- rclone copyto backup.tar.gz cellar:my-bucket/backups/backup.tar.gz
  ```

  {{< /tab >}}

  {{< tab name="Bun" icon="simple:bun" >}}

  ```bash
  export S3_ACCESS_KEY_ID="$CELLAR_ADDON_KEY_ID" S3_SECRET_ACCESS_KEY="$CELLAR_ADDON_KEY_SECRET"
  export S3_ENDPOINT="https://$CELLAR_ADDON_HOST"

  bun -e 'await Bun.write(Bun.file("s3://my-bucket/backups/backup.tar.gz"), Bun.file("backup.tar.gz"))'
  ```

  {{< /tab >}}

  {{< tab name="V" icon="simple:v" >}}

  This V script reads the variables of Cellar by itself. Run it with `v run backup.vsh`, or make it executable with `chmod +x backup.vsh`:

  ```v {filename="backup.vsh"}
  #!/usr/bin/env -S v

  import net.s3

  c := s3.new_client(s3.Credentials{
      ...s3.Credentials.from_env()
      bucket: 'my-bucket'
  })
  c.upload_file('backups/backup.tar.gz', 'backup.tar.gz')!
  println('Uploaded ${c.size('backups/backup.tar.gz')!} bytes')
  ```

  {{< /tab >}}

{{< /tabs >}}

### Use Cellar in local scripts

On your computer, load the variables of the add-on with Clever Tools, then run the same commands. `clever addon list` shows its ID:

```bash
source <(clever addon env addon_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx -F shell)
```

Bun and V need no S3 dependency, and suit short scripts, such as an export or a backup.

## Share and upload files with presigned URLs

A presigned URL gives access to one object for a limited time, without your credentials. A download URL shares a private file, and an upload URL lets a client, such as a browser, send a file with a `PUT` request. Clients sign these URLs locally, and renewing the secret invalidates them.

### Create URLs from the command line

These commands create a download URL valid for one hour, once you [configure the client](#configure-an-s3-client):

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  ```bash
  s3cmd signurl s3://my-bucket/reports/report.pdf +3600
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  ```bash
  aws s3 presign s3://my-bucket/reports/report.pdf --expires-in 3600
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  The RustFS CLI also creates upload URLs, with `--upload`:

  ```bash
  rc object share --expire 1h cellar/my-bucket/reports/report.pdf
  rc object share --upload --expire 15m cellar/my-bucket/uploads/photo.jpg
  ```

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  ```bash
  rclone link --expire 1h cellar:my-bucket/reports/report.pdf
  ```

  {{< /tab >}}

{{< /tabs >}}

### Sign URLs in your application

These examples use the client of [your language](#use-cellar-from-your-application). They create a download URL valid for one hour, and an upload URL valid for 15 minutes:

{{< tabs >}}

  {{< tab name="Bun" icon="simple:bun" >}}

  ```typescript
  const downloadUrl = cellar.presign("reports/report.pdf", { expiresIn: 3600 });
  const uploadUrl = cellar.presign("uploads/photo.jpg", { method: "PUT", expiresIn: 900 });
  ```

  {{< /tab >}}

  {{< tab name="Node.js" icon="simple:nodedotjs" >}}

  Install the `@aws-sdk/s3-request-presigner` package of the AWS SDK:

  ```bash
  npm install @aws-sdk/s3-request-presigner
  ```

  Then sign the URLs with the `s3` client:

  ```javascript
  import { GetObjectCommand, PutObjectCommand } from "@aws-sdk/client-s3";
  import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

  const downloadUrl = await getSignedUrl(
    s3,
    new GetObjectCommand({ Bucket: "my-bucket", Key: "reports/report.pdf" }),
    { expiresIn: 3600 },
  );
  const uploadUrl = await getSignedUrl(
    s3,
    new PutObjectCommand({ Bucket: "my-bucket", Key: "uploads/photo.jpg" }),
    { expiresIn: 900 },
  );
  ```

  {{< /tab >}}

  {{< tab name="Java" icon="java" >}}

  `S3Presigner` signs the URLs with the `credentials` of the S3 client:

  ```java
  import software.amazon.awssdk.services.s3.presigner.S3Presigner;

  import java.net.URL;
  import java.time.Duration;

  try (S3Presigner presigner = S3Presigner.builder()
          .endpointOverride(URI.create("https://" + System.getenv("CELLAR_ADDON_HOST")))
          .region(Region.US_EAST_1)
          .credentialsProvider(credentials)
          .build()) {
      URL downloadUrl = presigner.presignGetObject(request -> request
          .signatureDuration(Duration.ofHours(1))
          .getObjectRequest(object -> object.bucket("my-bucket").key("reports/report.pdf"))).url();
      URL uploadUrl = presigner.presignPutObject(request -> request
          .signatureDuration(Duration.ofMinutes(15))
          .putObjectRequest(object -> object.bucket("my-bucket").key("uploads/photo.jpg"))).url();
  }
  ```

  {{< /tab >}}

  {{< tab name="Python" icon="simple:python" >}}

  ```python
  download_url = s3.generate_presigned_url(
      "get_object",
      Params={"Bucket": "my-bucket", "Key": "reports/report.pdf"},
      ExpiresIn=3600,
  )
  upload_url = s3.generate_presigned_url(
      "put_object",
      Params={"Bucket": "my-bucket", "Key": "uploads/photo.jpg"},
      ExpiresIn=900,
  )
  ```

  {{< /tab >}}

  {{< tab name="Ruby" icon="ruby" >}}

  ```ruby
  presigner = Aws::S3::Presigner.new(client: s3)

  download_url = presigner.presigned_url(:get_object, bucket: "my-bucket", key: "reports/report.pdf", expires_in: 3600)
  upload_url = presigner.presigned_url(:put_object, bucket: "my-bucket", key: "uploads/photo.jpg", expires_in: 900)
  ```

  {{< /tab >}}

  {{< tab name="Rust" icon="simple:rust" >}}

  ```rust
  use std::time::Duration;

  use aws_sdk_s3::presigning::PresigningConfig;

  let download_url = s3.get_object()
      .bucket("my-bucket")
      .key("reports/report.pdf")
      .presigned(PresigningConfig::expires_in(Duration::from_secs(3600))?)
      .await?;
  let upload_url = s3.put_object()
      .bucket("my-bucket")
      .key("uploads/photo.jpg")
      .presigned(PresigningConfig::expires_in(Duration::from_secs(900))?)
      .await?;
  println!("{}\n{}", download_url.uri(), upload_url.uri());
  ```

  {{< /tab >}}

  {{< tab name="V" icon="simple:v" >}}

  ```v
  download_url := c.presign('reports/report.pdf', expires_in: 3600)!
  upload_url := c.presign('uploads/photo.jpg', method: .put, expires_in: 900)!
  ```

  {{< /tab >}}

{{< /tabs >}}

The client then sends the file to the upload URL, here in `UPLOAD_URL`, with its content type:

```bash
curl -T photo.jpg -H "Content-Type: image/jpeg" "$UPLOAD_URL"
```

### Check the integrity of uploads

To check the integrity of an uploaded file, sign the URL with the MD5 checksum of its content. The client must then send this checksum in the `Content-MD5` header, and Cellar rejects the upload with a `BadDigest` error if the content doesn't match it.

{{< tabs >}}

  {{< tab name="Node.js" icon="simple:nodedotjs" >}}

  This script uses the `s3` client of the [Node.js example](#use-cellar-from-your-application). `unhoistableHeaders` keeps `Content-MD5` in the signed headers:

  ```javascript
  import { createHash } from "node:crypto";
  import { PutObjectCommand } from "@aws-sdk/client-s3";
  import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

  const content = Buffer.from("hello world");
  const md5 = createHash("md5").update(content).digest("base64");

  const command = new PutObjectCommand({ Bucket: "my-bucket", Key: "uploads/hello.txt", ContentMD5: md5 });
  const url = await getSignedUrl(s3, command, {
    expiresIn: 3600,
    unhoistableHeaders: new Set(["content-md5"]),
  });
  console.log(url);
  ```

  {{< /tab >}}

  {{< tab name="Java" icon="java" >}}

  This code uses the `presigner` of the [Java example](#sign-urls-in-your-application):

  ```java
  import java.security.MessageDigest;
  import java.util.Base64;

  byte[] content = "hello world".getBytes();
  String md5 = Base64.getEncoder().encodeToString(MessageDigest.getInstance("MD5").digest(content));

  URL url = presigner.presignPutObject(request -> request
      .signatureDuration(Duration.ofHours(1))
      .putObjectRequest(object -> object.bucket("my-bucket").key("uploads/hello.txt").contentMD5(md5))).url();
  ```

  {{< /tab >}}

  {{< tab name="Python" icon="simple:python" >}}

  This script uses the `s3` client of the [Python example](#use-cellar-from-your-application):

  ```python
  import base64
  import hashlib

  content = b"hello world"
  md5 = base64.b64encode(hashlib.md5(content).digest()).decode()

  url = s3.generate_presigned_url(
      "put_object",
      Params={"Bucket": "my-bucket", "Key": "uploads/hello.txt", "ContentMD5": md5},
      ExpiresIn=3600,
  )
  print(url)
  ```

  {{< /tab >}}

  {{< tab name="Ruby" icon="ruby" >}}

  This code uses the `presigner` of the [Ruby example](#sign-urls-in-your-application):

  ```ruby
  require "digest"

  md5 = Digest::MD5.base64digest("hello world")
  url = presigner.presigned_url(:put_object, bucket: "my-bucket", key: "uploads/hello.txt", content_md5: md5, expires_in: 3600)
  ```

  {{< /tab >}}

  {{< tab name="Rust" icon="simple:rust" >}}

  Add the `md-5` and `base64` crates with `cargo add md-5 base64`. This code uses the `s3` client of the [Rust example](#use-cellar-from-your-application):

  ```rust
  use base64::{engine::general_purpose::STANDARD, Engine};
  use md5::{Digest, Md5};

  let md5 = STANDARD.encode(Md5::digest(b"hello world"));
  let url = s3.put_object()
      .bucket("my-bucket")
      .key("uploads/hello.txt")
      .content_md5(md5)
      .presigned(PresigningConfig::expires_in(Duration::from_secs(3600))?)
      .await?;
  ```

  {{< /tab >}}

{{< /tabs >}}

The client then uploads the file with the URL and its checksum. Without the `Content-MD5` header, Cellar rejects the request with a `403` error:

```bash
printf 'hello world' > hello.txt
curl -T hello.txt -H "Content-MD5: XrY7u+Ae7tCTyyK7j1rNww==" "$UPLOAD_URL"
```

Bun, V, and the [command-line clients](#create-urls-from-the-command-line) can't sign a checksum in their upload URLs, which then accept a file without the `Content-MD5` header. Cellar doesn't check the content against an `x-amz-checksum-sha256` checksum either: sign the URL with MD5.

## Control access

The credentials of the add-on grant full access to all its buckets: anyone who holds them can read, change, or delete your objects. Other requests can only read the objects you make public, or use [presigned URLs](#share-and-upload-files-with-presigned-urls).

### Make objects public

A public access control list (ACL) makes an object readable by anyone. Its URL holds the name of its bucket and its key, such as `https://my-bucket.cellar-c2.services.clever-cloud.com/images/logo.png`. These commands make an object public, then private again:

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  ```bash
  s3cmd put --acl-public logo.png s3://my-bucket/images/logo.png
  s3cmd setacl --acl-private s3://my-bucket/images/logo.png
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  ```bash
  aws s3 cp --acl public-read logo.png s3://my-bucket/images/logo.png
  aws s3api put-object-acl --bucket my-bucket --key images/logo.png --acl private
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  The RustFS CLI sets an ACL with a header at upload. For a folder, it replaces the current [bucket policy](#public-bucket-policy), and `private` deletes it:

  ```bash
  rc put -H "x-amz-acl: public-read" logo.png cellar/my-bucket/images/logo.png
  rc bucket anonymous set download cellar/my-bucket/images/
  rc bucket anonymous set private cellar/my-bucket
  ```

  The RustFS CLI can't make an object private again: use s3cmd or the AWS CLI.

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  rclone also sends the `--s3-acl` value when it checks the bucket, which Cellar refuses: add `--s3-bucket-acl private`.

  ```bash
  rclone copyto --s3-acl public-read --s3-bucket-acl private logo.png cellar:my-bucket/images/logo.png
  ```

  rclone can't make an object private again: use s3cmd or the AWS CLI.

  {{< /tab >}}

{{< /tabs >}}

Cellar serves the object at its exact key, but doesn't serve `index.html` for a folder or the root of a bucket. To serve a static website with index files, and your domain over HTTPS, deploy it with the [Static](/doc/deploy/applications/static/) runtime.

> [!NOTE] Public buckets
> A `public-read` ACL on a bucket, such as `aws s3api create-bucket --acl public-read`, lets anyone list the names of its objects, without making them public. `rc bucket anonymous set download` on a whole bucket makes both public.

### Public bucket policy

To make all the objects of a bucket readable by anyone, apply a bucket policy instead of public ACLs. Cellar supports [bucket policies](https://docs.ceph.com/en/latest/radosgw/bucketpolicy/) in the format of AWS S3. Replace `my-bucket` with the name of your bucket in this policy:

```json {filename="policy.json",hl_lines=[8]}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

This policy exposes every object of the bucket, so make sure it holds nothing private. A bucket holds a single policy. To combine rules, such as public reads and a [grant to another add-on](#grant-access-to-another-add-on), list their statements in its `Statement` array.

These commands apply the policy, show it, and delete it to make the objects private again, except the objects you uploaded with a public ACL:

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  ```bash
  s3cmd setpolicy policy.json s3://my-bucket
  s3cmd info s3://my-bucket
  s3cmd delpolicy s3://my-bucket
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  ```bash
  aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json
  aws s3api get-bucket-policy --bucket my-bucket
  aws s3api delete-bucket-policy --bucket my-bucket
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  ```bash
  rc bucket anonymous set-json policy.json cellar/my-bucket
  rc bucket anonymous get-json cellar/my-bucket
  rc bucket anonymous set private cellar/my-bucket
  ```

  {{< /tab >}}

{{< /tabs >}}

rclone doesn't manage bucket policies.

### Restrict access to IP addresses

This policy denies the reads, writes, and listings that don't come from `203.0.113.10`, previous versions included. It also applies to the add-on credentials, your applications, and the Cellar Explorer. Replace the address and `my-bucket`, then [apply it](#public-bucket-policy):

```json {filename="ip-policy.json",hl_lines=[11,13]}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": [
        "s3:GetObject", "s3:GetObjectVersion", "s3:ListBucket", "s3:ListBucketVersions",
        "s3:PutObject", "s3:DeleteObject", "s3:DeleteObjectVersion"
      ],
      "Resource": ["arn:aws:s3:::my-bucket", "arn:aws:s3:::my-bucket/*"],
      "Condition": {
        "NotIpAddress": { "aws:SourceIp": ["203.0.113.10/32"] }
      }
    }
  ]
}
```

> [!TIP] Keep access to the policy
> A `Deny` on `s3:*` also blocks the changes to the policy, and locks you out of the bucket. List the actions to deny instead, as this policy does: you can then delete the policy from any address.

### Grant access to another add-on

Cellar doesn't create other users for an add-on. To give a person or an application limited access to a bucket, create a second Cellar add-on and give them its credentials. Then grant access to this second add-on in a policy on your bucket.

The policy names the second add-on by its ID, which starts with `cellar_`. Clever Tools shows it as `Real ID` when it creates the add-on, and `clever addon list --format json` returns it as `realId`. This policy grants read-only access to `my-bucket`:

```json {filename="read-only-policy.json",hl_lines=[6,8]}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam:::user/cellar_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" },
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": ["arn:aws:s3:::my-bucket", "arn:aws:s3:::my-bucket/*"]
    }
  ]
}
```

Apply it with the credentials of the first add-on, which owns the bucket. rclone doesn't manage bucket policies:

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  ```bash
  s3cmd setpolicy read-only-policy.json s3://my-bucket
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  ```bash
  aws s3api put-bucket-policy --bucket my-bucket --policy file://read-only-policy.json
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  ```bash
  rc bucket anonymous set-json read-only-policy.json cellar/my-bucket
  ```

  {{< /tab >}}

{{< /tabs >}}

The second add-on can then list and download the objects of `my-bucket`, but not change them. The bucket doesn't appear in its list of buckets, so name it in each request, such as `s3cmd -c reader.s3cfg ls s3://my-bucket` with the `s3cfg` file of the second add-on.

## Serve a bucket on your domain

To serve public objects on your own domain, such as `cdn.example.com`, create a bucket with this exact name, then a CNAME record from this domain to `cellar-c2.services.clever-cloud.com.`. Cellar serves this domain over HTTP only, without a certificate: for HTTPS, serve your files from an application, such as the [Static](/doc/deploy/applications/static/) runtime.

Bucket names with dots don't match the certificate of Cellar. The AWS CLI, the RustFS CLI, and rclone switch to the path style for them:

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  s3cmd needs the path style, with `--host-bucket`:

  ```bash
  s3cmd --host-bucket=cellar-c2.services.clever-cloud.com mb s3://cdn.example.com
  s3cmd --host-bucket=cellar-c2.services.clever-cloud.com put --acl-public logo.png s3://cdn.example.com/logo.png
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  ```bash
  aws s3 mb s3://cdn.example.com
  aws s3 cp --acl public-read logo.png s3://cdn.example.com/logo.png
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  Make the objects public with a [bucket policy](#public-bucket-policy) on `cdn.example.com`:

  ```bash
  rc bucket create cellar/cdn.example.com
  rc put logo.png cellar/cdn.example.com/logo.png
  rc bucket anonymous set-json policy.json cellar/cdn.example.com
  ```

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  ```bash
  rclone mkdir cellar:cdn.example.com
  rclone copyto --s3-acl public-read --s3-bucket-acl private logo.png cellar:cdn.example.com/logo.png
  ```

  {{< /tab >}}

{{< /tabs >}}

## Configure CORS

To let browsers call your bucket from the pages of another origin, such as uploads from your website, set a [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) configuration on it. Each configuration holds one or several rules, in an XML file:

```xml {filename="cors.xml"}
<CORSConfiguration>
  <CORSRule>
    <AllowedOrigin>https://www.example.com</AllowedOrigin>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>DELETE</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
    <ExposeHeader>ETag</ExposeHeader>
  </CORSRule>
  <CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <MaxAgeSeconds>3600</MaxAgeSeconds>
  </CORSRule>
</CORSConfiguration>
```

The first rule accepts `PUT`, `POST`, and `DELETE` requests from `https://www.example.com`, with any header, and lets the browser read the `ETag` header of the response. The second accepts `GET` requests from any origin, and lets browsers cache their preflight requests for an hour.

Setting a configuration replaces the previous one, so save the current one first. These commands show, apply, and delete a configuration:

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  ```bash
  s3cmd info s3://my-bucket
  s3cmd setcors cors.xml s3://my-bucket
  s3cmd delcors s3://my-bucket
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  The AWS CLI reads the same rules in JSON:

  ```json {filename="cors.json"}
  {
    "CORSRules": [
      {
        "AllowedOrigins": ["https://www.example.com"],
        "AllowedMethods": ["PUT", "POST", "DELETE"],
        "AllowedHeaders": ["*"],
        "ExposeHeaders": ["ETag"]
      },
      {
        "AllowedOrigins": ["*"],
        "AllowedMethods": ["GET"],
        "MaxAgeSeconds": 3600
      }
    ]
  }
  ```

  ```bash
  aws s3api get-bucket-cors --bucket my-bucket
  aws s3api put-bucket-cors --bucket my-bucket --cors-configuration file://cors.json
  aws s3api delete-bucket-cors --bucket my-bucket
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  ```bash
  rc bucket cors list cellar/my-bucket
  rc bucket cors set cellar/my-bucket cors.xml
  rc bucket cors remove cellar/my-bucket
  ```

  {{< /tab >}}

{{< /tabs >}}

rclone doesn't manage CORS configurations.

## Versioning

Versioning keeps the previous versions of each object, when you replace or delete it, so that you can restore them. It applies to a whole bucket, and Cellar stores each version: they count in the storage of the add-on.

A bucket is unversioned when you create it. Once you enable versioning, you can suspend it, but the bucket never becomes unversioned again. Objects stored before you enable it have the `null` version ID.

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  s3cmd enables versioning, and `info` shows its status. `disable` suspends it:

  ```bash
  s3cmd setversioning s3://my-bucket enable
  s3cmd info s3://my-bucket
  s3cmd setversioning s3://my-bucket disable
  ```

  s3cmd can't list, download, or restore the versions of an object: use the RustFS CLI or the AWS CLI for these operations.

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  These commands use the [`cellar` profile](#configure-an-s3-client). Enable versioning, suspend it, or check its status:

  ```bash
  aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Enabled
  aws s3api put-bucket-versioning --bucket my-bucket --versioning-configuration Status=Suspended
  aws s3api get-bucket-versioning --bucket my-bucket
  ```

  List the versions of the objects of a bucket, or of the objects with a given prefix:

  ```bash
  aws s3api list-object-versions --bucket my-bucket
  aws s3api list-object-versions --bucket my-bucket --prefix report.pdf
  ```

  Download a version by its ID, here the version before the latest one:

  ```bash
  VERSION_ID=$(aws s3api list-object-versions --bucket my-bucket --prefix report.pdf \
    --query 'Versions[?IsLatest==`false`] | [0].VersionId' --output text)
  aws s3api get-object --bucket my-bucket --key report.pdf --version-id "$VERSION_ID" report-previous.pdf
  ```

  Deleting an object without a version ID adds a delete marker, which hides the object but keeps its versions. To restore the object, delete this marker by its version ID. Delete a version the same way:

  ```bash
  MARKER_ID=$(aws s3api list-object-versions --bucket my-bucket --prefix report.pdf \
    --query 'DeleteMarkers[?IsLatest==`true`] | [0].VersionId' --output text)
  aws s3api delete-object --bucket my-bucket --key report.pdf --version-id "$MARKER_ID"
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  These commands use the [`cellar` alias](#configure-an-s3-client). Enable versioning, check its status, or suspend it:

  ```bash
  rc bucket version enable cellar/my-bucket
  rc bucket version info cellar/my-bucket
  rc bucket version suspend cellar/my-bucket
  ```

  List the versions of the objects of a bucket, or of one object:

  ```bash
  rc object list --versions --recursive cellar/my-bucket
  rc bucket version list cellar/my-bucket/report.pdf
  ```

  Download a version by its ID, here the version before the latest one, which [jq](https://jqlang.org) extracts from the JSON output:

  ```bash
  VERSION_ID=$(rc --json bucket version list cellar/my-bucket/report.pdf \
    | jq -r '[.[] | select(.is_latest | not)][0].version_id')
  rc get --version-id "$VERSION_ID" cellar/my-bucket/report.pdf report-previous.pdf
  ```

  Deleting an object adds a delete marker, which hides it but keeps its versions. `undo` removes this marker:

  ```bash
  rc undo cellar/my-bucket/report.pdf
  ```

  Delete a version by its ID:

  ```bash
  rc object remove --version-id "$VERSION_ID" cellar/my-bucket/report.pdf
  ```

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  These commands use the [`cellar` remote](#configure-an-s3-client). Enable versioning, check its status, or suspend it:

  ```bash
  rclone backend versioning cellar:my-bucket Enabled
  rclone backend versioning cellar:my-bucket
  rclone backend versioning cellar:my-bucket Suspended
  ```

  With `--s3-versions`, rclone lists the previous versions with their date in their name. Download one of them by this name:

  ```bash
  rclone ls --s3-versions cellar:my-bucket
  rclone copyto --s3-versions cellar:my-bucket/report-v2026-11-24-083351-569.pdf report-previous.pdf
  ```

  rclone can't remove a delete marker: restore a deleted object with the RustFS CLI or the AWS CLI.

  {{< /tab >}}

{{< /tabs >}}

## Object Lock

Cellar supports [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html), which protects object versions from deletion or replacement with a [write-once-read-many (WORM)](https://en.wikipedia.org/wiki/Write_once_read_many) model. It reduces the risk of accidental or malicious deletion, and enforces retention policies.

Enable Object Lock when you create the bucket: Cellar doesn't accept it on an existing bucket. It enables [versioning](#versioning), which you can't suspend on this bucket. Object Lock protects no object until you set a default retention period, or protect some object versions yourself.

### Create a bucket with Object Lock

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  s3cmd has no Object Lock option for buckets, but sends the header that enables it:

  ```bash
  s3cmd --add-header=x-amz-bucket-object-lock-enabled:true mb s3://my-locked-bucket
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  ```bash
  aws s3api create-bucket --bucket my-locked-bucket --object-lock-enabled-for-bucket
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  ```bash
  rc bucket create --with-lock cellar/my-locked-bucket
  ```

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  ```bash
  rclone mkdir --s3-bucket-object-lock-enabled cellar:my-locked-bucket
  ```

  {{< /tab >}}

{{< /tabs >}}

### Set a default retention period

These commands protect each new version for 30 days, in governance mode. With s3cmd and rclone, [protect each version](#protect-a-version) instead.

{{< tabs >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  ```bash
  aws s3api put-object-lock-configuration \
    --bucket my-locked-bucket \
    --object-lock-configuration '{"ObjectLockEnabled":"Enabled","Rule":{"DefaultRetention":{"Mode":"GOVERNANCE","Days":30}}}'
  aws s3api get-object-lock-configuration --bucket my-locked-bucket
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  ```bash
  rc bucket lock set --mode governance --days 30 cellar/my-locked-bucket
  rc bucket lock info cellar/my-locked-bucket
  ```

  {{< /tab >}}

{{< /tabs >}}

Object Lock has two retention modes:

- **Governance**: only requests that bypass this mode can delete a version or shorten its retention
- **Compliance**: no request can delete a version or shorten its retention before it expires

To bypass the governance mode, add these options to your commands. s3cmd can't bypass it.

- AWS CLI: `--bypass-governance-retention`
- rclone: `--s3-bypass-governance-retention`
- RustFS CLI: `--bypass`

Replacing an object or deleting it without a version ID keeps the protected version, which you can restore.

### Protect a version

The default retention applies to the versions you upload after setting it. To protect an existing version, set its own retention, until a date of your choice. The RustFS CLI fails on this operation with Cellar.

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  ```bash
  s3cmd setobjectretention GOVERNANCE 2027-12-31T00:00:00Z s3://my-locked-bucket/report.pdf
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  Add `--version-id` to protect another version than the latest one:

  ```bash
  aws s3api put-object-retention \
    --bucket my-locked-bucket \
    --key report.pdf \
    --retention '{"Mode":"GOVERNANCE","RetainUntilDate":"2027-12-31T00:00:00Z"}'
  aws s3api get-object-retention --bucket my-locked-bucket --key report.pdf
  ```

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  rclone protects the files it uploads, for a duration or until a date:

  ```bash
  rclone copyto \
    --s3-object-lock-mode GOVERNANCE \
    --s3-object-lock-retain-until-date 30d \
    report.pdf cellar:my-locked-bucket/report.pdf
  ```

  {{< /tab >}}

{{< /tabs >}}

### Hold an object without an expiration date

A legal hold protects an object version until you remove it, whatever its retention. These commands set and remove a hold on `report.pdf`:

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  ```bash
  s3cmd setobjectlegalhold ON s3://my-locked-bucket/report.pdf
  s3cmd setobjectlegalhold OFF s3://my-locked-bucket/report.pdf
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  ```bash
  aws s3api put-object-legal-hold --bucket my-locked-bucket --key report.pdf --legal-hold Status=ON
  aws s3api put-object-legal-hold --bucket my-locked-bucket --key report.pdf --legal-hold Status=OFF
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  ```bash
  rc legalhold set cellar/my-locked-bucket/report.pdf
  rc legalhold info cellar/my-locked-bucket/report.pdf
  rc legalhold clear cellar/my-locked-bucket/report.pdf
  ```

  Add `--version-id` to target another version than the latest one.

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  rclone sets a legal hold on the files it uploads. Remove it with another client:

  ```bash
  rclone copyto --s3-object-lock-legal-hold-status ON report.pdf cellar:my-locked-bucket/report.pdf
  ```

  {{< /tab >}}

{{< /tabs >}}

## Server-side encryption with customer keys (SSE-C)

Cellar supports [server-side encryption with customer-provided keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html). You send a 256-bit key for the Advanced Encryption Standard (AES) with each upload and download of an object. Cellar encrypts the object with it, and decrypts it when you read it back, but doesn't keep the key. Without it, nobody can read the object, even with the add-on credentials.

Encryption applies per object, so a bucket can mix objects encrypted with SSE-C and objects stored without it. Supply the same key to `GetObject`, `HeadObject`, and `GetObjectAttributes` requests for an encrypted object. Cellar returns a `400` error if the key is missing or incorrect. For the same reason, a presigned URL alone isn't enough to download an encrypted object.

SSE-C protects the content of an object, not its existence: the add-on credentials still list, overwrite, or delete it without the key.

Cellar only accepts SSE-C requests over HTTPS. It rejects `CopyObject` requests with an SSE-C source, so copies, renames, and moves of encrypted objects can fail. `aws s3 mv` and `rclone moveto` fail on small objects, and only move large ones, which they copy in parts.

A copy request can't change the key of an object either. To rename an encrypted object or change its key, download it, then upload it again.

> [!NOTE] Keep your key safe
> Cellar can't decrypt an object without its key. If you lose the key, you lose access to every object encrypted with it.

Generate a random 32-byte key, encoded in base64:

```bash
openssl rand -base64 32
```

Store it with your application secrets. The following examples read it from an environment variable named `SSE_C_KEY`, which you define yourself. The Java and Rust SDKs also need the MD5 digest of the key: store it in `SSE_C_KEY_MD5`.

```bash
echo "$SSE_C_KEY" | base64 -d | openssl md5 -binary | base64
```

The AWS CLI and the RustFS CLI read the raw key from a file. Decode it into `sse-c.key`, readable only by you, outside your repository:

```bash
touch sse-c.key
chmod 600 sse-c.key
echo "$SSE_C_KEY" | base64 -d > sse-c.key
```

s3cmd doesn't support SSE-C: its `--server-side-encryption` option doesn't take a customer key, and `--encrypt` encrypts files on your machine before the upload. The S3 clients of Bun and V don't support SSE-C either.

{{< tabs >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  These commands use the [`cellar` profile](#configure-an-s3-client). `aws s3` commands take the key file with `--sse-c` and `--sse-c-key`:

  ```bash
  aws s3 cp report.pdf s3://my-bucket/reports/report.pdf --sse-c AES256 --sse-c-key fileb://sse-c.key
  aws s3 cp s3://my-bucket/reports/report.pdf report-downloaded.pdf --sse-c AES256 --sse-c-key fileb://sse-c.key
  aws s3 sync ./reports s3://my-bucket/reports --sse-c AES256 --sse-c-key fileb://sse-c.key
  ```

  `aws s3api` commands name these options differently. For example, read the metadata of an encrypted object with:

  ```bash
  aws s3api head-object \
    --bucket my-bucket \
    --key reports/report.pdf \
    --sse-customer-algorithm AES256 \
    --sse-customer-key fileb://sse-c.key
  ```

  See the AWS CLI documentation for [`aws s3 cp`](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) and [`aws s3api head-object`](https://docs.aws.amazon.com/cli/latest/reference/s3api/head-object.html).

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  These commands use the [`cellar` alias](#configure-an-s3-client) and the key file, including for multipart transfers:

  ```bash
  rc put --enc-c-destination-key-file sse-c.key report.pdf cellar/my-bucket/reports/report.pdf
  rc get --enc-c-source-key-file sse-c.key cellar/my-bucket/reports/report.pdf report-downloaded.pdf
  ```

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  rclone applies SSE-C to a whole remote. Configure a remote with your key to encrypt uploads and decrypt downloads:

  ```bash
  rclone config create cellar-encrypted s3 \
    provider=Cellar \
    access_key_id="$CELLAR_ADDON_KEY_ID" \
    secret_access_key="$CELLAR_ADDON_KEY_SECRET" \
    endpoint="https://$CELLAR_ADDON_HOST" \
    sse_customer_algorithm=AES256 \
    sse_customer_key_base64="$SSE_C_KEY"
  ```

  This remote uses your key for uploads and downloads, including multipart transfers:

  ```bash
  rclone copy --no-update-modtime ./reports cellar-encrypted:my-bucket/reports
  rclone sync --no-update-modtime ./reports cellar-encrypted:my-bucket/reports
  rclone copy cellar-encrypted:my-bucket/reports ./reports-restored
  ```

  `--no-update-modtime` avoids updating the timestamps of unchanged files with `CopyObject` requests, which Cellar rejects for SSE-C objects.

  A remote without the key lists encrypted objects, but fails to read them with a `400` error: see [`sse_customer_key_base64`](https://rclone.org/s3/#s3-sse-customer-key-base64).

  {{< /tab >}}

  {{< tab name="Node.js" icon="simple:nodedotjs" >}}

  This code uses the `s3` client of the [Node.js example](#use-cellar-from-your-application). The SDK takes the key in base64, and computes its MD5 digest:

  ```javascript
  import { readFileSync } from "node:fs";
  import { GetObjectCommand, PutObjectCommand } from "@aws-sdk/client-s3";

  const encryption = { SSECustomerAlgorithm: "AES256", SSECustomerKey: process.env.SSE_C_KEY };

  await s3.send(new PutObjectCommand({
    Bucket: "my-bucket",
    Key: "reports/report.pdf",
    Body: readFileSync("report.pdf"),
    ...encryption,
  }));
  const { Body } = await s3.send(new GetObjectCommand({ Bucket: "my-bucket", Key: "reports/report.pdf", ...encryption }));
  ```

  {{< /tab >}}

  {{< tab name="Java" icon="java" >}}

  This code uses the `s3` client of the [Java example](#use-cellar-from-your-application). Without `sseCustomerKeyMD5`, Cellar rejects the request:

  ```java
  import software.amazon.awssdk.core.sync.RequestBody;

  import java.nio.file.Path;

  String key = System.getenv("SSE_C_KEY");
  String keyMd5 = System.getenv("SSE_C_KEY_MD5");

  s3.putObject(request -> request.bucket("my-bucket").key("reports/report.pdf")
          .sseCustomerAlgorithm("AES256").sseCustomerKey(key).sseCustomerKeyMD5(keyMd5),
      RequestBody.fromFile(Path.of("report.pdf")));
  byte[] report = s3.getObjectAsBytes(request -> request.bucket("my-bucket").key("reports/report.pdf")
          .sseCustomerAlgorithm("AES256").sseCustomerKey(key).sseCustomerKeyMD5(keyMd5))
      .asByteArray();
  ```

  {{< /tab >}}

  {{< tab name="Python" icon="simple:python" >}}

  This code uses the `s3` client of the [Python example](#use-cellar-from-your-application). `upload_file` and `download_file` send the key with each part of large files:

  ```python
  import base64

  encryption = {
      "SSECustomerAlgorithm": "AES256",
      "SSECustomerKey": base64.b64decode(os.environ["SSE_C_KEY"]),
  }

  s3.upload_file("report.pdf", "my-bucket", "reports/report.pdf", ExtraArgs=encryption)
  s3.download_file("my-bucket", "reports/report.pdf", "report-downloaded.pdf", ExtraArgs=encryption)
  ```

  Pass the same `encryption` arguments to `put_object`, `get_object`, and `head_object`: boto3 computes the MD5 digest of the key.

  {{< /tab >}}

  {{< tab name="Ruby" icon="ruby" >}}

  This code uses the `s3` client of the [Ruby example](#use-cellar-from-your-application). The SDK takes the raw key, and computes its MD5 digest:

  ```ruby
  require "base64"

  encryption = { sse_customer_algorithm: "AES256", sse_customer_key: Base64.decode64(ENV.fetch("SSE_C_KEY")) }

  s3.put_object(bucket: "my-bucket", key: "reports/report.pdf", body: File.open("report.pdf"), **encryption)
  s3.get_object(bucket: "my-bucket", key: "reports/report.pdf", response_target: "report-downloaded.pdf", **encryption)
  ```

  {{< /tab >}}

  {{< tab name="Rust" icon="simple:rust" >}}

  This code uses the `s3` client of the [Rust example](#use-cellar-from-your-application). Without `sse_customer_key_md5`, Cellar rejects the request:

  ```rust
  let key = env::var("SSE_C_KEY")?;
  let key_md5 = env::var("SSE_C_KEY_MD5")?;

  s3.put_object()
      .bucket("my-bucket")
      .key("reports/report.pdf")
      .body(ByteStream::from_path("report.pdf").await?)
      .sse_customer_algorithm("AES256")
      .sse_customer_key(&key)
      .sse_customer_key_md5(&key_md5)
      .send()
      .await?;
  let report = s3.get_object()
      .bucket("my-bucket")
      .key("reports/report.pdf")
      .sse_customer_algorithm("AES256")
      .sse_customer_key(&key)
      .sse_customer_key_md5(&key_md5)
      .send()
      .await?;
  ```

  {{< /tab >}}

{{< /tabs >}}

## Delete buckets and the add-on

Cellar only deletes empty buckets. In the **Cellar Explorer**, delete the objects of a bucket first. S3 clients delete the objects and the bucket in one command, but s3cmd and the AWS CLI fail on a versioned bucket. The RustFS CLI and rclone also delete the versions of its objects:

{{< tabs >}}

  {{< tab name="s3cmd" icon="terminal" >}}

  ```bash
  s3cmd rb --recursive s3://my-bucket
  ```

  {{< /tab >}}

  {{< tab name="AWS CLI" icon="aws" >}}

  ```bash
  aws s3 rb --force s3://my-bucket
  ```

  {{< /tab >}}

  {{< tab name="RustFS CLI" icon="terminal" >}}

  ```bash
  rc bucket remove --force cellar/my-versioned-bucket
  ```

  {{< /tab >}}

  {{< tab name="rclone" icon="terminal" >}}

  ```bash
  rclone purge cellar:my-versioned-bucket
  ```

  {{< /tab >}}

{{< /tabs >}}

Versions under a retention or a legal hold block the deletion, and versions in compliance mode block it until they expire. Remove the legal holds, then delete the governance versions with the RustFS CLI or rclone:

```bash
rc object remove --recursive --versions --bypass --force cellar/my-locked-bucket/
rc bucket remove cellar/my-locked-bucket

rclone purge --s3-versions --s3-bypass-governance-retention cellar:my-locked-bucket
```

Delete the add-on at the bottom of its **Add-on dashboard**, or with `clever addon delete`. Clever Cloud deletes its buckets and their objects at least three days later: copy the files you want to keep first.

## Troubleshooting

{{% details title="SSL error with a bucket name that holds dots" closed="true" %}}

s3cmd reaches a bucket at `<bucket-name>.cellar-c2.services.clever-cloud.com` by default. For a name with dots, such as `cdn.example.com`, this host doesn't match the certificate of Cellar, and s3cmd fails with this error:

```text
ERROR: SSL certificate verification failure: [SSL: TLSV1_UNRECOGNIZED_NAME] tlsv1 unrecognized name
```

Add `--host-bucket=cellar-c2.services.clever-cloud.com` to s3cmd commands to use the path style for these buckets. The AWS CLI, the RustFS CLI, and rclone use it by themselves, as do the SDKs of Bun, Node.js, Python, Ruby, and V.

{{% /details %}}

{{% details title="MissingContentLength or 400 errors on uploads" closed="true" %}}

Recent AWS SDKs and AWS CLI versions add checksums that Cellar rejects. Set the checksum options to `when_required`, as the [examples](#use-cellar-from-your-application) show, or set these environment variables, which most AWS SDKs read:

```bash
export AWS_REQUEST_CHECKSUM_CALCULATION=when_required
export AWS_RESPONSE_CHECKSUM_VALIDATION=when_required
```

{{% /details %}}

{{% details title="InvalidBucketName or BucketAlreadyExists when creating a bucket" closed="true" %}}

`InvalidBucketName` means that the name breaks the [naming rules](#create-a-bucket), with uppercase letters or underscores for instance. `BucketAlreadyExists` means that another add-on of the region already uses this name: choose another one.

{{% /details %}}

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/deploy/storage/fs-bucket" title="FS Buckets" subtitle="Mount a persistent file system in your applications" icon="fsbucket" >}}
  {{< card link="/developers/guides/static-sites/hugo-cellar" title="Hugo and Cellar" subtitle="Publish the assets of a Hugo website to Cellar" icon="simple:hugo" >}}
  {{< card link="/developers/doc/deploy/applications/static" title="Static runtime" subtitle="Serve a static website, with index files and your domain over HTTPS" icon="static" >}}
{{< /cards >}}
