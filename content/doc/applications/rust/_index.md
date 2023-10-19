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


{{< readfile file="/content/partials/create-application.md" >}}

{{< readfile file="/content/partials/set-env-vars.md" >}}

{{< readfile file="/content/partials/language-specific-deploy/rust.md" >}}

{{< readfile file="/content/partials/deploy-git.md" >}}

### Deployment Video

<iframe width="853" height="480" src="https://www.youtube.com/embed/mz_8jzrM13Y?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>

{{< readfile file="/content/partials/link-addon.md" >}}

{{< readfile file="/content/partials/more-config.md" >}}
