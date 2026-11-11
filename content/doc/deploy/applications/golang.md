---
type: docs
linkTitle: Go
title: Go application runtime
description: Build and deploy Go applications on Clever Cloud with Go modules, from a single package to a module with several commands, with the Go version of your choice
keywords:
- chi
- echo
- gin
- go modules
- golang
- go app hosting
- net/http
aliases:
- /applications/golang
- /deploy/application/golang/go
- /doc/applications/golang
- /doc/deploy/application/golang
- /doc/deploy/application/golang/go
- /doc/getting-started/by-language/go
- /doc/go
- /doc/go-hosting
- /doc/go/go
- /doc/golang
- /doc/partials/language-specific-deploy/go
- /go
- /go/go
- /golang
---

## Overview

[Go](https://go.dev) is a compiled language, well suited to network services. Clever Cloud builds your [module](https://go.dev/doc/modules/gomod-ref) with `go install` and starts the binary it produces. It works with the `net/http` package of the standard library, or with frameworks such as [chi](https://go-chi.io), [Echo](https://echo.labstack.com), or [Gin](https://gin-gonic.com).

## Create your Go application

To create a new Go application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type go
```

- [Learn more about Clever Tools](/doc/tools/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/)

## Configure your Go application

### Mandatory needs

A Go application needs:

- A `go.mod` file, at the root of the project or of the folder set in `APP_FOLDER`, or a [Makefile](#build-with-a-makefile)
- A `main` package at the root of the module, or the path of another one set in [`CC_GO_PKG`](#build-another-package)
- A web server listening on `0.0.0.0`, on [the port in `PORT`](/doc/manage/#listen-on-the-right-port), unless the application runs as a [Clever Task](#go-applications-as-clever-tasks)

For instance, a minimal application with the standard library:

```text {filename="go.mod"}
module example.com/hello

go 1.27
```

```go {filename="main.go"}
package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
)

func main() {
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintln(w, "Hello from Go on Clever Cloud")
    })
    log.Fatal(http.ListenAndServe("0.0.0.0:"+port, nil))
}
```

Run `go mod init` with the path of your module to create `go.mod`, and `go mod tidy` to add your dependencies to it. Commit `go.mod` with your code, and `go.sum` once your module has dependencies. Your application reads its [environment variables](/doc/manage/environment-variables/) with `os.Getenv`, such as `PORT` or the credentials of the add-ons you link to the application.

### Build phase

On a new build, Clever Cloud reads the path of your module in `go.mod`, runs the pre-build [hook](/doc/manage/build-hooks/), then builds and installs the module:

```bash
go install example.com/hello
```

Go downloads the modules your code needs through the [Go module proxy](https://proxy.golang.org), then compiles it. It installs the binary in `~/go_home/bin`, which is in the `PATH`, under the last element of the module path: `hello` for `example.com/hello`. If this path ends with a major version, such as `/v2`, Clever Cloud doesn't find the binary. Move the `main` package to a folder such as `cmd/api`, then [build this package](#build-another-package).

With `CC_TROUBLESHOOT=true`, `go install` also runs with `-x`, to print each step, and `-race`. The application then runs with the race detector, which slows it down and needs `CGO_ENABLED=1`: keep this setting for debugging.

Go reads its usual [environment variables](https://pkg.go.dev/cmd/go#hdr-Environment_variables) during the build. Set `GOFLAGS`, or `CGO_ENABLED=0` for a binary without C dependencies, in the environment of your application to change how it compiles. The image includes `gcc`, for the packages that call C code.

### Build another package

When the `main` package isn't at the root of the module, such as in `cmd/server`, set its path in `CC_GO_PKG`. Otherwise, `go install` finds no Go file at the root, and the build fails with `no required module provides package`:

```bash
clever env set CC_GO_PKG ./cmd/server
```

Clever Cloud then runs `go install ./cmd/server`, and starts the `server` binary, named after the last element of this path.

### Go version

The image includes a recent Go release. When the `go` or `toolchain` line of `go.mod` requires a newer version, Go downloads it during the build, as [`GOTOOLCHAIN`](https://go.dev/doc/toolchain) is `auto`. To build with another version, from Go 1.21 and at least the one of the `go` line of `go.mod`, set `GOTOOLCHAIN`:

```bash
clever env set GOTOOLCHAIN go1.26.0
```

With `go 1.26` in `go.mod`, the deployment logs then show `go: downloading go1.26.0`, before the build.

### Build with a Makefile

To build with your own commands, set `CC_GO_BUILD_TOOL=makefile` and the path of the binary they produce in `CC_GO_BINARY`, from the folder of your project. Clever Cloud runs `make -f Makefile`, which builds the first target of the file, then starts this binary:

<!-- markdownlint-disable MD010 -->
```makefile {filename="Makefile"}
.PHONY: build
build:
	go build -o bin/app ./cmd/app
```
<!-- markdownlint-enable MD010 -->

```bash
clever env set CC_GO_BUILD_TOOL makefile
clever env set CC_GO_BINARY bin/app
```

Without `CC_GO_BINARY`, Clever Cloud ignores the Makefile. Without a `go.mod` file, a `Makefile` and `CC_GO_BINARY` are enough: Clever Cloud uses the Makefile without `CC_GO_BUILD_TOOL`. The [go-workspaces](https://github.com/CleverCloud/go-workspaces-example) example builds a Go workspace this way.

### Custom run command

By default, Clever Cloud starts the binary without arguments, from a folder that holds the files of your project. Relative paths, such as a `templates` folder, work as on your computer. To pass arguments, or start something else, set `CC_RUN_COMMAND`. Call the binary by its name: `~/go_home/bin`, where Go installs it, is in the `PATH`:

```bash
clever env set CC_RUN_COMMAND "hello --workers 4"
```

This command runs in a shell, from the root of your repository, even when `APP_FOLDER` sets another folder. Start it with `cd api &&` to keep the relative paths of an `api` folder. With a Makefile, call the binary with its path from this root, such as `./bin/app`.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit, with the binary and the downloaded modules. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

A new commit downloads the modules and compiles your code again: `CC_CACHE_DEPENDENCIES` doesn't keep them between commits. To build without downloading the modules, commit the `vendor` folder that `go mod vendor` creates: Go then builds from it, without the module proxy.

### Projects without go.mod

Without a `go.mod` file, Clever Cloud runs `go install main.go` and starts the `main` binary. Such a project can only use the standard library, in a single `main.go` file: run `go mod init` to turn it into a module. `CC_GO_BUILD_TOOL` also accepts the legacy `gobuild` and `goget` values.

## Go applications as Clever Tasks

A Go binary can run as a [Clever Task](/doc/deploy/tasks/), such as a job or a migration. Clever Cloud builds the project, then runs `CC_RUN_COMMAND` instead of starting a web server. A task needs `CC_RUN_COMMAND`, and doesn't use the build cache. Configure an application as Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/tools/cli/applications/#tasks), here for a `worker` binary that runs once with `--once`:

```bash
clever create --type go --task "worker --once"
clever deploy # or clever restart if there is no code change
```

## Go Further

{{< cards >}}
  {{< card link="/developers/guides/self-hosted/echoip" title="EchoIP" subtitle="Deploy EchoIP as a Go application" icon="simple:go" >}}
  {{< card link="/developers/doc/manage/healthcheck" title="Health check" subtitle="Check that your application answers before it gets any traffic" icon="shield-check" >}}
  {{< card link="/developers/doc/manage/request-flow" title="Request Flow" subtitle="Chain reverse proxies and middleware in front of your application" icon="traffic-light" >}}
{{< /cards >}}
