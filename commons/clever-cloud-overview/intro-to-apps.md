---
title: Intro to Apps
position: 1
shortdesc: A quick overview of the concept of application on Clever Cloud
tags:
- dashboard-setup
- apps
---

# Introduction to Applications

## Application's definition

An application is defined on Clever Cloud by the following elements:

* a dedicated language/framework
* a deployment method (FTP and/or Git)
* RAM and CPU consumption, depending on the language or framework used
* an optional configuration file you've added to your project

If one of these elements is missing, Clever Cloud can't deploy your application properly (except the configuration file, optional in some cases).

Supported platforms:

* [Docker](/doc/docker)
* [Go](/doc/go)
* [Haskell](/doc/haskell)
* [Java](/doc/java) [Play Framework 1 & 2, Maven, War files… ]
* [Node.js](/doc/nodejs)
* [PHP](/doc/php)
* [Python](/doc/python)
* [Ruby](/doc/ruby)
* [Rust](/doc/rust)
* [Scala](/doc/scala)


## How it works

When an application is pushed, the platform receives it. It then checks the resources’ requirements. If they are complete, the deployment is launched. When finished and successful, the application is up and running.

The log system retrieves all output from the application and displays it in your admin console.
