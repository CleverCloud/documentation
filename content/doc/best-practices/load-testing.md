---
type: docs
title: Load testing
position: 3
shortdesc: Considerations and methods to perform a load test on Clever Cloud
tags:
- develop
- best-practices
keywords:
- test
- stress
- load
- performance
type: docs
aliases:
- /doc/develop/load-testing
---
## Overview

Performing a performance test is the best way to determine how your application will perform under heavy load.

In general, these tests make it possible to identify:

* the maximum number of concurrent users
* whether the current resources are sufficient to operate your application in good conditions
* and the maximum operational capacity of your application

## Considerations to take into account

In the event that you use public front-ends, it is necessary to notify the support. Indeed, depending on the nature of the load, it is possible that a form of network blocking is performed by our teams if they are not notified.

In case you have dedicated frontends, note that too much load could impact your other applications behind this frontend. Because in general, the amount of private front-ends is lower than the number of public front-ends (new public front-ends are added on a regular basis).

## Why carry out these tests

Performing these tests will allow you:

* to have perspective on the performance and stability of your infrastructure.
* to be able to identify bottlenecks in particular stress scenarios
* to identify and remove any weaknesses in architectures via supervision and performance management strategies and increase scalability

The determining elements are:

* The response time of your transactions (poorly optimized requests, etc.)
* The performance of the application (single-threaded application, expectations of external services, generation of logs in a file, etc.)
* The performance of managed services such as databases (lack of indexes, unnecessary iterations, etc.)
* Software design in general
* Hardware limitations such as CPU, RAM, network, etc.
* bad middleware configurations (databases, server, etc.)
* The response time between the client and the application

## Online and local load tools

Choosing a load-testing solution will depend on several factors. If simplicity and speed are the most important factors, online tools are the most appropriate. On the other hand, if you have to test particular protocols, and have fine configuration options via a little programming / scripting and for a lower cost, you may want to use dedicated, local solutions.

### Online

Online services are available to perform your tests. Most offer typical user journey scenarios to allow you to simulate a user:

* [K6](https://k6.io/cloud)
* [Octoperf](https://octoperf.com)
* [Loader.io](https://loader.io)

### Local, with open source alternatives

Some open source services to be installed on an infrastructure (workstation or IaaS in the best case) are also available:

* [Gatling](https://gatling.io)
* [Drill](https://github.com/fcsonline/drill)
* [Locust](https://locust.io)
* [Jmeter](https://jmeter.apache.org)
