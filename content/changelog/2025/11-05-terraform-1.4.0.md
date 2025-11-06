---
title: Terraform provider 1.4.0
description: Deploy Elastic Stack directly from Terraform with the new Clever Cloud provider
date: 2025-11-05
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

The [1.4.0 release](https://github.com/CleverCloud/terraform-provider-clevercloud/releases/tag/v1.4.0) of the Clever Cloud Terraform provider is available. It now uses API when available for Keycloak, Metabase, Otoroshi, rather than [service dependencies](/changelog/2025/10-22-operators-cleanup/). It brings support for [Elastic Stack](/developers/doc/addons/elastic/) (Elasticsearch with APM, Kibana), load balancer datasource, and replaces applications when the region is changed.

* Learn more about [Clever Cloud Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
