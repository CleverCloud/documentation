---
title: Kubernetes 1.36 is available
description: Faster SELinux volume labeling, external ServiceAccount token signing, device taints for Dynamic Resource Allocation, and gitRepo volume driver removal
date: 2026-04-22
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

Kubernetes [release 1.36.0](https://github.com/kubernetes/kubernetes/releases/tag/v1.36.0) is available on Clever Kubernetes Engine. Headline changes include faster SELinux volume labeling promoted to GA, external signing of ServiceAccount tokens through cloud KMS or HSMs, and Dynamic Resource Allocation gaining taints and tolerations for physical devices. The `gitRepo` volume driver — deprecated since v1.11 — has been permanently removed; migrate to init containers or git-sync tools. Select 1.36 explicitly at creation with `--cluster-version 1.36`; the default for new clusters remains 1.35. Migration of existing clusters will be available soon.

- [Learn more about Kubernetes 1.36](https://kubernetes.io/blog/2026/03/30/kubernetes-v1-36-sneak-peek/)
- [Learn more about Kubernetes on Clever Cloud](/doc/kubernetes/)
