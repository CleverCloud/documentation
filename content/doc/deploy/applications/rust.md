---
type: docs
linkTitle: Rust
title: Rust application runtime
description: Build and deploy Rust applications on Clever Cloud with Cargo, from a single binary to a workspace, with the toolchain of your choice
keywords:
- axum
- actix web
- cargo
- rocket
- rust app hosting
- rust cloud
- rustup
aliases:
- /applications/rust
- /deploy/application/rust/rust
- /doc/applications/rust
- /doc/deploy/application/rust
- /doc/deploy/application/rust/rust
- /doc/getting-started/by-language/rust
- /doc/partials/language-specific-deploy/rust
- /doc/rust
- /doc/rust-hosting
- /doc/rust/rust
- /rust-hosting
---

## Overview

[Rust](https://www.rust-lang.org) is a compiled language focused on performance and memory safety. Clever Cloud builds your [Cargo](https://doc.rust-lang.org/cargo/) project in release mode and starts the binary it produces. It works with web frameworks such as [Axum](https://github.com/tokio-rs/axum), [Actix Web](https://actix.rs), or [Rocket](https://rocket.rs).

## Create your Rust application

To create a new Rust application, use the [Clever Cloud Console](https://console.clever-cloud.com) or [Clever Tools](https://github.com/CleverCloud/clever-tools):

```bash
clever create --type rust
```

- [Learn more about Clever Tools](/doc/manage/cli/)
- [Learn more about Clever Cloud application deployment](/doc/getting-started/#create-an-application-step-by-step)

## Configure your Rust application

### Mandatory needs

A Rust application needs:

- A `Cargo.toml` file with at least one binary target, at the root of the project or of the folder set in `APP_FOLDER`
- A committed `Cargo.lock` file: the build runs with `--locked`, so it fails if `Cargo.lock` is missing or out of date
- A web server listening on `0.0.0.0:8080`, the port also available in the `PORT` environment variable, unless the application runs as a [Clever Task](#rust-binaries-as-clever-tasks)

For instance, a minimal [Axum](https://github.com/tokio-rs/axum) application:

```toml {filename="Cargo.toml"}
[package]
name = "my-app"
version = "0.1.0"
edition = "2024"

[dependencies]
axum = "0.8"
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
```

```rust {filename="src/main.rs"}
use axum::{Router, routing::get};

#[tokio::main]
async fn main() {
    let port = std::env::var("PORT").unwrap_or_else(|_| "8080".to_string());
    let app = Router::new().route("/", get(|| async { "Hello from Rust on Clever Cloud" }));

    let listener = tokio::net::TcpListener::bind(format!("0.0.0.0:{port}")).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
```

Run `cargo generate-lockfile` or `cargo build` to create `Cargo.lock`, then commit it with your code. Your application reads its [environment variables](/doc/develop/common-configuration/environment-variables/) with `std::env::var`, such as the credentials of the add-ons you link to it.

### Build phase

On a new build, Clever Cloud selects the [Rust toolchain](#rust-version-and-tools) and runs the pre-build [hook](/doc/develop/common-configuration/build-hooks/). It then copies the sources of your dependencies with `cargo vendor --locked`, and builds your project:

```bash
cargo build --release --locked
```

Cargo reads its usual environment variables during the build. Set `RUSTFLAGS` or a [Cargo variable](https://doc.rust-lang.org/cargo/reference/environment-variables.html#configuration-environment-variables) such as `CARGO_PROFILE_RELEASE_LTO` in the environment of your application to change how it compiles. With `CC_TROUBLESHOOT=true`, Cargo also runs with `--verbose`.

Compiling Rust needs memory and CPU time. If your builds fail for lack of memory or take too long, enable a [dedicated build instance](/doc/develop/common-configuration/lifecycle/#edit-application-configuration) larger than your application instances. Most Rust projects need at least an `S` build instance:

```bash
clever scale --build-flavor S
```

### Select the binary to start

Clever Cloud looks for binary targets in the packages `cargo build` builds: your package, or the default members of your workspace. It starts:

1. The binary set in `CC_RUST_BIN`
2. Otherwise, the `default-run` binary of the `[package]` section
3. Otherwise, the only binary target of the project

If none of these rules finds a single binary, the deployment fails and asks you to set `default-run` or `CC_RUST_BIN`. For a project with `src/bin/web.rs` and `src/bin/worker.rs`, start the `web` binary with:

```toml {filename="Cargo.toml"}
[package]
name = "my-app"
version = "0.1.0"
edition = "2024"
default-run = "web"
```

The selection doesn't limit the build: `cargo build` compiles every binary of these packages. Cargo skips a binary with `required-features` until you enable these features: set them with `CC_RUST_FEATURES`, otherwise the binary doesn't exist and the application fails to start.

### Enable Cargo features

Set the features to enable in `CC_RUST_FEATURES`, with a comma or a space between them. Clever Cloud passes them to `--features`, and the default features stay enabled. For features `json` and `tls` declared in the `[features]` section of `Cargo.toml`:

```bash
clever env set CC_RUST_FEATURES "json,tls"
```

In a workspace, prefix a feature with its package name, such as `my-app/json`.

### Rust version and tools

The build uses the `stable` channel by default. The image includes the `stable`, `beta`, and `nightly` toolchains, and rustup downloads any other version during the build. To use another one, set `CC_RUSTUP_CHANNEL` to a channel, a version, or a dated nightly:

```bash
clever env set CC_RUSTUP_CHANNEL 1.88.0
```

A [`rust-toolchain.toml`](https://rust-lang.github.io/rustup/overrides.html#the-toolchain-file) file at the root of the project takes precedence over `CC_RUSTUP_CHANNEL`: rustup installs the toolchain it names during the build. Clever Cloud deletes the legacy `rust-toolchain` file, without extension, before the build.

The image also includes `clang`, `lld`, `pkg-config`, and OpenSSL, for crates that build C code or link system libraries. To install other tools, such as a CLI your build needs, use [Mise](/doc/develop/mise/).

### Build with cargo install

Set `CC_RUST_INSTALL=true` to build with `cargo install` instead of `cargo build`. Clever Cloud installs the binaries of the package holding the selected one in `/home/bas/.local/bin`, which is in the `PATH`. It then removes the release build artifacts with `cargo clean --release`, which keeps the build cache smaller.

### Custom run command

By default, Clever Cloud starts the selected binary without arguments. To pass arguments, or start something else, set `CC_RUN_COMMAND`. It runs from the folder of your project, the one set in `APP_FOLDER` if any. For a `web` binary that accepts a `--workers` option:

```bash
clever env set CC_RUN_COMMAND "./target/release/web --workers 4"
```

With `CC_RUST_INSTALL=true`, call the binary by its name, such as `web --workers 4`.

### Caches

After a successful build of an application, Clever Cloud keeps a build cache of the commit. Restarting the application without a code change reuses it and skips the build. To build again from scratch, restart without the cache (rebuild):

```bash
clever restart --without-cache
```

With `CC_CACHE_DEPENDENCIES=true`, Clever Cloud also keeps the Cargo home folder and the sources `cargo vendor` copied between commits. The next builds download fewer crates, but still compile them.

### Private dependencies

To use a crate from a private Git repository, declare it with its HTTPS URL:

```toml {filename="Cargo.toml"}
[dependencies]
private-dep = { git = "https://github.com/my-org/private-dep.git" }
```

Cargo needs a token to [fetch this repository](https://doc.rust-lang.org/cargo/appendix/git-authentication.html). Create a read-only one. On GitHub, use a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) with read access to the contents of the repository. On GitLab, use a [personal access token](https://docs.gitlab.com/user/profile/personal_access_tokens/) with the `read_repository` scope. Then give this token to Git with a pre-build hook, which runs before Cargo fetches the dependencies. Make the script executable with `chmod +x clevercloud/pre-build.sh`:

```bash {filename="clevercloud/pre-build.sh"}
#!/bin/bash
git config --global credential.helper store
echo "https://${GIT_USERNAME}:${GIT_TOKEN}@github.com" >> ~/.git-credentials
chmod 600 ~/.git-credentials
```

For a GitLab repository, replace `github.com` with `gitlab.com`. Then set `GIT_USERNAME`, `GIT_TOKEN`, and `CC_PRE_BUILD_HOOK=clevercloud/pre-build.sh` in the environment of your application.

To remove the credentials after a successful build, set `CC_POST_BUILD_HOOK="rm ~/.git-credentials"`.

## Rust binaries as Clever Tasks

A Rust binary can run as a [Clever Task](/doc/develop/tasks/), such as a job or a migration. Clever Cloud builds the project, then runs `CC_RUN_COMMAND` instead of starting a web server. A task needs `CC_RUN_COMMAND`, even with a single binary or a `default-run`. Configure an application as Tasks from the `Information` panel in [the Console](https://console.clever-cloud.com) or with [Clever Tools](/doc/manage/cli/applications/#tasks), here for a `worker` binary that runs once with `--once`:

```bash
clever create --type rust --task "./target/release/worker --once"
clever deploy # or clever restart if there is no code change
```

{{% content "url_healthcheck" %}}
{{% content "request-flow" %}}
