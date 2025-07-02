---
type: docs
title: Node.js & MongoDB
description: The goal of this article is to show you how to deploy a Node.js with MongoDB application on Clever Cloud.
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

* [GitHub repo](https://GitHub.com/CleverCloud/demo-nodejs-mongodb-rest)

{{< content "create-application" >}}

 {{< content "set-env-vars" >}}

## Configure your Node.js + MongoDB application

### My application does not exists already

If you want to test easily a Node.js deployment on Clever Cloud, just clone the [GitHub repo](https://GitHub.com/CleverCloud/demo-nodejs-mongodb-rest).

 {{< content "env-injection" >}}

 {{< content "deploy-git" >}}

 {{< content "link-addon" >}}

## Configure your database

Make sure you have created a MongoDB add-on in the Clever Cloud console, and that it's linked to your application. When it's done, you will be able to access all of your add-on [environment variables](#setting-up-environment-variables-on-clever-cloud) from the application.

{{< content "more-config" >}}
