---
title: Set Metabase domain at creation
description: You can now set a custom domain for Metabase admin interface when creating the add-on on Clever Cloud
date: 2025-12-23
tags:
  - addons
  - metabase
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

When you deploy a Metabase add-on on Clever Cloud, you can access its web interface through a `<random_chars>-metabase.services.clever-cloud.com` domain. You can now set a custom domain at creation through the `access-domain` option in Clever Tools:

```bash
clever addon create metabase yourMetabaseNameOrId --option access-domain=metabase.example.com
```

This domain DNS configuration needs to point to Clever Cloud's servers. For example, if the Metabase add-on is deployed in the `par` (Paris) region, you need to create a CNAME record pointing to `domain.par.clever-cloud.com.`.

- [Learn more about Metabase on Clever Cloud](/doc/addons/metabase/)
