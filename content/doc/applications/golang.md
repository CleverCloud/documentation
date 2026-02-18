---
type: docs
linkTitle: Go
title: Go
description: Deploy Go applications on Clever Cloud using the open source, compiled, garbage-collected, concurrent system programming language
keywords:
- golang
- go language
- compiled language
- concurrent programming
- microservices
- rest api
aliases:
- /applications/golang
- /deploy/application/golang/go
- /doc/deploy/application/golang
- /doc/deploy/application/golang/go
- /doc/getting-started/by-language/go
- /doc/go
- /doc/go/go
- /doc/golang
- /doc/partials/language-specific-deploy/go
- /go/go
- /go
- /golang
---

## Overview

Clever Cloud allows you to deploy any Go application. This page explains how to set up your project to run it on our service.

{{% content "create-application" %}}

{{% content "set-env-vars" %}}

## Configure your Go application

### Mandatory configuration

Be sure that your application:

- Listens on `0.0.0.0`, not only `localhost` or `127.0.0.1`
- Listens on port `8080`
- Contains a valid build configuration (see below)

### Complementary runtime

Go instances include additional runtime environments such as [Node.js](/doc/applications/nodejs) that you can use through scripts launched by [deployment hooks](/doc/develop/build-hooks). Some of these runtimes can be configured through environment variables. For example, to use a specific version of Node.js, set `CC_NODE_VERSION` (it could be `node` (latest), `lts/*`, `24` or `24.13.0`).

### Modern Go project structure

There are multiple ways to build/run a Go application, and this has evolved over the years. In its modern form a Go project can be a:

- **Package**: one or more `.go` files you can `build` or `run`. The `main` package and `main()` function are the default entry point
- **Module**: one or more packages you can `install`, defined in a `go.mod` file (`go.sum` for checksums)
- **Workspace**: one or more modules seamlessly combined, defined in a `go.work` file

Install any module locally or from a remote repository by passing its URL to the `install` command. A `Makefile` is sometimes used to define how to build, run and/or clean a Go project. The lightest form of a Go project is a `main.go` file to build. The `src/` folder was often used for source code, but using the `cmd/` folder instead is now a common practice.

If you want to limit from where a package can be imported, [place it](https://docs.google.com/document/d/1e8kOo3r51b2BWtTs_1uADIA5djfXhPT36s6eHVRIvaU/edit) in a folder named `internal/`. Access to functions in `.go` files is defined depending [on their name](https://go.dev/tour/basics/3): if it starts with a capital letter it's a public (exported) function, if not it's a private (unexported) function.

For a complete project, a common files/folders organisation can be:
{{< filetree/container >}}
  {{< filetree/folder name="application-root/" >}}
    {{< filetree/file name="go.work" >}}
    {{< filetree/file name="Makefile" >}}
    {{< filetree/folder name="cmd/" >}}
      {{< filetree/file name="main.go" >}}
      {{< filetree/file name="other-file.go" >}}
      {{< filetree/file name="other-package.go" >}}
      {{< filetree/file name="…" >}}
    {{< /filetree/folder >}}
        {{< filetree/folder name="module/" >}}
          {{< filetree/file name="go.mod" >}}
          {{< filetree/file name="go.sum" >}}
          {{< filetree/file name="main.go" >}}
          {{< filetree/file name="other-module-file.go" >}}
            {{< filetree/folder name="internal/" >}}
              {{< filetree/folder name="internal-package/" >}}
                {{< filetree/file name="internal-package-file.go" >}}
              {{< /filetree/folder >}}
            {{< /filetree/folder >}}
      {{< /filetree/folder >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

### Go build and deploy on Clever Cloud

Clever Cloud supports multiple ways to build and run a Go application. The build tool is determined by the `CC_GO_BUILD_TOOL` environment variable or by auto-detection. Available methods are `gomod` (for modules), `gobuild` (for packages), or `makefile` (for custom build steps). The `goget` method still exists but is deprecated.

> [!NOTE]
> If the Go version declared in your `go.mod` file is newer than the one installed on the instance, the Go toolchain downloads the required version automatically.

### Environment variables

| Name | Description |
| :--- | :---------- |
| `CC_GO_BUILD_TOOL` | Available values: `gomod`, `gobuild`, `makefile`. Determines how to build and install your application. `goget` still exists but is deprecated. |
| `CC_GO_BINARY` | Required when using the `makefile` build tool. Path to the built binary, used to launch your application. |
| `CC_GO_PKG` | Package path passed to `go install`. Overrides auto-detection from `go.mod`. Default is `main.go` when no `go.mod` is present. |
| `CC_GO_RUNDIR` | Run the application from the specified path, relative to `$GOPATH/src/`. Deprecated. |

The default `GOPATH` is `${HOME}/go_home`. The build command is `go install <package>` for all non-Makefile methods. If a `vendor/` directory is present, it is included in the build cache.

The resulting binary is placed at `$GOPATH/bin/<name>`, where `<name>` is the basename of the package path without the `.go` extension. For example, `CC_GO_PKG=cmd/server.go` produces a binary named `server`.

#### gomod

Builds a Go module. Requires a `go.mod` file at the root of your application. The module name is read from `go.mod` and passed to `go install`. If you need to build a different package within the module, set `CC_GO_PKG` to override it.

#### gobuild

Builds a Go package using `go install`. Set `CC_GO_PKG` to define the package path (default `main.go`). The application is moved to `$GOPATH/src/` before building.

#### makefile

Builds a Go project with a `Makefile`. Set `CC_GO_BINARY` with the path to the built binary, used to launch your application. The Makefile method is automatically selected when all these conditions are met: `CC_GO_BINARY` is set, a `Makefile` exists, and no `go.mod` file is present. If a `Makefile` is present without `CC_GO_BINARY`, a warning is logged and the Makefile is not used.

An example of a `Makefile`, to use with `CC_GO_BINARY=bin/myApp`:

```Makefile {filename="Makefile"}
BINARY=bin/myApp

build:
#	To install a specific Go version, you can add:
#	go install golang.org/dl/gox.xx.x@latest
#	${HOME}/go_home/bin/gox.xx.x download
#	Then use `${HOME}/go_home/bin/gox.xx.x` instead of `go`
	echo "Build the application as ./${BINARY}"
	go build -o ${BINARY} main.go
```

- [A more complex project using a Go Workspace and a Makefile](https://github.com/CleverCloud/go-workspaces)

> [!WARNING]
> Using `clevercloud/go.json` to define Makefile and binary paths is a deprecated method and should no longer be used.

### Custom run command

By default, the built binary is executed directly. Set `CC_RUN_COMMAND` to override this behavior and run a custom command instead of the binary. When defined, the binary is still built but `CC_RUN_COMMAND` is executed at start.

### Troubleshooting builds

Set `CC_TROUBLESHOOT=true` to enable verbose build output (`-x` flag) and the race detector (`-race` flag) during compilation. This applies to `gomod` and `gobuild` methods.

{{% content "env-injection" %}}

To access environment variables from your code, use `os.Getenv("MY_VARIABLE")`.

{{% content "deploy-git" %}}

{{% content "link-addon" %}}

{{% content "more-config" %}}

{{% content "url_healthcheck" %}}
{{% content "request-flow" %}}

## See also

- [Deploy EchoIP guide](/guides/go-echoip/)
