---
title: Deploy Rust apps
shortdesc: Rust is a systems programming language that runs blazingly fast, prevents segfaults, and guarantees thread safety.
tags:
- rust
keywords:
- rust
- cargo
---

<div class="panel panel-warning">
  <div class="panel-heading">
     <h4>Rust support is in beta</h4>
  </div>
  <div class="panel-body">
    If you encounter an issue, please contact the support.
  </div>
</div>

Clever Cloud allows you to deploy Rust web applications. This page will explain
you how to set up your application to run it on our service.

You do not need to change a lot in your application, the *requirements* will
help you to configure your apps with some mandatory files to add, and
properties to setup.

## Overview

Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety. You can build Rust web services with
frameworks like [Iron](http://ironframework.io/)

## Create an application

Refer to the page [Deploy an application on Clever Cloud](/doc/clever-cloud-overview/add-application/).

## Necessary information

Be sure that:

* you have pushed in <b>master branch</b>
* you listen on <b>port 8080</b>
* you have committed `Cargo.lock`
* you have at least one binary target in `Cargo.toml`

## Requirements

The result of `cargo build --release --locked` must be an executable which
starts a web server listening on `0.0.0.0:8080`.

For instance, a minimal iron application can look like this:

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

If your `Cargo.toml` defines multiple targets, you must specify the one you
want to run, with the `CARGO_BIN` environment variable. If `CARGO_BIN` is
specified, then the executable produced by this target is used to start the
application.

### Dependencies

Make sure to list all your dependencies in `Cargo.toml`. For the example
above, you need:

```toml
[package]
name = "my-app"
version = "0.1.0"
authors = []

[dependencies]
iron = "0.4.0"
```

Compiled dependencies are cached by default to speed up deployments. You can
disable dependencies caching completely by removing the `CACHE_DEPENDENCIES`
environment variable. If you want to rebuild your application from scratch,
you can select "rebuild and restart" from the console or launch `clever
restart --without-cache` from CLI.

### Private dependencies

If you use dependencies on a private git repository inside your project, it needs a bit of configuration until
[this cargo issue](https://github.com/rust-lang/cargo/issues/1851) has been resolved

First, you need to use the `HTTPS` url as the git url for your dependency in your `Cargo.toml`:

`private-dep = { git = "https://github.com/user/my-private-dep.git" }`

Then, you need to create a personal access token. It allows to not use your password:
- `Github`: https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
- `Gitlab`: https://docs.gitlab.com/ce/user/profile/personal_access_tokens.html (API rights are needed)

Once you have the token, we need to tell Git to use a credential store. For that, we are going to create it.

Create a `clevercloud/pre-build.sh` file at the root of your application and paste:

```bash
#!/usr/bin/env bash

git config --global credential.helper store
echo "https://${GIT_USERNAME}:${GIT_PASSWORD}@gitlab.com" > ~/.git-credentials
chmod 600 ~/.git-credentials
```

If you have multiple private repositories, add them accordingly.

Now, go into the environment variables page of your application and create those environment variables:
- `GIT_USERNAME`: your github / gitlab / other username
- `GIT_PASSWORD`: your github / gitlab / other password
- `CC_PRE_BUILD_HOOK`: clevercloud/pre-build.sh
- `CC_POST_BUILD_HOOK`: rm /home/bas/.git-credentials

It adds the git configuration before the build start and it cleans it after the build has been done.

### Rust channels

By default, your application is built with the latest stable version. If you
require beta, nightly or a specific Rust version, you can set `RUSTUP_CHANNEL`
to `beta`, `nightly` or a specific version (eg. `1.13.0`). The build uses
`rustup` to select the Rust version you need.

## Environment injection

Clever Cloud can inject environment variables that are defined in the
dashboard and by add-ons linked to your application.

You can access environment variables with `std::env::var(<KEY_NAME>)`.

If environment variables are needed for your application to work properly, the
best solution is to load them in your `main` function and use `.expect` to
fail early with a descriptive error.

```rust
use std::env;

fn main() {
    let my_config_value = env::var("MY_KEY").expect("Missing env var `MY_KEY`");

    something_that_runs_a_web_server(my_config_value);
}
```

For more information, you can read about [environment variables on Clever
Cloud](/doc/admin-console/environment-variables/).

## Deploy on Clever Cloud

Application deployment on Clever Cloud is via Git. Follow [these
steps](/doc/clever-cloud-overview/add-application/) to deploy your
application.

## Deployment Video

<iframe width="853" height="480" src="https://www.youtube.com/embed/mz_8jzrM13Y?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
