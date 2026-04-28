---
title: "Clever Tools 4.9: full Kubernetes lifecycle from the CLI"
date: 2026-04-28
description: Clever Tools 4.9 expands the Kubernetes command set with node groups, version updates, quotas and activity, and adds Swagger UI access for Otoroshi
tags:
  - clever-tools
  - cli
  - kubernetes
  - otoroshi
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Hubert Sablonnière
    link: https://github.com/hsablonniere
    image: https://github.com/hsablonniere.png?size=40
excludeSearch: true
---

[Clever Tools 4.9.0](https://github.com/CleverCloud/clever-tools/releases/tag/4.9.0) is available. This release significantly extends the `clever k8s` command set to cover the full lifecycle of [Clever Kubernetes Engine](/doc/kubernetes/), as it's now in public Beta. It also adds Swagger UI access to Otoroshi services and ships smaller quality-of-life improvements.

## Kubernetes lifecycle management

The `clever k8s` command set now covers cluster creation with detailed topology, ongoing operations, node group management, version upgrades and quota visibility. The `create` command accepts `--topology`, `--flavor`, `--cluster-version`, `--replication-factor`, `--autoscaling`, `--persistent-storage` and `--nodegroup` to provision a cluster matching your needs in a single command. The `get` output now reports topology, features, node groups and load balancers.

```bash
# Enable access to the k8s command set
clever features enable k8s

# Create a cluster with a control plane topology, version and initial node group
clever k8s create my-cluster \
  --topology dedicated_compute --flavor S --replication-factor 3 \
  --cluster-version 1.36 --autoscaling \
  --nodegroup XS:3 --persistent-storage

# Inspect the cluster (topology, features, node groups, load balancers)
clever k8s get my-cluster

# Update metadata or features
clever k8s update my-cluster --description "Production cluster" --tag env:prod,team:platform
```

Node groups have their own subcommands to list, create, get, update and delete, with autoscaling bounds and arbitrary tags:

```bash
# Create an autoscaling node group
clever k8s nodegroups create my-cluster workers XS:3 --autoscaling --min 3 --max 10

# List node groups attached to a cluster
clever k8s nodegroups list my-cluster

# Update bounds or target count
clever k8s nodegroups update my-cluster workers --count 5

# Delete a node group
clever k8s nodegroups delete my-cluster workers --yes
```

Version management is now first-class. The `version` subcommand reports the installed version and offers to upgrade to the latest available release when the cluster is outdated. The `version update` subcommand upgrades a cluster to an explicit target version when you prefer to drive the upgrade yourself:

```bash
# Check the current version and prompt for an upgrade if available
clever k8s version my-cluster

# Upgrade the cluster to a target version
clever k8s version update my-cluster --target 1.36
```

Two more commands round out the set: `clever k8s activity` shows recent deployment events of a cluster, and `clever k8s quota` reports the Kubernetes quota, current usage and remaining capacity for an organisation during public Beta.

```bash
clever k8s activity my-cluster --limit 100
clever k8s quota
```

Once your cluster reaches the `ACTIVE` state, retrieve its `kubeconfig` and drive it with `kubectl` like any other Kubernetes cluster. With `--persistent-storage` enabled at creation time, a default Ceph RBD `StorageClass` is provisioned on the cluster, so any `PersistentVolumeClaim` you create is bound automatically:

```bash
# Generate the kubeconfig and set it as your current context
clever k8s get-kubeconfig my-cluster > ~/.kube/config

# Inspect cluster nodes and the persistent storage driver
kubectl get nodes
kubectl get csidrivers
kubectl get storageclasses

# Deploy a workload and let it consume the default StorageClass
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=LoadBalancer
```

- [Learn more about Clever Kubernetes Engine](/doc/kubernetes/)

## Otoroshi Swagger UI

You can now open the Otoroshi Swagger UI directly from the CLI with a new `clever otoroshi open swaggerui` subcommand. The `clever otoroshi get` command also exposes the Swagger URL alongside the other endpoints, so you can hand it over to teammates or automation without opening the Console first.

```bash
# Open the Swagger UI of an Otoroshi service in your browser
clever otoroshi open swaggerui my-otoroshi

# Get service details, including the Swagger URL
clever otoroshi get my-otoroshi
```

## How to upgrade

To upgrade Clever Tools, [use your favourite package manager](/doc/cli/install/). For example with `npm`:

```bash
npm update -g clever-tools
clever version
```
