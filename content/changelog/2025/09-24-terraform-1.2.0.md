---
title: Terraform provider 1.2.0 is available
description: You can now use Ruby runtime and drains with a better Terraform provider experience
date: 2025-09-24
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

The [1.2.0 release](https://github.com/CleverCloud/terraform-provider-clevercloud/releases/tag/v1.2.0) of the Clever Cloud Terraform provider is available. It brings multiple bug fixes with some cleaning. It also adds support for Ruby runtime and drains.

There is a format change in domains management:
```
  vhosts = [
    "api.${var.cc_global_tld}/v4/addon-providers/es-addon",
    local.api_v2_vhost,
  ]
```

becomes:
```
  vhosts = [
    { fqdn = "api.${var.cc_global_tld}", path_begin = "/v4/addon-providers/es-addon" },
    { fqdn = "api.${var.cc_global_tld}", path_begin = "/v2/providers/es-addon" }
  ]
```

* Learn more about [our Terraform provider](https://registry.terraform.io/providers/CleverCloud/clevercloud/latest/docs)
