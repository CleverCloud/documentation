---
type: docs
linkTitle: Scaling
title: Application scaling
description: Choose the size and the number of instances of your Clever Cloud application, or let autoscaling adapt them to its load
keywords:
- application scaling
- autoscaling
- auto scaling
- horizontal scaling
- vertical scaling
- instance size
- flavor
- instances
aliases:
- /administrate/scalability
- /doc/administrate/instances
- /doc/administrate/scalability
- /doc/clever-cloud-overview/scaling
- /doc/common-configuration/scaling
- /doc/deploy/application/scalability
- /doc/reference/reference-scalability
- /doc/reference/reference-scaling
- /doc/administrate/scaling/
- /doc/develop/configure-applications/scaling/
- /doc/reference/scaling/
- /doc/scaling-tips
---

Your application runs on one or more instances of the same size, behind the load balancer. Choose their size and number in the **Scalability** menu of the [Console](https://console.clever-cloud.com), or with [`clever scale`](/doc/tools/cli/applications/configuration/#scale-and-dedicated-build). A single value keeps them fixed, a range lets Clever Cloud adapt them to the load: this is autoscaling.

## Instance sizes

| Size   | `pico`  | `nano`  | `XS`  | `S`   | `M`   | `L`   | `XL`   | `2XL`  | `3XL`  |
|--------|:-------:|:-------:|:-----:|:-----:|:-----:|:-----:|:------:|:------:|:------:|
| vCPU   | 1*      | 1*      | 1     | 2     | 4     | 6     | 8      | 12     | 16     |
| Memory | 256 MiB | 512 MiB | 1 GiB | 2 GiB | 4 GiB | 8 GiB | 16 GiB | 24 GiB | 32 GiB |

\* `pico` and `nano` instances share their vCPU with a lower priority, and always build on a [dedicated build instance](/doc/develop/common-configuration/#dedicated-build-instance). `XS` is the default size for new applications. The smallest size is `pico`, or `nano` for PHP, FrankenPHP, Static with Apache, and Docker applications.

## Fixed size and number

Set one size and one number of instances to keep them fixed, whatever the load:

```bash
clever scale --flavor M --instances 2
```

A change of the size or of the number of instances starts a deployment right away.

## Autoscaling

Clever Cloud monitors the CPU and memory usage of your instances. When it stays high for a few minutes, it scales your application up within the ranges you set, and scales it down when the load drops. Autoscaling absorbs lasting load increases, not short peaks.

Each change is a deployment. With [zero downtime deployment](/doc/develop/common-configuration/#zero-downtime-deployment), enabled by default, new instances start before the old ones stop. The [activity](/doc/develop/observability/activity/) of your application lists them as `UPSCALE` or `DOWNSCALE`, triggered by `Monitoring/Scaling`.

### Vertical scaling

With a range of sizes, Clever Cloud replaces your instances with larger ones when the load increases, and with smaller ones when it decreases:

```bash
clever scale --min-flavor XS --max-flavor M
```

### Horizontal scaling

With a range of numbers, Clever Cloud adds instances next to the running ones when the load increases, and removes them when it decreases. An application can have up to 40 instances, or 20 when you set them with Clever Tools:

```bash
clever scale --min-instances 1 --max-instances 4
```

### Both ranges

When you set both ranges, Clever Cloud first increases the size of your instances, up to the maximum size, then adds instances of this size. For instance, with sizes from `XS` to `S` and 1 to 2 instances, your application goes from one `XS` instance to one `S` instance, then to two `S` instances. When the load drops, Clever Cloud first removes the added instances, and keeps the larger size longer.

Autoscaling measures the usage of the whole instance. Code that runs on a single thread, such as the JavaScript of a Node.js process, only uses one vCPU. On a larger instance, this thread can reach its limit while the usage of the whole instance stays low: Clever Cloud may then not add instances. Run several processes, for instance with the [cluster mode](https://nodejs.org/api/cluster.html) of Node.js, to use every vCPU of your instances.

With zero downtime deployment, a new deployment keeps the size and the number of instances that autoscaling reached.

## Run on several instances

Each instance runs its own copy of your application, which changes a few things:

- Each instance runs your [CRON jobs](/doc/develop/cron/) and your [workers](/doc/develop/common-configuration/workers/). To keep a job from running on every instance, see [Avoid duplicate runs](/doc/develop/cron/#avoid-duplicate-runs).
- Local files aren't shared, and disappear with their instance: use an [FS Bucket](/doc/deploy/storage/fs-bucket/) or [Cellar Object Storage](/doc/deploy/storage/cellar/).
- Sessions kept in memory only exist on one instance. Store them in a [Materia KV](/doc/deploy/databases/materia-kv/) or [Redis®](/doc/deploy/databases/redis/) add-on, or enable [sticky sessions](/doc/develop/common-configuration/#sticky-sessions).
- The `INSTANCE_NUMBER` environment variable, `0`, `1`, and so on, tells your application which instance it runs on.

Clever Cloud bills each instance for the seconds it runs, within the ranges you set.

- [Learn more about consumption](/doc/account-billing/consumption/)
