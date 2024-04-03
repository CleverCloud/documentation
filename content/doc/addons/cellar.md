---
type: docs
title: Cellar, a S3-like object storage service
description: Cellar is an Amazon S3-compatible file storage system created and hosted by Clever Cloud.
tags:
- addons
keywords:
- S3
- amazon
- Storage
- file
- files
- s3cmd
- aws
aliases:
- /doc/deploy/addon/cellar
type: docs
---
{{< hextra/hero-subtitle >}}
  Cellar is S3-compatible online file storage web service. Use it with your favorite S3 client, or download the `s3cmd` configuration file from the add-on dashboard in Clever Cloud console.

{{< /hextra/hero-subtitle >}}

## Creating a bucket

Cellar stores files in buckets. When you create a Cellar add-on, no bucket exists yet.

### From Clever Cloud Console

{{% steps %}}

#### Go to Cellar options

Click on your Cellar add-on in your deployed services list to see its menu.

#### Name your bucket

From **Addon Dashboard**, insert the name of your bucket.

{{< callout type="info">}}
  Buckets' names are global for every region. **You can't give the same name to two different buckets in the same region**, because the URL already exists in the Cellar cluster on this region.
{{< /callout >}}

#### Create bucket

Click on **Create bucket**. Your new bucket should appear in the list below.

{{% /steps %}}

### With s3cmd

{{% steps %}}

#### Install s3cmd

