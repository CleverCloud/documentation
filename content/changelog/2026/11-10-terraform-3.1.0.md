---
title: Terraform provider 3.1.0
description: Runtime variables become attributes, and Kubernetes clusters get their version, control plane topology, persistent storage, and tags in the Clever Cloud Terraform provider
date: 2026-11-10
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

The [3.1.0 release](https://github.com/CleverCloud/terraform-provider-clevercloud/releases/tag/v3.1.0) of the Clever Cloud Terraform provider is available. Application resources now expose most variables of their runtime as attributes, from Docker to V, and the documentation of each attribute names the variable it sets. Variables without an attribute stay in `environment`. For example, `clevercloud_nodejs` gains `node_version`, `registry_basic_auth`, and `bun_install_cache_dir`:

```hcl {filename="main.tf"}
resource "clevercloud_nodejs" "storefront" {
  name               = "storefront"
  region             = "par"
  min_instance_count = 1
  max_instance_count = 2
  smallest_flavor    = "XS"
  biggest_flavor     = "M"
  node_version       = "24"
  package_manager    = "pnpm"
}
```

> [!NOTE] Move these variables out of `environment`
> The `environment` attribute now refuses a variable that an attribute of the resource manages, such as `CC_NODE_VERSION` or `CC_PRE_BUILD_HOOK`. Set through `environment`, these variables moved to their attribute on the next read, and the plan never converged. `terraform validate` and `terraform plan` now fail on each of them: find its attribute in the documentation of the resource.

The provider deprecates two attributes backed by variables the platform ignores, which have no effect: `integrations.redirectionio.backend_port`, and the `static_webroot` attribute of Ruby applications, replaced by `static_files_path` and `static_url_prefix`. Remove them from your configuration: a future release removes them.

A `clevercloud_kubernetes` cluster accepts a `version`, checked at plan time, and moves in place. A move to an older version warns that Kubernetes doesn't support downgrades. The `topology` attribute sets the control plane, as `ALL_IN_ONE`, `DEDICATED_COMPUTE`, or `DISTRIBUTED` with sized components. The cluster also gets `persistent_storage` and `tags`, and stays in the state if its creation fails:

```hcl {filename="main.tf"}
resource "clevercloud_kubernetes" "platform" {
  name               = "platform"
  version            = "1.36"
  persistent_storage = true
  tags               = ["env:prod"]

  topology = {
    type               = "DEDICATED_COMPUTE"
    flavor             = "S"
    replication_factor = 3
  }
}
```

Changing the `topology` of an existing cluster replaces it, with every workload and volume it holds: the plan warns about it, and `lifecycle { prevent_destroy = true }` protects a cluster you can't lose.

Add-on resources, except the generic `clevercloud_addon`, now refuse an import with their add-on ID (`addon_xxx`), and the error gives the real ID to use. Network Group members created for database add-ons now use their real ID, so their domain name resolves. To upgrade, run `terraform init -upgrade` with the `~> 3.0` constraint.

- Learn more about [Terraform on Clever Cloud](/doc/tools/terraform/)
- Learn more about [Clever Cloud Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
