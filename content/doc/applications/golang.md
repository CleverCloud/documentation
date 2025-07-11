---
type: docs
title: Go
shortdesc: Go, otherwise known as Golang, is an open source, compiled, garbage-collected, concurrent system programming language.
tags:
- deploy
keywords:
- go
- golang
str_replace_dict:
  "@application-type@": "Go"
type: docs
aliases:
- /developers/doc/go/go
- /doc/deploy/application/golang
- /doc/deploy/application/golang/go
- /doc/getting-started/by-language/go
- /doc/go/go
- /doc/partials/language-specific-deploy/go
---

## Overview

Clever Cloud allows you to deploy any Go application. This page explains how to set up your project to run it on our service. You won't need to change a lot, the *requirements* will help you configure your applications with some mandatory files to add, and properties to set up.

{{< content "create-application" >}}

{{< content "set-env-vars" >}}

## Configure your Go application

### Mandatory needs

By default, we consider that your repository contains a single application. Be sure that:
* It listens to the wild network `0.0.0.0`, not only `localhost` or `127.0.0.1`
* It listens on port `8080`
* You follow our build/run instructions

In most cases you won't need to change anything to your application, except host/port and some configuration variables.

### Complementary runtime

If you need a runtime environment such as [Node.js]({{< ref "/doc/applications/nodejs" >}}) or tools to build a frontend for example, some are available in our Go instances. You can use them through scripts launched by [deployments hooks]({{< ref "/doc/develop/build-hooks" >}}) and [Environment variables]({{< ref "/doc/reference/reference-environment-variables" >}}) sometimes allow you to configure them. So if you need a specific version of Node.js, set `CC_NODE_VERSION` (it could be `node` (latest), `lts/*`, `20` or `21.5.0`).

### Modern Go project structure

There are multiple ways to build/run a Go application, and this has evolved over the years. In its modern form a Go project can be a:
- `Package`: one or more `.go` files you can `build` or `run`. `main` package and `main()` function are the default entry point
- `Module`: one or more packages you can `install`, defined in a `go.mod` file (`go.sum` for checksums)
- `Workspace`: one or more modules seamlessly combined, defined in a `go.work` file

Install any module locally or from a remote repository by passing its URL to the `install` command. A `Makefile` is sometimes used to define how to build, run and/or clean a Go project. The lightest form of a Go project is a `main.go` file to build. The `src/` folder was often used for source code, but using the `cmd/` folder instead is now a common practice.

If you want to limit from where a package can be imported, [place it](https://docs.google.com/document/d/1e8kOo3r51b2BWtTs_1uADIA5djfXhPT36s6eHVRIvaU/edit) in a folder named `ìnternal/`. Access to functions in `.go` files is defined depending [on their name](https://go.dev/tour/basics/3): if it starts with a capital letter it's a public function, if not it's a private function.

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

In such a situation, our strategy is to let the user choose how to build/run its application and make the deployment easy anyway. At first, we used the `goget` method, which is now deprecated. Thus, you can now use `gobuild` (for packages), `gomod` (for modules) or `makefile`. The latter will allow you to define custom build steps and a `main` executable to start the application.

{{< callout type="info" >}}
  If the required Go version declared in the `go.mod` is superior to the version built in the instance, it will be automatically updated.
{{< /callout >}}

### Environment variables

If you don't want to add a file to your project, you can set one of these environment variables:

| Name | Description |
| :------- | :---- |
| `CC_GO_BUILD_TOOL` | Available values: `gomod`, `gobuild`, `makefile`. Build and install your application. `goget` still exists but is deprecated. |
| `CC_GO_BINARY` | Mandatory for a `Makefile` build, path to the built binary, used to launch your application. |
| `CC_GO_PKG` | Tell the `CC_GO_BUILD_TOOL` which file contains the `main()` function, default `main.go`. |
| `CC_GO_RUNDIR` | Run the application from the specified path, relative to `$GOPATH/src/`, now deprecated. |

{{< callout type="info" >}}
  The default `GO_PATH` is `${HOME}/go_home`.
  The command executed to launch the application is `go install $CC_GO_PKG`. \
  Your project may include vendored dependencies (in the `vendor/` folder).
{{< /callout >}}

#### gobuild

To build a Go package. `CC_GO_PKG` can be set to define the main file of your application (default `main.go`).

#### gomod

To build a Go module, be sure that the `go.mod` file is in your git tree and at the root of your application. Your project's entry point should be in the same folder as the `go.mod` file and be named `main.go`. If it isn't, you have to set `CC_GO_PKG=path/to/entrypoint.go`.

#### makefile

To build a Go project with a `Makefile`. You have to set `CC_GO_BINARY` with the path to the built binary, used to launch your application. If a `Makefile` is present with a `CC_GO_BINARY` set and no `go.mod` file at the root of your project, the `makefile` method will automatically be used.

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

{{< callout type="warning" >}}
  Using `clevercloud/go.json` to define Makefile and binary paths is a deprecated method and should no longer be used.
{{< /callout >}}

 {{< content "env-injection" >}}

To access environment variables from your code, just get them from the environment with `PATH`: `os.Getenv("MY_VARIABLE")`.

{{< content "deploy-git" >}}

{{< content "link-addon" >}}

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}

## See also

* [Deploy EchoIP guide](../../../guides/go-echoip/)
