---
type: docs
weight: 190
linkTitle: Terraform
title: Terraform & OpenTofu provider
description: Declare Clever Cloud applications, add-ons and networking as code with the official Terraform and OpenTofu provider
keywords:
- terraform
- opentofu
- infrastructure as code
- provider
- automation
- support matrix
aliases:
- /doc/products-support
- /doc/reference/products-support
- /doc/tools/products-support
---

The [`CleverCloud/clevercloud`](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest) provider declares Clever Cloud resources as code. It covers 45 resource types, from every application runtime to databases, storage, log drains, Network Groups, Kubernetes clusters and OAuth consumers, and works with both Terraform and OpenTofu.

## What it unlocks

**Reproducing an environment.** A staging stack becomes a module you instantiate twice with different variables, instead of a procedure someone follows by hand. What differs between environments is visible in a `.tfvars` file rather than buried in two Consoles.

**Catching drift.** A change made outside the code shows up in the next plan. Setting an environment variable with the CLI on a managed application produces a diff:

```text
# clevercloud_nodejs.app will be updated in-place
Plan: 0 to add, 1 to change, 0 to destroy.
```

**Wiring resources together.** An add-on identifier feeds an application's `dependencies`, a load balancer data source feeds your DNS provider, a Cellar bucket feeds an application's environment. The graph replaces the copy-paste of identifiers between screens.

**Deleting an environment for real.** `terraform destroy` removes every resource it created, which makes short-lived environments practical: a preview stack per branch costs what it runs.

## Configure the provider

Authentication reuses the OAuth token pair Clever Tools stores after `clever login`, and the organisation you target:

```bash
export CC_OAUTH_TOKEN="…"
export CC_OAUTH_SECRET="…"
export CC_ORGANISATION="orga_xxx"
```

`CC_ORGANISATION` accepts a `user_xxx` identifier to target a personal space. The provider block then stays empty:

```hcl {filename="main.tf"}
terraform {
  required_providers {
    clevercloud = {
      source  = "CleverCloud/clevercloud"
      version = "~> 2.1"
    }
  }
}

provider "clevercloud" {}
```

For a pipeline, prefer a dedicated [OAuth consumer](/doc/develop/login-with-clever-cloud/) over a personal token, and pass its `consumer_key` and `consumer_secret` to the provider. It needs five rights: access to personal information, access to organisations, and management of organisations, their applications and their add-ons.

## Declare resources

Resources follow the platform's own split: one per runtime, one per add-on. An application links to an add-on through `dependencies`, which is the same operation as `clever service link-addon`:

```hcl {filename="main.tf"}
resource "clevercloud_postgresql" "db" {
  name   = "my-app-db"
  plan   = "dev"
  region = "par"
}

resource "clevercloud_nodejs" "app" {
  name               = "my-app"
  region             = "par"
  min_instance_count = 1
  max_instance_count = 3
  smallest_flavor    = "XS"
  biggest_flavor     = "M"

  dependencies = [clevercloud_postgresql.db.id]

  environment = {
    NODE_ENV = "production"
  }
}
```

Two data sources read what you did not declare. `clevercloud_default_loadbalancer` returns the CNAME and IP addresses to point a domain at, which lets the same configuration also manage your DNS:

```hcl {filename="main.tf"}
data "clevercloud_default_loadbalancer" "lb" {
  application_id = clevercloud_nodejs.app.id
}

output "dns_target" {
  value = data.clevercloud_default_loadbalancer.lb.cname
}
```

`clevercloud_postgresql_backup` reads the backups of a database, which is useful before a migration you want to gate on a recent backup existing.

## Control how deployments happen

An application resource creates the application. Whether Terraform also deploys the code depends on the `deployment` block, and the distinction matters more than it looks:

| Configuration                | Behaviour                                                                                                |
| ---------------------------- | -------------------------------------------------------------------------------------------------------- |
| No `deployment` block        | Terraform never deploys and never shows a deployment diff, you push with the CLI, the Console or your CI |
| Block without `commit`       | The repository HEAD is deployed on create and update, and the running hash is recorded                   |
| `commit = "<hash>"`          | The commit is pinned, an outside deployment shows as a diff, and the next apply restores the pinned hash |
| `commit = "refs/heads/main"` | The reference is resolved and deployed, and kept as-is in the state                                      |
| `commit = "github_hook"`     | Deployments are delegated to GitHub, the provider never pushes                                           |

Leaving the block out is the right default when your pipeline already deploys. Pinning a hash is the opposite stance: the infrastructure code owns what runs, and any manual deployment is treated as drift.

Deploying from a private repository takes a GitHub fine-grained token with read access to repository contents:

```hcl {filename="main.tf"}
deployment {
  repository           = "https://github.com/OWNER/REPO.git"
  authentication_basic = "USER:${var.github_token}"
}
```

## Run operations with actions

Terraform `1.14` introduced `action` blocks, which run an operation instead of reconciling a resource. The provider ships three, and they cover the tasks that usually push people back to a shell script:

```hcl {filename="actions.tf"}
action "clevercloud_application_reboot" "restart" {
  config {
    application_id = clevercloud_nodejs.app.id
  }
}
```

`clevercloud_application_reboot` restarts an application and waits until the new instances answer. `clevercloud_database_query` runs SQL on a PostgreSQL add-on and can export the result to a JSON file, which turns a schema bootstrap into part of the apply. `clevercloud_fsbucket_upload` pushes local files, whole directories or the content of an HTTP URL into an FS Bucket over FTP, seeding a volume without a separate step.

> [!NOTE] Actions are Terraform-only for now
> Actions need Terraform `1.14` or later. OpenTofu does not implement them yet, and a configuration using them fails validation with `Blocks of type "action" are not expected here`.

## Store the state on Clever Cloud

A [Cellar](/doc/deploy/storage/cellar/) bucket holds the state through the S3 backend, so the state lives on the same platform as the resources. Create the add-on and the bucket before `terraform init`, since a backend cannot bootstrap itself:

```hcl {filename="backend.tf"}
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "production.tfstate"
    region = "us-east-1"

    endpoints = { s3 = "https://cellar-c2.services.clever-cloud.com" }

    use_path_style              = true
    skip_region_validation      = true
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    skip_requesting_account_id  = true
  }
}
```

Credentials come from the add-on, through the variables the AWS SDK expects:

```bash
export AWS_ACCESS_KEY_ID="$CELLAR_ADDON_KEY_ID"
export AWS_SECRET_ACCESS_KEY="$CELLAR_ADDON_KEY_SECRET"
export AWS_REQUEST_CHECKSUM_CALCULATION=when_required
```

> [!WARNING] Disable trailing checksums
> The last variable is not optional. Recent Terraform versions send the state with a trailing checksum that Cellar does not support yet, and every write fails with `api error XAmzContentSHA256Mismatch`. Reads are unaffected, and `skip_s3_checksum` does not help.

## Know the limits

`terraform import` brings an existing application into the state but never fills the `deployment` block, because the provider cannot guess whether you want it to manage deployments. Adding the block afterwards starts tracking the running commit, and the first apply then triggers a deployment.

When `commit` holds a Git reference rather than a hash, the provider does not report the running commit and cannot detect a deployment made elsewhere: comparing a reference to a hash would mean cloning the repository. For the same reason, a new commit pushed to your branch is not a diff by itself, and gets deployed on the next apply that carries another change.

- [Provider documentation on the Terraform Registry](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
- [Provider source and examples](https://github.com/CleverCloud/terraform-provider-clevercloud)
