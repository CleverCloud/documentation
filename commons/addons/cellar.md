---
title: Cellar, a S3-like object storage service
position: 3
shortdesc: Cellar is a Amazon S3-compatible file storage system created and hosted by Clever Cloud.
tags:
- addons
keywords:
- S3
- amazon
- Storage
- file
- files
---

Cellar is S3-compatible online file storage web service. You can use it with
your favorite S3 client.

To manually manage the files, you can use [s3cmd](http://s3tools.org/s3cmd).
You can download a s3cmd configuration file from the add-on configuration
page.

## Clever Cloud Cellar plans

<table class="table table-bordered table-striped dataTable"><caption>Cellar storage plans</caption>
<tr>
<th>Storage</th>
<th>Price / GB / mo</th>
<th>Price / TB / mo</th>
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

<table class="table table-bordered table-striped dataTable"><caption>Cellar trafic usage plans</caption>
<tr>
<th>Traffic (outbound)</th>
<th>Price / GB / mo</th>
<th>Price / TB / mo</th>
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

To create a bucket, you can use s3cmd:

```bash
    s3cmd mb s3://bucket-name
```
You can list files

```bash
    s3cmd ls s3://bucket-name
```

You can upload files (`--acl-public` makes the file readable by everyone).

```bash
    s3cmd put --acl-public image.jpg s3://bucket-name
```

### Using a custom domain

If you want to use a custom domain, for example cdn.example.com, you need to create a bucket named exactly like your domain:

```bash
    s3cmd mb s3://cdn.example.com
```

Then, you just have to create a CNAME record on your domain pointing to `cellar-c2.services.clever-cloud.com.`.

<div class="panel panel-warning">
  <div class="panel-heading">
    <h4 class="panel-title">S3 signature algorithm</h4>
  </div>
  <div class="panel-body">
    Cellar doesn't support the `v4` signature algorithm from S3. Please make sure
    your client is configured to use the `v2` signature algorithm. The
    s3cmd configuration file provided on the add-on configuration page already has it.
  </div>
</div>

## Using AWS SDK

To use cellar from your applications, you can use the [AWS SDK](https://aws.amazon.com/tools/#sdk).
You only need to specify a custom endpoint (eg `cellar.services.clever-cloud.com`) and to
force the use of the version 2 of the request signer.

### Node.js

```javascript
var AWS = require('aws-sdk');

AWS.config.update({accessKeyId: '<cellar_key_id>', secretAccessKey: '<cellar_key_secret>'});
var ep = new AWS.Endpoint('<cellar_host>');
var s3 = new AWS.S3({ endpoint: ep, signatureVersion: 'v2' });

s3.listBuckets(function(err, res) {
  // handle results
});

/* In order to share access to access non-public files via HTTP, you need to get a presigned url for a specific key
 * the example above present a 'getObject' presigned URL. If you want to put a object in the bucket via HTTP,
 * you'll need to use 'putObject' instead.
 * see doc : http://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#getSignedUrl-property
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
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.s3.AmazonS3Client;
import java.net.URL;

public class Main {
    public static void main(String[] argv) {
        ClientConfiguration opts = new ClientConfiguration()
        opts.setSignerOverride("S3SignerType"); // Force the use of V2 signer
        AmazonS3Client s3Client = new AmazonS3Client(new BasicAWSCredentials("<key>", "<secret>"), opts);
        s3Client.setEndpoint("<host>");
        // Use path style access to avoid java-related SNI issues
        S3ClientOptions s3ClientOptions = new S3ClientOptions().withPathStyleAccess(true);
        s3Client.setS3ClientOptions(s3ClientOptions);
        List<> buckets = s3Client.listBuckets();

        // handle results

        /* In order to share access to access non-public files via HTTP, you need to get a presigned url for a specific key
        * the example above present a 'getObject' presigned URL. If you want to put a object in the bucket via HTTP,
        * you'll need to use 'HttpMethod.PUT' instead.
        * see doc : http://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/AmazonS3.html#generatePresignedUrl-java.lang.String-java.lang.String-java.util.Date-com.amazonaws.HttpMethod-
        */
        URL presignedUrl = s3Client.generatePresignedUrl("<YourBucket>", "<YourKey>", <expiration date>, HttpMethod.GET);
    }
}
```
### Python

Based on [this article on dzone](https://dzone.com/articles/look-riak-cs-basho). This has been tested against python 3.6

This script use boto, the old implentation of the aws-sdk in python. Make sure to not use boto3, the API is completely different. For the moment, the host endpoint is `cellar.services.clever-cloud.com` (but check in the clever cloud console).

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
see doc : http://docs.pythonboto.org/en/latest/ref/s3.html#boto.s3.bucket.Bucket.generate_url
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

`force_path_style` must be set to `true` as described in the [Ruby S3 Client documentation](https://docs.aws.amazon.com/sdkforruby/api/Aws/S3/Client.html):

> `:force_path_style` (Boolean) — default: `false` —
> When set to true, the bucket name is always left in the request URI and never moved to the host as a sub-domain.

