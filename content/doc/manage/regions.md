---
type: docs
linkTitle: Regions
title: Regions and Availability Zones
description: Where Clever Cloud hosts your applications and add-ons, from its regions and availability zones to health data hosting, and how to choose or change the region of an application
keywords:
- regions
- zones
- availability zones
- data center
- zone migration
- region migration
- change region
- hds
- data location
- sovereignty
aliases:
- /doc/administrate/zone-migration
- /doc/zone-migration
- /doc/manage/zone-migration
---

Clever Cloud runs your applications and add-ons in several regions, in Europe, North America, Asia, and Oceania. You choose the region of each one at creation, and you can move an application to another region later. In Paris, the `par` region spreads over five availability zones, each one in a different data center. The [infrastructure page](https://www.clever.cloud/infrastructure/) of the Clever Cloud website lists the data centers of each region, and their certifications.

## Available regions

| Region           | Location             | Infrastructure |
| ---------------- | -------------------- | -------------- |
| `par`            | Paris, France        | Clever Cloud   |
| `parhds`         | Paris, France        | Clever Cloud   |
| `scw`            | Paris, France        | Scaleway       |
| `rbx`            | Roubaix, France      | OVHcloud       |
| `rbxhds`         | Roubaix, France      | OVHcloud       |
| `grahds`         | Gravelines, France   | OVHcloud       |
| `ldn`            | London, UK           | IONOS          |
| `wsw`            | Warsaw, Poland       | OVHcloud       |
| `mtl`            | Montreal, Canada     | OVHcloud       |
| `sgp`            | Singapore            | OVHcloud       |
| `syd`            | Sydney, Australia    | OVHcloud       |

The public API lists the regions available to applications:

```bash
curl -s https://api.clever-cloud.com/v4/products/zones \
  | jq -r '.[] | select(.tags | index("for:applications")) | .name'
```

Some organisations also have access to private regions, or are restricted to some regions. To list the regions of an organisation you're a member of, call the same route with its `ownerId` in an authenticated API request, for example through `clever curl`:

```bash
clever curl -s "https://api.clever-cloud.com/v4/products/zones?ownerId=<orgID>" \
  | jq -r '.[] | select(.tags | index("for:applications")) | .name'
```

Each region has its own load balancers, and its own outbound IP addresses. Point your domains to the [DNS records of the region](/doc/manage/domain-names/#configure-the-dns-records) of your application, and allow its [IP address ranges](/doc/network/ip-ranges/) on the external services that filter their clients.

### Health data hosting

The `parhds`, `rbxhds`, and `grahds` regions are certified for health data hosting (HDS). FS Buckets aren't available in these regions: to deploy a PHP application there, set [`CC_PHP_DISABLE_APP_BUCKET=true`](/doc/deploy/applications/php/sessions-emails/#speed-up-or-disable-the-session-fs-bucket), and store its sessions in Redis.

> [!NOTE] HDS contract
> To benefit from certified hosting for health data, you need to deploy in an HDS region and to sign up to a specific contract. This begins with [an initial discussion with the Clever Cloud team](https://www.clever.cloud/fr/hebergement-donnees-de-sante/contact-hds/).

## Choose a region

You set the region of an application or an add-on at creation, in the Console or with the `--region` option of Clever Tools, which defaults to `par`:

```bash
clever create --type node my-app --region rbx
clever addon create postgresql-addon my-database --plan xs_sml --region rbx
```

Each add-on lists the regions it's available in:

```bash
clever addon providers show postgresql-addon
```

Create an application and the add-ons it uses in the same region: each request between two regions adds latency.

The regions available to an organisation can be restricted, for instance to a geographic area or to a hosting environment. The Console only lists the regions available to the selected organisation. To change these restrictions, contact [Clever Cloud support](https://console.clever-cloud.com/ticket-center-choice).

## Move an application

An application keeps its configuration when it moves, and starts its new instances in the target region at its next deployment.

### Before you move

Your add-ons stay in their region. Move your databases with the [migration tool](/doc/develop/database-migration/), which can change their region.

An application mounts an [FS Bucket](/doc/deploy/storage/fs-bucket/) through the private network of its region: it can't mount an FS Bucket of another region. For each FS Bucket it mounts, create a new one in the target region, then transfer the files with a tool such as [LFTP](https://lftp.yar.ru/) or [Rclone](https://rclone.org/). Link the new FS Bucket to the application instead of the previous one. In `CC_FS_BUCKET`, and in its numbered variants such as `CC_FS_BUCKET_1`, replace the host of the previous bucket with the `BUCKET_HOST` of the new one, and keep the mount path.

If the application uses your own domains, their DNS records need to point to the target region after the move. To make this change fast, [lower their time to live (TTL)](/doc/manage/domain-names/#change-the-dns-records-of-a-domain) beforehand, in the DNS zone of your domain provider.

### Change the region

In the Console, open the application, then its **Information** menu. Select the target region in **Zone**, and save. Then, redeploy the application from its **Overview**: its new instances start in the target region, and the previous ones stop.

Clever Tools has no command for this: change the zone with an API call through `clever curl`, then restart the application:

```bash
clever curl -s -X PUT -H "Content-Type: application/json" -d '{"zone":"rbx"}' \
  "https://api.clever-cloud.com/v2/organisations/<orgID>/applications/<appID>"
clever restart --app "<appID>"
```

Members with the Admin, Manager, or Developer role can move an application to the regions available to its organisation.

### Update the domains

The `cleverapps.io` domains of the application follow it to the target region. Your own domains don't: update their DNS records to the [ones of the target region](/doc/manage/domain-names/#configure-the-dns-records), such as a `CNAME` record to `domain.rbx.clever-cloud.com.`, then check them:

```bash
clever domain diag --app "<appID>"
```

Until the DNS change spreads, during the TTL of the records, some visitors still reach the former region. It forwards their requests to the target region, which adds latency until the change reaches them.

### Applications that can't move

Clever Cloud refuses to move PHP applications and applications deployed with FTP or SFTP. A PHP application stores its sessions in an FS Bucket of its region, which it can't reach from another region. Recreate these applications in the target region:

1. Create the application in the target region, with the same runtime, scaling, and options
2. Copy its environment variables, and link its add-ons
3. Deploy its code with Git, or transfer its files with FTP or SFTP
4. Move its domains, then update their DNS records

To copy the environment variables of the previous application to the new one with Clever Tools, before you set any other variable on it:

```bash
clever env --app "<oldAppID>" -F json | jq '.env' | clever env import --json --app "<newAppID>"
```

This command replaces the variables of the new application, and only copies the ones you set: the variables of an add-on come with its link.

To move a domain with the shortest interruption, remove it from the previous application and add it to the new one in the same command:

```bash
clever domain rm "<domain>" --app "<oldAppID>"; clever domain add "<domain>" --app "<newAppID>"
```

During this switch, a few requests can fail with a `404` or `503` status.
