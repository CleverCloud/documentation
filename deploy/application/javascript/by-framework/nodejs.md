---
title: Deploy Node.js applications
shortdesc: Node.js is a platform built on Chrome's JavaScript runtime for building fast, scalable network applications.
tags:
- deploy
keywords:
- nodejs
str_replace_dict:
  "@application-type@": "Node"
---

## Overview

Clever Cloud allows you to deploy any [Node.js](https://nodejs.org) application. We do support **any stable version of node >= 0.6**.
This page will explain you how to set up your application to run it on our service.

{{< readfile "/content/partials/create-application.md" >}}

{{< readfile "/content/partials/set-env-vars.md" >}}

{{< readfile "/content/partials/language-specific-deploy/node.md" >}}

{{< readfile "/content/partials/new-relic.md" >}}

{{< readfile "/content/partials/env-injection.md" >}}

To access environment variables from your code, you can use `process.env.MY_VARIABLE`.

{{< readfile "/content/partials/deploy-git.md" >}}

## Troubleshooting your application

If you are often experiencing auto restart of your nodeJS instance, maybe you have an application crashing that we automatically restart.
To target this behaviour, you can gracefully shutdown with events handlers on `uncaughtExeption` `unhandledRejection` `sigint` and `sigterm` and log at this moment so you can fix the problem.

{{< readfile "/content/partials/link-addon.md" >}}

{{< readfile "/content/partials/more-config.md" >}}

## Deployment video

<iframe width="853" height="480" src="https://www.youtube.com/embed/dxhSjHnrrhA?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>