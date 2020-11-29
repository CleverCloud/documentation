---
title: Deploy Scala applications with SBT
shortdesc: Scala is an object-functional programming and scripting language that runs on the Java platform…
tags:
- deploy
keywords:
- scala
str_replace_dict:
  "@application-type@": "SBT + Scala"
---

## Overview

Clever Cloud allows you to deploy Scala (and Java) applications built with <acronym title="Simple Build Tool">SBT</acronym>. This document will explain you how to set up your app to run it on our service.

If you're looking to deploy a [Play Framework](https://www.playframework.com) application, you can have a look at our dedicated [deployment guide for play framework applications]({{< ref "deploy/application/scala/tutorials/play-framework-2" >}})

{{< readfile "/content/partials/create-application.md" >}}

{{< readfile "/content/partials/set-env-vars.md" >}}

{{< readfile "/content/partials/language-specific-deploy/scala.md" >}}

{{< readfile "/content/partials/new-relic.md" >}}

{{< readfile "/content/partials/env-injection.md" >}}

To access environment variables from your code, just get them from the environment with `System.getenv("MY_VARIABLE")`. Be aware that it can return null.

{{< readfile "/content/partials/deploy-git.md" >}}

{{< readfile "/content/partials/link-addon.md" >}}

{{< readfile "/content/partials/more-config.md" >}}