Install s3cmd on your machine following [these recommendations](https://s3tools.org/s3cmd).

#### Download the configuration file

Go to your add-on menu in the Clever Cloud console. Under the **Addon Dashboard**, click the *Download a pre-filled s3cfg file.* link. This provides you a configuration file that you need to add to your home on your machine.

#### Create a bucket

To create a bucket, you can use this s3cmd command:

```bash
s3cmd mb s3://bucket-name
```

The bucket is now be available at `https://<bucket-name>.cellar-c2.services.clever-cloud.com/`.

{{% /steps %}}

{{< callout type="warning">}}
  `ws-*` and `cf*` commands aren't available with a Cellar add-on.
{{< /callout >}}

### With AWS CLI

You can use the official [AWS cli](https://aws.amazon.com/cli/) with Cellar. Configure the `aws_access_key_id`, `aws_secret_access_key` and endpoint.

```bash
aws configure set aws_access_key_id $CELLAR_ADDON_KEY_ID
aws configure set aws_secret_access_key $CELLAR_ADDON_KEY_SECRET
```

Global endpoint configuration isn't available, so include the parameter each time you use the `aws` cli. Here's an example to create a bucket:

```bash
aws s3api create-bucket --bucket myBucket --acl public-read --endpoint-url https://cellar-c2.services.clever-cloud.com
```

To simplify this, you may want to configure an alias like so:

```bash
alias aws="aws --endpoint-url https://cellar-c2.services.clever-cloud.com"
```

## Managing your buckets

There are several ways to manage your buckets, find here a list of option.

### Using S3 clients

Some clients allows you to upload files, list them, delete them, etc, like:

- [Cyberduck](https://cyberduck.io)
- [Filestash](https://filestash.app)

This list isn't exhaustive. Feel free to [suggest other clients that you would like to see in this documentation](https://github.com/CleverCloud/documentation/discussions/new?category=general).

### Using s3cmd

`s3cmd` allows you to manage your buckets using its commands, after [configuring it on your machine](#with-s3cmd)

{{< tabs items="Upload,List" >}}

  {{< tab >}}
  You can upload files (`--acl-public` makes the file publicly readable) with:

  ```bash
  s3cmd put --acl-public image.jpg s3://bucket-name
  ```
  
  The file is then be publicly available at `https://<bucket-name>.cellar-c2.services.clever-cloud.com/image.jpg`.
  {{< /tab >}}

  {{< tab >}}
  You can list the files in your bucket, you should see the `image.png` file:

  ```bash
  s3cmd ls s3://bucket-name
  ```

  {{< /tab >}}

{{< /tabs >}}

#### Custom domain

If you want to use a custom domain, for example `cdn.example.com`, you need to create a bucket named exactly like your domain:

```bash
s3cmd --host-bucket=cellar-c2.services.clever-cloud.com mb s3://cdn.example.com
```

Then, create a CNAME record on your domain pointing to `cellar-c2.services.clever-cloud.com.`.

{{< callout type="info" >}}
  New cellar add-ons supports the `v4` signature algorithm from S3.
  If you are still using an old account (`cellar.services.clever-cloud.com`), make sure your client configuration uses the `v2` signature algorithm. The `s3cmd` configuration file provided by the add-on's dashboard is already configured.
{{< /callout >}}

## Using AWS SDK

To use cellar from your applications, you can use the [AWS SDK](https://aws.amazon.com/tools/#sdk).
You only need to specify a custom endpoint (eg `cellar-c2.services.clever-cloud.com`).

{{< tabs items="Node.js,Java,Python,Ruby" >}}

  {{< tab >}}
  **Node.js**

  ```javascript
  // Load the AWS SDK for Node.js
  const AWS = require('aws-sdk');

  // Set up config
  AWS.config.update({
    accessKeyId: '<cellar_key_id>', 
    secretAccessKey: '<cellar_key_secret>'
  });

  // Create S3 service object
  const s3 = new AWS.S3({ endpoint: '<cellar_host>' });

  // Create the parameters for calling createBucket
  const bucketParams = {
    Bucket : '<my-bucket-name>',
    CreateBucketConfiguration: {
      LocationConstraint: ''
    }
  };

  // call S3 to create the bucket
  s3.createBucket(bucketParams, function(err, data) {
    // handle results
  });

  // Call S3 to list the buckets
  s3.listBuckets(function(err, res) {
    // handle results
  });

  /* In order to share access to access non-public files via HTTP, you need to get a presigned url for a specific key
   * the example above present a 'getObject' presigned URL. If you want to put a object in the bucket via HTTP,
   * you'll need to use 'putObject' instead.
   * see doc : https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#getSignedUrl-property
   */
  s3.getSignedUrl('getObject', {Bucket: '<YouBucket>', Key: '<YourKey>'})
  ```

  {{< /tab >}}

  {{< tab >}}
  **Java**

  Import the AWS SDK S3 library. Maven uses the following dependency to do so :

  ```xml
  <dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>s3</artifactId>
    <version>2.21.35</version>
  </dependency>
  ```

  Make sure to use latest version of the `2.X`, new versions are released regularly. See [the AWS Java SDK Documentation](https://github.com/aws/aws-sdk-java-v2/#using-the-sdk) for more details.

  Below is a sample Java class, written in Java 21, listing the objects of all buckets :

  ```java
  import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
  import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
  import software.amazon.awssdk.services.s3.S3Client;
  import software.amazon.awssdk.services.s3.model.Bucket;
  import software.amazon.awssdk.services.s3.model.ListObjectsRequest;

  import java.net.URI;
  import java.util.List;

  public class CleverCloudCellarDemoApplication {

      // replace those values with your own keys, load them from properties or env vars
      private static final String CELLAR_HOST = "";
      private static final String CELLAR_KEY_ID = "";
      private static final String CELLAR_KEY_SECRET = "";

      public static void main(String[] args) {
          // initialize credentials with Cellar Key ID and Secret
          // you can also use `EnvironmentVariableCredentialsProvider` by setting AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY env vars
          var credentialsProvider = StaticCredentialsProvider.create(AwsBasicCredentials.create(CELLAR_KEY_ID, CELLAR_KEY_SECRET));

          // create a client builder
          var s3ClientBuilder = S3Client.builder()
                  // override the S3 endpoint with the cellar Host (starting with 'https://'
                  .endpointOverride(URI.create(CELLAR_HOST))
                  .credentialsProvider(credentialsProvider);

          // initialize the s3 client
          try (S3Client s3 = s3ClientBuilder.build()) {
              // list buckets
              List<Bucket> buckets = s3.listBuckets().buckets();
              buckets.forEach(bucket -> {
                  // list bucket objects
                  var listObjectsRequest = ListObjectsRequest.builder().bucket(bucket.name()).build();
                  var objects = s3.listObjects(listObjectsRequest).contents();
                  // handle results
              });

          }
      }
  }
  ```

  See the [AWS Java SDK code examples for S3](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3) for more example use cases.
  {{< /tab >}}

{{< tab >}}
  **Python**

  Tested with Python 3.6.

  This script uses boto, the old implementation of the aws-sdk in python. Make sure to not use boto3, the API is completely different. The host endpoint is `cellar-c2.services.clever-cloud.com` (verify the `CELLAR_ADDON_HOST` variable value in the Clever Cloud console, from the **Information** option).

  ```python
  from boto.s3.key import Key
  from boto.s3.connection import S3Connection
  from boto.s3.connection import OrdinaryCallingFormat

  apikey='<key>'
  secretkey='<secret>'
  host='<host>'

  cf=OrdinaryCallingFormat()  # This mean that you _can't_ use upper case name
  conn=S3Connection(aws_access_key_id=apikey, aws_secret_access_key=secretkey, host=host, calling_format=cf)

  b = conn.get_all_buckets()
  print(b)

  """
  In order to share access to non-public files via HTTP, you need to get a presigned url for a specific key
  the example above present a 'getObject' presigned URL. If you want to put a object in the bucket via HTTP,
  you'll need to use 'putObject' instead.
  see doc : https://docs.pythonboto.org/en/latest/ref/s3.html#boto.s3.bucket.Bucket.generate_url
  """
  b[0].generate_url(60)
  ```

  {{< /tab >}}

  {{< tab >}}
  **Active Storage (Ruby On Rails)**

  [Active Storage](https://guides.rubyonrails.org/active_storage_overview.html) can manage various cloud storage services like Amazon S3, Google Cloud Storage, or Microsoft Azure Storage. To use Cellar,
  you must configure a S3 service with a custom endpoint.

  Use this configuration in your `config/storage.yml`:

  ```yaml {filename="config/storage.yml"}
  cellar:
    service: S3
    access_key_id: <%= ENV.fetch('CELLAR_ADDON_KEY_ID') %>
    secret_access_key: <%= ENV.fetch('CELLAR_ADDON_KEY_SECRET') %>
    endpoint: https://<%= ENV.fetch('CELLAR_ADDON_HOST') %>
    region: 'us-west-1'
    force_path_style: true
    bucket: mybucket
  ```

  Although the `region` parameter appears, it's not used by Cellar. The region value serves to satisfy ActiveStorage and the aws-sdk-s3 gem. Without a region option, an exception would raise : `missing keyword: region (ArgumentError)`. If region is an empty string you will get the following error: `missing region; use :region option or export region name to ENV['AWS_REGION'] (Aws::Errors::MissingRegionError)`.

  Set `force_path_style` to `true` as described in the [Ruby S3 Client documentation](https://docs.aws.amazon.com/sdkforruby/api/Aws/S3/Client.html).
  {{< /tab >}}

{{< /tabs >}}

## Public bucket

You can upload all your objects with a public ACL, but you can also make your whole bucket publicly available in read mode. No one can access the write permission without authentication.

{{< callout type="warning" >}}
  This make all of your bucket's objects publicly readable. Be careful that there aren't objects you don't want to be publicly exposed (like your feet pics collection).
{{< /callout >}}

To set your bucket as public, you have to apply the following policy which you can save in a file named `policy.json`:

```json
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

All of your objects should now be publicly accessible.

If needed, you can delete this policy by using:

```bash
s3cmd delpolicy s3://<bucket-name>
```

The original ACL should apply to all of your objects after that.

## CORS Configuration

You can set a [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) configuration on your buckets if you need to share resources on websites that don't have the same origin as the one you are using.

Each CORS configuration can contain multiple rules, defined in an XML document:

```xml
<CORSConfiguration>
  <CORSRule>
    <AllowedOrigin>console.clever-cloud.com</AllowedOrigin>
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

Here this configuration has two `CORS` rules:

- The first rule allows cross-origin requests from the `console.clever-cloud.com` origin. Allowed cross-origin request methods are `PUT`, `POST` and `DELETE`. Using `AllowedHeaders *` allows all headers specified in the preflight `OPTIONS` request in the `Access-Control-Request-Headers` header. At the end, the `ExposeHeader` allows the client to access the `ETag` header in the response it received.
- The second one allows cross-origin `GET` requests for all origins. The `MaxAgeSeconds` directive tells the browser how much time (in seconds) it should cache the response of a preflight `OPTIONS` request for this particular resource.

{{< callout type="info" >}}

**Updating the CORS configuration replaces the old one**  
If you update your CORS configuration, the new configuration replaces the old one. Be sure to save it before you update it if you ever need to rollback.

{{< /callout >}}

{{% steps %}}

### View and save your current CORS configuration

To view and save your current CORS configuration, you can use `s3cmd info`:

```bash
s3cmd -c s3cfg -s info s3://your-bucket
```

### Set the CORS configuration

You can then set this CORS configuration using `s3cmd`:

```bash
s3cmd -c s3cfg -s setcors ./cors.xml s3://your-bucket
```

If you need to **rollback**, you can either set the old configuration or completely drop it:

```bash
s3cmd -c s3cfg -s delcors s3://your-bucket
```

{{% /steps %}}

## Static hosting

You can use a bucket to host your static website, this [blog post](https://www.clever-cloud.com/blog/engineering/2020/06/24/deploy-cellar-s3-static-site/) describes how to. Be aware that SPA applications won't work because Clever Cloud proxy serving the bucket needs to find an HTML file that match the route.

For example if your path is `/login` you need to have a file `login.html` because the `index.html` isn't the default entrypoint to handle the path.

You may use SSG (Static Site Generated) to  dynamically generate your content during your build.

## Troubleshooting

{{% details title="SSL error with s3cmd" closed="true" %}}

If you created a bucket with a [custom domain name](#using-a-custom-domain) and use `s3cmd` to manipulate it, you will experience this error:

```log
[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1125)
```

The error comes from the host used to make the request, which is build like this `%s.cellar-c2.services.clever-cloud.com`.

For example with a bucket named `blog.mycompany.com`:

Clever Cloud certificate covers `*.cellar-c2.services.clever-cloud.com` but not `blog.mycompany.com.cellar-c2.services.clever-cloud.com`, which triggers the error.

Solve it by **forcing s3cmd to use path style endpoint** with the option `--host-bucket=cellar-c2.services.clever-cloud.com`.
{{% /details %}}

{{% details title="I can't delete a bucket/Cellar add-on" closed="true" %}}

The buckets need to be empty before you can delete them. Solve this error by deleting the content of your bucket using a [bucket management option](#managing-your-buckets).

{{% /details %}}
