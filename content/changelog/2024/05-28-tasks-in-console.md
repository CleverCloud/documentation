---
title: Manage Clever Tasks in the Console
date: 2024-05-28
tags:
  - console
  - tasks
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Pierre De Soyres
    link: https://github.com/pdesoyres-cc
    image: https://github.com/pdesoyres-cc.png?size=40
description: Just a box to check
aliases:
- /changelog/2024-05-28-tasks-in-console
excludeSearch: true
---

Since [its release 3.5.2](../04-11-clever-tools-3.5.2/), Clever Tools is able to manage [Clever Tasks](/developers/doc/develop/tasks/). It's now possible to create, configure and deploy them directly from the Console. To declare an application as a Task, check the corresponding box in the `Information` tab.

A Clever Task can be run on demand. It executes the command you've set in the `CC_RUN_COMMAND` environment variable, without waiting for any HTTP request on the `8080` port. After that, the application stops. It's just billed for the execution time.

![Clever Task Management in Console](/images/changelog/clever-tasks.webp "Defines a Clever Cloud application as a Task in Console")
