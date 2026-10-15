---
title: Terraform provider 3.0.0
description: Redeployment on new commits, API token authentication, tags and a Java Maven resource in the Clever Cloud Terraform provider
date: 2026-10-15
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

The [3.0.0 release](https://github.com/CleverCloud/terraform-provider-clevercloud/releases/tag/v3.0.0) of the Clever Cloud Terraform provider is available. Its major version comes from a change in how applications get deployed. When the `deployment` block of an existing application sets no `commit`, every `terraform plan` now reads the repository HEAD. A new commit shows up as a diff and the next apply deploys it, instead of waiting for an unrelated change to the resource.

The provider opens a local `file://` repository and only lists the references of a remote one, without cloning it. If the repository is unreachable, the plan goes on with a warning. `deployment.repository` now requires an `https://`, `http://` or `file://` scheme.

The provider also authenticates with an [API token](/doc/manage/cli/#tokens), set in `CLEVER_API_TOKEN` or in the `api_token` parameter, as an alternative to OAuth credentials. An API token can't push code over Git, so applications that push code through a `deployment` block still need OAuth credentials. Every application and add-on resource now accepts `tags`, and a `clevercloud_java_maven` resource joins the [Java](/doc/deploy/applications/java/java-maven/) WAR and JAR ones:

```hcl {filename="main.tf"}
resource "clevercloud_java_maven" "inventory_api" {
  name               = "inventory-api"
  region             = "par"
  min_instance_count = 1
  max_instance_count = 2
  smallest_flavor    = "XS"
  biggest_flavor     = "M"
  tags               = ["env:production", "team:platform"]
}
```

Pushing a large local repository now streams it with bounded memory, works from a linked Git worktree, and no longer retries a push rejected as too large. You can import a `clevercloud_cellar_bucket` with its Cellar ID and name, such as `cellar_xxx/my-bucket`, and a Rust application rebuilds without its build cache when its features change.

This release follows 2.3.0, which added node auto-provisioning to Kubernetes clusters through the `node_autoprovisioning` attribute. It also writes environment maps into configurations generated with `BYPASS_SENSITIVE_IMPORTS=true`, retries server errors instead of failing, and no longer replaces imported Elasticsearch add-ons. To upgrade, set the provider constraint to `~> 3.0` and run `terraform init -upgrade`.

- Learn more about [Terraform on Clever Cloud](/doc/tools/terraform/)
- Learn more about [Clever Cloud Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
