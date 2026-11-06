---
type: docs
linkTitle: Immutable infrastructure
title: Immutable infrastructure
description: Clever Cloud never updates a running instance, it replaces it. Learn what triggers a replacement, what persists, and how to build applications for this model
keywords:
- immutable infrastructure
- instances
- deployment
- persistence
- rollback
- paas
---

On Clever Cloud, you don't administer servers: the platform runs your application on instances it creates and replaces. It never updates a running instance: it starts new ones from your runtime image and your code, then stops the old ones. This is immutable infrastructure.

## What replaces an instance

- **A deployment**: a push, a restart, or a redeployed commit. With [zero downtime deployment](/doc/manage/#zero-downtime-deployment), the new instances get the traffic once they pass the [health check](/doc/manage/healthcheck/), then the old ones stop. Without it, the old instances stop first.
- **A change of size** that you or [autoscaling](/doc/manage/scaling/) trigger. Changing the number of instances doesn't replace the others.
- **A maintenance or an image update**, when Clever Cloud moves your application to a new runtime image, with updated packages
- **The monitoring**, when an instance stops answering

The [activity](/doc/manage/activity/) of your application lists each of these deployments.

## What persists

Your code, your [environment variables](/doc/manage/environment-variables/), the data of your add-ons, and files in an [FS Bucket](/doc/deploy/storage/fs-bucket/) or [Cellar Object Storage](/doc/deploy/storage/cellar/) persist.

What only exists on an instance disappears with it: files written on its disk, packages installed by hand, changes made through [SSH](/doc/develop/ssh-access/), and data in memory. Sessions kept in memory, for instance, log your users out when their instance is replaced.

## Build for this model

- Keep your configuration in environment variables, and install your tools during the build, with [deployment hooks](/doc/manage/build-hooks/) or [Mise](/doc/develop/mise/)
- Store your data and your sessions outside the instance, in add-ons, an FS Bucket, or Cellar Object Storage
- Start fast to shorten each replacement: with zero downtime deployment, old instances serve until the new ones are healthy
- Debug an instance through SSH if you need to, then bring the fix to your code and redeploy
- To roll back, redeploy a previous commit from the activity of your application
