---
title: Deploy Go applications
shortdesc: Go, otherwise known as Golang, is an open source, compiled, garbage-collected, concurrent system programming language.
tags:
- deploy
keywords:
- go
- golang
str_replace_dict:
  "@application-type@": "Go"
---

## Overview

Clever Cloud allows you to deploy any Go application. This page will explain you how to set up your application to run it on our service.

We currently support single module applications only. That means that your sources files just need to be at the project's root, and you can't have multiple modules running.

You do not need to change a lot in your application, the *requirements* will help you configure your applications with some mandatory files to add, and properties to setup.


{{< readfile file="/content/partials/create-application.md" >}}

{{< readfile file="/content/partials/set-env-vars.md" >}}

{{< readfile file="/content/partials/language-specific-deploy/go.md" >}}

{{< readfile file="/content/partials/deploy-git.md" >}}

{{< readfile file="/content/partials/link-addon.md" >}}

{{< readfile file="/content/partials/more-config.md" >}}
