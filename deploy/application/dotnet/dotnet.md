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

{{< alert "warning" ".NET support is in beta" >}}
  If you encounter an issue, please contact the support.
{{< /alert >}}

Clever Cloud allows you to deploy .NET web applications. This page will explain
you how to set up your application to run it on our service.

You do not need to change a lot in your application, the *requirements* will
help you to configure your apps with some mandatory files to add, and
properties to setup.

## .NET version

The default version used on Clever Cloud is `5.0`. You can change it to `3.1` by setting the `CC_DOTNET_VERSION` environment variable to `3.1`. No support will be provided for end-of-life versions.

{{< readfile "/content/partials/create-application.md" >}}

## Necessary information

Be sure that:

* You have pushed in **master** branch.
* You listen on port **8080**, by default each .NET application is created with the `ASPNETCORE_URLS="http://0.0.0.0:8080"` environment variable.
* You have committed the different files of your project and the corresponding project file (`.csproj`, `.fsproj` or `.vbproj`).

## Requirements

Let's take an example with the Microsoft [TodoApi project](https://github.com/Azure-Samples/dotnet-core-api.git). 

During deployment, the `TodoApi.csproj` file and the target framework `netcoreapp3.1` are automatically detected. Then, the .NET project is published:

```bash
dotnet publish --framework netcoreapp3.1 --configuration Release
```

No additional configuration is required (unless multiple project files or target frameworks are present, see the documentation below).

### Multiple project files in the repository

If multiple project files are present in your repository, you can specify the file to use (without the .*proj extension) with the `CC_DOTNET_PROJ` environment variable.

```bash
CC_DOTNET_PROJ=TodoApi2
```

### Multiple binary targets

If your project file defines multiple targets, like :

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>netcoreapp3.0;netcoreapp3.1</TargetFramework>
  </PropertyGroup>
  ...
```

You must specify the one you want to run, with the `CC_DOTNET_TFM` environment variable.

If `CC_DOTNET_TFM` is specified, then the executable produced by this target is used to start the application.

```bash
CC_DOTNET_TFM=netcoreapp3.1
```

### Dependencies

Make sure to list all your dependencies in your project file. For example:

```xml
  ...
  <ItemGroup>
    <PackageReference Include="EntityFramework" Version="6.4.0" />
    <PackageReference Include="Microsoft.VisualStudio.Web.CodeGeneration.Design" Version="3.1.2" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="3.1.3">
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
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

If you need to run a custom command (or just pass options to the program), you can specify it through the `CC_RUN_COMMAND` [environment variable](#setting-up-environment-variables-on-clever-cloud).

For instance, you can have `CC_RUN_COMMAND=./bin/Release/net5.0/myapp <options>`.

### Private dependencies

Support for private dependencies will be available soon.

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via Git. Follow [these steps]({{< ref "getting-started/quickstart.md" >}}) to deploy your application.

{{< readfile "/content/partials/more-config.md" >}}
