---
type: docs
title: Rust
shortdesc: Rust is a system programming language that runs blazingly fast, prevents segfaults, and guarantees thread safety.
tags:
- deploy
keywords:
- rust
- cargo
str_replace_dict:
  "@application-type@": "Rust"
type: docs
aliases:
- /developers/doc/rust/rust
- /doc/deploy/application/rust
- /doc/deploy/application/rust/rust
- /doc/getting-started/by-language/rust
- /doc/partials/language-specific-deploy/rust
- /doc/rust/rust
comments: false
---

## Overview

Rust is a system programming language that runs blazingly fast, prevents segfaults, and guarantees thread safety. You can build Rust web services with frameworks like [Actix](https://actix.rs/) or [Iron](https://github.com/iron/iron).

Clever Cloud allows you to deploy Rust web applications. This page will explain you how to set up your application to run it on our service.

{{< content "create-application" >}}

{{< content "set-env-vars" >}}

## Configure your Rust application

### Mandatory configuration

Make sure that:

* you have pushed in **master** branch
* you listen on port **8080**
* you have committed `Cargo.lock`
* you have at least one binary target in `Cargo.toml`

The result of `cargo build --release --locked` must be an executable which starts a web server listening on `0.0.0.0:8080`.

For instance, a minimal [iron](https://github.com/iron/iron) application can look like this:

```rust
extern crate iron;

use iron::prelude::*;
use iron::status;

fn main() {
    fn hello_world(_: &mut Request) -> IronResult<Response> {
        Ok(Response::with((status::Ok, "Hello World!")))
    }

    let _server = Iron::new(hello_world).http("0.0.0.0:8080").unwrap();
    println!("On 8080");
}
```

### Multiple binary targets

If your `Cargo.toml` defines multiple targets, you must specify the one you want to run, with the `CC_RUST_BIN` environment variable.
If `CC_RUST_BIN` is specified, then the executable produced by this target is used to start the application.

### Custom run command

If you need to run a custom command (or just pass options to the program), you can specify it through the `CC_RUN_COMMAND` [environment variable](#setting-up-environment-variables-on-clever-cloud).

For instance, you can have `CC_RUN_COMMAND=./target/release/myapp <options>`.

### Dependencies

Make sure to list all your dependencies in `Cargo.toml`. For the example above, you need:

```toml
[package]
name = "my-app"
version = "0.1.0"
authors = []

[dependencies]
iron = "0.4.0"
```

### Cached dependencies

#### Enabling dependencies caching

You can enable dependencies caching by adding the `CC_CACHE_DEPENDENCIES=true` [environment variable](#setting-up-environment-variables-on-clever-cloud) in your application.

#### Disabling dependencies caching

You can disable dependencies caching completely by removing the `CC_CACHE_DEPENDENCIES` environment variable from the Clever Cloud console, in the **Environment variables** menu of your application. Or by setting it to `CC_CACHE_DEPENDENCIES=false`.

To fully remove cached dependencies, you have to rebuild your application from scratch. You can select "rebuild and restart" from the Clever Cloud console or launch `clever restart --without-cache` with the Clever Tools CLI.

### Private dependencies

If you use dependencies on a private git repository inside your project, it needs a bit of configuration until [this cargo issue](https://GitHub.com/rust-lang/cargo/issues/1851) has been resolved.

First, you need to use the `HTTPS` url as the git url for your dependency in your `Cargo.toml`:

`private-dep = { git = "https://github.com/user/my-private-dep.git" }`

Then, you need to create a personal access token. It allows to not use your password:

* `Github`: <https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/>
* `GitLab`: <https://docs.gitlab.com/user/profile/personal_access_tokens/> (API rights are needed)

Once you have the token, we need to tell Git to use a credential store. For that, we are going to create it.

Create a `clevercloud/pre-build.sh` file at the root of your application and paste:

```bash
#! /usr/bin/env bash

git config --global credential.helper store
echo "https://${GIT_USERNAME}:${GIT_PASSWORD}@gitlab.com" > ~/.git-credentials
chmod 600 ~/.git-credentials
```

If you have multiple private repositories, add them accordingly.

Now, go into the environment variables page of your application and create those environment variables:

* `GIT_USERNAME`: your Github / gitlab / other username
* `GIT_PASSWORD`: your Github / gitlab / other password
* `CC_PRE_BUILD_HOOK`: clevercloud/pre-build.sh
* `CC_POST_BUILD_HOOK`: rm /home/bas/.git-credentials

This adds the git configuration before the build start and it cleans it after the build has been done.

### Rust channels

By default, your application is built with the latest stable rust version. If you require beta, nightly or a specific Rust version, you can set `CC_RUSTUP_CHANNEL` [environment variable](#setting-up-environment-variables-on-clever-cloud) value to `beta`, `nightly` or a specific version (eg. `1.36.0`).

The build uses `rustup` to select the Rust version you need.

### Cargo features

You can enable specific features for your crate by settings the `CC_RUST_FEATURES`
environment variable to the list of features to enable.

To access environment variables from your code, just get them from the environment with `std::env::var(<KEY_NAME>)`.

If some environment variables are critical to your application, here is an approach you can use:

```rust
use std::env;

fn main() {
    let my_config_value = env::var("MY_VAR").expect("Missing env var `MY_VAR`");

    something_that_runs_a_web_server(my_config_value);
}
```

This loads the environment variable in your `main` function and use `.expect` to fail early. This way, the application will refuse to start with an helpful error message if `MY_VAR` is not defined.

{{< content "deploy-git" >}}

### Deployment Video

{{< youtube id="mz_8jzrM13Y" >}}

{{< content "link-addon" >}}

{{< content "more-config" >}}

{{< content "url_healthcheck" >}}

