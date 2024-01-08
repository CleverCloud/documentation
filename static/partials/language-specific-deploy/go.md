## Configure your Go application

### Mandatory configuration

Be sure that:

* Your application listens to the wild network **0.0.0.0**, not only `localhost` or `127.0.0.1`
* Your application listens on port **8080**
* You put your main code in a file named `main.go` (if you do not do that, Go will generate a library and not an executable)

Apart from listening on port 8080, there is nothing to change on your application.

### Go production build on Clever Cloud

* We automatically build and run your application, see [Build the application](#build-the-application).
* By default, we consider that your repository contains a single application. We put your application in `${GOPATH}/src/{app_id}` and then run `go get {app_id}`. Refer to [clevercloud/go.json settings](#clevercloud/go.json-settings) if you want to override this behaviour.
* By default, we deploy your application as a Go project named "<app_id>". You can find the app_id of your application under the environment variable `APP_ID`. Please refer to [environment injection](#environment-injection) to know how to query it in your application.
* The executable is run with the application's root as its current path. So if your application has a `static` folder at its root, it will be accessible via `./static` in your application.

## Build the application

To build your application, you can use one of the three methods available:

* `go modules`
* `go build`
* `go get` (default)

### Go modules

If your project is compatible with go modules, be sure that the `go.mod` file is in your git tree. Note that it **must** be at the root of your application (see the [`APP_FOLDER` environment variable if it isn't]({{< ref "doc/reference/reference-environment-variables.md" >}})

For now, you have to add the environment variable `CC_GO_BUILD_TOOL=gomod` to build using the go modules. In a future release, we will automatically
build with go modules if the `go.mod` file is present at the root of your git tree.

Your project's entrypoint should be in the same folder as the `go.mod` file and be named `main.go`. If it isn't, you have to specify it using the following environment variable:

`CC_GO_PKG=./path/to/entrypoint.go`

### Go build

If your project does not support `go modules`, it may include your vendored dependencies. In this case, `go build` must be used.

To use `go build`, you have to set the `CC_GO_BUILD_TOOL=gobuild` environment variable.
We will then deploy your project in a classic `GOPATH` hierarchy using `go build`.

The `CC_GO_PKG` environment variable can be used to define the main file of your application. Defaults to `main.go`.

### Go get

* If your application has submodules and imports them with their full path *or* your main project is an external package hosted, for instance on GitHub (like `github.com/me/myproject`), you can [define the environment variable](#setting-up-environment-variables-on-clever-cloud) `CC_GO_PKG=github.com/me/myproject`. We will now run `go get ${CC_GO_PKG}` instead of `go get <app_id>`.

Also, go get requires that you put your main code in a file named `main.go`. If you
do not do that, go will generate a library and not an executable. So if you get a `Nothing
listening on port 8080`, please check that your main file is named `main.go`.

You can also force the use of `go get` by setting the environment variable `CC_GO_BUILD_TOOL=goget`. This is currently the default.

**Note**: if you get a `Nothing listening on port 8080` error, please check that your main file is named `main.go`.

### Customize build using environment variables

You can customize the build process of your Go application using the following environment variables:

Variable | Usage
---------|------
`CC_GO_PKG` | Makes the deployer run `go get ${CC_GO_PKG}` instead of `go get <app_id>` or `go install ${CC_GO_PKG}` instead of `go install mypackage`.
`CC_GO_BUILD_TOOL` | Available values: `gomod`, `goget`, `gobuild`. Makes the deployer use `go modules`, `go get`, or `go build` to build your application. If not specified, defaults to `goget`.
`CC_GO_RUNDIR` | Makes the deployer use the specified directory to run your binary. If your application must be in `$GOPATH/src/company/project` for your vendored dependencies, set this variable to `company/project`.

### clevercloud/go.json

This configuration file is optional.

If you want to configure precisely your dependencies (e.g. have private libraries, or specific versions of some libraries), here is the way:

1. Make your repository have a `GOPATH` structure:

{{< filetree/container >}}
  {{< filetree/folder name="./" >}}
    {{< filetree/folder name="myapp" >}}
    {{< /filetree/folder >}}
    {{< filetree/folder name="foo" >}}
        {{< filetree/folder name="module1" >}}
        {{< /filetree/folder >}}
        {{< filetree/folder name="module2" >}}
        {{< /filetree/folder >}}
    {{< /filetree/folder >}}
    {{< filetree/folder name="module3" >}}
    {{< /filetree/folder >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

Here you have the modules `myapp`, `foo/module1`, `foo/module2` and `module3`.

2. Create a *clevercloud/go.json* file at the top of your repository:

{{< filetree/container >}}
  {{< filetree/folder name="./" >}}
    {{< filetree/folder name="clevercloud" >}}
      {{< filetree/file name="go.json" >}}
    {{< /filetree/folder >}}
    {{< filetree/folder name="src" >}}
      {{< filetree/folder name="myapp" >}}
      {{< /filetree/folder >}}
    {{< /filetree/folder >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

3. In the go.json file, put the following:

```json{linenos=table}
{
    "deploy": {
        "appIsGoPath": true,
        "main": "myapp"
    }
}
```

If `appIsGoPath` is present and equals `true`, then we consider that your repo root is the *GOPATH*.

The `main` field then becomes mandatory and must be the name of the module you want to run.

E.g. if you want to run `module1`, `main` must be `foo/module1`.

4. (Optional) Add a "execDir" field to the "deploy" object:

    ```json{linenos=table}
    {
        "deploy": {
            "appIsGoPath": true,
            "main": "myapp",
            "execDir": "src/myapp"
        }
    }
    ```

The `execDir` value must be relative to the root of your repo.

In the example above, we will run the application in the src/myapp directory.

{{< readfile file="env-injection.md" >}}

To access environment variables from your code, just get them from the environment with `PATH`: `os.Getenv("MY_VARIABLE")`.
