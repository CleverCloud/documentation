---
title: Kubernetes 1.37 is available
description: SELinux volume labeling through mount options by default, Pod certificates, ClusterTrustBundles and DRA device taints reach GA, while kube-proxy ipvs mode and kube-dns are deprecated
date: 2026-09-22
tags:
  - kubernetes
  - release
authors:
  - name: Gilles Biannic
    link: https://github.com/GillesBIANNIC
    image: https://github.com/GillesBIANNIC.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

[Kubernetes 1.37 "Garhwal"](https://github.com/kubernetes/kubernetes/releases/tag/v1.37.0) is available on Clever Kubernetes Engine. Features reaching GA include Pod certificates, ClusterTrustBundles, configurable HPA tolerance, the `metrics.k8s.io` v1 API and Dynamic Resource Allocation device taints and tolerations. HPA scale-to-zero for object and external metrics and memory QoS with cgroup v2 move to beta and are enabled by default.

On nodes with SELinux enabled, volumes from CSI drivers that support it now get their SELinux label through mount options by default, instead of a recursive relabeling of every file. Pods with different SELinux labels sharing a volume on the same node may then fail to start: set `seLinuxChangePolicy: Recursive` on these Pods to keep the previous behavior. Static Pods can no longer reference Secrets or ConfigMaps.

The `ipvs` mode of kube-proxy is deprecated in favor of the `nftables` and `iptables` modes, kube-dns in favor of CoreDNS. The `--filename` option of `kubectl run` is also deprecated.

Select Kubernetes 1.37 when you create a cluster, or update an existing one, with [Clever Tools](/doc/manage/cli/kubernetes/):

```bash
clever k8s create myCluster --cluster-version 1.37
clever k8s version update myClusterNameOrId --target 1.37
```

- [Learn more about Kubernetes 1.37](https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/)
- [Learn more about Kubernetes on Clever Cloud](/doc/deploy/kubernetes/)
