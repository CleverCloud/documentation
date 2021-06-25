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

{{< readfile "/content/partials/create-application.md" >}}

{{< readfile "/content/partials/set-env-vars.md" >}}

{{< readfile "/content/partials/language-specific-deploy/dotnet.md" >}}

{{< readfile "/content/partials/deploy-git.md" >}}

{{< readfile "/content/partials/link-addon.md" >}}

{{< readfile "/content/partials/more-config.md" >}}