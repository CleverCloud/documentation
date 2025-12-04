---
title: Set Otoroshi admin and routes domains at creation
description: You can now set custom domains for Otoroshi admin interface and routes when creating the add-on on Clever Cloud
date: 2025-11-28
tags:
  - addons
  - otoroshi
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

When you deploy an Otoroshi add-on on Clever Cloud, you can access its admin interface through a `<random_chars>-otoroshi.services.clever-cloud.com` domain. When you create a new route, it starts with a `app-id.cleverapps.io`. You can now set custom domains at creation through the `base-domain` and `routes-domain` options in Clever Tools:

```bash
clever addon create otoroshi myOtoroshiName --option base-domain=otoroshi.example.com --option routes-domain=routes.example.com
```

These domains' DNS configuration needs to point to Clever Cloud's servers. For example, if the Otoroshi add-on is deployed in the `par` (Paris) region, you need to create CNAME records pointing to `domain.par.clever-cloud.com.`.

- [Learn more about Otoroshi on Clever Cloud](/doc/addons/otoroshi/)
- [Learn more about DNS and custom domains on Clever Cloud](/doc/administrate/domain-names/)
