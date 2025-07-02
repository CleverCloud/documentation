---
title: mdBook
description: Build your website with the mdBook Static Site Generator (SSG) and host it on Clever Cloud. No dedicated runner needed.
tags:
- guides
keywords:
- mdbook
- rust
- static
- ssg
- html
- js
- css
- website
type: "docs"
comments: false
draft: false
---
If you need an example source code, init a new project (you'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Rust](https://www.rust-lang.org/tools/install)):
```bash
cargo install mdbook
mdbook init myStaticApp --title="my mdBook" --ignore=git
```

{{< content "language-specific-deploy/create-static" >}}

## Configure environment variables
Next, we configure the application with a medium build instance to quickly generate static files. The host instance is nano-sized, enough for a simple website. As Clever Cloud is based on standards, you only need to define a few variables:
```bash
clever scale --build-flavor M
clever scale --flavor nano

clever env set CC_WEBROOT "/book"
clever env set CC_OVERRIDE_BUILDCACHE "/book"
clever env set CC_PRE_BUILD_HOOK "cargo install mdbook"
clever env set CC_POST_BUILD_HOOK "/home/bas/.cargo/bin/mdbook build"
```

{{< content "git-push" >}}