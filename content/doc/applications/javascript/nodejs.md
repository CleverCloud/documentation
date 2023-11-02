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
---

## Overview

Clever Cloud allows you to deploy any [Node.js](https://nodejs.org) application. We do support **any stable version of node >= 0.6**.
This page will explain you how to set up your application to run it on our service.

{{< readfile file="create-application.md" >}}

{{< readfile file="set-env-vars.md" >}}

{{< readfile file="language-specific-deploy/node.md" >}}

{{< readfile file="new-relic.md" >}}

{{< readfile file="env-injection.md" >}}

To access environment variables from your code, you can use `process.env.MY_VARIABLE`.

{{< readfile file="deploy-git.md" >}}

## Troubleshooting your application

If you are often experiencing auto restart of your Node.js instance, maybe you have an application crashing that we automatically restart.
To target this behaviour, you can gracefully shutdown with events handlers on `uncaughtExeption` `unhandledRejection` `sigint` and `sigterm` and log at this moment so you can fix the problem.

{{< readfile file="link-addon.md" >}}

{{< readfile file="more-config.md" >}}

## Deployment video

{{< youtube id="dxhSjHnrrhA" >}}