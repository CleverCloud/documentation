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

The [`CleverCloud/clevercloud`](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest) provider declares Clever Cloud resources as code. It covers 48 resource types, from every application runtime to databases, storage, log drains, Network Groups, Kubernetes clusters and OAuth consumers, and works with both Terraform and OpenTofu.

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

After `clever login`, the provider reads the credentials of the active Clever Tools profile. It only needs the organisation you target:

```shell
export CC_ORGANISATION="orga_xxx"
```

`CC_ORGANISATION` accepts a `user_xxx` identifier to target a personal space. Wherever Clever Tools isn't logged in, set `CC_OAUTH_TOKEN` and `CC_OAUTH_SECRET` as well: they take precedence over the profile. The provider block then stays empty:

```hcl {filename="main.tf"}
terraform {
  required_providers {
    clevercloud = {
      source  = "CleverCloud/clevercloud"
      version = "~> 3.0"
    }
  }
}

provider "clevercloud" {}
```

For a pipeline, the provider also accepts an [API token](/doc/manage/cli/#tokens), created with `clever tokens create`. Set it in `CLEVER_API_TOKEN`, or pass it as `api_token`, and the provider sends it as a Bearer token to the API bridge. Choose one authentication method: in the provider block, `api_token` excludes the OAuth parameters. Explicit parameters take precedence over environment variables. Without explicit parameters, setting both `CLEVER_API_TOKEN` and `CC_OAUTH_TOKEN` with `CC_OAUTH_SECRET` causes an error:

```shell
clever tokens create terraform-ci --expiration 4w
export CLEVER_API_TOKEN="API_TOKEN"
```

An API token can't authenticate a Git push, so application resources that push code through a `deployment` block still need OAuth credentials. In that case, prefer a dedicated [OAuth consumer](/doc/develop/login-with-clever-cloud/) over a personal token, and pass its `consumer_key` and `consumer_secret` to the provider, along with the `token` and `secret` of the user it acts for. It needs five rights: access to personal information, access to organisations, and management of organisations, their applications and their add-ons.

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

  tags = ["env:production", "team:platform"]
}
```

Every application and add-on resource accepts `tags`, either plain (`production`) or key/value (`env:production`). When the attribute is unset, Terraform leaves the tags set elsewhere untouched and never reports them. Removing it from the configuration keeps the current tags: set `tags = []` to remove them all.

On a `clevercloud_kubernetes` cluster, `node_autoprovisioning = true` enables node auto-provisioning, which creates and deletes nodes on demand instead of resizing node groups. It provisions nothing until you deploy `NodePool` and `CleverNodeClass` resources in the cluster, requires Kubernetes 1.34 or later, and excludes the cluster-wide autoscaler.

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

| Configuration                | Behaviour                                                                                                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No `deployment` block        | Terraform doesn't push code or track the running commit: you deploy with the CLI, the Console or your CI. An environment change restarts the application if it has already been deployed |
| Block without `commit`       | Terraform deploys the repository HEAD on creation. Then each plan reads the HEAD, and the next apply deploys a new commit shown as a diff                                                |
| `commit = "<hash>"`          | The commit is pinned, an outside deployment shows as a diff, and the next apply restores the pinned hash                                                                                 |
| `commit = "refs/heads/main"` | The reference is resolved and deployed, and kept as-is in the state                                                                                                                      |
| `commit = "github_hook"`     | GitHub handles deployments. The provider never pushes code and keeps `github_hook` in the state instead of tracking the running commit                                                   |

Leaving the block out is the right default when your pipeline already deploys. Pinning a hash is the opposite stance: the infrastructure code owns what runs, and any manual deployment is treated as drift.

`repository` takes an `https://`, `http://` or `file://` URL. Without `commit`, when the provider can't reach the repository during a plan, it emits a warning and can't detect a new HEAD in that plan.

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

An action runs only when you invoke it:

```shell
terraform apply -invoke action.clevercloud_application_reboot.restart
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

```shell
export AWS_ACCESS_KEY_ID="$CELLAR_ADDON_KEY_ID"
export AWS_SECRET_ACCESS_KEY="$CELLAR_ADDON_KEY_SECRET"
export AWS_REQUEST_CHECKSUM_CALCULATION=when_required
```

> [!WARNING] Disable trailing checksums
> The last variable is not optional. Recent Terraform versions send the state with a trailing checksum that Cellar does not support yet, and every write fails with `api error XAmzContentSHA256Mismatch`. Reads are unaffected, and `skip_s3_checksum` does not help.

## Know the limits

`terraform import` brings an existing application into the state but never fills the `deployment` block, because the provider cannot guess whether you want it to manage deployments. Adding the block afterwards enables the deployment behavior described above. With `commit` unset or pinned to a hash, the provider tracks the running commit. The next apply pushes the resolved target if it differs from the running commit, unless `commit = "github_hook"`. In that mode, the provider neither pushes code nor tracks the running commit.

When `commit` holds a Git reference rather than a hash, the provider doesn't report the running commit and doesn't detect a deployment made elsewhere. A new commit pushed to your branch isn't a diff by itself either, and gets deployed on the next apply that carries another change. Remove `commit` from the configuration to track the repository HEAD again on the next plans.

To adopt existing resources, prefer `import` blocks with `terraform plan -generate-config-out=generated.tf`, as described in the [provider documentation](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs). Add-ons are imported by their real ID, except `clevercloud_addon`, which takes the add-on ID, and a `clevercloud_cellar_bucket` by its Cellar ID and name, such as `cellar_xxx/my-bucket`. Terraform never writes sensitive values, such as the environment of an application, into a generated configuration. Set `BYPASS_SENSITIVE_IMPORTS=true` for the generating command only: while it's set, plans and the generated configuration expose sensitive resource attributes, including environment variables. The credentials of the provider stay redacted:

```shell
BYPASS_SENSITIVE_IMPORTS=true terraform plan -generate-config-out=generated.tf
```

- [Provider documentation on the Terraform Registry](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
- [Provider source and examples](https://github.com/CleverCloud/terraform-provider-clevercloud)
