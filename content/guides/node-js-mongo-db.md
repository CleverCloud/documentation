---
type: docs
title: Node.js + MongoDB sample application
shortdesc: The goal of this article is to show you how to deploy a Node.js + MongoDB application on Clever Cloud.
tags:
- deploy
keywords:
- nodejs
- mongodb
str_replace_dict:
  "@application-type@": "Node"
type: docs
aliases:
- /doc/deploy/application/javascript/tutorials/node-js-mongo-db
---

## Overview

The goal of this article is to show you how to deploy a Node.js + MongoDB application on Clever Cloud.
The application is a very simple todo list. You can add and delete values. More information about the application:

*  [GitHub repo](https://GitHub.com/CleverCloud/demo-nodejs-mongodb-rest)
*  [Clever Cloud demo](https://nodejs-demo.cleverapps.io/)

{{< readfile file="create-application.md" >}}

{{< readfile file="set-env-vars.md" >}}

## Configure your Node.js + MongoDB application
### My application does not exists already

If you want to test easily a Node.js deployment on Clever Cloud, just clone the [GitHub repo](https://GitHub.com/CleverCloud/demo-nodejs-mongodb-rest) and jump to [My application already exists](#my-application-already-exists)

{{< readfile file="env-injection.md" >}}

{{< readfile file="deploy-git.md" >}}

{{< readfile file="link-addon.md" >}}

## Configure your database

Make sure you have created a MongoDB add-on in the Clever Cloud console, and that it's linked to your application. When it's done, you will be able to access all of your add-on [environment variables](#setting-up-environment-variables-on-clever-cloud) from the application.

{{< readfile file="more-config.md" >}}
