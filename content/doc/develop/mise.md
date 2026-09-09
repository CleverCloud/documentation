---
type: docs
weight: 65
linkTitle: Mise Package Manager
title: Mise Package Manager
description: Pin and install the tool versions your application needs at build time with mise on Clever Cloud
keywords:
- mise
- package manager
- tools
- versions
- tasks
- declarative
---

[Mise](https://mise.jdx.dev) is a tool version manager, an environment manager and a task runner in one file. Clever Cloud ships it on every runtime and runs it before your build.

## What a mise.toml unlocks

A deployment usually scatters its setup: a version pinned in a build hook, credentials mapped in a start script, a command typed in an environment variable. Mise collapses that into one committed file, which changes what you can do rather than only how it looks.

**Deploy software with no dedicated runtime.** On the [Linux runtime](/doc/deploy/applications/linux/), Mise installs a release, maps add-on credentials to the variables the software reads, and defines how to build and start it. That covers most self-hosted applications without writing a Dockerfile.

**Add a tool the runtime does not provide.** A Node.js application needing `jq`, a Python one needing a linter, a Go one needing `protoc`: one line in `[tools]`, installed on every build, on any runtime.

**Keep environments apart in the same repository.** `MISE_ENV` selects an extra configuration file, so a staging application and a production one share a `mise.toml` and differ by `mise.staging.toml` and `mise.production.toml`.

**Make a deployment reviewable.** Tools, environment mapping, build and run commands appear in one diff and travel with the branch, instead of living in the Console.

## Install tools

List what you need under `[tools]`:

```toml {filename="mise.toml"}
[tools]
node = "24"
jq = "1.7.1"
```

Before the build phase, Clever Cloud runs `mise trust` then `mise install` in the directory holding your `mise.toml`, and the tools land on the `PATH` for both the build and the running application. Versions accept an exact number, a fuzzy prefix such as `"3"`, or `"latest"`.

Prefer the runtime's own version variable when one exists, and derive the Mise version from it rather than pinning the same number twice:

```toml {filename="mise.toml"}
[tools]
node = "{{ env.CC_NODE_VERSION }}"
```

Mise also reads the version files your ecosystem already uses, `.tool-versions`, `.nvmrc`, `.python-version` or `go.mod` among others, and honours them alongside `mise.toml`. A `mise.toml` still has to exist for the platform to trigger the installation at all.

### Pick a backend

Beyond its own registry, Mise installs from several sources. Naming the backend in the tool key is enough:

```toml {filename="mise.toml"}
[tools]
"npm:cowsay" = "1.6.0"
"ubi:sharkdp/fd" = "10.2.0"
"github:drakkan/sftpgo" = "2.7.5"

["http:outline"]
version = "v1.9.2"
url = "https://github.com/outline/outline/archive/refs/tags/{{ version }}.tar.gz"
strip_components = 1
```

`ubi` and `github` fetch a release binary, `npm`, `pipx`, `cargo` and `go` install from a language registry, and `http` downloads and extracts an archive. Together they replace the `curl | tar` step most self-hosted software asks for, with a pinned version and a checksum.

A tool can also finish its own installation:

```toml {filename="mise.toml"}
[tools]
node = { version = "24", postinstall = "corepack enable" }
```

## Shape the environment

The `[env]` section does more than set values. It maps add-on credentials to the names your software expects, reading platform variables through templating:

```toml {filename="mise.toml"}
[env]
DATABASE_URL = "{{ env.POSTGRESQL_ADDON_URI }}"
AWS_ACCESS_KEY_ID = "{{ env.CELLAR_ADDON_KEY_ID }}"
SERVER_PORT = "{{ env.PORT }}"
```

Four directives cover the cases a template cannot:

```toml {filename="mise.toml"}
[env]
_.path = ["./bin"]                  # prepend directories to PATH
_.file = ".env.deploy"              # load a dotenv, JSON, YAML or TOML file
_.source = "./scripts/env.sh"       # run a script and keep what it exports
LOG_LEVEL = { default = "info" }    # only if nothing else set it
API_TOKEN = { value = "…", redact = true }
```

`redact` keeps a value out of the deployment logs while the application still receives it, which matters for anything built from a secret. `{ required = true }` does the opposite and fails the deployment when a variable is missing, turning a silent misconfiguration into an explicit error.

Reusable values live in `[vars]`, and stay out of the application environment:

```toml {filename="mise.toml"}
[vars]
release = "2.1.0"

[env]
INSTALL_DIR = "{{ env.APP_HOME }}/releases/{{ vars.release }}"
```

> [!NOTE] Where the environment applies
> `[env]` applies to the processes Mise starts. It reaches your application on the Linux runtime, where Mise launches it through the `run` task below. On the other runtimes the platform starts the application itself, so declare those variables with `clever env set` instead.

### Split configuration per environment

Set `MISE_ENV` on an application and Mise loads `mise.<value>.toml` on top of `mise.toml`. One repository then serves several applications:

```bash
clever env set MISE_ENV production
```

```toml {filename="mise.production.toml"}
[env]
LOG_LEVEL = "warn"
NODE_ENV = "production"
```

## Declare the build and run commands

Name a task `build` or `run`, and the [Linux runtime](/doc/deploy/applications/linux/) uses it as the build command and the start command:

```toml {filename="mise.toml"}
[tasks.build]
description = "Compile the application"
run = "gleam deps download && gleam build"

[tasks.run]
description = "Start the web server on 0.0.0.0:8080"
run = "gleam run"
```

The deployment logs name what they picked:

```text
Build command defined by Mise, using it for the build phase
Run command defined by Mise, using it to launch the application
```

### Compose several steps

`depends` splits a long build into named tasks. Dependencies run before the task, and Mise runs them concurrently rather than in the order you list them, so they must not rely on each other:

```toml {filename="mise.toml"}
[tasks.deps]
run = "yarn install --immutable"

[tasks.assets]
run = "yarn build:assets"

[tasks.build]
depends = ["deps", "assets"]
run = "yarn build:server"
```

`sources` and `outputs` let Mise skip a task whose inputs have not changed. This helps a task invoked several times inside one build, but not across deployments: each one starts from a fresh instance, so the task runs again.

### Write tasks as files

Anything longer than a couple of lines reads better as a script. Two forms exist, and the platform detects both.

Point a TOML task at a file:

```toml {filename="mise.toml"}
[tasks.report]
file = "scripts/report.sh"
```

Or drop an executable in `mise-tasks/`, named after the task, with its description in a header comment:

```bash {filename="mise-tasks/build"}
#!/usr/bin/env bash
#MISE description="Install dependencies and build assets"
set -euo pipefail
corepack enable
yarn install --immutable
yarn build
```

Run `chmod +x mise-tasks/*` before committing. A `mise.toml` is not needed for tasks alone, only as soon as you install tools.

### Know which command wins

Three sources can define the build and run commands, and the first that answers wins:

1. `CC_BUILD_COMMAND` and `CC_RUN_COMMAND`, set as environment variables
2. Mise tasks named `build` and `run`
3. A `Makefile` with `build` and `run` targets

Setting `CC_RUN_COMMAND` therefore overrides a Mise `run` task without removing it, which is a practical way to start a one-off command on an existing application.

## Configure the integration

| Variable            | Effect                                                                                    |
| ------------------- | ----------------------------------------------------------------------------------------- |
| `CC_MISE_FILE_PATH` | Path to the configuration file, relative to your application root, `mise.toml` by default |
| `CC_DISABLE_MISE`   | Set to `true` to skip tool installation and task detection entirely                       |
| `MISE_ENV`          | Name of the extra `mise.<value>.toml` file to load                                        |

`CC_MISE_FILE_PATH` also sets the directory Mise works from, since the platform passes the file's parent directory to `mise --cd`. Pointing it at `config/mise.toml` therefore runs your tasks from `config/`, not from the application root.

## Troubleshooting

A configuration error anywhere in the file stops Mise before it lists the tasks, and the deployment fails on the consequence rather than the cause:

```text
[ERROR] You must define a CC_RUN_COMMAND or a 'run' task with Makefile or Mise
```

Read the lines above it, where Mise reports what it could not parse. A dotenv file loaded through `_.file` is a frequent culprit, since a value containing spaces has to be quoted:

```bash {filename=".env.deploy"}
GREETING="loaded from the dotenv file"
```

Values are rendered with templates, not by the shell, so `$OTHER_VAR` stays literal. Use `{{ env.OTHER_VAR }}` instead.

- [Linux runtime](/doc/deploy/applications/linux/)
- [Mise configuration reference](https://mise.jdx.dev/configuration.html)
- [Mise tasks](https://mise.jdx.dev/tasks/)
