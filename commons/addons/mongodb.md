---
title: MongoDB add-on
position: 5
shortdesc: A noSQL and document-oriented database, operated by Clever Cloud.
tags:
- addons
keywords:
- mongo
- mongodb
- document
- nosql
- database
---

MongoDB is an open source NoSQL document-oriented database. We provide these databases with daily backups and monitoring for both shared and dedicated plans.

## MongoDB version

The version currently installed by the add-on is :

- on shared plans (Peanut) : MongoDB 4.0.3
- on newly created dedicated databases (plans Hazelnut and above) : MongoDB 4.0.3

## About Free Databases

Free plans are recommended for test and development usage only. Using these databases in production is not recommended, because performance may vary depending on the global usage of the cluster. Therefore, before switching to production, consider upgrading to a dedicated database for better performance.

### Important Note About Fair Use on Free Databases

Heavy usage of free databases may impact the shared cluster they rely upon. It will degrade performance of the other databases. To that extent, we set a soft limit of **15 operations/second**. Going above the limit will expose your database to disconnection, would you not answer our notices.

## Daily Backups and Retention

By default, Clever Cloud perfoms a free backup every day, with a retention of seven days. Each backup can be found in the add-on dashboard in the web console, along with the credentials.

## Database Migration Process

The migration process is pretty much the same for each of these cases:

- migrating from a Clever Cloud shared database to a dedicated one
- migrating from an external database to a Clever Cloud one
- migrating between Clever Cloud Databases

The process consists in three steps:

1. First, perform a backup and download it, either with the Clever Cloud add-on dashboard or the `mongodump` command from your workstation.
2. Install `mongorestore` (a tool packaged with [MongoDB](https://docs.mongodb.com/manual/administration/install-community/))
3. On your workstation, use the taylor-made `mongorestore` command line located in your mongodb dashboard page. If needed, change the `nsFrom` and `nsTo` flags, depending on what you actually want to do (importing this database in another, importing another to this one, ...)


## MongoDB plans

<table class="table table-bordered table-striped dataTable"><caption>MongoDB pricing plans</caption>
<tr>
<th>Name</th>
<th>Disk</th>
<th>Cache (Memory)</th>
<th>Price /mo</th>
</tr>
<tr>
<td class="cc-col__price "><span class="label cc-label__price label-info">Peanut</span></td>
<td>500 MB</td>
<td>SHARED</td>
<td>Free</td>
</tr>
<tr>
<td class="cc-col__price "><span class="label cc-label__price label-info">Hazelnut</span></td>
<td>1 GB</td>
<td>512 MB</td>
<td>20.00€</td>
</tr>
<tr>
<td class="cc-col__price "><span class="label cc-label__price label-info">Shamrock</span></td>
<td>5 GB</td>
<td>1 GB</td>
<td>40.00€</td>
</tr>
<tr>
<td class="cc-col__price "><span class="label cc-label__price label-info">Vine</span></td>
<td>30 GB</td>
<td>2 GB</td>
<td>75.00€</td>
</tr>
<tr>
<td class="cc-col__price "><span class="label cc-label__price label-info">Gunnera</span></td>
<td>100 GB</td>
<td>4 GB</td>
<td>150.00€</td>
</tr>
</table>

## Encryption at rest

MongoDB dedicated addons can be encrypted using LUKS with `aes-xts`.

The passphrase is encrypted in our database using Cipher and Nonce as bytes arrays.

To enable it, you need to ask to our support then we will perform invoicing configuration (more informations about pricing are available through support) and enable the encryption for your addon. Once it's done, you will need to migrate your addon then the encryption at rest will be up.
