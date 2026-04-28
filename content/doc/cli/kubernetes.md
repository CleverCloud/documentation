---
type: docs
linkTitle: Kubernetes
title: Clever Kubernetes Engine (CKE)
description: Create and manage Kubernetes clusters using Clever Kubernetes Engine from Clever Tools
keywords:
- kubernetes
- cke
- materia
- etcd
- k8s
- cluster
- topology
- node group
- autoscaling
- csi
- persistent storage
- kubeconfig
- load balancers
- quota
- version
---

Clever Tools 4.9+ exposes the full lifecycle of [Clever Kubernetes Engine](/doc/kubernetes/): cluster creation with detailed topology, ongoing operations, node group management, version upgrades and quota visibility. Once a cluster is `ACTIVE`, you drive it with `kubectl` like any other Kubernetes cluster.

- [Learn more about Kubernetes on Clever Cloud](/doc/kubernetes/)

## Prerequisites

Activate the `k8s` feature flag once per user account:

```bash
clever features enable k8s
```

Check the command set is available:

```bash
clever k8s
```

In all examples below, target a specific organisation with the `--org` (or `-o`) option. Output format defaults to a human-readable table; pass `--format json` (or `-F json`) on read commands when you need structured output for scripts or pipelines.

## Create a cluster

The fastest way to create a cluster is to provide only a name. The platform picks `ALL_IN_ONE` as the default topology, the smallest available flavor (`S`) and a replication factor of `1`:

```bash
clever k8s create myCluster --org <your_org_id>
```

Add `--watch` to follow the deployment until the cluster reaches `ACTIVE`:

```bash
clever k8s create myCluster --watch --org <your_org_id>
```

When you need a specific shape, combine topology, flavor, replication factor, version and an initial node group in a single command. Topology values (`all_in_one`, `dedicated_compute`, `distributed`) are accepted in lowercase or uppercase. The `--nodegroup <flavor>:<count>` option provisions an initial node group named `default`, ready to schedule workloads as soon as the cluster reaches `ACTIVE`. Use it on `dedicated_compute` and `distributed` clusters, which otherwise come up with no worker. `all_in_one` bundles already include an integrated worker on each bundle VM, so passing `--nodegroup` adds an *extra* pool — Clever Tools warns you and asks for confirmation in that case:

```bash
clever k8s create myCluster --org <your_org_id> \
  --topology dedicated_compute --flavor S --replication-factor 3 \
  --cluster-version 1.36 \
  --description "Production cluster" \
  --tag env:prod,team:platform \
  --autoscaling \
  --persistent-storage \
  --nodegroup M:3
```

The `--cluster-version` value is validated against the platform-supported versions before the API call; an unsupported value (e.g. `0.99`) is rejected upfront with the list of available versions.

## List, get and inspect

List the Kubernetes clusters of the active organisation:

```bash
clever k8s list
clever k8s list --format json
```

Get full details for one cluster (topology, features, node groups, load balancers, storage usage). The first form resolves a cluster by name when unambiguous; the second targets a specific cluster by ID:

```bash
clever k8s get myCluster
clever k8s get kubernetes_id -F json
```

The human format shows topology and feature state in a single table, with extra tables for control plane components (in `DISTRIBUTED`), node groups and load balancers when present:

```text
┌────────────────────┬─────────────────────────────────────────┐
│ (index)            │ Values                                  │
├────────────────────┼─────────────────────────────────────────┤
│ Name               │ 'myCluster'                             │
│ ID                 │ 'kubernetes_id'                         │
│ Status             │ 'ACTIVE'                                │
│ Version            │ '1.36'                                  │
│ Topology           │ 'DEDICATED_COMPUTE (S, rf=3)'           │
│ Autoscaling        │ 'enabled'                               │
│ Persistent storage │ 'enabled'                               │
│ Tags               │ 'env:prod, team:platform'               │
│ Description        │ 'Production cluster'                    │
└────────────────────┴─────────────────────────────────────────┘
```

## Update cluster metadata

Rename the cluster, change its description or tags, and toggle autoscaling without redeploying. Pass at least one of `--name`, `--description`, `--tag`, `--autoscaling` or `--disable-autoscaling`. The `--autoscaling` and `--disable-autoscaling` flags are mutually exclusive:

