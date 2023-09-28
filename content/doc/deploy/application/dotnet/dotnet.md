---
title: Deploy .NET apps
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
---

## Overview

Clever Cloud allows you to deploy .NET web applications. This page will explain you how to set up your application to run it on our service.

You do not need to change a lot in your application, the *requirements* will help you to configure your apps with some mandatory files to add, and properties to setup.

{{< alert "warning" ".NET support is in beta" >}}
  If you encounter an issue, please contact the support.
{{< /alert >}}

{{< readfile file="/content/partials/create-application.md" >}}

{{< readfile file="/content/partials/set-env-vars.md" >}}

{{< readfile file="/content/partials/language-specific-deploy/dotnet.md" >}}

{{< readfile file="/content/partials/env-injection.md" >}}

To access environment variables from your code, you can use `System.Environment.GetEnvironmentVariable("MY_VARIABLE")"`.

{{< readfile file="/content/partials/deploy-git.md" >}}

{{< readfile file="/content/partials/link-addon.md" >}}

{{< readfile file="/content/partials/more-config.md" >}}