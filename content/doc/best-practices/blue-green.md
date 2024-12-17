---
type: docs
title: Blue/Green Deployments
shortdesc: An explanation of what is Blue/Green deployment
tags:
- develop
- best-practices
keywords:
- blue/green
- deployment

type: docs
aliases:
- /doc/develop/blue-green
---

Blue/Green deployment is a technique used in automated deployment of applications, databases and services.
Its main goal is to minimize the downtime and risks of an application by running two identical environment instances, one called *Blue* and the other one called *Green*.

## Contextual example

Let's say you have a production environment called *Blue*, running for instance an e-commerce application. Your customers are routed to this *Blue* instance. In parallel, you will have a "sleeping clone" of *Blue*, named *Green*.
Now let's say you have achieved a new feature and want your customers to benefit of it. Using the "Blue/Green" technique, the new code will be used in *Green*. Once *Green* is ready, you will redirect your customers to *Green*, and we will put *Blue* in "sleeping mode". When you will add new modification you will do it on *Blue* this time, then on *Green* again, and so on.

There are many benefits to this approach:

- if *Green* fails to deploy there will be no downtime for your customers or users as you will not use the broken *Green* and stay on "Blue" until you fix your code so it can start
- if you are not happy with the changes you added in *Green*, you can "awake" *Blue* and get back to the previous version easily by routing the traffic to it

## In the Clever Cloud context

When you push your source code to the Clever Cloud git remote, Clever Cloud will automatically use the "Blue/Green" pattern to apply your changes to your production.

A new VM, let's call it *Blue* is created. The deployment is successful when there's no error in the build phase and the [deployment healthcheck]({{< ref "doc/develop/healthcheck" >}}) is successful. And that's it, you will use the new version on production within seconds.

If you push new changes, a *Green* VM will be created.

### Deployment succeeds

If the deployment succeeds, *Green* will be the version in production and *Blue* will be turned off minutes later.
This way, if you are not happy with the changes you made, just go the Clever Cloud web console, select your application and in the **Overview** menu, click the "Start last pushed commit" button, this will "awake" *Blue* and reverse your changes in production within a few minutes.

#### Deployment fails

If there is an error during the build phase or if the *Green* servers answers an error code on :8080/, we will alert you by email and *Blue* will remain the production server.

Next time you push code a new *Green* VM will be created, then a *Blue* one, and so on.

You also may see some deployments that you haven't triggered in your logs. It's because Clever Cloud uses "Blue/Green" pattern to update VMs, either security patches or versions updates.
