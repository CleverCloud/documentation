---
title: Set Matomo domain at creation
description: You can now set a custom domain for Matomo web analytics interface when creating the add-on on Clever Cloud
date: 2025-12-12
tags:
  - addons
  - matomo
authors:
  - name: Sébastien Allemand
    link: https://github.com/allemas
    image: https://github.com/allemas.png?size=40
  - name: David Legrand
    link: https://github.com/davlgd
    image: https://github.com/davlgd.png?size=40
excludeSearch: true
---

When you deploy a Matomo add-on on Clever Cloud, you can access its web interface through a `<random_chars>-matomo.services.clever-cloud.com` domain. You can now set a custom domain at creation through the `access-domain` option in Clever Tools:

```bash
clever addon create addon-matomo yourMatomoNameOrId --option access-domain=matomo.example.com
```

This domain DNS configuration needs to point to Clever Cloud's servers. For example, if the Matomo add-on is deployed in the `par` (Paris) region, you need to create a CNAME record pointing to `domain.par.clever-cloud.com.`.

- [Learn more about Matomo on Clever Cloud](/doc/addons/matomo/)
- [Learn more about DNS and custom domains on Clever Cloud](/doc/administrate/domain-names/)
