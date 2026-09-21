---
title: Terraform provider 2.2.0
description: Deployed commit tracking and Haskell runtime in the Clever Cloud Terraform provider
date: 2026-09-14
tags:
  - addons
  - terraform
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Rémi Collignon-Ducret
    link: https://github.com/miton18
    image: https://github.com/miton18.png?size=40
excludeSearch: true
---

The [2.2.0 release](https://github.com/CleverCloud/terraform-provider-clevercloud/releases/tag/v2.2.0) of the Clever Cloud Terraform provider is available. When the `deployment` block of an application sets no `commit` or pins a hash, `deployment.commit` now reflects the commit running on the platform. With a pinned hash, a deployment made outside Terraform shows up as drift in the next plan.

The provider adds a `clevercloud_haskell` resource for the [Haskell](/doc/deploy/applications/haskell/) runtime. Before creating a Network Group member, the provider now checks that its FQDN ends with a platform DNS suffix, such as `cc-ng.cloud`.

Configuration providers now take their region from the API instead of always using `par`. This release also migrates the state of .NET, FrankenPHP, Rust and V applications created with older schema versions, and decodes Datadog drain URLs correctly.

- Learn more about [Terraform on Clever Cloud](/doc/tools/terraform/)
- Learn more about [Clever Cloud Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
