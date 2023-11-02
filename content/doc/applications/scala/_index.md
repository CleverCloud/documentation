---
type: docs
title: Scala
shortdesc: Scala is an object-functional programming and scripting language that runs on the Java platform…
tags:
- deploy
keywords:
- scala
str_replace_dict:
  "@application-type@": "SBT + Scala"
type: docs
aliases:
- /doc/applications/scala
comments: false
---

## Overview

Clever Cloud allows you to deploy Scala (and Java) applications built with <acronym title="Simple Build Tool">SBT</acronym>. This document will explain you how to set up your app to run it on our service.

If you're looking to deploy a [Play Framework](https://www.playframework.com) application, you can have a look at our dedicated [deployment guide for play framework applications]({{< ref "/guides/play-framework-2" >}})

{{< readfile file="create-application.md" >}}

{{< readfile file="set-env-vars.md" >}}

{{< readfile file="language-specific-deploy/scala.md" >}}

{{< readfile file="new-relic.md" >}}

{{< readfile file="env-injection.md" >}}

To access environment variables from your code, just get them from the environment with `System.getenv("MY_VARIABLE")`. Be aware that it can return null.

{{< readfile file="deploy-git.md" >}}

{{< readfile file="link-addon.md" >}}

{{< readfile file="more-config.md" >}}
