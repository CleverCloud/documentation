---
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
---

Cellar is S3-compatible online file storage web service. You can use it with your favorite S3 client.

To manually manage the files, you can use [s3cmd](https://s3tools.org/s3cmd).
You can download a s3cmd configuration file from the add-on configuration page.

## Clever Cloud Cellar plans

<table class="table table-bordered table-striped dataTable"><caption>Cellar storage plans</caption>
<tr>
<th>Storage</th>
<th>Price / GB / month</th>
<th>Price / TB / month</th>
</tr>
<tr>
<td>First 1 TB</td>
<td>€ 0.02</td>
<td>€ 20.48</td>
</tr>
<tr>
<td>Till 25 TB</td>
<td>€ 0.015</td>
<td>€ 15.36</td>
</tr>
<tr>
<td>Till 50 TB</td>
<td>€ 0.01</td>
<td>€ 10.24</td>
</tr>
</table>

<table class="table table-bordered table-striped dataTable"><caption>Cellar traffic usage plans</caption>
<tr>
<th>Traffic (outbound)</th>
<th>Price / GB / month</th>
<th>Price / TB / month</th>
</tr>
<tr>
<td>till 10TB </td>
<td>€ 0.09</td>
<td>€ 92.16</td>
</tr>
<tr>
<td>Till 40 TB</td>
<td>€ 0.07</td>
<td>€ 71.68</td>
</tr>
</table>

## Creating a bucket

In Cellar, files are stored in buckets. When you create a Cellar addon, no
bucket is created yet.

You will need to install the s3cmd on your machine following [these recommendations](https://s3tools.org/s3cmd).
Once s3cmd is installed, you can go to your add-on menu in the Clever Cloud console. Under the **Addon Dashboard**, click the *Download a pre-filled s3cfg file.* link. This will provide you a configuration file that you just need to add to your home on your machine.

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

If you want to use a custom domain, for example cdn.example.com, you need to create a bucket named exactly like your domain:

```bash
    s3cmd mb s3://cdn.example.com
```

Then, you just have to create a CNAME record on your domain pointing to `cellar-c2.services.clever-cloud.com.`.

{{< alert "warning" "S3 signature algorithm" >}}
    New cellar add-ons supports the `v4` signature algorithm from S3.
    If you are still using an old account (cellar.services.clever-cloud.com), please make sure your client is configured to use the `v2` signature algorithm. The s3cmd configuration file provided by the add-on's dashboard is already configured.
{{< /alert >}}

## Using AWS CLI

You can use the official [AWS cli](https://aws.amazon.com/cli/) with cellar. You will need to configure the `aws_access_key_id`, `aws_secret_access_key` and endpoint.

```
aws configure set aws_access_key_id $CELLAR_ADDON_KEY_ID
aws configure set aws_secret_access_key $CELLAR_ADDON_KEY_SECRET
```

Sadly the endpoint cannot be configured globally and has to be given as a parameter each time you use the `aws` cli. Here's an example to create a bucket: `aws s3api create-bucket --bucket myBucket  --acl public-read --endpoint-url https://cellar-c2.services.clever-cloud.com`

To simplify this, you may want to configure an alias like so: `alias aws="aws --endpoint-url https://cellar-c2.services.clever-cloud.com"`.

## Using AWS SDK

To use cellar from your applications, you can use the [AWS SDK](https://aws.amazon.com/tools/#sdk).
You only need to specify a custom endpoint (eg `cellar-c2.services.clever-cloud.com`).

### Node.js

```javascript
const AWS = require('aws-sdk');

AWS.config.update({accessKeyId: '<cellar_key_id>', secretAccessKey: '<cellar_key_secret>'});

const s3 = new AWS.S3({ endpoint: '<cellar_host>' });

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

Make sure to use at least version `1.11.232`. Older versions don't support
Server Name Indication, so if you have SSL certificates errors, check that
you're not using an old version.

```java
import com.amazonaws.ClientConfiguration;
import com.amazonaws.HttpMethod;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.Bucket;
import java.net.URL;
import java.util.List;

public class Main {
    public static void main(String[] argv) {
        ClientConfiguration opts = new ClientConfiguration(); // Only needed for "old" Cellar (V1)
        opts.setSignerOverride("S3SignerType"); // Force the use of V2 signer
        EndpointConfiguration endpointConfiguration = new EndpointConfiguration("<host>", null);
        AWSStaticCredentialsProvider credentialsProvider = new AWSStaticCredentialsProvider(
            new BasicAWSCredentials("<key>", "<secret>"));
        AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
            .withCredentials(credentialsProvider)
            .withClientConfiguration(opts)
            .withEndpointConfiguration(endpointConfiguration)
            .withPathStyleAccessEnabled(Boolean.TRUE)
            .build();

        List<Bucket> buckets = s3Client.listBuckets();

        // handle results

        /* In order to share access to access non-public files via HTTP, you need to get a presigned url for a specific key
        * the example above present a 'getObject' presigned URL. If you want to put a object in the bucket via HTTP,
        * you'll need to use 'HttpMethod.PUT' instead.
        * see doc : https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/AmazonS3.html#generatePresignedUrl-java.lang.String-java.lang.String-java.util.Date-com.amazonaws.HttpMethod-
        */
        URL presignedUrl = s3Client.generatePresignedUrl("<YourBucket>", "<YourFileKey>", <expiration date>, HttpMethod.GET);
    }
}
```
### Python

This has been tested against python 3.6

This script uses boto, the old implentation of the aws-sdk in python. Make sure to not use boto3, the API is completely different. For the moment, the host endpoint is `cellar-c2.services.clever-cloud.com` (but check in the clever cloud console).

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

{{< alert "warning" "Any object will be exposed publicly" >}}
    This will make all of your bucket's objects publicly available to anyone. Be careful that there are no objects you do not want to be publicly exposed.
{{< /alert >}}


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
    <AllowedHeaders>*</AllowedHeaders>
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
```
s3cmd -c s3cfg -s info s3://your-bucket
```

You can then set this `CORS` configuration using `s3cmd`:
```
s3cmd -c s3cfg -s setcors ./cors.xml s3://your-bucket
```

If you need to rollback, you can either set the old configuration or completely drop it:
```
s3cmd -c s3cfg -s delcors s3://your-bucket
```
