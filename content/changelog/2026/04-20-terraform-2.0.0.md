---
title: Terraform provider 2.0.0
description: The Clever Cloud Terraform provider 2.0.0 manages the lightweight Static runtime and renames the Static with Apache resource
date: 2026-04-20
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

The [2.0.0 release](https://github.com/CleverCloud/terraform-provider-clevercloud/releases/tag/v2.0.0) of the Clever Cloud Terraform provider is available. It brings a breaking change: `clevercloud_static` now manages the lightweight [Static](/doc/deploy/applications/static/) runtime, without Apache. Applications running [Static with Apache](/doc/deploy/applications/static-apache/) move to the new `clevercloud_static_apache` resource.

If you manage a Static with Apache application with `clevercloud_static`, rename the resource and add a `moved` block, so Terraform updates the state without recreating the application. Moving state between resource types requires Terraform 1.8 or later:

```hcl
moved {
  from = clevercloud_static.website
  to   = clevercloud_static_apache.website
}

resource "clevercloud_static_apache" "website" {
  # Keep the configuration you had before
}
```

`terraform plan` then shows the move with no other change, and `terraform apply` saves it to the state. Without this block, the next plan stops with a `Resource variant mismatch` error before any change applies. This release also fixes the PostgreSQL state upgrade and adds debug logs for environment variable changes.

- Learn more about [Clever Cloud Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
