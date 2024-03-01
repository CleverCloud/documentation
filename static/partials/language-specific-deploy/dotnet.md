<!-- markdownlint-disable MD041-->
## Configure your Dotnet application

### .NET version

The default version used on Clever Cloud is `6.0`. You can change it to `5.0` by setting the `CC_DOTNET_VERSION` environment variable to `5.0`. No support will be provided for end-of-life versions.

### Requirements

Be sure that:

* You have pushed in **master** branch.
* You listen on port **8080**, by default each .NET application is created with the `ASPNETCORE_URLS="http://0.0.0.0:8080"` environment variable.
* You have committed the different files of your project and the corresponding project file (`.csproj`, `.fsproj` or `.vbproj`).

Let's take an example with the [simple-feed-reader project](https://github.com/dotnet-architecture/simple-feed-reader).

First, you need to add the `APP_FOLDER=SimpleFeedReader` environment variable to define the application folder inside the Git repository.

During deployment, the `SimpleFeedReader.csproj` file and the target framework `net5.0` are automatically detected. Then, the .NET project is published:

```bash
dotnet publish --framework net5.0 --configuration Release
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
    <TargetFramework>net5.0;net6.0</TargetFramework>
  </PropertyGroup>
  ...
```

You must specify the one you want to run, with the `CC_DOTNET_TFM` environment variable.

If `CC_DOTNET_TFM` is specified, then the executable produced by this target is used to start the application.

```bash
CC_DOTNET_TFM=net5.0
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

For instance, you can have `CC_RUN_COMMAND=./bin/Release/net5.0/myapp <options>`.

### Private dependencies

Support for private dependencies will be available soon.