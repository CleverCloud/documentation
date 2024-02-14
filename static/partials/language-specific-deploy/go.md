## Configure your Go application

### Mandatory needs
By default, we consider that your repository contains a single application. Be sure that:
* It listens to the wild network `0.0.0.0`, not only `localhost` or `127.0.0.1`
* It listens on port `8080`
* You follow our build/run instructions

In most cases you won't need to change anything to your application, except host/port and some configuration variables. 

### Complementary runtime
If you need a runtime environment such as [Node.js](/doc/applications/javascript/nodejs/) or tools to build a frontend for example, some are available in our Go instances. You can use them through scripts launched by [deployments hooks](/doc/develop/build-hooks/) and [Environment variables](/doc/reference/reference-environment-variables/) sometimes allow you to configure them. So if you need a specific version of Node.js, set `CC_NODE_VERSION` (it could be `node` (latest), `lts/*`, `20` or `21.5.0`).

### Modern Go project structure
There are multiple ways to build/run a Go application, and this has evolved over the years. In its modern form a Go project can be a:
- `Package`: one or more `.go` files you can `build` or `run`. `main` package and `main()` function are the default entry point
- `Module`: one or more packages you can `install`, defined in a `go.mod` file (`go.sum` for checksums)
- `Workspace`: one or more modules seamlessly combined, defined in a `go.work` file

A module can be installed locally or from a remote repository if you pass its URL to the `install` command. A `Makefile` is sometimes used to define how a Go project is built, run and/or cleaned. The lightest form of a Go project is a `main.go` file to build. Some years ago, the `src/` folder was often used for source code, but using the `cmd/` folder instead is now a common practice. 

If you want to limit from where a package can be imported it [should placed](https://docs.google.com/document/d/1e8kOo3r51b2BWtTs_1uADIA5djfXhPT36s6eHVRIvaU/edit) in a folder named `ìnternal/`. Access to functions in `.go` files is defined depending [on their name](https://go.dev/tour/basics/3): if it starts with a capital letter it's a public functions, if not it's a private function.

For a complete project, a common files/folders organization can be:
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
In such a situation, our strategy is to let the user choose how to build/run its application and make the deployment easy anyway. At first, we used the `goget` method, which is now deprecated. Thus, you can now use `gobuild` (for packages), `gomod` (for modules) or a configuration file. The latter will allow you to define a `Makefile` for custom build and a `main` executable to start the application.

{{< callout type="info" >}}
  If the required Go version declared in the `go.mod` is superior to the version built in the instance, it will be automatically updated.
{{< /callout >}}

#### Through Makefile and JSON configuration
Create a file name `go.json` in a `clevercloud/` folder at the root of your repository. It will allow you to ask for a custom build through a `Makefile` ([learn more about it](https://en.wikipedia.org/wiki/Make_(software)#Makefiles)). For example with a single package in `main.go`:

```json {filename="clevercloud/go.json"}
{
  "deploy": {
    "makefile": "Makefile",
    "main": "bin/myApp"
  }
}
```

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

You'll find a more complex project using a Go Workspace and a `Makefile` [here](https://github.com/CleverCloud/go-workspaces).

#### Through Environment variables
If you don't want to add a file to your project, you can set one of these environment variables:

| Name | Description |
| :------- | :---- |
| `CC_GO_BUILD_TOOL` | Available values: `gomod`, `gobuild`. Build and install your application. `goget` still exists but is deprecated. |
| `CC_GO_RUNDIR` | Run the application from the specified path, relative to `$GOPATH/src/`, now deprecated. |
| `CC_GO_PKG` | Tell the `CC_GO_BUILD_TOOL` which file contains the `main()` function, default `main.go`. |

- **gobuild**
To build a Go package, your project may include vendored dependencies (in the `vendor/` folder). `CC_GO_PKG` can be set to define the main file of your application (default `main.go`).

- **gomod**
To build a Go module, be sure that the `go.mod` file is in your git tree and at the root of your application. Your project's entrypoint should be in the same folder as the `go.mod` file and be named `main.go`. If it isn't, you have to set `CC_GO_PKG=path/to/entrypoint.go`.

The final command will be: 

```
go install $CC_GO_PKG
```
{{< readfile file="env-injection.md" >}}

To access environment variables from your code, just get them from the environment with `PATH`: `os.Getenv("MY_VARIABLE")`.
