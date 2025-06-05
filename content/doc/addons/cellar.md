---
type: docs
title: Cellar, S3-compatible object storage service
linkTitle: Cellar Object Storage
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
  Cellar is a S3-compatible online file storage web service. Use it with your favorite S3 client, or download the `s3cmd` configuration file from the add-on dashboard in Clever Cloud console.

{{< /hextra/hero-subtitle >}}

## Creating a bucket

Cellar stores files in buckets. When you create a Cellar add-on, no bucket exists yet.

### From Clever Cloud Console

{{% steps %}}

#### Go to Cellar options

Click on your Cellar add-on in your deployed services list to see its menu.

#### Name your bucket

From **Add-on Dashboard**, insert the name of your bucket.

{{< callout type="info">}}
  Buckets' names are global for every region. **You can't give the same name to two different buckets in the same region**, because the URL already exists in the Cellar cluster on this region. bucket names can't use underscores `(_)`.
{{< /callout >}}

#### Create bucket

Click on **Create bucket**. Your new bucket should appear in the list below.

{{% /steps %}}

### With s3cmd

{{% steps %}}

#### Install s3cmd

Install s3cmd on your machine following [these recommendations](https://s3tools.org/s3cmd).

#### Download the configuration file

Go to your add-on menu in the Clever Cloud console. Under the **Add-on Dashboard**, click the *Download a pre-filled s3cfg file.* link. This provides you a configuration file that you need to add to your home on your machine.

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

There are several ways to manage your buckets, find in this section a list of options.

### Using S3 clients

Some clients allows you to upload files, list them, delete them, etc, like:

- [Cyberduck](https://cyberduck.io)
- [Filestash](https://www.filestash.app/)
- [MinIO](https://min.io/docs/minio/linux/reference/minio-mc.html)
- [S3 Browser](https://s3browser.com/)
- [WinSCP](https://winscp.net)

This list isn't exhaustive. Feel free to [suggest other clients that you would like to see in this documentation](https://github.com/CleverCloud/documentation/discussions/new?category=general).

### Using s3cmd command line tools

`s3cmd` allows you to manage your buckets using its commands, after [configuring it on your machine](#with-s3cmd)

{{< tabs items="Upload,List" >}}

  {{< tab >}}
  You can upload files (`--acl-public` makes the file publicly readable) with:

  ```bash
  s3cmd put --acl-public image.jpg s3://bucket-name
  ```

  The file is then publicly available at `https://<bucket-name>.cellar-c2.services.clever-cloud.com/image.jpg`.
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

  This script uses boto, the old implementation of the aws-sdk in python. The host endpoint is `cellar-c2.services.clever-cloud.com` (verify the `CELLAR_ADDON_HOST` variable value in the Clever Cloud console, from the **Information** option).

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

## Policies

Cellar allows you to create policies to control the actions on your buckets. Find below two policies examples, and [further documentation](https://docs.ceph.com/en/latest/radosgw/bucketpolicy/).

### Public bucket policy

You can upload all your objects with a public ACL, but you can also make your whole bucket publicly available in read mode. No one can access the write permission without authentication.

{{< callout type="warning" >}}
  This makes all of your bucket's objects publicly readable. Be careful that there aren't objects you don't want publicly exposed.
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

💡 If you encounter errors, you might need to specify the [configuration file path](#download-the-configuration-file):

```bash
s3cmd setpolicy ./policy.json -c path/to/s3cfg.txt s3://<bucket-name>
```

All of your objects should now be publicly accessible.

If needed, you can delete this policy by using:

```bash
s3cmd delpolicy s3://<bucket-name>
```

The original ACL should apply to all of your objects after that.


### IP restrictions

If you need to restrict your S3 Cellar to certain IPs, you can use a policy.
To do so, you can use the template below in a `policy.json` file. This example show how to block actions from any IP that isn't `192.168.1.6`.

- Replace the `<bucket-name>` with your bucket name in the policy file.
- Change the `Effect` to `Allow` or `Deny` depending on your needs.
- Change the IP address under `Condition` to select which IP should trigger the rule.

```json {filename="IP-restriction-policy.json"}
{
    "Version": "2012-10-17",
    "Id": "S3PolicyIPRestrict",
    "Statement": [
        {
            "Sid": "IPAllow",
            "Effect": "Deny",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::<bucket>",
                "arn:aws:s3:::<bucket>/*"
            ],
            "Condition" : {
                "IpAddress" : {
                    "aws:SourceIp": ["0.0.0.0/0"]
                },
                "NotIpAddress": {
                    "aws:SourceIp": ["192.168.1.6/32"]
                }
            }
        }
    ]
}
```

To apply the policy, use this command:
```
s3cmd setpolicy ./policy.json s3://<bucket-name>
```

To delete the policy, use this command:
```
s3cmd delpolicy ./policy.json s3://<bucket-name>
```

### User access

Cellar doesn't natively support creating different user accesses for the same add-on. Granting access to your Cellar add-on grants full access to all of your buckets. To grant limited access to a bucket, do the following:

1. Create your main Cellar add-on (we'll call it `Cellar-1`)
2. Download `Cellar 1` s3cfg file
3. Create a second Cellar add-on (we'll call it `Cellar-2`)
4. Get the `ADDON ID` from `Cellar-2` dashboard (it should look like `cellar_xxx`)
5. Create a policy for `Cellar-1` and inject the `ADDON ID` from `Cellar-2` as the user.

Now, you can pass `Cellar-2` credentials to a third party to grant read-only access to `Cellar-1` buckets.

#### Read-only policy example

This policy example grants read-only access to a bucket for another user, using the preceding procedure.

```json {filename="read-only-policy.json"}
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": [
          "s3:GetObject",
          "s3:ListBucket"
        ],
        "Effect": "Allow",
        "Resource": "arn:aws:s3:::<bucket-name>/*",
        "Principal": {"AWS": "arn:aws:iam::cellar_xxx"}

      }
    ]
  }

```

Replace the `<bucket-name>` with your bucket name in the policy file.

Set the policy to your bucket using s3cmd:

```bash
s3cmd --config=<path/to/s3cfg-file> setpolicy ./policy.json s3://<bucket-name>
```

💡Download the [configuration file from Clever Cloud](#download-the-configuration-file):

```bash
s3cmd setpolicy ./policy.json -c path/to/s3cfg.txt s3://<bucket-name>
````

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

**Updating the CORS configuration replaces the old one:** if you update your CORS configuration, the new configuration replaces the old one. Be sure to save it before you update it if you ever need to roll back.

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

## Versioning

### What is bucket versioning

Versioning enables you to store multiple versions of an object in your bucket. When you upload a file with the same name as an existing one, Cellar automatically saves the previous version of that object. This safeguards your data against accidental actions, such as deleting a file by mistake.

Only the latest version of a file is visible, while previous versions remain hidden but securely stored in the bucket. This ensures you can easily restore an earlier version if needed.

### How does versioning work

Versioning can't be enabled for a single file: it will cover the entire bucket.
A bucket can be in one of three state :

 - Unversioned (The default)
 - Versioning-enabled
 - Versioning-suspended

You enable and suspend versioning at the bucket level. Once you enable versioning on a bucket, it can never return to an unversioned state. But you can suspend versioning on that bucket at any time. 
Once versioning is enabled, any object you add have a unique version ID. Object that were already existing before enabling versioning have a version ID of `null`.

For that reason, we do recommend you to enable versioning when creating a new bucket. It will be easier to navigate through version IDs.

> [!WARNING]
> Versioning can quickly take up a lot of space since multiple version of an object are stored in the bucket.  

{{< tabs items="MinIO,  AWS CLI" >}}

  {{< tab >}}
  
  To use [minIO](https://min.io/docs/minio/linux/reference/minio-mc.html#command-mc), you must create an alias.

  ```sh
  mc alias set <ALIAS_NAME> https://cellar-c2.services.clever-cloud.com <ACCESS_KEY> <SECRET_KEY>
  ```

  ### Activate versioning with MinIO

  To activate versioning, you can use MinIO and the following command.

  ```sh
  mc version enable <alias>/<bucket-name>
  ```

  If you want to suspend versioning, you can replace `enable` by `suspend`

  You can check that versioning is enabled for your bucket with :

  ```sh
  mc version info <alias>/<bucket-name> --json
  ```

  ### How to use versioning

When versioning is enabled, the newly added object is automatically provided with a unique identifier. Only the latest version of an object is shown with a `mc ls <alias>/<bucket-name>`.

  #### List versioned objects

  If you need to list all the object in your bucket, including the different versions of the files stored in it, you can run : 

  ```sh
  mc ls --versions --recursive <alias>/<bucket-name>
  ```

  You can list all the version of a specific file with 

  ```sh
  mc ls --versions <alias>/<bucket-name>/<object_name>
  ```

  #### Get a version of an object 

  You can get the specific version of an object using its version ID obtained using the previous command.

  ```sh
  mc get --vid <version_id> <alias>/<bucket-name>/<object_name> <path/to/save/file>
  ```

  #### Delete a version of an object 

  You can delete the specific version of an object using its version ID.

  ```sh
  mc rm --vid <version_id> <alias>/<bucket-name>/<object_name>
  ```


  {{< /tab >}}

  {{< tab >}}

  The following command assumes you have configured your AWS CLI and added an alias as shown earlier in the section [Creating a bucket with AWS CLI](https://www.clever-cloud.com/developers/doc/addons/cellar/#with-aws-cli)

  ### Activate versioning with AWS CLI

  To activate versioning, you can use AWS CLI. You can use the following command to enable it on a bucket.

  ```sh
  aws s3api put-bucket-versioning --bucket <bucket_name> --versioning-configuration Status=Enabled
  ```

  If you want to turn off versioning, you can use the following:
  
```sh
  aws s3api put-bucket-versioning --bucket <bucket_name> --versioning-configuration Status=Suspended

  You can check if versioning is enabled on your bucket with :

  ```sh
  aws s3api get-bucket-versioning --bucket <bucket_name>
  ```

  ### How to use versioning

  When versioning is enabled, the added object automatically gets a versionID. Only the latest version of an object if shown.

  #### List all versioned Object

  If you need to list all the objects in your bucket, including the different versions of the files stored in it, you can use : 

  ```sh
  aws s3api list-object-versions --bucket <bucket_name>
  ```

  #### List all the version of a specific Object

  If you want to check the different versions of a specific object, you can use the following command. In this example, we find the versions of test.txt :

  ```sh
  aws s3api list-object-versions --bucket <bucket_name> --prefix <file_name>
  ```

  #### Get the version of an Object

  If you want to retrieve the previous version of an object, you need the versionID that you can get with any of the two previous command. You can use :

  ```sh
  aws s3api get-object --bucket <bucket_name> --version-id '<version_id>' --key <file_name> /path/to/save/file/copy/test.txt
  ```

  #### Delete the version of an object

  To remove a version of an object, you can use this command : 

  ```sh
  aws s3api delete-object --bucket <bucket_name> --version-id '<version_id>' --key <file_name>
  ```

{{< /tab >}}

{{< /tabs >}}

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
