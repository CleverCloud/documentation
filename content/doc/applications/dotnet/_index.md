---
type: docs
title: .NET
shortdesc: .NET. Free, Cross-platform, Open source. A developer platform for building all your apps.
tags:
- deploy
keywords:
- .NET
- csproj
- fsproj
- vbproj
str_replace_dict:
  "@application-type@": ".NET"
type: docs
aliases:
- /doc/deploy/application/dotnet/dotnet
---

## Overview

Clever Cloud allows you to deploy .NET web applications. This page will explain you how to set up your application to run it on our service.

You do not need to change a lot in your application, the *requirements* will help you to configure your apps with some mandatory files to add, and properties to setup.

{{< callout type="warning">}}
  If you encounter an issue, please contact the support.
{{< /callout >}}

{{< readfile file="create-application.md" >}}

{{< readfile file="set-env-vars.md" >}}

{{< readfile file="language-specific-deploy/dotnet.md" >}}

{{< readfile file="env-injection.md" >}}

To access environment variables from your code, you can use `System.Environment.GetEnvironmentVariable("MY_VARIABLE")"`.

{{< readfile file="deploy-git.md" >}}

{{< readfile file="link-addon.md" >}}

{{< readfile file="more-config.md" >}}