---
title: Deploy Docker containers on Clever Cloud with Terraform (or OpenTofu)
date: 2024-07-03
tags:
  - docker
  - terraform
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Rémi Collignon-Ducret
    link: https://github.com/miton18
    image: https://github.com/miton18.png?size=40
description: Manage your Docker containers on Clever Cloud with Terraform or compatible tools such as OpenTofu
aliases:
- /changelog/2024-07-03-docker-terraform
excludeSearch: true
---

To manage your resources as code on Clever Cloud, from applications to add-ons (object storage, databases, etc.), you can use our Terraform provider. It's compatible with tools such as [OpenTofu](https://opentofu.org/) and can now deploy applications using [our Docker runtime](/developers/doc/applications/docker/).

You can define instances count or flavors, region, dependencies, ports, Dockerfile and application paths, registry credentials and more. Read [the full parameters list](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs/resources/docker).

* Learn more about [our Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
