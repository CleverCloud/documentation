---
type: docs
title: Node.js
shortdesc: Node.js is a platform built on Chrome's JavaScript runtime for building fast, scalable network applications.
tags:
- deploy
keywords:
- nodejs
str_replace_dict:
  "@application-type@": "Node"
type: docs
aliases:
- /doc/applications/javascript/by-framework/nodejs
- /doc/nodejs/nodejs
---

## Overview

Clever Cloud allows you to deploy any [Node.js](https://nodejs.org) application. We do support **any stable version of node >= 0.6**.
This page will explain you how to set up your application to run it on our service.

{ {{% content/create-application %}}

 {{% content/set-env-vars %}}

{{< readfile file="language-specific-deploy/node.md" >}}

 {{% content/new-relic %}}

 {{% content/env-injection %}}

To access environment variables from your code, you can use `process.env.MY_VARIABLE`.

 {{% content/deploy-git %}}

## Troubleshooting your application

If you are often experiencing auto restart of your Node.js instance, maybe you have an application crashing that we automatically restart.
To target this behaviour, you can gracefully shutdown with events handlers on `uncaughtExeption` `unhandledRejection` `sigint` and `sigterm` and log at this moment so you can fix the problem.

 {{% content/link-addon %}}

{{% content/more-config %}}

 {{% content/env-injection %}}

## Deployment video

{{< youtube id="dxhSjHnrrhA" >}}