```bash
clever k8s update myCluster --description "Production cluster, EU" --tag env:prod,team:platform
clever k8s update myCluster --name myCluster-eu
clever k8s update myCluster --autoscaling
clever k8s update myCluster --disable-autoscaling
```

Updating `--tag` replaces the full list of tags. Pass an empty value to clear them.

## Add persistent storage

Enable persistent storage on an existing cluster with a Ceph RBD CSI driver. The cluster gains a default `StorageClass` named `csi-rbd-sc`, ready to back any `PersistentVolumeClaim`:

```bash
clever k8s add-persistent-storage myCluster
```

Persistent storage is a one-way toggle; once enabled, it cannot be removed from a running cluster. Create a new cluster without `--persistent-storage` if you no longer need it.

## Get the kubeconfig file

Retrieve the kubeconfig of an `ACTIVE` cluster. Wait for the cluster to reach `ACTIVE` before redirecting the output to a file — the command is a no-op on non-ready clusters:

```bash
clever k8s get-kubeconfig myCluster
clever k8s get-kubeconfig myCluster > ~/.kube/config
```

Once the kubeconfig is in place, drive the cluster with `kubectl` as usual. With `--persistent-storage` enabled, the default `StorageClass` is provisioned automatically. `kubectl get nodes` lists the integrated workers immediately on `all_in_one` clusters; on `dedicated_compute` and `distributed` clusters, the list stays empty until you add a node group:

```bash
kubectl get nodes
kubectl get csidrivers
kubectl get storageclasses

kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=LoadBalancer
```

## Activity and quota

`activity` lists recent deployment events of a cluster (creation steps, control plane rollout, node group resizes). The default limit is `50`; pass `--limit N` (between `1` and `1000`) to widen the window:

```bash
clever k8s activity myCluster
clever k8s activity myCluster --limit 100
clever k8s activity myCluster -F json
```

`quota` reports the Kubernetes quota, current usage and remaining capacity for the active organisation. Each organisation starts with **40 vCPU and 40 GB of RAM** during the public Beta:

```bash
clever k8s quota
clever k8s quota -F json
```

## Cluster version

Report the installed Kubernetes version of a cluster, and offer an interactive upgrade prompt when an upgrade is available:

```bash
clever k8s version myCluster
clever k8s version check myCluster
```

Drive the upgrade explicitly to a target version. The target is validated against the supported versions before the API call:

```bash
clever k8s version update myCluster --target 1.36
```

## Node groups

A node group is a pool of worker VMs of the same flavor. `dedicated_compute` and `distributed` clusters need at least one node group to schedule workloads; `all_in_one` clusters already include an integrated worker on each bundle VM and only need a node group when you want extra capacity beyond the bundle. Create one alongside a cluster (with `--nodegroup` on `clever k8s create`) or independently with `nodegroups create`. The third positional argument follows the `<flavor>:<count>` format and accepts lowercase flavors:

```bash
clever k8s nodegroups create myCluster workers XS:3
clever k8s nodegroups create myCluster workers XS:3 --autoscaling --min 3 --max 10
clever k8s nodegroups create myCluster workers XS:3 --description "GPU-intensive workers" --tag env:prod
```

Inspect node groups attached to a cluster:

```bash
clever k8s nodegroups list myCluster
clever k8s nodegroups list myCluster -F json
clever k8s nodegroups get myCluster workers
clever k8s nodegroups get myCluster node_group_id
```

Update bounds, target count, autoscaling state or metadata. Pass at least one of `--count`, `--min`, `--max`, `--autoscaling`, `--disable-autoscaling`, `--description` or `--tag`. Resizes are queued: the API rejects a second update while a previous resize is still running:

```bash
clever k8s nodegroups update myCluster workers --count 5
clever k8s nodegroups update myCluster workers --autoscaling --min 2 --max 10
clever k8s nodegroups update myCluster workers --disable-autoscaling
clever k8s nodegroups update myCluster workers --description "Updated description"
```

Delete a node group; nodes are drained and the underlying VMs are removed. Skip the confirmation prompt with `--yes`:

```bash
clever k8s nodegroups delete myCluster workers
clever k8s nodegroups delete myCluster workers --yes
```

## Delete a cluster

Delete a cluster by name (when unambiguous) or by ID. Skip the confirmation prompt with `--yes`:

```bash
clever k8s delete myCluster
clever k8s delete myCluster --yes
clever k8s delete kubernetes_id --yes
```
