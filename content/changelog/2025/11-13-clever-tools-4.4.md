---
title: Clever Tools 4.4 is available
date: 2025-11-13
description: Clever Tools teams up with otoroshictl and improves drains management
tags:
  - clever-tools
  - cli
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
excludeSearch: true
---

[Clever Tools 4.4.0](https://github.com/CleverCloud/clever-tools/releases/tag/4.4.0) is available. In this release, the `drain` command uses API v4 with more reliable behavior and information about your logs drains. The `otoroshi` command comes with a new `get-config` subcommand to retrieve an Otoroshi configuration in YAML format, used by [otoroshictl](https://github.com/cloud-apim/otoroshictl). Thus, you can now easily add a Clever Cloud Otoroshi instance to your `otoroshictl` configuration and manage it with a CLI tool:

```bash
# Install otoroshictl with Rust's Cargo and enable operators/otoroshi command in Clever Tools:
cargo install otoroshictl
clever features enable operators

clever otoroshi get-config <otoroshi_id_or_name> | otoroshictl config import --current --stdin
otoroshictl resources get routes
```

## How to upgrade

To upgrade Clever Tools, [use your favorite package manager](/doc/cli/install/). For example with `npm`:

```
npm update -g clever-tools
clever version
```
