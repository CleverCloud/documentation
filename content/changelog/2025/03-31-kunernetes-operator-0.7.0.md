---
title: 'Clever Kubernetes Operator v0.7.0 with wider products support'
date: 2025-03-31
tags:
  - kubernetes
  - operator
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Florentin Dubois
    link: https://github.com/FlorentinDUBOIS
    image: https://github.com/FlorentinDUBOIS.png?size=40
description: Deploy Azimutt, Cellar, Keycloak, Matomo and Otoroshi on Clever Cloud from Kubernetes
excludeSearch: true
---
[Clever Kubernetes Operator v0.7.0](https://github.com/CleverCloud/clever-kubernetes-operator/releases/tag/v0.6.0) is available. It now uses [clevercloud-sdk-rust v0.15.0](https://github.com/CleverCloud/clevercloud-sdk-rust/releases/tag/v0.15.0) and [oauth10a v2.1.1](https://github.com/CleverCloud/oauth10a-rust/releases/tag/v2.1.1). It fixes some bugs, comes with updated documentation and PostgreSQL versions. If you're connected to [Clever Tools](/developers/doc/cli), credentials are automatically detected and used with this release. [Azimutt](https://azimutt.app/docs), [Cellar](/developers/doc/addons/cellar), [Keycloak](/developers/doc/addons/keycloak), [Matomo](/developers/doc/addons/matomo) and [Otoroshi](/developers/doc/addons/otoroshi) can now be deployed as custom resources.

- [Learn more about Clever Kubernetes Operator](/developers/guides/kubernetes-operator)
