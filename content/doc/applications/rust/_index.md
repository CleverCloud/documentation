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
- /doc/applications/rust
comments: false
---

## Overview

Rust is a system programming language that runs blazingly fast, prevents segfaults, and guarantees thread safety. You can build Rust web services with frameworks like [Actix](https://actix.rs/) or [Iron](https://github.com/iron/iron).

Clever Cloud allows you to deploy Rust web applications. This page will explain you how to set up your application to run it on our service.


{{< readfile file="create-application.md" >}}

{{< readfile file="set-env-vars.md" >}}

{{< readfile file="language-specific-deploy/rust.md" >}}

{{< readfile file="deploy-git.md" >}}

### Deployment Video

{{< youtube id="mz_8jzrM13Y" >}}

{{< readfile file="link-addon.md" >}}

{{< readfile file="more-config.md" >}}
