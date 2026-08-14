---
title: Terraform provider 2.1.0
description: TCP redirections for applications, Network Groups for Otoroshi and Clever Tools profiles support in the Clever Cloud Terraform provider
date: 2026-08-13
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

The [2.1.0 release](https://github.com/CleverCloud/terraform-provider-clevercloud/releases/tag/v2.1.0) of the Clever Cloud Terraform provider is available. Application resources now declare [TCP redirections](/doc/develop/common-configuration/tcp-redirections/), and the Otoroshi resource can join a [Network Group](/doc/network/network-groups/). The provider also reads credentials from the profiles format of Clever Tools, so `clever login` is enough to authenticate it.

This release restarts an application when only its environment variables change. Importing a MySQL, PostgreSQL or MongoDB add-on no longer forces an unnecessary replacement, and PostgreSQL connection details refresh after a migration. It also fixes Network Groups without a description, keeps their peers in sync, and reads Otoroshi API credentials from the add-on.

- Learn more about [Clever Cloud Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
