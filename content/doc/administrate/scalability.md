---
type: docs
title: Application scaling
position: 3
shortdesc: How does Clever Cloud give your application the resources it needs?
tags:
- administrate
keywords:
- scale
- scalability
- autoscale
type: docs
---

When your application is running, you don't have the same number of users all the time. During an event for example,
the number of users can increase, as will the load on the server. If too many requests are done on your
server at the same time, the response time will increase and could slow down your website.

To avoid this problem and keep a fast website, the main solution is to deploy more **Scalers** for your application to
support the load. That's what scaling is: adapting automatically the number of **Scalers** and their size to fit the
load of your application, without any action from you.

Clever Cloud gives you the ability to fine tune your application's scaling by managing both horizontal and vertical
scaling. These two parameters can be combined to adapt to your needs.

## What is a Scaler?

A **Scaler** is a Clever Cloud "instance". It is an individual and independent virtual machine hosting your application. A Scaler is defined by two factors: RAM and CPU.

With the Scalers, Clever Cloud gives you the ability to scale your application **up and down** with **two non
exclusive methods**: horizontal and vertical scaling.

### Enable auto-scalability

To enable the scalability of your application, open the [console](https://console.clever-cloud.com/) and go in the
"scalability" section of your application. Then, enable the auto-scalability.

## Horizontal scaling

You can enable it by defining how many maximum instances you need under the "Horizontal scaling" section of the "Scaling" menu.

In case of large traffic, we detect a high load on your application and spawn **another instance in parallel**.
This will automatically set up another identical application with same size. Both will run in parallel with load
balancing. If the traffic grows even more, we will repeat the process until the maximum instances count you defined.


This process is exactly the opposite when the **load decreases**. A Scaler is removed and so on till a **minimum
reasonable level** is reached.

The following scheme depicts a Scaler replication in case of a load increase:

{{< image "/images/doc/scaling_horizontal_scheme.jpg" "You can manage the range of Scalers you consider in the application configurator. The range is from 1 to 40." >}}

{{< image "/images/doc/select-scalab-horizontal.png" "Horizontal scaling: the amount of scaler will increase and the sclaer size will vary between XS and S" >}}

## Vertical scaling

In case of large traffic, we detect a high load on your application and set up **a new larger Scaler**.

In case of low traffic, we detect a low load and set up **a new smaller Scaler**.

You give more power to your application by setting up a larger instance that will replace the previous one. The more the
load, the larger the instance.

The following scheme depicts a larger Scaler replacement in case of a load increase:

{{< image "/images/doc/scaling_vertical_scheme.jpg" "vertical scaling" >}}

You can choose the type of Scalers you consider by defining a maximum instance size manually or just let Clever Cloud choose for you by defining nothing:

{{< image "/images/doc/select-scalab.png" "Vertical scaling: the scaler size will from S to XL." >}}

## Combination of both scalings

When both scalings are set up, **vertical scaling** is privileged over **horizontal scaling**. In the case you set the
vertical scaling from S to L, and the horizontal scaling from 2 scalers to 4 scalers, Clever Cloud will firstly increase
the size of the 2 scalers already launched.

If the 2 initials scalers are at their maximum size, Clever Cloud will launch new scalers with the maximum size of scalers.
This is how it'll be done:

2-S => 2-M => 2-L => 3-L => 4-L.
