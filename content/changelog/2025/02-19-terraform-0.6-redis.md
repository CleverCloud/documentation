---
title: Deploy Redis® on Clever Cloud with Terraform (or OpenTofu), update your plan
description: No more destroy/recreate
date: 2025-02-19
tags:
  - addons
  - terraform
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Rémi Collignon-Ducret
    link: https://github.com/miton18
    image: https://github.com/miton18.png?size=40
excludeSearch: true
---

You can now deploy [Redis®](/developers/doc/addons/redis) add-ons using our Terraform provider, compatible with OpenTofu. The [0.6.0 release](https://github.com/CleverCloud/terraform-provider-clevercloud/releases/tag/v0.6.0) of the Clever Cloud Terraform provider also introduce the resource update. You can now apply a new plan without destroying and recreating the resource starting with PHP applications.

* Learn more about [our Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
