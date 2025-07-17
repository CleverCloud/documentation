---
title: "Lagging server: our Sōzu testing tool available as a Rust Crate"
date: 2024-08-01
tags:
  - sōzu
  - tools
authors:
  - name: Emmanuel Bosquet
    link: https://github.com/Keksoj
    image: https://github.com/Keksoj.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
description: n2 is the new n1
aliases:
- /changelog/2024-08-01-lagging-server-crate
excludeSearch: true
---

When we release new versions of our reverse proxy [Sōzu](https://www.sozu.io), we now systematically run performances tests. To conduct some of them directly from our CI, we developed a small tool: Lagging Server. It's open source, and now [available as a Rust crate](https://crates.io/crates/lagging_server) anyone can use.

* Learn more about [Lagging Server](https://github.com/CleverCloud/lagging_server) {{< icon "github" >}}