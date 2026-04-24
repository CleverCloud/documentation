---
title: Kubernetes 1.36 is available
description: Fine-grained kubelet authorization, faster SELinux volume labelling, workload aware scheduling and removal of the gitRepo volume plugin
date: 2026-04-24
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

We added support for [Kubernetes 1.36.0 "Haru"](https://github.com/kubernetes/kubernetes/releases/tag/v1.36.0), which ships multiple enhancements. Fine-grained kubelet API authorization and faster SELinux labelling of volumes reach GA, while Workload Aware Scheduling and DRA device taints and tolerations move to beta. The long-deprecated `gitRepo` volume plugin is permanently removed, and `Service.spec.externalIPs` enters deprecation ahead of its removal in v1.43. Kubernetes 1.36.0 can be selected for new deployments; v1.35 remains the default for now. Migration of existing clusters will be available soon.

- [Learn more about Kubernetes 1.36](https://kubernetes.io/blog/2026/04/22/kubernetes-v1-36-release/)
- [Learn more about Kubernetes on Clever Cloud](/doc/kubernetes/)
