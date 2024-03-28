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
- /doc/deploy/application/dotnet
- /doc/deploy/application/dotnet/dotnet
- /doc/partials/language-specific-deploy/dotnet
---

## Overview

Clever Cloud allows you to deploy .NET web applications. This page will explain you how to set up your application to run it on our service.

You do not need to change a lot in your application, the *requirements* will help you to configure your apps with some mandatory files to add, and properties to setup.

{{< callout type="warning">}}
  If you encounter an issue, please contact the support.
{{< /callout >}}

{{% content/create-application %}}

{{% content/set-env-vars %}}

## Configure your Dotnet application

### .NET version

The default version used on Clever Cloud is `8.0`. You can change it by setting the `CC_DOTNET_VERSION` environment variable to `6.0`. We don't support non-LTS and older versions.

### Requirements

Be sure that:

* You have pushed in **master** branch.
* You listen on port **8080**, by default each .NET application is created with the `ASPNETCORE_URLS="http://0.0.0.0:8080"` environment variable.
* You have committed the different files of your project and the corresponding project file (`.csproj`, `.fsproj` or `.vbproj`).

Let's take an example with the [simple-feed-reader project](https://github.com/dotnet-architecture/simple-feed-reader).

First, you need to add the `APP_FOLDER=SimpleFeedReader` environment variable to define the application folder inside the Git repository.

During deployment, the runtime automatically detects the `SimpleFeedReader.csproj` file and the target framework `net8.0`. Then, it publishes the .NET project:

```bash
dotnet publish --framework net8.0 --configuration Release
```

No additional configuration is required (unless multiple project files or target frameworks are present, see the documentation below).

### Multiple project files in the repository

If multiple project files are present in your repository, you can specify the file to use (without the .*proj extension) with the `CC_DOTNET_PROJ` environment variable.

```bash
CC_DOTNET_PROJ=SimpleFeedReader
```

### Multiple binary targets

If your project file defines multiple targets, like :

```xml{linenos=table}
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net6.0;net8.0</TargetFramework>
  </PropertyGroup>
  ...
```

You must specify the one you want to run, with the `CC_DOTNET_TFM` environment variable.

If `CC_DOTNET_TFM` is specified, then the executable produced by this target is used to start the application.

```bash
CC_DOTNET_TFM=net6.0
```

### Dependencies

Make sure to list all your dependencies in your project file. For example:

```xml{linenos=table}
  ...
  <ItemGroup>
    <PackageReference Include="AutoMapper.Extensions.Microsoft.DependencyInjection" Version="5.0.1" />
    <PackageReference Include="Microsoft.SyndicationFeed.ReaderWriter" Version="1.0.2" />
  </ItemGroup>
  </ItemGroup>
</Project>
```

Compiled dependencies are cached by default to speed up deployments. You can disable dependencies caching completely by removing the `CC_CACHE_DEPENDENCIES` environment variable.

If you want to rebuild your application from scratch, you can select "rebuild and restart" from the console or launch `clever restart --without-cache` from [CLI](https://github.com/CleverCloud/clever-tools)

### Configure profile

The default profile is `Release` but you can use the `CC_DOTNET_PROFILE` environment variable to change this configuration.

```bash
CC_DOTNET_PROFILE=Debug
```

### Custom run command

If you need to run a custom command (or just pass options to the program), you can specify it through the `CC_RUN_COMMAND` environment variable.

For instance, you can have `CC_RUN_COMMAND=./bin/Release/net6.0/myapp <options>`.

### Private dependencies

Support for private dependencies will be available soon.

{{% content/env-injection %}}

To access environment variables from your code, you can use `System.Environment.GetEnvironmentVariable("MY_VARIABLE")"`.

{{% content/deploy-git %}}

{{% content/link-addon %}}
 
{{% content/more-config %}}

{{% content/url_healthcheck %}}

