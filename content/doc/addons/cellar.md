---
type: docs
title: Cellar, a S3-like object storage service
position: 3
shortdesc: Cellar is an Amazon S3-compatible file storage system created and hosted by Clever Cloud.
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

Cellar is S3-compatible online file storage web service. You can use it with your favorite S3 client.

To manually manage the files, you can use [s3cmd](https://s3tools.org/s3cmd). You can download a s3cmd configuration file from the add-on configuration page.

{{< callout type="warning">}}
  `ws-*` and `cf*` commands are not avaible with a Cellar add-on.
{{< /callout >}}

## Creating a bucket

In Cellar, files are stored in buckets. When you create a Cellar addon, no bucket is created yet.

You will need to install the s3cmd on your machine following [these recommendations](https://s3tools.org/s3cmd).

Once s3cmd is installed, you can go to your add-on menu in the Clever Cloud console.

Under the **Addon Dashboard**, click the *Download a pre-filled s3cfg file.* link.

This will provide you a configuration file that you just need to add to your home on your machine.

To create a bucket, you can use s3cmd:

```bash
s3cmd mb s3://bucket-name
```

The bucket will now be available at `https://<bucket-name>.cellar-c2.services.clever-cloud.com/`.

You can upload files (`--acl-public` makes the file publicly readable):

```bash
s3cmd put --acl-public image.jpg s3://bucket-name
```

The file will then be publicly available at `https://<bucket-name>.cellar-c2.services.clever-cloud.com/image.jpg`.

You can list the files in your bucket, you should see the `image.png` file:

```bash
s3cmd ls s3://bucket-name
```

### Using a custom domain

If you want to use a custom domain, for example `cdn.example.com`, you need to create a bucket named exactly like your domain:

```bash
s3cmd --host-bucket=cellar-c2.services.clever-cloud.com mb s3://cdn.example.com
```

Then, you just have to create a CNAME record on your domain pointing to `cellar-c2.services.clever-cloud.com.`.

{{< callout type="warning" >}}
  New cellar add-ons supports the `v4` signature algorithm from S3.
  If you are still using an old account (`cellar.services.clever-cloud.com`), please make sure your client is configured to use the `v2` signature algorithm. The `s3cmd` configuration file provided by the add-on's dashboard is already configured.
{{< /callout >}}

#### SSL error with s3cmd

If you created a bucket with a [custom domain name](#using-a-custom-domain) and use `s3cmd` to manipulate it, you will experience this error:

```log
[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1125)
```

The error comes from the host used to make the request, which is build like this `%s.cellar-c2.services.clever-cloud.com`.

For example with a bucket named `blog.mycompany.com`:

Our certificate covers `*.cellar-c2.services.clever-cloud.com` but not `blog.mycompany.com.cellar-c2.services.clever-cloud.com`, which triggers the error.

It can be solved by forcing s3cmd to use path style endpoint with the option `--host-bucket=cellar-c2.services.clever-cloud.com`.


#### Static hosting

You can use a bucket to host your static website, this [blog article](https://www.clever-cloud.com/blog/engineering/2020/06/24/deploy-cellar-s3-static-site/) describe well how it can be done.

Be aware that SPA applications won't work because our proxy serving the bucket needs to find an HTML file that match the route.

For example if your path is `/login` you need to have a file `login.html` because the `index.html` is not the default entrypoint to handle the path.

You may use SSG (Static Site Generated) to  dynamically generate your content during your build.

## Using AWS CLI

You can use the official [AWS cli](https://aws.amazon.com/cli/) with cellar. You will need to configure the `aws_access_key_id`, `aws_secret_access_key` and endpoint.

```bash
aws configure set aws_access_key_id $CELLAR_ADDON_KEY_ID
aws configure set aws_secret_access_key $CELLAR_ADDON_KEY_SECRET
```

Sadly the endpoint cannot be configured globally and has to be given as a parameter each time you use the `aws` cli. Here's an example to create a bucket:

```bash
aws s3api create-bucket --bucket myBucket --acl public-read --endpoint-url https://cellar-c2.services.clever-cloud.com
```

To simplify this, you may want to configure an alias like so:

```bash
alias aws="aws --endpoint-url https://cellar-c2.services.clever-cloud.com"
```

## Using AWS SDK

To use cellar from your applications, you can use the [AWS SDK](https://aws.amazon.com/tools/#sdk).
You only need to specify a custom endpoint (eg `cellar-c2.services.clever-cloud.com`).

### Node.js

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


### Java

Import the AWS SDK S3 library.
With maven, it can be done with the following dependency :

```xml
<dependency>
  <groupId>software.amazon.awssdk</groupId>
  <artifactId>s3</artifactId>
  <version>2.21.35</version>
</dependency>
```

Make sur to use latest version of the `2.X`, new versions are released regularly. See [the AWS Java SDK Documentation](https://github.com/aws/aws-sdk-java-v2/#using-the-sdk) for more details.

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

### Python

This has been tested against python 3.6

This script uses boto, the old implementation of the aws-sdk in python. Make sure to not use boto3, the API is completely different. For the moment, the host endpoint is `cellar-c2.services.clever-cloud.com` (but check in the clever cloud console).

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

### Active Storage (Ruby On Rails)

[Active Storage](https://guides.rubyonrails.org/active_storage_overview.html) can manage various 
cloud storage services like Amazon S3, Google Cloud Storage, or Microsoft Azure Storage. To use Cellar,
you must configure a S3 service with a custom endpoint.

Use this configuration in your `config/storage.yml`:

```yaml
cellar:
  service: S3
  access_key_id: <%= ENV.fetch('CELLAR_ADDON_KEY_ID') %>
  secret_access_key: <%= ENV.fetch('CELLAR_ADDON_KEY_SECRET') %>
  endpoint: https://<%= ENV.fetch('CELLAR_ADDON_HOST') %>
  region: 'us-west-1'
  force_path_style: true
  bucket: mybucket
```

A `region` parameter must be provided, although it is not used by Cellar.
The region value is used to satisfy ActiveStorage and the aws-sdk-s3 gem. Without a region option, an exception will be raised : `missing keyword: region (ArgumentError)`. If region is an empty string you will get the following error: `missing region; use :region option or export region name to ENV['AWS_REGION'] (Aws::Errors::MissingRegionError)`.

`force_path_style` must be set to `true` as described in the [Ruby S3 Client documentation](https://docs.aws.amazon.com/sdkforruby/api/Aws/S3/Client.html).

## Public bucket

You can upload all your objects with a public ACL, but you can also make your whole bucket publicly available in read mode. Writes won't be allowed to anyone that is not authenticated.

{{< callout type="warning" >}}
  This will make all of your bucket's objects publicly available to anyone. Be careful that there are no objects you do not want to be publicly exposed.
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

All of your objects should now be restrained to their original ACL.

## CORS Configuration

You can set a [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) configuration on your buckets if you need to share resources on websites that do not have the same origin as the one you are using.

Each CORS configuration can contain multiple rules. Those are defined using an XML document:

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

- The first rule allows cross-origin requests from the `console.clever-cloud.com` origin. `PUT`, `POST` and `DELETE` methods are allowed to be used by the cross-origin request. Then, all headers specified in the preflight `OPTIONS` request in the `Access-Control-Request-Headers` header are allowed using `AllowedHeaders *`. At the end, the `ExposeHeader` allows the client to access the `ETag` header in the response it received.
- The second one allows cross-origin `GET` requests for all origins. The `MaxAgeSeconds` directive tells the browser how much time (in seconds) it should cache the response of a preflight `OPTIONS` request for this particular resource.

<div class="panel panel-warning">
  <div class="panel-heading">
    <h4 class="panel-title">Updating the `CORS` configuration replaces the old one</h4>
  </div>
  <div class="panel-body">
    If you update your `CORS` configuration, the old configuration will be replaced by the new one. Be sure to save it before you update it if you ever need to rollback.
  </div>
</div>

To view and save your current `CORS` configuration, you can use `s3cmd info`:

```bash
s3cmd -c s3cfg -s info s3://your-bucket
```

You can then set this `CORS` configuration using `s3cmd`:

```bash
s3cmd -c s3cfg -s setcors ./cors.xml s3://your-bucket
```

If you need to rollback, you can either set the old configuration or completely drop it:

```bash
s3cmd -c s3cfg -s delcors s3://your-bucket
```
