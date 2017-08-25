---
title: Deploy rust apps
shortdesc: Rust is a systems programming language that runs blazingly fast, prevents segfaults, and guarantees thread safety.
tags:
- rust
keywords:
- rust
- cargo
---

# Deploy Rust apps

<div class="panel panel-warning">
  <div class="panel-heading">
     <h4>Rust support is in private beta</h4>
  </div>
  <div class="panel-body">
    If you are interested in accessing the beta test, please contact the support.
  </div>
</div>

Clever Cloud allows you to deploy rust web applications. This page will explain
you how to set up your application to run it on our service.

You do not need to change a lot in your application, the *requirements* will
help you to configure your apps with some mandatory files to add, and
properties to setup.

## Overview

Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety. You can build rust web services with
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

### Rust channels

By default, your application is built with the latest stable version. If you
require beta, nightly or a specific rust version, you can set `RUSTUP_CHANNEL`
to `beta`, `nightly` or a specific version (eg. `1.13.0`). The build uses
`rustup` to select the rust version you need.

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
