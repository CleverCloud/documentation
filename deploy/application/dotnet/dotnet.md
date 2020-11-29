---
title: Deploy .NET apps
shortdesc: .NET. Free, Cross-platform, Open source. A developer platform for building all your apps.
tags:
- .NET
- dotnet
keywords:
- .NET
- dotnet
- csproj
- fsproj
- vbproj
---

<div class="panel panel-warning">
  <div class="panel-heading">
     <h4>.NET support is in beta</h4>
  </div>
  <div class="panel-body">
    If you encounter an issue, please contact the support.
  </div>
</div>

Clever Cloud allows you to deploy .NET web applications. This page will explain
you how to set up your application to run it on our service.

You do not need to change a lot in your application, the *requirements* will
help you to configure your apps with some mandatory files to add, and
properties to setup.

## .NET version

The version used on Clever Cloud is `3.1`, so you can deploy applications for the two current LTS versions as shown on this [page](https://dotnet.microsoft.com/download/dotnet-core). No support will be provided for end-of-life versions.

## Create an application

Refer to the page [Deploy an application on Clever Cloud](/doc/clever-cloud-overview/add-application/).

## Necessary information

Be sure that:

* You have pushed in `master branch`.
* You listen on `port 8080`, by default each .NET application is created with the `ASPNETCORE_URLS="http://0.0.0.0:8080"` environment variable.
* You have committed the different files of your project and the corresponding project file (`.csproj`, `.fsproj` or `.vbproj`). If the project file is not at the root of the repository, you can use the APP_FOLDER environment variable. See the list of environment variables [here](https://www.clever-cloud.com/doc/get-help/reference-environment-variables/).

## Requirements

Let's take an example with the Microsoft [TodoApi project](https://github.com/Azure-Samples/dotnet-core-api.git). 

During deployment, the `TodoApi.csproj` file and the target framework `netcoreapp3.1` are automatically detected. Then, the .NET project is published :
```sh
dotnet publish --framework netcoreapp3.1 --configuration Release
```

No additional configuration is required (unless multiple project files or target frameworks are present, see the documentation below).

### Multiple project files in the repository

If multiple project files are present in your repository, you can specify the file to use (without the .*proj extension) with the 
`CC_DOTNET_PROJ` environment variable.
```sh
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
You must specify the one you want to run, with the `CC_DOTNET_TFM` environment variable. If `CC_DOTNET_TFM` is
specified, then the executable produced by this target is used to start the
application.
```sh
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

Compiled dependencies are cached by default to speed up deployments. You can
disable dependencies caching completely by removing the `CC_CACHE_DEPENDENCIES`
environment variable. If you want to rebuild your application from scratch,
you can select "rebuild and restart" from the console or launch `clever
restart --without-cache` from [CLI](https://github.com/CleverCloud/clever-tools)

### The configuration to publish for
`Release` by default, you can use the `CC_DOTNET_PROFILE` environment variable to change this configuration.
```sh
CC_DOTNET_PROFILE=Debug
```

### Private dependencies

Support for private dependencies will be available soon.

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via Git. Follow [these
steps](/doc/clever-cloud-overview/add-application/) to deploy your
application.