---
title: Create Kubernetes clusters from the Console
description: Enable Clever Kubernetes Engine in the Console Labs to create clusters with their topology, flavor, replication factor, autoscaling, and persistent storage, then manage them from their dashboard
date: 2026-04-29
tags:
  - console
  - kubernetes
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

The [Clever Cloud Console](https://console.clever-cloud.com) menu lists your [Clever Kubernetes Engine](/doc/deploy/kubernetes/) (CKE) clusters. Each one gets a dashboard with its state, Kubernetes version, and creation date. From there, you download its kubeconfig file or delete it from the danger zone. You can now create clusters from the Console too.

Clever Kubernetes is in public beta. To create a cluster from the Console, open the [Labs](https://console.clever-cloud.com/users/me/feature-list) page from your profile menu and enable `Clever Kubernetes Engine`. Kubernetes then appears among the resources you can create.

The form asks for a name, optional tags, and the Kubernetes version. Then pick the topology of the cluster: Essential (All In One), Business (Dedicated Compute), or Enterprise (Distributed). Each topology offers its own control plane flavors and replication factors. Two toggles enable autoscaling and persistent storage. Topology and replication factor can't change after creation, so pick them carefully.

Once created, the cluster starts its deployment and appears in the menu of your organisation.

- [Learn more about Clever Kubernetes Engine](/doc/deploy/kubernetes/)
- [Manage your clusters from Clever Tools](/doc/manage/cli/kubernetes/)
- [Share your feedback on the Console](https://github.com/CleverCloud/Community/discussions/categories/console)
