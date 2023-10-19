---
type: docs
title: "Managing your MongoDB"
date: 2023-06-20T15:01:20+02:00
position: 3
shortdesc: Managing your MongoDB database
tags:
- monitoring
- document
- nosql
- database
- managed service
type: docs
---

## Can I use Mongo Ops Manager on Clever Cloud?

To be able to use [Mongo Ops Manager](https://www.mongodb.com/products/ops-manager), you'll need a valid MongoDB Enterprise Advanced subscription and to deploy a [Linux version of their manager solution](https://www.mongodb.com/try/download/ops-manager). If you haven't purchased any license from MongoDB and you are using the Community version, you might be looking for a similar service for your databases.

## Does Clever Cloud provide a similar service?

The features available with Mongo Ops Manager could be relevant if you managed your infrastructure and the maintenance of your MongoDB databases yourself. However, if you use Clever Cloud to access our Mongo add-ons, you are already opting for a managed service, and will therefore benefit from the following features similar to Mongo Ops Manager:

- **A centralized interface** to access your database settings and perform operations on them.
- **A monitoring and alert system** that can be configured with Grafana (an example with Slack alerts can be found [here](https://www.clever-cloud.com/blog/features/2021/12/03/slack-alerts-for-grafana/)).
- **A backup and restore system** already configured for our add-ons (customizable upon request) with easy migration and one-click importation.
- The ability to **automate tasks** with our CLI.
- **Enhanced security** through our default access management on Clever Cloud (encryption at rest, default unauthorized super admin operations, etc.).

Note that these features are available for all our databases add-ons, in addition to MongoDB.

**The managed databases provide an advantage if you want to avoid the complexity of installing and deploying databases** and if you want simple-to-use management and monitoring tools.
