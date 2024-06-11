---
type: docs
title: MongoDB
position: 5
shortdesc: A noSQL and document-oriented database, operated by Clever Cloud.
aliases:
- /../addon/mongodb
tags:
- addons
keywords:
- mongo
- mongodb
- document
- nosql
- database
aliases:
- /doc/deploy/addon/mongodb/mongodb
- /doc/deploy/addon/mongodb/managing-mongodb
type: docs
---
## Overview

MongoDB is an open source NoSQL document-oriented database. We provide these databases with daily backups and monitoring for both shared and dedicated plans.

### Supported versions

In order to comply with [MongoDB Server Side Public License](https://www.mongodb.com/licensing/server-side-public-license), the version currently installed by the add-on is:

{{< software_versions_shared_dedicated mongo>}}

### Higher Versions

If you puchased a higher version from MongoDB and you want to deploy your database on Clever Cloud, please [contact us](https://www.clever-cloud.com/contact/).

## About Free Databases

Free plans are recommended for test and development usage only. Using these databases in production is not recommended, because performance may vary depending on the global usage of the cluster. Therefore, before switching to production, consider upgrading to a dedicated database for better performance.

### Important Note About Fair Use on Free Databases

Heavy usage of free databases may impact the shared cluster they rely upon. It will degrade performance of the other databases. To that extent, we set a soft limit of **15 operations/second**. Going above the limit will expose your database to disconnection, would you not answer our notices.

{{% content/db-backup %}}

## Database Migration Process

The migration process is pretty much the same for each of these cases:

- migrating from a Clever Cloud shared database to a dedicated one
- migrating from an external database to a Clever Cloud one
- migrating between Clever Cloud Databases

The process consists in three steps:

1. First, perform a backup and download it, either with the Clever Cloud add-on dashboard or the `mongodump` command from your workstation.
2. Install `mongorestore` (a tool packaged with [MongoDB](https://docs.mongodb.com/manual/administration/install-community/))
3. On your workstation, use the taylor-made `mongorestore` command line located in your mongodb dashboard page (open the "Backup" panel and click on the "Restore" link to find the complete command line to perform the database import). If needed, change the `nsFrom` and `nsTo` flags, depending on what you actually want to do (importing this database in another, importing another to this one, ...).

## Encryption at rest

Encryption at rest is available on MongoDB. You can have more information on the [dedicated page]({{< ref "doc/administrate/encryption-at-rest.md" >}})

## Can I use Mongo Ops Manager on Clever Cloud?

To be able to use [Mongo Ops Manager](https://www.mongodb.com/products/ops-manager), you'll need a valid MongoDB Enterprise Advanced subscription and to deploy a [Linux version of their manager solution](https://www.mongodb.com/try/download/ops-manager). If you haven't purchased any license from MongoDB and you are using the Community version, you might be looking for a similar service for your databases.

### Does Clever Cloud provide a similar service?

The features available with Mongo Ops Manager could be relevant if you managed your infrastructure and the maintenance of your MongoDB databases yourself. However, if you use Clever Cloud to access our Mongo add-ons, you are already opting for a managed service, and will therefore benefit from the following features similar to Mongo Ops Manager:

- **A centralized interface** to access your database settings and perform operations on them.
- **A monitoring and alert system** that can be configured with Grafana (an example with Slack alerts can be found [here](https://www.clever-cloud.com/blog/features/2021/12/03/slack-alerts-for-grafana/)).
- **A backup and restore system** already configured for our add-ons (customizable upon request) with easy migration and one-click importation.
- The ability to **automate tasks** with our CLI.
- **Enhanced security** through our default access management on Clever Cloud (encryption at rest, default unauthorized super admin operations, etc.).

Note that these features are available for all our databases add-ons, in addition to MongoDB.

**The managed databases provide an advantage if you want to avoid the complexity of installing and deploying databases** and if you want simple-to-use management and monitoring tools.

{{% content/managed-services %}}
