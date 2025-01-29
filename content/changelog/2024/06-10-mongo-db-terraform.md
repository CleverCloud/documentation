---
title: Deploy MongoDB add-ons with our Terraform provider
date: 2024-06-10
tags:
  - mongodb
  - terraform
authors:
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
  - name: Mathieu Barcelo
    link: https://github.com/TheCrabe
    image: https://github.com/TheCrabe.png?size=40
description:
aliases:
- /changelog/2024-06-10-mongo-db-terraform
excludeSearch: true
---

If you can deploy on Clever Cloud through our [Console](https://console.clever-cloud.com), our CLI ([Clever Tools](https://github.com/CleverCloud/clever-tools)), or our [API](/developers/api/), you can also use Terraform and compatible tools such as [OpenTofu](https://opentofu.org/). We maintain a provider that allows you to manage your resources as code, from applications to add-ons (object storage, databases, etc.).

We've recently added support for Python and [Materia KV](/developers/doc/addons/materia-kv/). It's MongoDB's turn [to be available](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs/resources/mongodb). You can now create such an add-on, choose its plan, region and get the credentials to connect to it.

* Learn more about [our Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
