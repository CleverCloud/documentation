---
title: Kubernetes 1.36 is now used by default
description: Kubernetes 1.36 is now the default version for new clusters on Clever Kubernetes Engine
date: 2026-05-05
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

Kubernetes 1.36 "Haru" is available on Clever Kubernetes Engine [since its release](/changelog/2026/04-24-kubernetes-1.36/). It's now the default version deployed when no `--cluster-version` is specified. New clusters will run on v1.36 unless you explicitly pick another supported one.

You can still target v1.35 or v1.34 with `--cluster-version`, as long as they remain supported (n-2 from the current release, mirroring the official Kubernetes support policy):

```bash
clever k8s create myCluster --cluster-version 1.35
```

Existing clusters are not migrated automatically. To move one to v1.36, use [Clever Tools](/doc/cli/kubernetes/):

```bash
clever k8s version update myClusterNameOrId 1.36
```

- [Learn more about Kubernetes 1.36](/changelog/2026/04-24-kubernetes-1.36/)
- [Learn more about Kubernetes on Clever Cloud](/doc/kubernetes/)
