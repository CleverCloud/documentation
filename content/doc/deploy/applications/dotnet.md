---
type: docs
linkTitle: .NET
title: .NET application runtime
description: Build and deploy .NET applications on Clever Cloud with the .NET SDK, from an ASP.NET Core API to a project with several target frameworks
keywords:
- asp.net core
- csharp
- dotnet app hosting
- dotnet cloud
- fsharp
- nuget
- visual basic
aliases:
- /applications/dotnet
- /deploy/application/dotnet/dotnet
- /doc/applications/dotnet
- /doc/deploy/application/dotnet
- /doc/deploy/application/dotnet/dotnet
- /doc/develop/env-variables/doc/applications/dotnet
- /doc/dotnet
- /doc/dotnet/dotnet
- /doc/partials/language-specific-deploy/dotnet
- /dotnet
---

## Overview

[.NET](https://dotnet.microsoft.com) is a cross-platform development platform for C#, F#, and Visual Basic. Clever Cloud publishes your project with `dotnet publish` and starts the executable it produces. It works with web frameworks such as [ASP.NET Core](https://learn.microsoft.com/aspnet/core/).

## Create your .NET application

To create a new .NET application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type dotnet
```

- [Learn more about Clever Tools](/doc/tools/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

## Configure your .NET application

### Mandatory needs

A .NET application needs:

- A project file, at the root of the project or of the folder set in `APP_FOLDER`
- A web server listening on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port)

The project file is a `.csproj` file for C#, `.fsproj` for F#, or `.vbproj` for Visual Basic. It describes the [version of .NET your code targets](#net-version-and-target-framework), and the libraries it uses, called NuGet packages. A [Clever Task](#net-applications-as-clever-tasks) doesn't need a web server.

With the .NET 8 SDK, `dotnet new web --name hello` creates this [ASP.NET Core](https://learn.microsoft.com/aspnet/core/) web application, adapted to listen on `PORT`:

```xml {filename="hello.csproj"}
<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
</Project>
```

```csharp {filename="Program.cs"}
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

var port = Environment.GetEnvironmentVariable("PORT") ?? "8080";
app.MapGet("/", () => "Hello from .NET on Clever Cloud");

app.Run($"http://0.0.0.0:{port}");
```

By default, ASP.NET Core doesn't read `PORT`, and only listens on `localhost`. Pass the address to `app.Run`, as here, or set it in `ASPNETCORE_URLS`, such as `http://0.0.0.0:8080`. With [Request Flow](/doc/manage/request-flow/), the port is `9000`.

Read the [environment variables](/doc/manage/environment-variables/), such as add-on credentials, with `Environment.GetEnvironmentVariable`.

### .NET version and target framework

Two settings define the .NET version of your application:

- The target framework moniker (TFM), such as `net8.0`, set in the project file
- The .NET SDK, such as `8.0`, set in `CC_DOTNET_VERSION`

The target framework is the .NET version your code is compiled for. The SDK holds the tools that build it, and comes with the runtime that runs it.

Your application uses the runtime of the selected SDK: use the same major version for both, such as `10.0` for `net10.0`. Otherwise:

- An older SDK doesn't build the project: the build fails with a `NETSDK1045` error
- A newer SDK builds it, but the application doesn't start, with the default project settings

The .NET versions available on Clever Cloud:

{{< runtimes_versions dotnet >}}

To move a project to .NET 10, change its `TargetFramework` to `net10.0`, then set:

```bash
clever env set CC_DOTNET_VERSION 10.0
```

### Several projects or target frameworks

Clever Cloud looks for project files at the root of the repository, or of the folder set in `APP_FOLDER`, but not in the folders below. If your web project is in `src/Api/`, for instance, set `APP_FOLDER=src/Api`.

If this folder holds several project files, set the one to publish in `CC_DOTNET_PROJ`, by its name without extension:

```bash
clever env set CC_DOTNET_PROJ hello
```

A project can also target several .NET versions, listed in `TargetFrameworks`, plural:

```xml {filename="hello.csproj"}
<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFrameworks>net8.0;net10.0</TargetFrameworks>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
</Project>
```

Clever Cloud publishes only one: set it in `CC_DOTNET_TFM`, or the deployment fails, and `CC_DOTNET_VERSION` to match:

```bash
clever env set CC_DOTNET_TFM net10.0
clever env set CC_DOTNET_VERSION 10.0
```

### Build phase

On a new build, Clever Cloud installs the [SDK](#net-version-and-target-framework) and runs the pre-build [hook](/doc/manage/build-hooks/). It then restores the [local tools](https://learn.microsoft.com/dotnet/core/tools/local-tools-how-to-use) listed in `.config/dotnet-tools.json`, if any, and publishes your project.

`dotnet publish` downloads the NuGet packages, compiles the project, and gathers what it needs to run in a folder. It targets `exherbo-x64`, the Linux system of Clever Cloud instances. For the initial `net8.0` example:

```bash
dotnet tool restore
dotnet publish --framework net8.0 --runtime exherbo-x64 --configuration Release hello.csproj
```

Two variables change this command:

- `CC_DOTNET_PROFILE` replaces the `Release` configuration, optimized for production, such as with `Debug`
- `CC_TROUBLESHOOT=true` adds `--verbosity diagnostic`, for more detailed logs

### Start command

`dotnet publish` produces an executable named after the project file, such as `hello` for `hello.csproj`, in this folder:

```text
bin/<configuration>/<framework>/exherbo-x64/publish/
```

Clever Cloud starts it from this folder. If you set another `AssemblyName` in the project file, the deployment fails.

To pass arguments, set `CC_RUN_COMMAND`. It runs from the root of the repository, not from `publish`. For the initial `net8.0` example:

```bash
clever env set CC_RUN_COMMAND "./bin/Release/net8.0/exherbo-x64/publish/hello --verbose"
```

With `APP_FOLDER`, start the path of the executable with this folder.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps the NuGet packages between commits, so builds download fewer of them.

### Private dependencies

To use packages from a private repository, or feed, declare it in a `nuget.config` file at the root of your project:

```xml {filename="nuget.config"}
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <clear />
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" />
    <add key="private" value="%PACKAGE_REGISTRY_URI%" />
  </packageSources>
  <packageSourceCredentials>
    <private>
      <add key="Username" value="%PACKAGE_REGISTRY_USERNAME%" />
      <add key="ClearTextPassword" value="%PACKAGE_REGISTRY_PASSWORD%" />
    </private>
  </packageSourceCredentials>
</configuration>
```

NuGet replaces each `%VARIABLE%` with the environment variable of the same name: set them in your application.

## .NET applications as Clever Tasks

A .NET application can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration: Clever Cloud publishes it, then runs `CC_RUN_COMMAND`.

Configure Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks), here for a `worker` project:

```bash
clever create --type dotnet --task "./bin/Release/net8.0/exherbo-x64/publish/worker --once"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
