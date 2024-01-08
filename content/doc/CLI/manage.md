---
type: docs
title: Manage
weight: 4
shortdesc: Manage your application using the Clever Cloud CLI tool
tags:
- cli
- reference
keywords:
- cli
- clever-tools
- stop
- restart
- env
- scalability
- flavor
- instance
- domain

aliases:
- /doc/administrate/clever-tools/manage

---

## Stop or restart your application

`clever stop <app-name>` allows you to stop your application.
If you want to restart your application, you can use :

```shell
clever restart <app-name>

# Restart the application with a specific commit id
clever restart <app-name> --commit <commit-id>
```

You can use `--quiet` when you restart, logs won't appear during deployment.

## Deploy a new commit

Use `clever deploy` to push your commits, which then starts a deployment

## Environment

Clever-tools allows you to get and update the environment of your application.

### Get the whole environment

Simply use the command down below to get all your variables.

```shell
clever env
```

### Update an environment variable

Use `set` to add or update an environment variable and `rm` to remove one.

```shell
# Add or update an environment variable
clever env set <variable-name> <variable-value>

# Remove an environment variable
clever env rm <variable-name>
```

If your environment variable contains a `-`, then write: `clever env set test -- ---foo---`

Or you can put the dashes before the remaining arguments, as follows: `clever -- env set test ---bar---`

The `--` indicates that there are no options to be parsed.

### Load environment variables

Clever-tools allows you to load variables from STDIN.

```shell
cat <env-file> | clever env import
```

## Scalability

### Flavors

You can choose the scale of your application using `--flavor <flavor>` where `<flavor>` can be pico, nano, XS, S, M, L or XL.

```shell
# Change the scale of your application
clever scale --flavor <flavor>

# Set the minimum and maximum scale for your application
clever scale --min-flavor <min-flavor> --max-flavor <max-flavor>
```

### Instances

You can choose the number of parallels instances using `--instances <instances>` where `<instance>` is a number between 1 and 20.

```shell
# Change the number of parallels instances
clever scale --instances <instances>

# Set the minimum and maximum number of parallels instances
clever scale --min-instances <min-instances> --max-instances <max-instances>
```

## Domains

### List your domains

If you want to list your domain, use :

```shell
clever domain
```

### Add or remove domains

Using `clever domain`, you can add or remove domain names.

```shell
# Add a domain
clever domain add <domain-name>

# Remove a domain
clever domain remove <domain-name>
```
