---
type: docs
title: Zone Migration
tags:
- migration
- zone
- application
- addon
type: docs
---

In this document, we will see how you can migrate your Clever Cloud services from one zone to another zone, for example from Paris to Montreal.
For most of the services, you will be able to migrate them as-is. For others, you will need to create them and do a manual migration.
Keep in mind that our support team remains available, should you have any questions regarding zone migration.

## Application migration

Most of the applications will migrate without issues. If one of your applications matches any criteria is in the list below, you will need extra steps
described in the following sub-sections.

- Any application that uses a FSBucket add-on
- PHP applications

In this case, please read the prerequisites below first and then follow the right sub-section.

### Prerequisites

Besides redeploying your application in your target zone, you have to keep a few things in mind:

- Increased latency might be observed during DNS propagation (more below)
- You will need to update your DNS settings, so make sure you have access to your DNS registrar

One of the first things you can do is to lower your DNS records TTL (time to live). In order to speed up the DNS propagation during the update of your domains DNS records.

On your registrar's interface, find your application's domain. Usually, the DNS record will be `domain.tld IN CNAME domain.<current-zone>.clever-cloud.com` with a certain TTL.
Edit that TTL to 60 seconds instead of the existing value, and wait for this change to propagate (wait as much time as the old TTL value). This change will allow a faster DNS propagation when
you have to update the `CNAME` record value to `domain.<target-zone>.clever-cloud.com`, lowering the amount of time your users will experience an increased latency.

{{< callout type="info" >}}
After the migration, you can set back your old TTL value.
{{< /callout >}}

#### Increased latency

Once your application has been redeployed to your target zone, your application's domain will still have its DNS pointing to the old zone. As a consequence, the
latency may increase for your users. For example, if you are migrating from Paris (PAR) to Montreal (MTL), your visitors will connect to our Paris infrastructure, which will
then redirect the traffic to our Montreal infrastructure, leading requests to take more time.

You might also experience an increased latency between your application and other services (like a PostgreSQL add-on for example). If your application has switched to the Montreal zone
and your PostgreSQL add-on is still in Paris, your application will need extra time to query the database.

#### DNS updates

Once your application has been migrated to your target zone, you will find in the `Domain names` section the new `A` and `CNAME` DNS records to use for your application's domains.
If you were using `A` records, update the records (there might be more or fewer of them than what you had previously, this is normal). If you used a `CNAME` record, simply change the value.

Once done, it will take as much time to propagate as the TTL defined for that record. If you followed the prerequisites above, it should take a few minutes tops.

### Migration

If your application doesn't match any criteria of the list in the `Application migration` section, then you can go to the `Information` pane of your application. Under the `Zone` label, chose your target zone.
Once selected, you can save your changes using the `Save` button at the bottom of the page.

After saving, you can now redeploy your application in the `Overview`, it will redeploy on the new zone.

### Applications using an FSBucket

FSBuckets can only be mounted by applications on the same zone. This means that you cannot use an FSBucket add-on hosted in Paris, if your application is in Montreal.

To migrate FSBuckets, see the [section below](#fsbucket).

### PHP Applications

Because of technical reasons, a PHP application can not be migrated to another zone. In this case, you will have to re-create the application.
When domains are switched from the old application to the new one, a small downtime may occur. 404 or 503 errors might happen for a few seconds.

First, create a new PHP application on your target zone.
Then, you can easily copy / paste the environment variable from the old application to the new one using the `Expert mode` of our environment variables interface.
Don't forget to link all services that were linked to your old application. Linking multiple times the same service to different application doesn't cause any issue.
Make sure the Scalability section of your application is the same as the old one, as well as the various options you can find in the `Information pane` (HTTPS redirection, build cache, …).

Once everything is setup again, we can push the code. If you are using Git, you can find the new Git URL in the `Information` panel.
If you are using FTP, please read the [FSBucket migration section](#fsbucket).

Your new application should now be deployed. You can update the domain names: for each domain of your old application, delete it and add it to the new application.

You can use the CLI to do it and minimize the downtime:

```shell
clever -a <old-application-alias> domain rm <domain>; clever -a <new-application-alias> domain add <domain>
```

You can now update your DNS as described in the [DNS updates](#dns-updates) section.

## Add-on migration

Add-ons can be migrated from one zone to another. For some of them, our support team can help you do it.

### PostgreSQL, MySQL, MongoDB, Redis

You can migrate these add-ons using the [Migration Tool]({{< ref "/doc/administrate/database-migration" >}}).

Once your migration is over, the services connecting to the add-on might be impacted by an increased latency due to DNS updates. The domain of your add-on will have its DNS records
changed but it will take up to 1 hour for them to propagate. This means that during that time, your services might still connect to the old zone, which will then redirect to the target zone
where your database has been migrated.

### Jenkins, Elasticsearch, Cellar, Pulsar

These add-ons can not be automatically migrated across zones. Please reach out to our support team so we can assist you further for this migration.

### FSBucket

FSBuckets can not be migrated across zones either. You will have to create a new FSBucket in the target zone and transfer its content from the old to the new one.

To do so, you can use the [LFTP](https://lftp.yar.ru/) or [Rclone](https://rclone.org/) tools. Or you can ask our support team and we will be able to do it for you.

{{< callout type="warning" >}}
In case of a FSBucket add-on (and not a PHP+FTP add-on), remember to link it to your application once it has been migrated to the new zone.
{{< /callout >}}
