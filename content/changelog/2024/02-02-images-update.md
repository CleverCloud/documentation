---
title: February 2024 images update (part 1)
date: 2024-02-02
tags:
  - images
  - update
  - security
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: An in-depth work leading to faster updates
aliases:
- /changelog/2024-02-02-images-update
excludeSearch: true
---

Over the past few months, we've overhauled the way we build our applications and add-ons images from tooling to included binaries. We'll deliver soon the first public milestone of this project, which will leads us to more frequent releases.

In the meantime, we've updated Docker, Erlang, Go, Haskell, Ruby and Rust images into production with no impact for our users. They include security patches and now use Linux kernel 6.7.1, OpenSSL 3.2.1 and Node.js 20.11.0 by default. For the latter, you can change it in the updated images via the `CC_NODE_VERSION` [environment variable](/developers/doc/reference/reference-environment-variables/#commons-to-all-applications). Other changes are as follows:

- **Docker**:
  - moby 25.0.2
  - runc 1.1.12
  - containerd 1.7.13
  - docker-cli 25.0.2
- **Erlang**:
  - elixir 1.15.7, erlang 26.2.1
  - elixir 1.16.0, erlang 26.2.1
- **Rust**:
  - Stable: 1.75.0
  - Beta: 1.76.0
  - Nightly: 1.77.0
- **Go**:
  - go 1.21.6

Other images will be updated the same way in the coming days.
